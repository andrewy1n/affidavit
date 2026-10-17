---
{
  "base_kind": "phase",
  "id": "rec-206dc7a5-a4a7-4e2e-ad14-8c28cab7ed68",
  "identity": "unknown",
  "lifecycle_state": "planned",
  "payload": {
    "effort": "evidence-layer",
    "ordinal": 4,
    "title": "Phase-end evidence report"
  },
  "record_type": "project:phase",
  "recorded_at": "2026-10-17T04:46:20+00:00",
  "relationships": {},
  "revision": "sha256:7dc03d2cabe51770dbeb6bcb387c6f56ace857e05665ab8c185797936f9c1f5d",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "phase-end-evidence"
}
---

## Problem

Code can change in ways no requirement asked for, and tests can be blind to hunks they execute. The phase-end reviewer agent is not the desired gate.

## Approach

not yet scoped — discuss when this phase is current. Direction: advisory phase-end report (hunk revert, capped LLM mutants, differential where pure), survivors to oracle author, unexplained changes as Needs-you.

## Exit criteria

Decide at plan-phase. At minimum: phase end produces an evidence report with unnoticed hunks and unexplained behavior deltas, advisory (does not block Landing).
