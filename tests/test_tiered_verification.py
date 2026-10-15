"""Tier-2 background suite, check-run metadata, gate, and fix clustering."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from conftest import REPO_ROOT
from skill_extraction import extract_invocations

sys.path.insert(0, str(REPO_ROOT))

from affidavit.tier2 import (  # noqa: E402
    EVIDENCE_KIND,
    METHOD,
    build_tier2_check_run_payload,
    cluster_by_module,
    module_fix_subject,
    orphan_recovery_hint,
    parse_failing_node_ids,
    phase_tier2_gate_holds,
    poll_tier2,
    readme_suite_command,
    route_tier2_failures,
    should_rerun_tier2,
    start_tier2_background,
    tier2_subject,
    Tier2Result,
    Tier2Start,
)

SKILL = REPO_ROOT / "skills" / "execute-phase" / "SKILL.md"
README = REPO_ROOT / "README.md"

HEAD = "abcdef0123456789abcdef0123456789abcdef01"
PHASE = "tiered-verification"


def _skill_text() -> str:
    return SKILL.read_text()


def _skill_flat() -> str:
    return re.sub(r"\s+", " ", _skill_text())


def _fake_tmux_runner(calls: list):
    def runner(args, **kwargs):
        calls.append(list(args))

        class R:
            returncode = 0
            stdout = ""
            stderr = ""

        return R()

    return runner


def test_background_tmux_start_is_non_blocking(tmp_path: Path):
    work = tmp_path / "wt"
    work.mkdir()
    (work / ".git").mkdir()
    # Minimal git so git_head works: init a real repo.
    import subprocess

    subprocess.run(["git", "init"], cwd=work, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "t@example.com"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "t"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    (work / "README").write_text("x\n")
    subprocess.run(["git", "add", "README"], cwd=work, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "init"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=work,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    calls: list = []
    started = start_tier2_background(
        worktree=work,
        phase_slug=PHASE,
        phase_head=head,
        log_dir=tmp_path / "logs",
        suite_command="echo ok",
        runner=_fake_tmux_runner(calls),
    )
    assert isinstance(started, Tier2Start)
    assert started.blocking is False
    assert calls, "tmux must be invoked"
    assert "-d" in calls[0], "tmux session must be detached (non-blocking)"
    assert "new-session" in calls[0]
    assert started.session_name.startswith("se-tier2-")
    # Parent returns before suite finishes: exit file not written by start.
    assert not started.exit_path.exists()


def test_runner_records_tier2_check_run_payload_fields():
    tier2 = Tier2Result(
        exit_code=1,
        duration_s=12.5,
        output=(
            "FAILED tests/test_foo.py::test_a\n"
            "FAILED tests/test_bar.py::test_b\n"
        ),
        output_sha256="deadbeef" * 8,
        failing_node_ids=[
            "tests/test_foo.py::test_a",
            "tests/test_bar.py::test_b",
        ],
        result="fail",
        revision=HEAD,
    )
    payload = build_tier2_check_run_payload(
        phase_slug=PHASE,
        effort="workflow-loop",
        tier2=tier2,
    )
    assert payload["revision"] == HEAD
    assert payload["exit_code"] == 1
    assert payload["duration_s"] == 12.5
    assert payload["output_sha256"] == "deadbeef" * 8
    assert payload["evidence_kind"] == EVIDENCE_KIND == "integration"
    assert payload["method"] == METHOD
    assert payload["runner"] == "aff"
    assert json.loads(payload["failing_node_ids"]) == [
        "tests/test_foo.py::test_a",
        "tests/test_bar.py::test_b",
    ]
    assert payload["criterion_id"] == tier2_subject(PHASE)


def test_tmux_poll_collects_check_run_ready_result(tmp_path: Path):
    work = tmp_path / "wt"
    work.mkdir()
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    job = Tier2Start(
        session_name="se-tier2-demo",
        worktree=work,
        phase_slug="demo",
        phase_head=HEAD,
        log_path=log_dir / "se-tier2-demo.log",
        exit_path=log_dir / "se-tier2-demo.exit",
        started_monotonic=0.0,
        blocking=False,
    )
    assert poll_tier2(job) is None
    job.log_path.write_text("1 passed\n")
    job.exit_path.write_text("0\n")
    # collect without git: patch via allow_dirty path needs git; use collect after
    # writing files and monkeypatch resolve through a clean worktree with git.
    import subprocess

    subprocess.run(["git", "init"], cwd=work, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "t@example.com"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "t"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    (work / "f").write_text("1\n")
    subprocess.run(["git", "add", "f"], cwd=work, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "c"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=work,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    job.phase_head = head
    result = poll_tier2(job)
    assert result is not None
    assert result.exit_code == 0
    assert result.result == "pass"
    assert result.revision == head
    assert result.output_sha256
    assert result.failing_node_ids == []


def test_parse_failing_node_ids_and_digest_meta():
    output = """
