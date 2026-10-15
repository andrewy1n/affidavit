"""Compatibility shim: suite runner lives in ``affidavit.suite``.

Prefer importing from ``affidavit.suite``. Names here keep older call sites
working; check-run subjects use ``-suite`` (not ``-tier2``).
"""

from __future__ import annotations

from typing import Any

from affidavit.suite import (  # noqa: F401
    EVIDENCE_KIND,
    METHOD,
    SUBJECT_SUFFIX,
    SuiteFixRouting,
    SuitePolicy,
    SuiteResult,
    SuiteStart,
    acceptance_passes_at_head,
    advisory_finding_payload,
    build_suite_check_run_payload,
    cluster_by_module,
    collect_suite,
    is_suite_check_run,
    is_suite_subject,
    load_suite_policy,
    module_fix_subject,
    normalize_suite_policy,
    orphan_recovery_hint,
    parse_failing_node_ids,
    phase_suite_gate_holds,
    poll_suite,
    readme_suite_command,
    record_suite_check_run,
    route_suite_failures,
    should_rerun_suite,
    start_suite_background,
    suite_command_for_policy,
    suite_job_finished,
    suite_pass_at_head,
    suite_subject,
    resolve_suite_revision,
)

# Historical names
Tier2FixRouting = SuiteFixRouting
Tier2Result = SuiteResult
Tier2Start = SuiteStart
tier2_subject = suite_subject
is_tier2_subject = is_suite_subject
should_rerun_tier2 = should_rerun_suite
resolve_tier2_revision = resolve_suite_revision
start_tier2_background = start_suite_background
tier2_job_finished = suite_job_finished
poll_tier2 = poll_suite
collect_tier2 = collect_suite
is_tier2_check_run = is_suite_check_run
tier2_pass_at_head = suite_pass_at_head
phase_tier2_gate_holds = phase_suite_gate_holds
record_tier2_check_run = record_suite_check_run


def build_tier2_check_run_payload(
    *,
    phase_slug: str,
    effort: str,
    tier2: SuiteResult,
    criterion_id: str | None = None,
) -> dict[str, Any]:
    return build_suite_check_run_payload(
        phase_slug=phase_slug,
        effort=effort,
        suite=tier2,
        criterion_id=criterion_id,
    )


def route_tier2_failures(
    node_ids,
    *,
    fix_budget_remaining: int,
    policy: SuitePolicy | None = None,
):
    return route_suite_failures(
        node_ids,
        fix_budget_remaining=fix_budget_remaining,
        policy=policy,
    )
