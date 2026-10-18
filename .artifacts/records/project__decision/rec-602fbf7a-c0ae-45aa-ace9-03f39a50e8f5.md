---
{
  "base_kind": "claim",
  "epistemic_status": "asserted",
  "id": "rec-602fbf7a-c0ae-45aa-ace9-03f39a50e8f5",
  "identity": "unknown",
  "lifecycle_state": "active",
  "payload": {
    "alternatives": "fold support paths into oracle_hashes; hash a whole declared env tree",
    "choice": "manifest declares support_files paths and a runner-argv digest; both use the same amendment rule as oracle_hashes",
    "effort": "evidence-layer",
    "phase": "frozen-environment"
  },
  "record_type": "project:decision",
  "recorded_at": "2026-10-18T03:08:47+00:00",
  "relationships": {},
  "revision": "sha256:934acbc87e87609662704bf562f102a26d235e03de43c86939a9eba441c216af",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "support-files-schema",
  "time": {
    "as_of": "2026-10-18T03:08:47+00:00"
  }
}
---

## Rationale

An explicit support_files list keeps oracle tests and environment files distinct while reusing authorize(). Hashing the runner argv closes the deferred runner-template-freeze gap without inventing a second approval channel.

## Counter-argument

Folding support paths into oracle_hashes would avoid new fields. That blurs what a witness is and makes amendments harder to read when only conftest changed.