=========================== FAILURES ===========================
FAILED tests/test_a.py::test_one - AssertionError
FAILED tests/test_b.py::TestCls::test_two - AssertionError
=========================== short test summary info ===========================
FAILED tests/test_a.py::test_one
FAILED tests/test_b.py::TestCls::test_two
"""
    nodes = parse_failing_node_ids(output)
    assert "tests/test_a.py::test_one" in nodes
    assert "tests/test_b.py::TestCls::test_two" in nodes
    tier2 = Tier2Result(
        exit_code=1,
        duration_s=1.0,
        output=output,
        output_sha256="abc",
        failing_node_ids=nodes,
        result="fail",
        revision=HEAD,
    )
    payload = build_tier2_check_run_payload(
        phase_slug=PHASE, effort="workflow-loop", tier2=tier2,
    )
    assert "failing_node_ids" in payload
    assert payload["evidence_kind"] == "integration"
    assert "output_sha256" in payload


def test_phase_gate_requires_acceptances_and_tier2_at_head():
    acc_a = {"id": "acc-a", "lifecycle_state": "active"}
    acc_b = {"id": "acc-b", "lifecycle_state": "active"}
    runs_ok = [
        {
            "criterion_id": "acc-a",
            "revision": HEAD,
            "result": "pass",
            "method": "tdd",
            "runner": "aff",
        },
        {
            "criterion_id": "acc-b",
            "revision": HEAD,
            "result": "pass",
            "method": "check",
            "runner": "aff",
        },
        {
            "subject": tier2_subject(PHASE),
            "criterion_id": tier2_subject(PHASE),
            "revision": HEAD,
            "result": "pass",
            "method": "check",
            "evidence_kind": "integration",
            "runner": "aff",
        },
    ]
    assert (
        phase_tier2_gate_holds(
            acceptances=[acc_a, acc_b],
            check_runs=runs_ok,
            phase_head=HEAD,
            phase_slug=PHASE,
        )
        is True
    )
    # Missing tier-2 blocks merge.
    assert (
        phase_tier2_gate_holds(
            acceptances=[acc_a, acc_b],
            check_runs=runs_ok[:-1],
            phase_head=HEAD,
            phase_slug=PHASE,
        )
        is False
    )
    # Failing tier-2 blocks merge.
    failing = list(runs_ok)
    failing[-1] = {**failing[-1], "result": "fail"}
    assert (
        phase_tier2_gate_holds(
            acceptances=[acc_a, acc_b],
            check_runs=failing,
            phase_head=HEAD,
            phase_slug=PHASE,
        )
        is False
    )
    # Acceptance pass at wrong SHA blocks.
    wrong = list(runs_ok)
    wrong[0] = {**wrong[0], "revision": "0000000000000000000000000000000000000000"}
    assert (
        phase_tier2_gate_holds(
            acceptances=[acc_a, acc_b],
            check_runs=wrong,
            phase_head=HEAD,
            phase_slug=PHASE,
        )
        is False
    )
    flat = _skill_flat()
    assert "tier-2" in flat or "tier2" in flat
    assert "phase-head" in flat or "phase head" in flat
    assert "blocks merge" in flat or "Missing or failing tier-2" in flat


def test_fix_cluster_budget_no_inline_rerun():
    nodes = [
        "tests/test_foo.py::test_a",
        "tests/test_foo.py::test_b",
        "tests/test_bar.py::test_c",
    ]
    clusters = cluster_by_module(nodes)
    assert set(clusters) == {"tests/test_foo.py", "tests/test_bar.py"}
    assert module_fix_subject("tests/test_foo.py") == "fix-test_foo"
    routed = route_tier2_failures(nodes, fix_budget_remaining=1)
    assert routed.reopen_done is False
    assert routed.inline_fix_and_rerun is False
    assert sum(routed.create_fix_flags) == 1
    assert routed.escalate is True
    routed2 = route_tier2_failures(nodes, fix_budget_remaining=3)
    assert sum(routed2.create_fix_flags) == 2
    assert all(s.startswith("fix-") for s in routed2.fix_subjects)
    assert should_rerun_tier2(fix_tasks_created=sum(routed2.create_fix_flags))
    assert not should_rerun_tier2(fix_tasks_created=0)
    flat = _skill_flat()
    assert "cluster" in flat or "failing test file" in flat or "module" in flat
    assert "inline" in flat and ("fix-and-rerun" in flat or "fix and rerun" in flat or "fix-and-rerun" in _skill_text())
    assert "never reopen" in flat or ("never" in flat and "`done`" in flat)
    assert "retry" in flat and "budget" in flat


def test_execute_phase_documents_tier2_after_reviewer_and_check_run():
    text = _skill_text()
    flat = _skill_flat()
    assert "tier-2" in flat
    assert "background" in flat or "detached tmux" in flat
    assert "affidavit.tier2" in text or "start_tier2_background" in text
    review_at = flat.index("reviewer")
    tier_at = flat.index("tier-2")
    # Phase-end order names reviewer before tier-2.
    order = text.index("Phase-end order")
    segment = text[order : order + 400]
    assert segment.index("reviewer") < segment.index("tier-2")
    creates = [
        inv
        for inv in extract_invocations(text)
        if inv["subcommand"] == "create" and inv["type"] == "project:check-run"
    ]
    tier2_creates = [
        inv
        for inv in creates
        if "-tier2" in (inv.get("subject") or "")
        or "-tier2" in (inv.get("raw") or "")
    ]
    assert tier2_creates, "execute-phase must document creating a tier-2 check-run"
    raw = tier2_creates[0]["raw"]
    assert "evidence_kind" in raw and "integration" in raw
    assert "output_sha256" in raw
    assert "failing_node_ids" in raw
    assert "orphan" in flat or "reattach" in flat
    assert orphan_recovery_hint(
        Tier2Start(
            session_name="se-tier2-x",
            worktree=Path("/tmp"),
            phase_slug="x",
            phase_head=HEAD,
            log_path=Path("/tmp/a.log"),
            exit_path=Path("/tmp/a.exit"),
            started_monotonic=0.0,
        )
    )


def test_readme_suite_command_matches_testing_section():
    cmd = readme_suite_command()
    assert '-n 4 -m "not tmux"' in cmd
    assert "-m tmux" in cmd
    readme = README.read_text()
    assert "tier-2" in readme or "tier2" in readme
    assert "phase-level" in readme or "phase level" in readme
    assert '-n 4 -m "not tmux"' in readme


def test_evidence_kind_integration_not_regression():
    tier2 = Tier2Result(
        exit_code=0,
        duration_s=1.0,
        output="ok",
        output_sha256="x",
        failing_node_ids=[],
        result="pass",
        revision=HEAD,
    )
    payload = build_tier2_check_run_payload(
        phase_slug=PHASE, effort="workflow-loop", tier2=tier2,
    )
    assert payload["evidence_kind"] == "integration"
    assert payload["evidence_kind"] != "regression"
    # Contract must allow the field.
    design = json.loads((REPO_ROOT / "contract" / "project-design.json").read_text())
    check = next(r for r in design["records"] if r["name"] == "check-run")
    assert "failing_node_ids" in check["optional_payload"]
    assert "integration" in check["payload_enum"]["evidence_kind"]
