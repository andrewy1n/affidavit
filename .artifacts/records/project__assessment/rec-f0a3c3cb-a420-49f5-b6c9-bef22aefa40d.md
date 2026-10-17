---
{
  "base_kind": "claim",
  "epistemic_status": "asserted",
  "id": "rec-f0a3c3cb-a420-49f5-b6c9-bef22aefa40d",
  "identity": "unknown",
  "lifecycle_state": "active",
  "payload": {
    "confidence": "high",
    "effort": "evidence-layer",
    "missing": "",
    "next": "release",
    "phase": "standalone-aff",
    "requirement": "R4",
    "status": "verified"
  },
  "record_type": "project:assessment",
  "recorded_at": "2026-10-17T22:48:44+00:00",
  "relationships": {},
  "revision": "sha256:935d89a878a6474161256245199bcb6f772374650309e023ce4ef28a5cc6760c",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "standalone-aff-R4",
  "time": {
    "as_of": "2026-10-17T22:48:44+00:00"
  }
}
---

## Evidence

check-run rec-e02d9d80-9036-481f-acec-0cc6f8f8c321 result=pass revision=2483da2da2ad4929ad5853978d57335072ff577a method=tdd requirement=R4. pytest tests/test_affidavit_import_boundary.py: 2 passed.

## Missing

none

## Reason

The close path imports affidavit.oracle_red, and the boundary test passes: orchestra and dashboard do not import affidavit.aa, affidavit.aa_resolve, affidavit.check, affidavit.policy, or affidavit.verdict.
