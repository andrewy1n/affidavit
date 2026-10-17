---
{
  "base_kind": "phase",
  "id": "rec-47faad46-864c-40bd-baf1-d0d46755ca4b",
  "identity": "unknown",
  "lifecycle_state": "planned",
  "payload": {
    "effort": "evidence-layer",
    "ordinal": 5,
    "title": "End-to-end deliver loop through aff from a phase worktree"
  },
  "record_type": "project:phase",
  "recorded_at": "2026-10-17T04:46:20+00:00",
  "relationships": {},
  "revision": "sha256:a1bf945994d44558b045a771d17ea39e6c5bd612c17110a87b8b96a5fbf593cc",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "evidence-e2e"
}
---

## Problem

The manifest, verdict, split, evidence_kind, and report only prove themselves together, through a real orchestration client running from a phase worktree.

## Approach

not yet scoped — decide at plan-phase.

## Exit criteria

Decide at plan-phase. At minimum: the orchestration client runs a deliver loop end to end (claim, oracle, red, implement, verdict, report) from a phase worktree against this repo's `aff` entry point, verified by an integration test.
