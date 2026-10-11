"""Phase-level tier-2 full-suite runner: background tmux, check-run, gate, fix routing.

Parent session starts the README suite in a detached tmux window in the phase
worktree, polls for completion, and records one ``project:check-run`` with
``evidence_kind: integration``. Does not fix-and-rerun inline.
"""

from __future__ import annotations

import hashlib
import json
import re
import shlex
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from se_workflow import aa
from se_workflow.check import (
    OUTPUT_BODY_CHARS,
    RUNNER,
    git_diff_sha256,
    git_head,
    git_is_dirty,
)
from se_workflow.policy import dirty_pass_decision, map_process_outcome
from se_workflow.reviewer import _revision_matches

EVIDENCE_KIND = "integration"
SUBJECT_SUFFIX = "-tier2"
METHOD = "check"

# README Testing: fast non-tmux, then serial tmux.
FAST_SUITE_CMD = (
    'uv run --with textual --with pytest --with pytest-xdist '
    'python -m pytest tests -q -n 4 -m "not tmux"'
)
TMUX_SUITE_CMD = (
    "uv run --with textual --with pytest "
    "python -m pytest tests -q -m tmux"
)

_NODE_ID_RE = re.compile(
    r"(?:FAILED|ERROR)\s+(\S+::\S+)"
)
_SUMMARY_NODE_RE = re.compile(
    r"^(?:FAILED|ERROR)\s+(\S+::\S+)",
    re.MULTILINE,
)


def tier2_subject(phase_slug: str) -> str:
    slug = (phase_slug or "").strip()
    if not slug:
        raise ValueError("phase_slug is required")
    if slug.endswith(SUBJECT_SUFFIX):
        return slug
    return f"{slug}{SUBJECT_SUFFIX}"


def is_tier2_subject(subject: str) -> bool:
    return (subject or "").strip().endswith(SUBJECT_SUFFIX)


def readme_suite_command() -> str:
    """Command chain matching README Testing full suite (fast then tmux)."""
    return f"{FAST_SUITE_CMD} && {TMUX_SUITE_CMD}"


def parse_failing_node_ids(output: str) -> list[str]:
    """Extract pytest node ids from failure/error lines (stable order, unique)."""
    seen: set[str] = set()
    ordered: list[str] = []
    for match in _SUMMARY_NODE_RE.finditer(output or ""):
        node = match.group(1).strip()
        if node not in seen:
            seen.add(node)
            ordered.append(node)
    if ordered:
        return ordered
    for match in _NODE_ID_RE.finditer(output or ""):
        node = match.group(1).strip()
        if node not in seen:
            seen.add(node)
            ordered.append(node)
    return ordered


def cluster_by_module(node_ids: Sequence[str]) -> dict[str, list[str]]:
    """Cluster node ids by test file / module path (text before ``::``)."""
    clusters: dict[str, list[str]] = {}
    for node in node_ids:
        module = node.split("::", 1)[0] if "::" in node else node
        clusters.setdefault(module, []).append(node)
    return clusters


def module_fix_subject(module: str) -> str:
    """Stable fix work-item subject for a failing module path."""
    cleaned = module.strip().replace("\\", "/")
    if cleaned.startswith("tests/"):
        cleaned = cleaned[len("tests/") :]
    if cleaned.endswith(".py"):
        cleaned = cleaned[:-3]
    cleaned = re.sub(r"[^a-zA-Z0-9._-]+", "-", cleaned).strip("-")
    return f"fix-{cleaned}"


@dataclass
class Tier2FixRouting:
    clusters: dict[str, list[str]] = field(default_factory=dict)
    fix_subjects: list[str] = field(default_factory=list)
    create_fix_flags: list[bool] = field(default_factory=list)
    escalate: bool = False
    reopen_done: bool = False
    inline_fix_and_rerun: bool = False


