"""Fail closed if verify-work or close_batch invent binary check-runs for tdd/check.

R5 / check-run-authority: tdd/check check-runs come only from
`se-workflow check` (or an already runner-produced id). Agents write
assessments, not invented pass/fail.
"""

from __future__ import annotations

import re
import sys

import pytest

from conftest import REPO_ROOT
from skill_extraction import extract_invocations

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import close_batch  # noqa: E402

SKILL = REPO_ROOT / "skills" / "verify-work" / "SKILL.md"
SCRIPT = REPO_ROOT / "scripts" / "close_batch.py"


def _skill() -> str:
    return SKILL.read_text()


def _normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def test_skill_documents_se_workflow_check_for_tdd_and_check():
    text = _skill()
    flat = _normalized(text)
    assert "se-workflow check" in text
    assert "--acceptance" in text
    assert "Do **not** `adaptive-artifacts create --type" in text
    assert "project:check-run` for `method` `tdd` or `check`" in flat or (
        "for `method` `tdd` or `check`" in text
    )
    assert "assessment" in flat


def test_skill_does_not_document_hand_create_for_tdd_or_check_methods():
    creates = [
        inv
        for inv in extract_invocations(_skill())
        if inv["subcommand"] == "create"
        and inv["type"] == "project:check-run"
        and inv.get("payload")
    ]
    assert creates, "manual check-run create examples must remain"
    for inv in creates:
        method = inv["payload"].get("method")
        assert method == "manual", (
            f"verify-work must not document create with method={method!r}; "
            "tdd/check check-runs come from se-workflow check"
        )


def test_skill_keeps_assessment_writes():
    assessments = [
        inv
        for inv in extract_invocations(_skill())
        if inv["subcommand"] in {"create", "supersede"}
        and inv["type"] == "project:assessment"
        and inv.get("payload")
    ]
    assert assessments
    assert "next" in assessments[0]["payload"]


def test_skill_close_request_references_check_run_id_for_runner_methods():
    text = _skill()
    assert "check_run_id" in text
    assert '"method": "tdd"' in text or '"method": "tdd"' in text.replace(" ", "")
    # Close examples for tdd/check must not invent revision/signed_by creates.
    close_at = text.index("## Close")
    close = text[close_at:]
    assert "check_run_id" in close
    assert '"method": "tdd"' in close
    assert '"method": "check"' in close
    # Invented create shape must not appear in Close for runner methods.
    assert '"method": "tdd", "revision"' not in close.replace(" ", "")
    assert not re.search(
        r'"method"\s*:\s*"tdd"[^}]*"revision"',
        close,
    )
    assert not re.search(
        r'"method"\s*:\s*"check"[^}]*"revision"',
        close,
    )


def test_close_batch_refuses_invented_tdd_pass_without_check_run_id():
    request = {
        "subject": "task-1",
        "effort": "effort-1",
        "work_item_id": "rec-wi",
        "transition": "done",
        "execution_report_id": None,
        "acceptance_ids": ["rec-ac1"],
        "criteria": [
            {
                "criterion_id": "rec-ac1",
                "result": "pass",
                "method": "tdd",
                "revision": "abc123",
                "signed_by": "",
            }
        ],
        "finding": None,
    }
    with pytest.raises(close_batch.CloseRequestError, match="check_run_id"):
        close_batch.build_batch(request)


def test_close_batch_refuses_invented_check_fail_without_check_run_id():
    request = {
        "subject": "task-1",
        "effort": "effort-1",
        "work_item_id": "rec-wi",
        "transition": "done",
        "execution_report_id": None,
        "acceptance_ids": ["rec-ac1"],
        "criteria": [
            {
                "criterion_id": "rec-ac1",
                "result": "fail",
                "method": "check",
                "revision": "abc123",
                "signed_by": "",
            }
        ],
        "finding": {
            "claim": "gap",
            "basis": "deferred",
            "invalidated_when": "re-run",
            "body": "## Evidence\n\nx\n\n## Consequence\n\ny\n\n## Follow-up\n\nz",
        },
    }
    with pytest.raises(close_batch.CloseRequestError, match="check_run_id"):
        close_batch.build_batch(request)


def test_close_batch_does_not_emit_check_run_create_for_runner_methods():
    ops = close_batch.build_batch(
        {
            "subject": "task-1",
            "effort": "effort-1",
            "work_item_id": "rec-wi",
            "transition": "done",
            "execution_report_id": "rec-er",
            "acceptance_ids": ["rec-ac1"],
            "criteria": [
                {
                    "criterion_id": "rec-ac1",
                    "method": "tdd",
                    "check_run_id": "rec-runner-cr",
                    "result": "pass",
                }
            ],
            "finding": None,
        }
    )
    assert [op["op"] for op in ops] == ["update"]
    assert not any(op.get("type") == "project:check-run" for op in ops)


def test_close_batch_still_creates_manual_check_runs():
    ops = close_batch.build_batch(
        {
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
                    "signed_by": "maintainer",
                }
            ],
            "finding": None,
        }
    )
    assert ops[0]["type"] == "project:check-run"
    assert ops[0]["payload"]["method"] == "manual"
    assert ops[0]["payload"]["result"] == "pass"


def test_close_batch_source_mentions_runner_authority():
    src = SCRIPT.read_text()
    assert "se-workflow check" in src or "runner-produced" in src
    assert "check_run_id" in src
    assert "RUNNER_METHODS" in src
