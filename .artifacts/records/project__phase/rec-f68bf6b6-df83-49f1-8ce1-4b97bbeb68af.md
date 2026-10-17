---
{
  "base_kind": "phase",
  "id": "rec-f68bf6b6-df83-49f1-8ce1-4b97bbeb68af",
  "identity": "unknown",
  "lifecycle_state": "planned",
  "payload": {
    "effort": "evidence-layer",
    "ordinal": 12,
    "title": "A non-Python runner through the adapter"
  },
  "record_type": "project:phase",
  "recorded_at": "2026-10-17T22:58:47+00:00",
  "relationships": {},
  "revision": "sha256:11f71dafcd0dcb444f79fae3f117dbe021e44ec9aae28d36e80f36838a22c500",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "second-runner"
}
---

## Problem

The runner adapter is unproven until a non-Python suite runs through it.

## Approach

not yet scoped — discuss when this phase is current. Direction: add one non-Python runner template (vitest or `go test` via gotestsum) and run verdict and `aff audit` against a fixture repo in that language.

## Exit criteria

Decide at plan-phase. At minimum: verdict and the audit's revert step judge claims in a non-Python fixture repo with no change to affidavit modules beyond the template.