def route_tier2_failures(
    node_ids: Sequence[str],
    *,
    fix_budget_remaining: int,
) -> Tier2FixRouting:
    """Create fix-task subjects clustered by module under the retry budget.

    Never reopens ``done``. Never implies an inline verifier fix-and-rerun.
    """
    clusters = cluster_by_module(list(node_ids))
    modules = list(clusters.keys())
    remaining = max(0, int(fix_budget_remaining))
    flags: list[bool] = []
    subjects: list[str] = []
    for module in modules:
        subject = module_fix_subject(module)
        if remaining > 0:
            flags.append(True)
            subjects.append(subject)
            remaining -= 1
        else:
            flags.append(False)
            subjects.append("")
    escalate = bool(modules) and not any(flags)
    if sum(flags) < len(modules) and any(flags):
        escalate = True
    return Tier2FixRouting(
        clusters=clusters,
        fix_subjects=subjects,
        create_fix_flags=flags,
        escalate=escalate,
        reopen_done=False,
        inline_fix_and_rerun=False,
    )


def should_rerun_tier2(*, fix_tasks_created: int) -> bool:
    """After fix tasks land, tier-2 is expected to rerun at the new head."""
    return bool(fix_tasks_created)


def _output_sha256(output: str) -> str:
    return hashlib.sha256(output.encode("utf-8", "replace")).hexdigest()


def _body_tail(output: str) -> str:
    if len(output) <= OUTPUT_BODY_CHARS:
        return output
    return output[-OUTPUT_BODY_CHARS:]


@dataclass
class Tier2Start:
    """Non-blocking start handle for a background tier-2 job."""

    session_name: str
    worktree: Path
    phase_slug: str
    phase_head: str
    log_path: Path
    exit_path: Path
    started_monotonic: float
    blocking: bool = False


@dataclass
class Tier2Result:
    exit_code: int
    duration_s: float
    output: str
    output_sha256: str
    failing_node_ids: list[str]
    result: str  # pass | fail | blocked
    revision: str
    diff_sha256: str | None = None
    refuse: bool = False
    refuse_message: str = ""


def resolve_tier2_revision(
    cwd: Path,
    *,
    allow_dirty: bool = False,
    provisional_result: str = "pass",
) -> tuple[str, str | None, str | None]:
    """Return (revision, diff_sha256|None, refuse_message|None).

    Dirty pass is refused without ``allow_dirty``, matching check dirty policy.
    """
    head = git_head(cwd)
    dirty = git_is_dirty(cwd)
    diff = git_diff_sha256(cwd) if dirty else None
    decision = dirty_pass_decision(
        dirty=dirty,
        result=provisional_result,  # type: ignore[arg-type]
        head=head,
        diff_sha256=diff,
        allow_dirty=allow_dirty,
    )
    if decision.refuse:
        return decision.revision, decision.diff_sha256, decision.refuse_message
    return decision.revision, decision.diff_sha256, None


def start_tier2_background(
    *,
    worktree: Path,
    phase_slug: str,
    phase_head: str | None = None,
    session_name: str | None = None,
    log_dir: Path | None = None,
    suite_command: str | None = None,
    allow_dirty: bool = False,
    tmux: str = "tmux",
    runner: Any = None,
) -> Tier2Start | Tier2Result:
    """Start the README suite in a detached tmux session; return immediately.

    On dirty-pass refusal, returns a ``Tier2Result`` with ``refuse=True`` and
    does not start tmux. ``runner`` is an optional callable used by tests to
    fake ``subprocess.run`` for tmux (signature like ``subprocess.run``).
    """
    work = worktree.resolve()
    head = phase_head or git_head(work)
    revision, _diff, refuse_msg = resolve_tier2_revision(
        work, allow_dirty=allow_dirty, provisional_result="pass",
    )
    if refuse_msg:
        return Tier2Result(
            exit_code=3,
            duration_s=0.0,
            output="",
            output_sha256=_output_sha256(""),
            failing_node_ids=[],
            result="blocked",
            revision=revision,
            refuse=True,
            refuse_message=refuse_msg,
        )

    slug = phase_slug.strip()
    name = session_name or f"se-tier2-{slug}"
    out_dir = (log_dir or (work / ".tier2")).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / f"{name}.log"
    exit_path = out_dir / f"{name}.exit"
    for path in (log_path, exit_path):
        if path.exists():
            path.unlink()

    cmd = suite_command or readme_suite_command()
    # Record exit code after the chain; keep full stdout/stderr in the log.
    inner = (
        f"cd {shlex.quote(str(work))} && "
        f"({{ {cmd}; }}; ec=$?; echo $ec > {shlex.quote(str(exit_path))}; "
        f"exit $ec) >{shlex.quote(str(log_path))} 2>&1"
    )
    tmux_args = [
        tmux,
        "new-session",
        "-d",
        "-s",
        name,
        "-c",
        str(work),
        f"bash -lc {shlex.quote(inner)}",
    ]
    run = runner or subprocess.run
    run(tmux_args, check=False, capture_output=True, text=True)
    return Tier2Start(
        session_name=name,
        worktree=work,
        phase_slug=slug,
        phase_head=head,
        log_path=log_path,
        exit_path=exit_path,
        started_monotonic=time.monotonic(),
        blocking=False,
    )


