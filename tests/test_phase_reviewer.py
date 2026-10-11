"""Phase-end reviewer: restricted brief excludes builder self-grades."""

from __future__ import annotations

import sys
from pathlib import Path

from conftest import REPO_ROOT

sys.path.insert(0, str(REPO_ROOT))

from se_workflow.reviewer import build_reviewer_brief  # noqa: E402

# Unique markers so exclusion asserts cannot false-pass on incidental text.
MARKER_EXEC = "UNIQUE_EXEC_REPORT_BODY_xyz789"
MARKER_CHECK = "UNIQUE_CHECK_RUN_OUTPUT_xyz789"
MARKER_ASSESS = "UNIQUE_ASSESSMENT_REASON_xyz789"
MARKER_ASSIGN = "UNIQUE_ASSIGNMENT_NOTES_xyz789"
MARKER_TASK = "Implement the status tabs per description"
MARKER_ACCEPT = "Tabs render Active and Done filters"
MARKER_REQ = "R2 reviewer receives only task descriptions"
MARKER_INVARIANT = "Reviewer writes no store records"
MARKER_DIFF = "diff --git a/dashboard/app.py b/dashboard/app.py"


def test_reviewer_brief_excludes_execution_report_check_run_and_assessment():
    records = [
        {
            "record_type": "project:work-item",
            "subject": "status-tabs",
            "title": "status-tabs",
            "body": (
                "## Description\n\n"
                f"{MARKER_TASK}\n\n"
                "## Approach\n\nShip Active and Done tabs."
            ),
        },
        {
            "record_type": "project:acceptance",
            "subject": "status-tabs",
            "title": "status-tabs",
            "body": f"**criterion**: {MARKER_ACCEPT}",
            "criterion": MARKER_ACCEPT,
        },
        {
            "record_type": "project:requirement",
            "subject": "phase-reviewer",
            "title": "R2",
            "body": MARKER_REQ,
        },
        {
            "record_type": "project:design",
            "subject": "phase-reviewer",
            "title": "invariants",
            "body": f"## Invariants\n\n- {MARKER_INVARIANT}",
        },
        {
            "record_type": "project:execution-report",
            "subject": "status-tabs",
            "title": "status-tabs",
            "body": MARKER_EXEC,
        },
        {
            "record_type": "project:check-run",
            "subject": "status-tabs",
            "title": "status-tabs",
            "body": MARKER_CHECK,
            "result": "pass",
        },
        {
            "record_type": "project:assessment",
            "subject": "status-tabs",
            "title": "status-tabs",
            "body": MARKER_ASSESS,
        },
        {
            "record_type": "project:assignment",
            "subject": "status-tabs",
            "title": "status-tabs",
            "body": MARKER_ASSIGN,
        },
    ]

    brief = build_reviewer_brief(
        records=records,
        phase_diff=MARKER_DIFF + "\n+tabs",
        base="main",
        phase_head="abc1234",
    )

    assert MARKER_TASK in brief
    assert MARKER_ACCEPT in brief
    assert MARKER_REQ in brief
    assert MARKER_INVARIANT in brief
    assert MARKER_DIFF in brief
    assert "main..abc1234" in brief or "git diff main..abc1234" in brief

    for marker in (MARKER_EXEC, MARKER_CHECK, MARKER_ASSESS, MARKER_ASSIGN):
        assert marker not in brief, f"excluded content leaked into brief: {marker}"

    lowered = brief.lower()
    for kind in ("execution-report", "check-run", "assessment", "assignment"):
        assert f"## {kind}" not in lowered
        assert f"### {kind}" not in lowered
