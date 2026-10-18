---
{
  "base_kind": "task",
  "id": "rec-7b9dc4bd-56d7-460c-bc57-f00a38ffc048",
  "identity": "unknown",
  "lifecycle_state": "planned",
  "payload": {
    "assignee": "",
    "decisions": "audit-probes",
    "effort": "evidence-layer",
    "estimate_minutes": 15,
    "executor": "inline",
    "kind": "deliver",
    "phase": "audit-differential",
    "requirements": "R4",
    "size": "M",
    "title": "aff audit reports red-first revision-on-tdd relaxation as unclaimed"
  },
  "record_type": "project:work-item",
  "recorded_at": "2026-10-18T04:20:50+00:00",
  "relationships": {
    "depends_on": [
      "rec-f91285b8-56a2-4c0a-9fe5-6d091873e41e"
    ]
  },
  "revision": "sha256:56c0ef8cbfec644aa147f4df806eeea51aa36f5bb6ad59e054b4ad7461ffba9a",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "audit-unclaimed-range"
}
---

## Description

R4: On the `red-first` range from the differential spike, the audit reports the `revision`-on-`tdd` relaxation as a difference no claim covers.

## Approach

1. Vendor a fixture probe (and minimal base/head modules or request JSON from `spikes/differential`) that exercises a close-request with `revision` on a `tdd` criterion across `b3159b6..c14dedb` or an equivalent vendored pair.
2. Wire that probe so `aff audit` reports an unclaimed diff for the relaxation; no claim cite suppresses it.
3. Do not edit frozen oracles after freeze.