def tier2_job_finished(job: Tier2Start) -> bool:
    return job.exit_path.is_file()


def poll_tier2(
    job: Tier2Start,
    *,
    allow_dirty: bool = False,
) -> Tier2Result | None:
    """If the background job finished, return a ``Tier2Result``; else ``None``."""
    if not tier2_job_finished(job):
        return None
    return collect_tier2(job, allow_dirty=allow_dirty)


def collect_tier2(
    job: Tier2Start,
    *,
    allow_dirty: bool = False,
) -> Tier2Result:
    """Read exit code / log for a finished (or finishing) job."""
    output = ""
    if job.log_path.is_file():
        output = job.log_path.read_text(encoding="utf-8", errors="replace")
    exit_code = 1
    if job.exit_path.is_file():
        raw = job.exit_path.read_text(encoding="utf-8", errors="replace").strip()
        try:
            exit_code = int(raw.splitlines()[-1])
        except (ValueError, IndexError):
            exit_code = 1
    duration = max(0.0, time.monotonic() - job.started_monotonic)
    result = map_process_outcome(exit_code=exit_code)
    revision, diff, refuse_msg = resolve_tier2_revision(
        job.worktree,
        allow_dirty=allow_dirty,
        provisional_result=result,
    )
    if refuse_msg:
        return Tier2Result(
            exit_code=3,
            duration_s=round(duration, 6),
            output=output,
            output_sha256=_output_sha256(output),
            failing_node_ids=parse_failing_node_ids(output),
            result="blocked",
            revision=revision,
            diff_sha256=diff,
            refuse=True,
            refuse_message=refuse_msg,
        )
    # Prefer the captured phase head when the tree stayed clean at that SHA.
    if revision not in ("dirty",) and job.phase_head:
        revision = job.phase_head
    nodes = parse_failing_node_ids(output) if result == "fail" else []
    return Tier2Result(
        exit_code=exit_code,
        duration_s=round(duration, 6),
        output=output,
        output_sha256=_output_sha256(output),
        failing_node_ids=nodes,
        result=result,
        revision=revision,
        diff_sha256=diff,
    )


def build_tier2_check_run_payload(
    *,
    phase_slug: str,
    effort: str,
    tier2: Tier2Result,
    criterion_id: str | None = None,
) -> dict[str, Any]:
    """Parent-only payload for the tier-2 ``project:check-run``."""
    subject = tier2_subject(phase_slug)
    payload: dict[str, Any] = {
        "criterion_id": criterion_id or subject,
        "revision": tier2.revision,
        "result": tier2.result,
        "effort": effort,
        "method": METHOD,
        "signed_by": "",
        "evidence_kind": EVIDENCE_KIND,
        "runner": RUNNER,
        "duration_s": tier2.duration_s,
        "output_sha256": tier2.output_sha256,
        "exit_code": tier2.exit_code,
    }
    if tier2.diff_sha256:
        payload["diff_sha256"] = tier2.diff_sha256
    if tier2.failing_node_ids:
        payload["failing_node_ids"] = json.dumps(tier2.failing_node_ids)
    return payload


