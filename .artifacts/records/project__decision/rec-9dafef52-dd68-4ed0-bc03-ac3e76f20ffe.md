---
{
  "base_kind": "claim",
  "epistemic_status": "asserted",
  "id": "rec-9dafef52-dd68-4ed0-bc03-ac3e76f20ffe",
  "identity": "unknown",
  "lifecycle_state": "active",
  "payload": {
    "alternatives": "pure git ordering and paths without signer checks; store oracle_commit fields in the manifest without verifying git",
    "choice": "verdict checks git history: oracle paths land before implementation, oracle commits touch only oracle/support paths, and when commits are SSH-signed the oracle signer differs from the implementation signer",
    "effort": "evidence-layer",
    "phase": "oracle-provenance"
  },
  "record_type": "project:decision",
  "recorded_at": "2026-10-18T03:08:48+00:00",
  "relationships": {},
  "revision": "sha256:c74bc6a546e8b65c65c0ac260dee75b88196c55f7c1373fd42429179205f695a",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "oracle-provenance-check",
  "time": {
    "as_of": "2026-10-18T03:08:48+00:00"
  }
}
---

## Rationale

The core guarantee is that the test author is not the agent that benefits. Git ordering and path allowlists catch the common rewrite; different SSH commit signers close the principal gap when history is signed.

## Counter-argument

Manifest-stored oracle_commit fields would be explicit and easy to read. Without verifying them against git they are as forgeable as any other agent-edited file.
