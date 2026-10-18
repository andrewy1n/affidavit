---
{
  "base_kind": "phase",
  "id": "rec-ec2a17c7-ada2-4c03-ba16-b0392baa8ea9",
  "identity": "unknown",
  "lifecycle_state": "planned",
  "payload": {
    "effort": "evidence-layer",
    "ordinal": 7,
    "title": "Verdict checks who wrote the oracle and when"
  },
  "record_type": "project:phase",
  "recorded_at": "2026-10-18T03:08:48+00:00",
  "relationships": {},
  "revision": "sha256:54120ac89571ca01c945c010a19bcbb07811ee2c2b5eeaaec2b30438e12440c1",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "oracle-provenance"
}
---

## Problem

The core guarantee is that the test author is not the agent that benefits from a pass. Today orchestra keeps that by process. A standalone user gets nothing that enforces it.

## Approach

Adopt `oracle-provenance-check`: verdict uses git for oracle-before-impl ordering, oracle/support-only paths on the oracle commit, and different SSH commit signers when history is signed. Phase-end reviewer skipped.

## Exit criteria

- Fail fixtures for oracle-after-impl, oracle touching source, and shared signer.
- Pass fixture that meets all three.

## Landing

- **branch:** `phase/oracle-provenance`
- **worktree:** `/home/andrewyin/affidavit--oracle-provenance`
- **base:** `main`
- **close:** commit code on the phase branch; merge that branch into `main`; commit the store on the primary checkout
- **push:** not a stop (do not push)
