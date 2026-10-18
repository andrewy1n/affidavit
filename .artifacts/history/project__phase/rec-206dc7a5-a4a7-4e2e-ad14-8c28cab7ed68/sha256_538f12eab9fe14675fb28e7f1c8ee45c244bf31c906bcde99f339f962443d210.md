---
{
  "base_kind": "phase",
  "id": "rec-206dc7a5-a4a7-4e2e-ad14-8c28cab7ed68",
  "identity": "unknown",
  "lifecycle_state": "planned",
  "payload": {
    "effort": "evidence-layer",
    "ordinal": 10,
    "title": "aff audit: changed code no witness checks"
  },
  "record_type": "project:phase",
  "recorded_at": "2026-10-18T03:08:49+00:00",
  "relationships": {},
  "revision": "sha256:538f12eab9fe14675fb28e7f1c8ee45c244bf31c906bcde99f339f962443d210",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "phase-end-evidence"
}
---

## Problem

Tests can be blind to code they execute. A claim's witness can pass at head while a changed block, or a small bug in it, goes unnoticed.

## Approach

Adopt `audit-hunk-mutants`: `aff audit --base --head` productizes hunk-revert + capped mutants, judges with frozen claim tests via `run_tests`, advisory JSON, never reports test-file blocks. Phase-end reviewer skipped.

## Exit criteria

- On the check-runner range, reports the unnoticed cwd block and at least one surviving mutant from the spike findings.
- Never reports a test-file block.

## Landing

- **branch:** `phase/phase-end-evidence`
- **worktree:** `/home/andrewyin/affidavit--phase-end-evidence`
- **base:** `main`
- **close:** commit code on the phase branch; merge that branch into `main`; commit the store on the primary checkout
- **push:** not a stop (do not push)
