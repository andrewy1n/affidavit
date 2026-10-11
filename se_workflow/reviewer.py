"""Build a phase-end reviewer brief with restricted inputs (no builder self-grades)."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, Mapping, Sequence

# Kinds the reviewer must never see (builder self-grades / dispatch notes).
EXCLUDED_KINDS = frozenset(
    {
        "execution-report",
        "check-run",
        "assessment",
        "assignment",
        "assignment-amendment",
    }
)

# Store-derived text the brief may include.
ALLOWED_KINDS = frozenset(
    {
        "work-item",
        "acceptance",
        "requirement",
        "specification",
        "design",
    }
)


def _short_kind(record_type: str) -> str:
    name = (record_type or "").strip()
    if ":" in name:
        name = name.split(":", 1)[1]
    return name


def is_excluded_kind(record_type: str) -> bool:
    return _short_kind(record_type) in EXCLUDED_KINDS


def filter_reviewer_records(
    records: Sequence[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    """Drop excluded kinds; keep only allowed task/spec text."""
    kept: list[Mapping[str, Any]] = []
    for record in records:
        kind = _short_kind(str(record.get("record_type") or record.get("kind") or ""))
        if kind in EXCLUDED_KINDS:
            continue
        if kind and kind not in ALLOWED_KINDS:
            continue
        kept.append(record)
    return kept


def phase_diff_range(base: str, phase_head: str) -> str:
    return f"{base}..{phase_head}"


def git_phase_diff(
    cwd: Path,
    *,
    base: str = "main",
    phase_head: str = "HEAD",
) -> str:
    """Return `git diff <base>..<phase-head>` text (empty string on failure)."""
    result = subprocess.run(
        ["git", "-C", str(cwd), "diff", f"{base}..{phase_head}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return ""
    return result.stdout or ""


def _record_text(record: Mapping[str, Any]) -> str:
    parts: list[str] = []
    title = record.get("title") or record.get("subject") or ""
    subject = record.get("subject") or ""
    if title:
        parts.append(f"**{title}**" + (f" (`{subject}`)" if subject and subject != title else ""))
    criterion = record.get("criterion")
    if criterion:
        parts.append(f"**criterion**: {criterion}")
    body = record.get("body") or record.get("text") or ""
    if body:
        parts.append(str(body).rstrip())
    return "\n\n".join(parts)


def build_reviewer_brief(
    *,
    records: Sequence[Mapping[str, Any]],
    phase_diff: str,
    base: str = "main",
    phase_head: str = "HEAD",
) -> str:
    """Compose the reviewer brief from allowed records plus the phase diff.

    Strips execution-report, check-run, assessment, and assignment content
    even if present in ``records``.
    """
    allowed = filter_reviewer_records(records)
    sections: list[str] = [
        "# Reviewer brief",
        "",
        "Inputs are limited to work-item descriptions/Approach goals, "
        "acceptances, requirements/invariants, and the phase diff. "
        "Execution reports, check-runs, assessments, and assignment notes "
        "are excluded.",
        "",
    ]

    by_kind: dict[str, list[Mapping[str, Any]]] = {}
    for record in allowed:
        kind = _short_kind(str(record.get("record_type") or record.get("kind") or "work-item"))
        by_kind.setdefault(kind, []).append(record)

    heading = {
        "work-item": "Work items",
        "acceptance": "Acceptance criteria",
        "requirement": "Requirements",
        "specification": "Specification",
        "design": "Design / invariants",
    }
    for kind in ("work-item", "acceptance", "requirement", "specification", "design"):
        items = by_kind.get(kind) or []
        if not items:
            continue
        sections.append(f"## {heading[kind]}")
        sections.append("")
        for item in items:
            text = _record_text(item)
            if text:
                sections.append(text)
                sections.append("")

    diff_label = phase_diff_range(base, phase_head)
    sections.append("## Phase diff")
    sections.append("")
    sections.append(f"`git diff {diff_label}`")
    sections.append("")
    sections.append("```diff")
    sections.append(phase_diff.rstrip() if phase_diff else "(empty)")
    sections.append("```")
    sections.append("")

    return "\n".join(sections)
