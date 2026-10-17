---
{
  "base_kind": "claim",
  "epistemic_status": "asserted",
  "id": "rec-1aaa8c5e-adec-4df2-bc30-d09600c12903",
  "identity": "unknown",
  "lifecycle_state": "active",
  "payload": {
    "criterion": "A forged stored check-run does not change the verdict",
    "effort": "evidence-layer",
    "method": "tdd",
    "phase": "claims-manifest",
    "requirement": "R1",
    "verify_command": "python3 -m pytest tests/test_verdict.py -q -k forged_check_run"
  },
  "record_type": "project:acceptance",
  "recorded_at": "2026-10-17T05:02:42+00:00",
  "relationships": {},
  "revision": "sha256:63c8a664aa8ce2a61e7e89aa6822f53222da539d119539bda79e70bbda74d540",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "verify-claims-manifest-forge",
  "time": {
    "as_of": "2026-10-17T05:02:42+00:00"
  }
}
---

