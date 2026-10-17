---
{
  "base_kind": "phase",
  "id": "rec-47faad46-864c-40bd-baf1-d0d46755ca4b",
  "identity": "unknown",
  "lifecycle_state": "planned",
  "payload": {
    "effort": "evidence-layer",
    "ordinal": 13,
    "title": "End to end on an external repo and through orchestra"
  },
  "record_type": "project:phase",
  "recorded_at": "2026-10-17T22:58:47+00:00",
  "relationships": {},
  "revision": "sha256:e9cf8fc7bb6a2b964fa89a83e7e0e04bbf7d698e7774c7a74ac737f244cc9f9c",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "evidence-e2e"
}
---

## Problem

The manifest, verdict, attestation, provenance, and audit only prove themselves together, on a repo that is not this one and through a client that is not affidavit.

## Approach

not yet scoped — decide at plan-phase. Direction: run the full loop on an external repo with no orchestra (claim add, freeze, oracle commit, implement, signed verdict in CI, audit), and run orchestra's deliver loop from a phase worktree against `aff verdict` and `aff audit`.

## Exit criteria

Decide at plan-phase. At minimum: an integration test drives both paths end to end and a gate accepts only the signed verdict.
