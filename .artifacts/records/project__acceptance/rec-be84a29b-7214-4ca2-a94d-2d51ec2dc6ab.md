---
{
  "base_kind": "claim",
  "epistemic_status": "asserted",
  "id": "rec-be84a29b-7214-4ca2-a94d-2d51ec2dc6ab",
  "identity": "unknown",
  "lifecycle_state": "active",
  "payload": {
    "criterion": "a pytest runs bin/orchestra check --help and bin/orchestra close-batch --help and each exits 0",
    "effort": "evidence-layer",
    "method": "check",
    "phase": "standalone-aff",
    "requirement": "R3",
    "verify_command": "cd \"$HOME/orchestra\" && python3 -m pytest tests/test_affidavit_check.py -q -k orchestra_subcommand_help"
  },
  "record_type": "project:acceptance",
  "recorded_at": "2026-10-17T23:07:38+00:00",
  "relationships": {},
  "revision": "sha256:c2d1913b3703aee88c4250067cf1002828ece24491a29ee2cf103d3aba961f15",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "fix-orchestra-help-tests",
  "time": {
    "as_of": "2026-10-17T23:07:38+00:00"
  }
}
---

