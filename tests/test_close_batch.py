"""Tests for se-workflow close-batch -- the batch builder behind the
verify-work `close` procedure.

The pure `build_batch` tests exercise the refusal policy directly; the
`test_end_to_end_*` tests drive the real `adaptive-artifacts` CLI (via the
shared `cli`/`resolved_contract` fixtures) to prove the emitted NDJSON is
actually accepted by `apply` and lands the record shape the skill promises.

For tdd/check, check-runs are runner-produced ahead of close; the batch
must not invent them.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

import helpers as h
from conftest import REPO_ROOT
from affidavit import close_batch

CLI = REPO_ROOT / "bin" / "aff"

RUNNER = "aff"


def _tdd_pass_only_entry(**extra):
    entry = {
        "criterion_id": "rec-ac1",
        "method": "tdd",
        "check_run_id": "rec-runner-cr",
        "result": "pass",
    }
    entry.update(extra)
    return entry


def _tdd_with_dirty_red(**extra):
    """Valid fail→pass via dirty red + diff_sha256 (no git ancestry needed)."""
    entry = {
        "criterion_id": "rec-ac1",
        "method": "tdd",
        "check_run_id": "rec-runner-green",
        "result": "pass",
        "revision": "deadbeef",
        "red_check_run_id": "rec-runner-red",
        "red_result": "fail",
        "red_revision": "dirty",
        "red_runner": RUNNER,
        "red_diff_sha256": "a" * 64,
    }
    entry.update(extra)
    return entry


def _request(**overrides):
    base = {
        "subject": "task-1",
        "effort": "effort-1",
        "work_item_id": "rec-wi",
        "transition": "done",
        "execution_report_id": "rec-er",
        "acceptance_ids": ["rec-ac1"],
        "criteria": [_tdd_with_dirty_red()],
        "finding": None,
    }
    base.update(overrides)
    return base


def _matching_loader(request: dict):
    """Echo request-carried check-run fields as store records (unit-test hook)."""
    by_id: dict[str, dict] = {}
    for entry in request.get("criteria", []):
        cid = entry.get("check_run_id")
        if cid:
            payload = {
                "criterion_id": entry["criterion_id"],
                "result": entry.get("result"),
                "runner": entry.get("runner", RUNNER),
                "revision": entry.get("revision", "deadbeef"),
                "method": entry.get("method"),
            }
            by_id[cid] = {"id": cid, "payload": payload}
        red_id = entry.get("red_check_run_id")
        if red_id:
            red_payload = {
                "criterion_id": entry["criterion_id"],
                "result": entry.get("red_result", "fail"),
                "runner": entry.get("red_runner", RUNNER),
                "revision": entry.get("red_revision", "dirty"),
                "method": "tdd",
            }
            if "red_diff_sha256" in entry:
                red_payload["diff_sha256"] = entry["red_diff_sha256"]
            by_id[red_id] = {"id": red_id, "payload": red_payload}

    def load(check_run_id: str) -> dict:
        if check_run_id not in by_id:
            raise LookupError(check_run_id)
        return by_id[check_run_id]

    return load


def _build(request: dict, *, cwd: Path | None = None, load_check_run=None, **kwargs):
    """build_batch with a matching store loader unless one is supplied."""
    loader = load_check_run
    if loader is None and request.get("transition") == "done":
        loader = _matching_loader(request)
    return close_batch.build_batch(
        request, cwd=cwd, load_check_run=loader, **kwargs
    )


def _git(cwd: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(cwd), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def _ancestry_repo(tmp_path: Path) -> tuple[Path, str, str]:
    """Temp git repo with parent (red) → child (green) commits."""
    repo = tmp_path / "ancestry-repo"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "test@example.com")
    _git(repo, "config", "user.name", "Test")
    (repo / "f.txt").write_text("red\n")
    _git(repo, "add", "f.txt")
    _git(repo, "commit", "-m", "red")
    red_sha = _git(repo, "rev-parse", "HEAD")
    (repo / "f.txt").write_text("green\n")
    _git(repo, "add", "f.txt")
    _git(repo, "commit", "-m", "green")
    green_sha = _git(repo, "rev-parse", "HEAD")
    return repo, red_sha, green_sha


def _run_script(
    request: dict,
    tmp_path: Path,
    *,
    cwd: Path | None = None,
    process_cwd: Path | None = None,
) -> tuple[subprocess.CompletedProcess, Path]:
    input_path = tmp_path / "close-request.json"
    input_path.write_text(json.dumps(request))
    out_path = tmp_path / "close-batch.ndjson"
    cmd = [sys.executable, str(CLI), "close-batch", "--input", str(input_path), "--out", str(out_path)]
    if cwd is not None:
        cmd.extend(["--cwd", str(cwd)])
    # process_cwd is the primary checkout (store discovery); --cwd is code HEAD.
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(process_cwd) if process_cwd is not None else None,
    )
    return result, out_path


def _manual_request(**overrides):
    base = {
        "subject": "task-1",
        "effort": "effort-1",
        "work_item_id": "rec-wi",
        "transition": "done",
        "execution_report_id": "rec-er",
        "acceptance_ids": ["rec-ac1"],
        "criteria": [
            {
                "criterion_id": "rec-ac1",
                "method": "manual",
                "result": "pass",
                "revision": "abc123",
                "signed_by": "",
            }
        ],
        "finding": None,
    }
    base.update(overrides)
    return base


# -- build_batch: pure policy tests -----------------------------------


def test_all_pass_runner_batch_is_only_the_transition():
    ops = _build(_request())
    assert [op["op"] for op in ops] == ["update"]
    assert ops[-1] == {
        "op": "update",
        "type": "project:work-item",
        "id": "rec-wi",
        "transition": "done",
        "expected_revision": "@current",
    }


def test_manual_pass_batch_is_one_check_run_then_the_transition():
    ops = _build(_manual_request())
    assert [op["op"] for op in ops] == ["create", "update"]
    check_run = ops[0]
    assert check_run["type"] == "project:check-run"
    assert check_run["subject"] == "task-1"
    assert check_run["payload"]["result"] == "pass"
    assert check_run["payload"]["method"] == "manual"
    assert check_run["rel"] == ["informed_by:rec-ac1", "informed_by:rec-er"]


def test_refuses_done_with_failing_criterion_and_no_finding():
    request = _request(
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "check",
                "check_run_id": "rec-runner-cr",
                "result": "fail",
            }
        ]
    )
    with pytest.raises(close_batch.CloseRefused):
        _build(request)


def test_refuses_done_with_a_criterion_never_checked_at_all():
    request = _request(
        acceptance_ids=["rec-ac1", "rec-ac2"],
        criteria=[_tdd_with_dirty_red()],
    )
    with pytest.raises(close_batch.CloseRefused):
        _build(request)


def test_withdrawn_does_not_require_a_finding_for_a_failing_criterion():
    request = _request(
        transition="withdrawn",
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "check",
                "check_run_id": "rec-runner-cr",
                "result": "fail",
            }
        ],
    )
    ops = _build(request)
    assert ops[-1]["transition"] == "withdrawn"


def test_finding_permits_the_close_and_needs_is_forced_to_human():
    request = _request(
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "check",
                "check_run_id": "rec-runner-cr",
                "result": "fail",
            }
        ],
        finding={
            "claim": "closed with a known gap",
            "basis": "deferred deliberately",
            "invalidated_when": "when re-verified",
            "needs": "none",  # deliberately wrong -- the script must override this
            "body": "## Evidence\n\nx\n\n## Consequence\n\ny\n\n## Follow-up\n\nz",
        },
    )
    ops = _build(request)
    finding_op = next(op for op in ops if op["type"] == "project:finding")
    assert finding_op["payload"]["needs"] == "human"
    assert ops[-1]["op"] == "update" and ops[-1]["transition"] == "done"
    assert not any(op.get("type") == "project:check-run" for op in ops)


def test_no_execution_report_omits_the_second_informed_by_on_manual():
    ops = _build(_manual_request(execution_report_id=None))
    assert ops[0]["rel"] == ["informed_by:rec-ac1"]


def test_criteria_entry_outside_acceptance_ids_is_malformed():
    request = _request(
        criteria=[_tdd_with_dirty_red(criterion_id="rec-not-active")]
    )
    with pytest.raises(close_batch.CloseRequestError):
        _build(request)


def test_missing_top_level_field_is_malformed_not_refused():
    request = _request()
    del request["work_item_id"]
    with pytest.raises(close_batch.CloseRequestError):
        _build(request)


def test_invented_tdd_with_signed_by_is_malformed():
    request = _request(criteria=[_tdd_with_dirty_red(signed_by="agent")])
    with pytest.raises(close_batch.CloseRequestError, match="signed_by"):
        _build(request)


def test_invented_check_with_revision_is_malformed():
    request = _request(
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "check",
                "check_run_id": "rec-runner-cr",
                "result": "pass",
                "revision": "abc123",
            }
        ]
    )
    with pytest.raises(close_batch.CloseRequestError, match="revision"):
        _build(request)


# -- CLI wrapper: exit codes and output-file behavior ------------------


def test_cli_refusal_exits_2_prints_why_and_writes_no_file(tmp_path):
    request = _request(
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "check",
                "check_run_id": "rec-runner-cr",
                "result": "fail",
            }
        ]
    )
    result, out_path = _run_script(request, tmp_path)
    assert result.returncode == 2
    assert "rec-ac1" in result.stderr
    assert not out_path.exists()


def test_cli_fabricated_check_run_id_exits_2_and_writes_no_file(tmp_path):
    """CLI path uses the real store; fabricated ids refuse with no batch."""
    result, out_path = _run_script(_request(), tmp_path)
    assert result.returncode == 2
    assert not out_path.exists()


def test_cli_malformed_json_exits_1(tmp_path):
    input_path = tmp_path / "close-request.json"
    input_path.write_text("{not json")
    out_path = tmp_path / "close-batch.ndjson"
    result = subprocess.run(
        [sys.executable, str(CLI), "close-batch", "--input", str(input_path), "--out", str(out_path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert not out_path.exists()


# -- end to end against the real CLI -----------------------------------


def _build_work_item_family(cli, defs, subject: str, effort: str, *, method: str = "tdd"):
    phase = h.create_generic_record(cli, defs, "project:phase", extra_payload={"effort": effort})
    work_item = h.create_generic_record(
        cli,
        defs,
        "project:work-item",
        subject=subject,
        extra_payload={"effort": effort, "phase": phase["subject"], "kind": "deliver"},
    )
    work_item = h._apply_transition(
        cli, defs["project:work-item"], "project:work-item", work_item, "in_progress"
    )
    acceptance = h.create_generic_record(
        cli,
        defs,
        "project:acceptance",
        subject=subject,
        extra_payload={"effort": effort, "phase": phase["subject"], "method": method},
    )
    assignment = h.create_generic_record(
        cli,
        defs,
        "project:assignment",
        subject=subject,
        extra_payload={"effort": effort, "work_item": subject},
    )
    execution_report = h.create_generic_record(
        cli,
        defs,
        "project:execution-report",
        subject=subject,
        extra_payload={
            "work_item": subject,
            "assignment": assignment["subject"],
            "result": "pass",
            "verdict": "pass",
            "revision": "deadbeef",
        },
    )
    return work_item, acceptance, execution_report


def _seed_runner_check_run(
    cli,
    defs,
    subject,
    acceptance,
    execution_report,
    *,
    result="pass",
    revision="deadbeef",
    diff_sha256=None,
):
    payload = {
        "criterion_id": acceptance["id"],
        "revision": revision,
        "result": result,
        "effort": acceptance["payload"]["effort"],
        "method": acceptance["payload"]["method"],
        "signed_by": "",
        "runner": "aff",
    }
    if diff_sha256 is not None:
        payload["diff_sha256"] = diff_sha256
    args = [
        "create",
        "--type",
        "project:check-run",
        "--subject",
        subject,
        "--payload",
        json.dumps(payload),
        "--rel",
        f"informed_by:{acceptance['id']}",
        "--rel",
        f"informed_by:{execution_report['id']}",
    ]
    body = h.generic_body(defs["project:check-run"])
    if body:
        args.extend(["--body", body])
    created = cli(*args)
    assert created.returncode == 0, created.stdout + created.stderr
    return json.loads(created.stdout)["record"]


def test_end_to_end_all_pass_closes_the_work_item_to_done(
    cli, store, resolved_contract, tmp_path
):
    defs = h.record_defs_by_id(resolved_contract)
    subject = "demo-close-task"
    effort = "demo-effort"
    work_item, acceptance, execution_report = _build_work_item_family(cli, defs, subject, effort)
    red_digest = "b" * 64
    red_cr = _seed_runner_check_run(
        cli,
        defs,
        subject,
        acceptance,
        execution_report,
        result="fail",
        revision="dirty",
        diff_sha256=red_digest,
    )
    green_cr = _seed_runner_check_run(cli, defs, subject, acceptance, execution_report)

    request = {
        "subject": subject,
        "effort": effort,
        "work_item_id": work_item["id"],
        "transition": "done",
        "execution_report_id": execution_report["id"],
        "acceptance_ids": [acceptance["id"]],
        "criteria": [
            {
                "criterion_id": acceptance["id"],
                "method": "tdd",
                "check_run_id": green_cr["id"],
                "result": "pass",
                "revision": "deadbeef",
                "red_check_run_id": red_cr["id"],
                "red_result": "fail",
                "red_revision": "dirty",
                "red_runner": RUNNER,
                "red_diff_sha256": red_digest,
            }
        ],
        "finding": None,
    }
    result, out_path = _run_script(request, tmp_path, process_cwd=store)
    assert result.returncode == 0, result.stderr

    apply_result = cli("apply", str(out_path))
    assert apply_result.returncode == 0, apply_result.stdout + apply_result.stderr
    applied = json.loads(apply_result.stdout)
    assert applied["ok"] is True
    assert applied["applied"] == 1
    assert applied["failed"] == 0

    final_work_item = json.loads(cli("get", "--type", "project:work-item", "--id", work_item["id"]).stdout)
    assert final_work_item["lifecycle_state"] == "done"

    check_runs = json.loads(
        cli("list", "--type", "project:check-run", "--subject", subject, "--full").stdout
    )["records"]
    assert len(check_runs) == 2
    by_id = {cr["id"]: cr for cr in check_runs}
    assert by_id[green_cr["id"]]["payload"]["result"] == "pass"
    assert by_id[green_cr["id"]]["payload"].get("runner") == "aff"
    assert by_id[red_cr["id"]]["payload"]["result"] == "fail"


def test_end_to_end_refusal_leaves_the_work_item_in_progress(
    cli, store, resolved_contract, tmp_path
):
    defs = h.record_defs_by_id(resolved_contract)
    subject = "demo-refuse-task"
    effort = "demo-effort"
    work_item, acceptance, execution_report = _build_work_item_family(
        cli, defs, subject, effort, method="check"
    )
    runner_cr = _seed_runner_check_run(
        cli, defs, subject, acceptance, execution_report, result="fail"
    )

    request = {
        "subject": subject,
        "effort": effort,
        "work_item_id": work_item["id"],
        "transition": "done",
        "execution_report_id": execution_report["id"],
        "acceptance_ids": [acceptance["id"]],
        "criteria": [
            {
                "criterion_id": acceptance["id"],
                "method": "check",
                "check_run_id": runner_cr["id"],
                "result": "fail",
            }
        ],
        "finding": None,
    }
    result, out_path = _run_script(request, tmp_path, process_cwd=store)
    assert result.returncode == 2
    assert not out_path.exists()

    final_work_item = json.loads(cli("get", "--type", "project:work-item", "--id", work_item["id"]).stdout)
    assert final_work_item["lifecycle_state"] == "in_progress"


def test_end_to_end_failing_criterion_with_finding_closes_and_surfaces_needs_human(
    cli, store, resolved_contract, tmp_path
):
    defs = h.record_defs_by_id(resolved_contract)
    subject = "demo-deferred-task"
    effort = "demo-effort"
    work_item, acceptance, execution_report = _build_work_item_family(
        cli, defs, subject, effort, method="check"
    )
    runner_cr = _seed_runner_check_run(
        cli, defs, subject, acceptance, execution_report, result="fail"
    )

    request = {
        "subject": subject,
        "effort": effort,
        "work_item_id": work_item["id"],
        "transition": "done",
        "execution_report_id": execution_report["id"],
        "acceptance_ids": [acceptance["id"]],
        "criteria": [
            {
                "criterion_id": acceptance["id"],
                "method": "check",
                "check_run_id": runner_cr["id"],
                "result": "fail",
            }
        ],
        "finding": {
            "claim": f"{subject} closed done with an unmet or unverified criterion",
            "basis": "live verification deliberately deferred",
            "invalidated_when": "the criterion is re-run and passes",
            "body": "## Evidence\n\nthe check-run above\n\n## Consequence\n\nunverified in prod\n\n## Follow-up\n\nre-run before next release",
        },
    }
    result, out_path = _run_script(request, tmp_path, process_cwd=store)
    assert result.returncode == 0, result.stderr

    apply_result = cli("apply", str(out_path))
    assert apply_result.returncode == 0, apply_result.stdout + apply_result.stderr
    applied = json.loads(apply_result.stdout)
    assert applied["applied"] == 2

    final_work_item = json.loads(cli("get", "--type", "project:work-item", "--id", work_item["id"]).stdout)
    assert final_work_item["lifecycle_state"] == "done"

    findings = json.loads(
        cli("list", "--type", "project:finding", "--subject", subject, "--full").stdout
    )["records"]
    assert len(findings) == 1
    assert findings[0]["payload"]["needs"] == "human"


# -- red-first gate (tdd done) ----------------------------------------


def test_red_first_pass_only_refuses_and_names_criterion():
    request = _request(criteria=[_tdd_pass_only_entry()])
    with pytest.raises(close_batch.CloseRefused, match="rec-ac1") as excinfo:
        _build(request)
    assert "red" in str(excinfo.value).lower()


def test_red_first_pass_only_cli_exits_2(tmp_path):
    request = _request(criteria=[_tdd_pass_only_entry()])
    result, out_path = _run_script(request, tmp_path)
    assert result.returncode == 2
    assert "rec-ac1" in result.stderr
    assert not out_path.exists()


def test_red_first_request_accepts_fail_then_pass_with_dirty_red():
    ops = _build(_request(criteria=[_tdd_with_dirty_red()]))
    assert ops[-1]["transition"] == "done"


def test_red_first_request_refuses_non_runner_red():
    request = _request(criteria=[_tdd_with_dirty_red(red_runner="hand-authored")])
    with pytest.raises(close_batch.CloseRefused, match="rec-ac1") as excinfo:
        _build(request)
    assert "runner" in str(excinfo.value).lower()


def test_red_first_request_refuses_red_result_not_fail():
    request = _request(criteria=[_tdd_with_dirty_red(red_result="pass")])
    with pytest.raises(close_batch.CloseRefused, match="rec-ac1") as excinfo:
        _build(request)
    assert "fail" in str(excinfo.value).lower()


def test_red_first_request_resolves_red_from_store_loader():
    """Red-first uses the injectable store loader (production path is aa.get)."""
    request = _request(criteria=[_tdd_with_dirty_red()])
    seen: list[str] = []

    def tracking_loader(check_run_id: str) -> dict:
        seen.append(check_run_id)
        return _matching_loader(request)(check_run_id)

    ops = _build(request, load_check_run=tracking_loader)
    assert ops[-1]["transition"] == "done"
    assert "rec-runner-green" in seen
    assert "rec-runner-red" in seen


def test_red_first_order_accepts_when_green_descends_from_red(tmp_path):
    repo, red_sha, green_sha = _ancestry_repo(tmp_path)
    entry = {
        "criterion_id": "rec-ac1",
        "method": "tdd",
        "check_run_id": "rec-runner-green",
        "result": "pass",
        "revision": green_sha,
        "red_check_run_id": "rec-runner-red",
        "red_result": "fail",
        "red_revision": red_sha,
        "red_runner": RUNNER,
    }
    ops = _build(_request(criteria=[entry]), cwd=repo)
    assert ops[-1]["transition"] == "done"


def test_red_first_order_accepts_equal_sha(tmp_path):
    repo, red_sha, _green_sha = _ancestry_repo(tmp_path)
    entry = {
        "criterion_id": "rec-ac1",
        "method": "tdd",
        "check_run_id": "rec-runner-green",
        "result": "pass",
        "revision": red_sha,
        "red_check_run_id": "rec-runner-red",
        "red_result": "fail",
        "red_revision": red_sha,
        "red_runner": RUNNER,
    }
    ops = _build(_request(criteria=[entry]), cwd=repo)
    assert ops[-1]["transition"] == "done"


def test_red_first_order_refuses_when_green_is_ancestor_of_red(tmp_path):
    """Wrong order: green SHA is parent of red (green does not descend from red)."""
    repo, red_sha, green_sha = _ancestry_repo(tmp_path)
    entry = {
        "criterion_id": "rec-ac1",
        "method": "tdd",
        "check_run_id": "rec-runner-green",
        "result": "pass",
        "revision": red_sha,  # older
        "red_check_run_id": "rec-runner-red",
        "red_result": "fail",
        "red_revision": green_sha,  # newer — not an ancestor of red_sha
        "red_runner": RUNNER,
    }
    with pytest.raises(close_batch.CloseRefused, match="rec-ac1"):
        _build(_request(criteria=[entry]), cwd=repo)


def test_red_first_order_refuses_non_ancestor_on_divergent_history(tmp_path):
    repo, red_sha, green_sha = _ancestry_repo(tmp_path)
    _git(repo, "checkout", "-b", "other", red_sha)
    (repo / "f.txt").write_text("other\n")
    _git(repo, "add", "f.txt")
    _git(repo, "commit", "-m", "side")
    side_sha = _git(repo, "rev-parse", "HEAD")
    entry = {
        "criterion_id": "rec-ac1",
        "method": "tdd",
        "check_run_id": "rec-runner-green",
        "result": "pass",
        "revision": green_sha,
        "red_check_run_id": "rec-runner-red",
        "red_result": "fail",
        "red_revision": side_sha,
        "red_runner": RUNNER,
    }
    with pytest.raises(close_batch.CloseRefused, match="rec-ac1"):
        _build(_request(criteria=[entry]), cwd=repo)


def test_red_first_order_dirty_red_requires_nonempty_diff_sha256():
    request = _request(
        criteria=[_tdd_with_dirty_red(red_diff_sha256="")]
    )
    with pytest.raises(close_batch.CloseRefused, match="rec-ac1") as excinfo:
        _build(request)
    assert "diff_sha256" in str(excinfo.value)


def test_red_first_order_dirty_red_without_digest_refused():
    entry = _tdd_with_dirty_red()
    del entry["red_diff_sha256"]
    # Store red is dirty without digest when request omits red_diff_sha256.
    with pytest.raises(close_batch.CloseRefused, match="rec-ac1"):
        _build(_request(criteria=[entry]))


def test_red_first_escape_permits_tdd_done_without_red_and_forces_human():
    request = _request(
        criteria=[_tdd_pass_only_entry()],
        finding={
            "claim": "closing without red-first evidence for rec-ac1",
            "basis": "refactor-only change; prior red unavailable",
            "invalidated_when": "a runner fail then pass is recorded",
            "needs": "none",
            "body": "## Evidence\n\nno red\n\n## Consequence\n\ngap\n\n## Follow-up\n\nre-verify",
        },
    )
    ops = _build(request)
    finding_op = next(op for op in ops if op["type"] == "project:finding")
    assert finding_op["payload"]["needs"] == "human"
    assert ops[-1]["transition"] == "done"


def test_red_first_other_methods_check_closes_without_red_check_run_id():
    request = _request(
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "check",
                "check_run_id": "rec-runner-cr",
                "result": "pass",
            }
        ]
    )
    ops = _build(request)
    assert ops[-1]["transition"] == "done"
    assert "red_check_run_id" not in request["criteria"][0]


def test_red_first_other_methods_manual_closes_without_red_check_run_id():
    ops = _build(_manual_request())
    assert ops[-1]["transition"] == "done"
    assert [op["op"] for op in ops] == ["create", "update"]


# -- store authority (claim-witnesses) ---------------------------------


def test_store_authority_refuses_fabricated_check_run_id():
    request = _request(criteria=[_tdd_with_dirty_red()])

    def missing(_cid: str) -> dict:
        raise LookupError("fabricated")

    with pytest.raises(close_batch.CloseRefused, match="rec-ac1") as excinfo:
        _build(request, load_check_run=missing)
    assert "not found" in str(excinfo.value).lower() or "fabricated" in str(excinfo.value).lower()


def test_store_authority_refuses_fabricated_red_check_run_id():
    request = _request(criteria=[_tdd_with_dirty_red()])
    base = _matching_loader(request)

    def green_only(cid: str) -> dict:
        if cid == "rec-runner-red":
            raise LookupError(cid)
        return base(cid)

    with pytest.raises(close_batch.CloseRefused, match="rec-ac1") as excinfo:
        _build(request, load_check_run=green_only)
    assert "red" in str(excinfo.value).lower()


def test_store_authority_mismatch_result_refuses():
    request = _request(criteria=[_tdd_with_dirty_red()])
    base = _matching_loader(request)

    def wrong_result(cid: str) -> dict:
        rec = base(cid)
        if cid == "rec-runner-green":
            rec = {
                "id": cid,
                "payload": {**rec["payload"], "result": "fail"},
            }
        return rec

    with pytest.raises(close_batch.CloseRefused, match="mismatch") as excinfo:
        _build(request, load_check_run=wrong_result)
    assert "result" in str(excinfo.value).lower()


def test_store_authority_mismatch_revision_refuses():
    request = _request(criteria=[_tdd_with_dirty_red()])
    base = _matching_loader(request)

    def wrong_revision(cid: str) -> dict:
        rec = base(cid)
        if cid == "rec-runner-green":
            rec = {
                "id": cid,
                "payload": {**rec["payload"], "revision": "otherrev"},
            }
        return rec

    with pytest.raises(close_batch.CloseRefused, match="mismatch") as excinfo:
        _build(request, load_check_run=wrong_revision)
    assert "revision" in str(excinfo.value).lower()


def test_cli_store_authority_fabricated_writes_no_batch(tmp_path):
    result, out_path = _run_script(_request(), tmp_path)
    assert result.returncode == 2
    assert not out_path.exists()


def test_red_store_resolves_and_accepts_dirty_red():
    ops = _build(_request(criteria=[_tdd_with_dirty_red()]))
    assert ops[-1]["transition"] == "done"


def test_red_store_refuses_when_store_red_is_not_fail():
    request = _request(criteria=[_tdd_with_dirty_red()])
    base = _matching_loader(request)

    def red_pass(cid: str) -> dict:
        rec = base(cid)
        if cid == "rec-runner-red":
            # Request still says fail — mismatch on result.
            return {
                "id": cid,
                "payload": {**rec["payload"], "result": "pass"},
            }
        return rec

    with pytest.raises(close_batch.CloseRefused, match="rec-ac1"):
        _build(request, load_check_run=red_pass)


def test_dirty_green_refuses_when_red_is_sha(tmp_path):
    repo, red_sha, _green_sha = _ancestry_repo(tmp_path)
    entry = {
        "criterion_id": "rec-ac1",
        "method": "tdd",
        "check_run_id": "rec-runner-green",
        "result": "pass",
        "revision": "dirty",
        "red_check_run_id": "rec-runner-red",
        "red_result": "fail",
        "red_revision": red_sha,
        "red_runner": RUNNER,
    }
    with pytest.raises(close_batch.CloseRefused, match="dirty") as excinfo:
        _build(_request(criteria=[entry]), cwd=repo)
    assert "green" in str(excinfo.value).lower() or "dirty" in str(excinfo.value).lower()


def test_missing_green_revision_refuses_with_sha_red(tmp_path):
    repo, red_sha, green_sha = _ancestry_repo(tmp_path)
    entry = {
        "criterion_id": "rec-ac1",
        "method": "tdd",
        "check_run_id": "rec-runner-green",
        "result": "pass",
        # revision omitted — mutant a-missing-green-revision-ok
        "red_check_run_id": "rec-runner-red",
        "red_result": "fail",
        "red_revision": red_sha,
        "red_runner": RUNNER,
    }
    # Matching loader still plants a store revision; request omission must refuse.
    loader = _matching_loader(_request(criteria=[{**entry, "revision": green_sha}]))
    with pytest.raises(close_batch.CloseRefused, match="green revision"):
        close_batch.build_batch(
            _request(criteria=[entry]), cwd=repo, load_check_run=loader
        )


def test_tdd_revision_without_red_is_request_error():
    request = _request(
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "tdd",
                "check_run_id": "rec-runner-cr",
                "result": "pass",
                "revision": "abc123",
            }
        ]
    )
    with pytest.raises(close_batch.CloseRequestError, match="revision"):
        _build(request)


def test_revision_allowed_tdd_with_red_fields():
    ops = _build(_request(criteria=[_tdd_with_dirty_red()]))
    assert ops[-1]["transition"] == "done"


def test_missing_check_run_id_is_request_error():
    request = _request(
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "tdd",
                "result": "pass",
            }
        ]
    )
    with pytest.raises(close_batch.CloseRequestError, match="check_run_id"):
        _build(request)


def test_missing_result_is_request_error_not_result_optional_pass():
    request = _request(
        criteria=[
            {
                "criterion_id": "rec-ac1",
                "method": "check",
                "check_run_id": "rec-runner-cr",
            }
        ]
    )
    with pytest.raises(close_batch.CloseRequestError, match="result"):
        _build(request)
