# Brief: workflow-skills-policy

> Derived brief — not authoritative. Composed on demand from `project:brief`; edit records, not this file.

## Work Item

### workflow-skills-policy
**title**: Document record vs bind in verify-work and execute-phase; **phase**: evidence-workflow; **kind**: deliver; **effort**: evidence-layer; state: in_progress

## Description

R1: The orchestra verify-work skill text names when to record an evidence-observation versus when to aff bind an observation to a claim.
R2: The orchestra execute-phase skill text names when bind or recheck is required before treating a manifest claim as earned.
R3: A verify-work or handoff path documented in those skills shows the linkage claim → evidence-binding → evidence-observation.

## Approach

In the orchestra worktree, edit skills/verify-work/SKILL.md and skills/execute-phase/SKILL.md. Add a clear Record versus bind section: techniques/audit may record unbound observations; earning a manifest claim requires aff bind (and recheck when the skill says so). Include one worked path: claim id → evidence-binding → evidence-observation. Do not add aff CLI modes. Do not call adaptive-artifacts.

## Acceptance Criteria

### workflow-skills-policy
**method**: tdd; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_verify_work_names_when_to_record_an_observation_versus_aff_bind -q; state: active

### workflow-skills-policy-execute
**method**: tdd; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_execute_phase_names_when_bind_or_recheck_before_a_claim_is_earned -q; state: active

### workflow-skills-policy-linkage
**method**: tdd; **effort**: evidence-layer; **verify_command**: python3 -m pytest tests/test_record_bind_policy.py::test_verify_or_execute_skill_shows_claim_binding_observation_linkage -q; state: active

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
