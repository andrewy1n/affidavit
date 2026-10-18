# Brief: workflow-no-mode-guard

> Derived brief — not authoritative. Composed on demand from `project:brief`; edit records, not this file.

## Work Item

### workflow-no-mode-guard
**title**: Orchestra test: no aff mode for record-versus-bind; **phase**: evidence-workflow; **kind**: deliver; **effort**: evidence-layer; state: planned

## Description

R4: No new aff work-kind, mode flag, or policy switch is added to encode record-versus-bind; policy lives in orchestra skills only.
R5: A check in the orchestra tree fails a fixture skill that invents an aff mode for record-versus-bind, and passes on the updated skills.

## Approach

In the orchestra worktree, add tests that assert live skills do not invent an aff mode for record-versus-bind, and that a forbidden fixture skill inventing such a mode fails the check. Do not change aff CLI. Do not call adaptive-artifacts.

## Acceptance Criteria

### workflow-no-mode-guard
**method**: tdd; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_aff_has_no_record_versus_bind_mode_and_policy_lives_in_skills -q; state: active

### workflow-no-mode-guard-fixture
**method**: tdd; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_fixture_skill_inventing_an_aff_mode_fails_the_scanner tests/test_record_bind_policy.py::test_live_skills_pass_the_scanner_when_policy_is_present -q; state: active

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
