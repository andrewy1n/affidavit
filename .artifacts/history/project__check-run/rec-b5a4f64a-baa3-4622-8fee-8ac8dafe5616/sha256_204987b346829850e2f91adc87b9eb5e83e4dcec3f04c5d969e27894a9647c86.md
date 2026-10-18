---
{
  "base_kind": "event",
  "id": "rec-b5a4f64a-baa3-4622-8fee-8ac8dafe5616",
  "identity": "unknown",
  "lifecycle_state": "recorded",
  "payload": {
    "criterion_id": "rec-554e4e13-762d-4e70-9082-9f345ef104c1",
    "effort": "evidence-layer",
    "evidence_kind": "review",
    "method": "review",
    "requirement": "R1",
    "result": "pass",
    "revision": "780b98ed03d068aea39f95a1974c5294a2b1bfe9",
    "signed_by": "parent"
  },
  "provenance": {
    "sources": [
      "audit-differential-review"
    ]
  },
  "record_type": "project:check-run",
  "recorded_at": "2026-10-18T04:25:13+00:00",
  "relationships": {
    "informed_by": [
      "rec-554e4e13-762d-4e70-9082-9f345ef104c1"
    ]
  },
  "revision": "sha256:204987b346829850e2f91adc87b9eb5e83e4dcec3f04c5d969e27894a9647c86",
  "subject": "audit-differential-review",
  "time": {
    "observed": "2026-10-18T04:25:13+00:00",
    "recorded": "2026-10-18T04:25:13+00:00"
  }
}
---

# Phase-end review: audit-differential

## Verdict
PASS

## Summary
Declared probes extend aff audit without changing verdict. Unclaimed diffs surface; claim cites suppress. Red-first fixture reports the revision-on-tdd relaxation.

## Findings
none

## Integration
### interfaces
aff audit --probes; .affidavit/probes.json; advisory diffs[] alongside blocks/mutants
### assumptions
Historical red-first SHAs remain in repo history; fixture probe imports scripts/close_batch.py at those revisions
### invariants
Claim-covered diffs stay quiet; unclaimed diffs appear in diffs
### conflicts
none
