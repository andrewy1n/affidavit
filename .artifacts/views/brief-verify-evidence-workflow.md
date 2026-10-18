# Brief: verify-evidence-workflow

> Derived brief — not authoritative. Composed on demand from `project:brief`; edit records, not this file.

## Work Item

### verify-evidence-workflow
**title**: Verify evidence-workflow; **phase**: evidence-workflow; **kind**: deliver; **effort**: evidence-layer; state: in_progress

## Description

Prove the phase exit criteria hold together: skill policy text, linkage path, and orchestra no-mode fixture tests pass through the real pytest entry point in the orchestra checkout.

## Approach

In the orchestra worktree, run the phase's orchestra tests for record-versus-bind policy and confirm aff --help still has no record-versus-bind mode. Do not call adaptive-artifacts.

## Acceptance Criteria

### verify-evidence-workflow
**method**: check; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_verify_work_names_when_to_record_an_observation_versus_aff_bind -q; state: active

### verify-evidence-workflow-execute
**method**: check; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_execute_phase_names_when_bind_or_recheck_before_a_claim_is_earned -q; state: active

### verify-evidence-workflow-fixture
**method**: tdd; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_fixture_skill_inventing_an_aff_mode_fails_the_scanner tests/test_record_bind_policy.py::test_live_skills_pass_the_scanner_when_policy_is_present -q; state: active

### verify-evidence-workflow-linkage
**method**: check; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_verify_or_execute_skill_shows_claim_binding_observation_linkage -q; state: active

### verify-evidence-workflow-nomode
**method**: check; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_aff_has_no_record_versus_bind_mode_and_policy_lives_in_skills -q; state: active

## Findings

_None._

## Constraints

### campaign-landing-automerge
**statement**: For evidence-layer phases 5-11, Landing merges the phase branch into main and commits the store without asking; push is not a human stop; **applies_to**: Landing close for evidence-layer phases frozen-environment through audit-differential; **effort**: evidence-layer; state: active

## Basis

The campaign is autonomous after discuss. Merge and store commit are mechanical once the phase gate holds. Push stays off unless a later stop names it.

### phase-end-reviewer-milestones
**statement**: For evidence-layer phases 5-11, run the phase-end se-reviewer only on frozen-environment and audit-differential; skip reviewer, review check-run requirement, and integration-report on signed-verdict, oracle-provenance, evidence-kind, claim-authoring, and phase-end-evidence; **applies_to**: execute-phase phase-end for evidence-layer phases frozen-environment through audit-differential; **effort**: evidence-layer; state: active

## Basis

The owner asked not to run a reviewer agent at the end of every phase. Bookend review on the first and last phase of this batch keeps an independent grade without seven reviewer passes. Until orchestra encodes this, the parent honors it as an effort constraint (soft override of the deliver review@head gate for the skipped phases).

## Position

### evidence-layer
**position**: evidence-technique-ingest done; next evidence-workflow; **scope**: effort; state: active

### evidence-workflow
**position**: planning evidence-workflow tasks; **scope**: phase; state: active

## Unapplied Amendments

_None._
