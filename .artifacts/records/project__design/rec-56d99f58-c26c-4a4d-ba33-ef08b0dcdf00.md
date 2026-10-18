---
{
  "base_kind": "claim",
  "epistemic_status": "asserted",
  "id": "rec-56d99f58-c26c-4a4d-ba33-ef08b0dcdf00",
  "identity": "unknown",
  "lifecycle_state": "active",
  "payload": {
    "decisions": "oracle-provenance-check",
    "effort": "evidence-layer",
    "phase": "oracle-provenance"
  },
  "record_type": "project:design",
  "recorded_at": "2026-10-18T03:08:48+00:00",
  "relationships": {},
  "revision": "sha256:caa6236256fd97088f946ee4db7f8b5bab68daebb74fe58835bc56b4f9455c47",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "oracle-provenance",
  "time": {
    "as_of": "2026-10-18T03:08:48+00:00"
  }
}
---

## Architecture

1. Add a provenance check in the verdict path (helper module ok) that resolves, per claim, the introducing commit(s) for oracle paths via git history.
2. Enforce ancestor ordering vs implementation tip/`--at`.
3. Diff the oracle commit for path allowlist (oracle + support only).
4. When commit signatures exist, compare principals via SSH commit verify; fail on shared principal.
5. Fixture repos with signed commits cover R1–R4.

## Interfaces

- Internal API from verdict; optional CLI flag only if plan-phase needs it.
- Failure reasons distinct enough to test (ordering / paths / signer).

## Decisions

- `oracle-provenance-check`: git + path allowlist + different signers; not manifest-only fields.

## Invariants

- Git is authority for provenance.
- Pass requires R1–R3 as applicable.

## Assumptions

- frozen-environment support set is available.
- Plan-phase defines behavior when commits are unsigned (fixture path still proves R3).

## Tradeoffs

- Signed-history requirement for R3 increases fixture complexity.
- Pure git without signers is weaker against rewritten local history.

## Risks

- Squash merges obscure introducing commits. Mitigation: document expected history shape; fixtures use linear signed commits.