def is_tier2_check_run(run: Mapping[str, Any], *, phase_slug: str | None = None) -> bool:
    evidence = str(run.get("evidence_kind") or "")
    if evidence != EVIDENCE_KIND:
        return False
    subject = str(run.get("subject") or "")
    criterion = str(run.get("criterion_id") or "")
    if phase_slug:
        expected = tier2_subject(phase_slug)
        return subject == expected or criterion == expected or is_tier2_subject(subject)
    return is_tier2_subject(subject) or is_tier2_subject(criterion)


def acceptance_passes_at_head(
    *,
    acceptance_id: str,
    check_runs: Sequence[Mapping[str, Any]],
    phase_head: str,
) -> bool:
    """True when a runner check-run for this criterion passes at the phase head."""
    matching: list[Mapping[str, Any]] = []
    for run in check_runs:
        if str(run.get("criterion_id") or "") != acceptance_id:
            continue
        if is_tier2_check_run(run):
            continue
        if str(run.get("method") or "") == "review":
            continue
        if not _revision_matches(str(run.get("revision") or ""), phase_head):
            continue
        matching.append(run)
    if not matching:
        return False
    # Prefer last in list (callers should pass chronological order).
    latest = matching[-1]
    return str(latest.get("result") or "") == "pass"


def tier2_pass_at_head(
    *,
    check_runs: Sequence[Mapping[str, Any]],
    phase_head: str,
    phase_slug: str,
) -> bool:
    for run in check_runs:
        if not is_tier2_check_run(run, phase_slug=phase_slug):
            continue
        if str(run.get("result") or "") != "pass":
            continue
        if _revision_matches(str(run.get("revision") or ""), phase_head):
            return True
    return False


def phase_tier2_gate_holds(
    *,
    acceptances: Sequence[Mapping[str, Any]],
    check_runs: Sequence[Mapping[str, Any]],
    phase_head: str,
    phase_slug: str,
) -> bool:
    """Merge gate: every active acceptance pass@head plus tier-2 pass@head.

    Missing or failing tier-2 blocks merge. Acceptances without a runner
    pass at the phase head also block.
    """
    for acc in acceptances:
        state = str(acc.get("lifecycle_state") or "active")
        if state in ("withdrawn", "superseded"):
            continue
        acc_id = str(acc.get("id") or acc.get("criterion_id") or "")
        if not acc_id:
            continue
        if not acceptance_passes_at_head(
            acceptance_id=acc_id,
            check_runs=check_runs,
            phase_head=phase_head,
        ):
            return False
    if not tier2_pass_at_head(
        check_runs=check_runs,
        phase_head=phase_head,
        phase_slug=phase_slug,
    ):
        return False
    return True


def record_tier2_check_run(
    *,
    store_root: Path,
    phase_slug: str,
    effort: str,
    tier2: Tier2Result,
    criterion_id: str | None = None,
) -> dict[str, Any]:
    """Create the tier-2 check-run via adaptive-artifacts (parent session only)."""
    if tier2.refuse:
        raise RuntimeError(tier2.refuse_message or "refusing tier-2 check-run")
    subject = tier2_subject(phase_slug)
    payload = build_tier2_check_run_payload(
        phase_slug=phase_slug,
        effort=effort,
        tier2=tier2,
        criterion_id=criterion_id,
    )
    body_parts = [_body_tail(tier2.output)]
    if tier2.failing_node_ids:
        body_parts.append(
            "\n## Failing node IDs\n\n"
            + "\n".join(f"- {n}" for n in tier2.failing_node_ids)
        )
    return aa.create_record(
        store_root,
        record_type="project:check-run",
        subject=subject,
        payload=payload,
        body="\n".join(body_parts),
    )


def orphan_recovery_hint(job: Tier2Start) -> str:
    """Document how to recover if the tmux job is orphaned."""
    return (
        f"Orphaned tier-2: reattach with `tmux attach -t {job.session_name}` "
        f"or inspect `{job.log_path}` / `{job.exit_path}`; "
        f"re-run start_tier2_background in the phase worktree if the session is gone."
    )
