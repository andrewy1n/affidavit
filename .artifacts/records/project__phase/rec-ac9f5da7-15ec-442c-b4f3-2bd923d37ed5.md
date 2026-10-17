---
{
  "base_kind": "phase",
  "id": "rec-ac9f5da7-15ec-442c-b4f3-2bd923d37ed5",
  "identity": "unknown",
  "lifecycle_state": "planned",
  "payload": {
    "effort": "evidence-layer",
    "ordinal": 6,
    "title": "Signed verdict attestation from CI"
  },
  "record_type": "project:phase",
  "recorded_at": "2026-10-17T22:58:46+00:00",
  "relationships": {},
  "revision": "sha256:24917dc7ef0ec1cb6d4f7f06f698e72b65641d43128778920db516aad58399e7",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "signed-verdict"
}
---

## Problem

If the agent runs `aff verdict` in its own shell, it can still report a pass it did not earn. A merge gate that reads a log line trusts the agent.

## Approach

not yet scoped — discuss when this phase is current. Direction: verdict runs where the agent does not control the environment (CI first), and emits a signed attestation of claim results bound to the commit, the manifest hash, and the runner template, using the SSH signing already used for amendments. A gate verifies the attestation, not the output. Ship a CI action that runs verdict on a pull request.

## Exit criteria

Decide at plan-phase. At minimum: `aff verdict` can emit a signed attestation, a verify command rejects a tampered or unsigned attestation and one for a different commit or manifest, and the CI action runs on a fixture repo.
