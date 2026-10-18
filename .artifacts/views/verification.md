# Project Verification

> Derived view — not authoritative. Edit underlying records, not this file.
> Store state: sha256:f3b0f47f262626218a91acc3ee8364797ae83b8f0223d04be3a6f73a6630b44e

## amendment-sign

### Acceptance
- **amendment-sign**: A hash or test-id change is authorized only by a signature chain that verifies under the base allowlist; a changed allowlist, a bad signature, and a missing step are refused; tdd; evidence-layer; python3 -m pytest tests/test_amendment.py -q _(id: [rec-ea520f42-d62e-4b5d-879a-9dfd8ecc6d43](.artifacts/records/project__acceptance/rec-ea520f42-d62e-4b5d-879a-9dfd8ecc6d43.md))_

### Check
- **amendment-sign**: rec-ea520f42-d62e-4b5d-879a-9dfd8ecc6d43; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-2c20c34a-b30d-443d-ba55-2c46584f8e93](.artifacts/records/project__check-run/rec-2c20c34a-b30d-443d-ba55-2c46584f8e93.md))_
- **amendment-sign**: rec-ea520f42-d62e-4b5d-879a-9dfd8ecc6d43; 86c5ca7847a05fa40cadb02bfe61dd5736b1a33c; fail; tdd _(id: [rec-44d1f822-2988-4f96-8fa3-06c74a717db2](.artifacts/records/project__check-run/rec-44d1f822-2988-4f96-8fa3-06c74a717db2.md))_
- **amendment-sign**: rec-ea520f42-d62e-4b5d-879a-9dfd8ecc6d43; 512796fda9f16f54a5848fdca999755a8e48eb27; pass; tdd _(id: [rec-a80065af-b7ba-4ec6-a3e1-f47232321681](.artifacts/records/project__check-run/rec-a80065af-b7ba-4ec6-a3e1-f47232321681.md))_
- **amendment-sign**: rec-ea520f42-d62e-4b5d-879a-9dfd8ecc6d43; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; pass; tdd _(id: [rec-d49e2b00-a060-46ec-a607-773810081b00](.artifacts/records/project__check-run/rec-d49e2b00-a060-46ec-a607-773810081b00.md))_

## attest-ci

### Acceptance
- **attest-ci**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_ci_workflow_runs_verdict_and_attest -q _(id: [rec-9d1b0910-9edf-4f6f-834f-bdc4a4eb650f](.artifacts/records/project__acceptance/rec-9d1b0910-9edf-4f6f-834f-bdc4a4eb650f.md))_

### Check
- **attest-ci**: rec-9d1b0910-9edf-4f6f-834f-bdc4a4eb650f; dirty; fail; tdd _(id: [rec-4ddd848d-f237-48f0-9551-c40bbb22a0f5](.artifacts/records/project__check-run/rec-4ddd848d-f237-48f0-9551-c40bbb22a0f5.md))_
- **attest-ci**: rec-9d1b0910-9edf-4f6f-834f-bdc4a4eb650f; 678568be6e44d42569de8196f94b55bca3b5f912; pass; tdd _(id: [rec-80e91e40-7fdc-4f35-9baf-c2820b7e5847](.artifacts/records/project__check-run/rec-80e91e40-7fdc-4f35-9baf-c2820b7e5847.md))_

## attest-core

### Acceptance
- **attest-core**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_emit_signed_attestation_includes_commit_manifest_runner_and_claims -q _(id: [rec-2620c049-5db4-4593-b467-1f13191c8832](.artifacts/records/project__acceptance/rec-2620c049-5db4-4593-b467-1f13191c8832.md))_

### Check
- **attest-core**: rec-2620c049-5db4-4593-b467-1f13191c8832; 678568be6e44d42569de8196f94b55bca3b5f912; pass; tdd _(id: [rec-30f6a564-e496-438a-8dae-89a01a9b506e](.artifacts/records/project__check-run/rec-30f6a564-e496-438a-8dae-89a01a9b506e.md))_
- **attest-core**: rec-2620c049-5db4-4593-b467-1f13191c8832; dirty; fail; tdd _(id: [rec-71a81db7-27ca-47c4-9e64-1348cf7c5b82](.artifacts/records/project__check-run/rec-71a81db7-27ca-47c4-9e64-1348cf7c5b82.md))_

## attest-core-bind

### Acceptance
- **attest-core-bind**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_verify_rejects_wrong_commit tests/test_attestation.py::test_verify_rejects_bind_mismatch_on_manifest_hash -q _(id: [rec-af4de5c3-440e-4e5f-9175-039d591a6fea](.artifacts/records/project__acceptance/rec-af4de5c3-440e-4e5f-9175-039d591a6fea.md))_

### Check
- **attest-core-bind**: rec-af4de5c3-440e-4e5f-9175-039d591a6fea; 678568be6e44d42569de8196f94b55bca3b5f912; pass; tdd _(id: [rec-5d3dafa1-00c3-49e0-9190-5f76c9ab7800](.artifacts/records/project__check-run/rec-5d3dafa1-00c3-49e0-9190-5f76c9ab7800.md))_
- **attest-core-bind**: rec-af4de5c3-440e-4e5f-9175-039d591a6fea; dirty; fail; tdd _(id: [rec-7c98dc9c-21d5-481b-9ddf-6fa6fd38e64e](.artifacts/records/project__check-run/rec-7c98dc9c-21d5-481b-9ddf-6fa6fd38e64e.md))_

## attest-core-sig

### Acceptance
- **attest-core-sig**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_verify_rejects_bad_signature tests/test_attestation.py::test_verify_rejects_tampered_payload -q _(id: [rec-27204235-9eb7-4d4e-a858-0c140858be15](.artifacts/records/project__acceptance/rec-27204235-9eb7-4d4e-a858-0c140858be15.md))_

### Check
- **attest-core-sig**: rec-27204235-9eb7-4d4e-a858-0c140858be15; dirty; fail; tdd _(id: [rec-3a31f66d-062e-43e0-a87e-3aa210ea7a61](.artifacts/records/project__check-run/rec-3a31f66d-062e-43e0-a87e-3aa210ea7a61.md))_
- **attest-core-sig**: rec-27204235-9eb7-4d4e-a858-0c140858be15; 678568be6e44d42569de8196f94b55bca3b5f912; pass; tdd _(id: [rec-e80caaf0-bd34-4b68-8d5a-3200cddcd927](.artifacts/records/project__check-run/rec-e80caaf0-bd34-4b68-8d5a-3200cddcd927.md))_

## audit-blocks

### Acceptance
- **audit-blocks**: tdd; evidence-layer; python3 -m pytest tests/test_audit.py::test_r1_audit_labels_each_source_block tests/test_audit.py::test_r1_audit_reads_claim_tests_from_manifest -q _(id: [rec-4d99e4a9-8eed-4abf-bbfd-63d23ba1bf0e](.artifacts/records/project__acceptance/rec-4d99e4a9-8eed-4abf-bbfd-63d23ba1bf0e.md))_

### Check
- **audit-blocks**: rec-4d99e4a9-8eed-4abf-bbfd-63d23ba1bf0e; dirty; fail; tdd _(id: [rec-0311d276-0ad9-4a06-b361-85e2b62e8827](.artifacts/records/project__check-run/rec-0311d276-0ad9-4a06-b361-85e2b62e8827.md))_
- **audit-blocks**: rec-4d99e4a9-8eed-4abf-bbfd-63d23ba1bf0e; 6e3c322296cde831f0eda91572459f238c775750; pass; tdd _(id: [rec-56baa4af-58a5-424f-a241-92a9b0677237](.artifacts/records/project__check-run/rec-56baa4af-58a5-424f-a241-92a9b0677237.md))_

## audit-blocks-range

### Acceptance
- **audit-blocks-range**: tdd; evidence-layer; python3 -m pytest tests/test_audit.py::test_r3_audit_reports_unnoticed_build_batch_cwd_block -q _(id: [rec-a402e4fe-db71-4c0b-9504-4bc345fe82fb](.artifacts/records/project__acceptance/rec-a402e4fe-db71-4c0b-9504-4bc345fe82fb.md))_

### Check
- **audit-blocks-range**: rec-a402e4fe-db71-4c0b-9504-4bc345fe82fb; 6e3c322296cde831f0eda91572459f238c775750; pass; tdd _(id: [rec-02472dd8-b1a7-42e8-9e8e-d153de588901](.artifacts/records/project__check-run/rec-02472dd8-b1a7-42e8-9e8e-d153de588901.md))_
- **audit-blocks-range**: rec-a402e4fe-db71-4c0b-9504-4bc345fe82fb; dirty; fail; tdd _(id: [rec-e5724a8e-f9e4-4eee-81b9-93fcc41fe352](.artifacts/records/project__check-run/rec-e5724a8e-f9e4-4eee-81b9-93fcc41fe352.md))_

## audit-blocks-tests

### Acceptance
- **audit-blocks-tests**: tdd; evidence-layer; python3 -m pytest tests/test_audit.py::test_r2_audit_never_reports_test_file_blocks -q _(id: [rec-80251ecf-6081-4c0c-8ebb-aff653eb663a](.artifacts/records/project__acceptance/rec-80251ecf-6081-4c0c-8ebb-aff653eb663a.md))_

### Check
- **audit-blocks-tests**: rec-80251ecf-6081-4c0c-8ebb-aff653eb663a; 6e3c322296cde831f0eda91572459f238c775750; pass; tdd _(id: [rec-0fa16b59-d417-41ba-9a0c-d0d6b32230a7](.artifacts/records/project__check-run/rec-0fa16b59-d417-41ba-9a0c-d0d6b32230a7.md))_
- **audit-blocks-tests**: rec-80251ecf-6081-4c0c-8ebb-aff653eb663a; dirty; fail; tdd _(id: [rec-62371e89-de0b-4a55-a4ad-11ba495d7e8a](.artifacts/records/project__check-run/rec-62371e89-de0b-4a55-a4ad-11ba495d7e8a.md))_

## audit-differential-review

### Acceptance
- **audit-differential-review**: manual; evidence-layer _(id: [rec-554e4e13-762d-4e70-9082-9f345ef104c1](.artifacts/records/project__acceptance/rec-554e4e13-762d-4e70-9082-9f345ef104c1.md))_

### Check
- **audit-differential-review**: rec-554e4e13-762d-4e70-9082-9f345ef104c1; 780b98ed03d068aea39f95a1974c5294a2b1bfe9; pass; review; parent _(id: [rec-b5a4f64a-baa3-4622-8fee-8ac8dafe5616](.artifacts/records/project__check-run/rec-b5a4f64a-baa3-4622-8fee-8ac8dafe5616.md))_

## audit-mutants

### Acceptance
- **audit-mutants**: tdd; evidence-layer; python3 -m pytest tests/test_audit.py::test_r4_audit_plants_mutants_only_in_noticed_blocks -q _(id: [rec-1b284b3d-549e-44c3-9ebb-819ea7e633c0](.artifacts/records/project__acceptance/rec-1b284b3d-549e-44c3-9ebb-819ea7e633c0.md))_

### Check
- **audit-mutants**: rec-1b284b3d-549e-44c3-9ebb-819ea7e633c0; 5bbd8cb571d2ad193b61f35159e3648c5adfd0f0; pass; tdd _(id: [rec-8cd85805-5437-4ac9-b5d3-2857bf26dbc5](.artifacts/records/project__check-run/rec-8cd85805-5437-4ac9-b5d3-2857bf26dbc5.md))_
- **audit-mutants**: rec-1b284b3d-549e-44c3-9ebb-819ea7e633c0; dirty; fail; tdd _(id: [rec-aa8e39d0-c2c2-49d9-aba7-34ab35058329](.artifacts/records/project__check-run/rec-aa8e39d0-c2c2-49d9-aba7-34ab35058329.md))_

## audit-probes

### Acceptance
- **audit-probes**: tdd; evidence-layer; python3 -m pytest tests/test_audit_probes.py::test_r1_audit_runs_declared_probes_at_base_and_head -q _(id: [rec-282b9531-ae72-4d08-bb9e-3b90139f7561](.artifacts/records/project__acceptance/rec-282b9531-ae72-4d08-bb9e-3b90139f7561.md))_

### Check
- **audit-probes**: rec-282b9531-ae72-4d08-bb9e-3b90139f7561; a12a5f17c1f2cc53ffcb08848fe4cd3f60723658; fail; tdd _(id: [rec-49f05e3b-c440-425f-91d5-0566c12b5b7e](.artifacts/records/project__check-run/rec-49f05e3b-c440-425f-91d5-0566c12b5b7e.md))_
- **audit-probes**: rec-282b9531-ae72-4d08-bb9e-3b90139f7561; dirty; fail; tdd _(id: [rec-68cb1a7b-9f22-4372-88e3-2cf81ecafddd](.artifacts/records/project__check-run/rec-68cb1a7b-9f22-4372-88e3-2cf81ecafddd.md))_
- **audit-probes**: rec-282b9531-ae72-4d08-bb9e-3b90139f7561; 846120fa770a16408c4425dc2d61a0ddacd08005; pass; tdd _(id: [rec-8358194f-4fae-4856-8192-d09dc72c575e](.artifacts/records/project__check-run/rec-8358194f-4fae-4856-8192-d09dc72c575e.md))_
- **audit-probes**: rec-282b9531-ae72-4d08-bb9e-3b90139f7561; 62a8bf14f65eff352375e1679a7380c384abe17f; pass; tdd _(id: [rec-9a9ebe03-930a-4f4c-943f-3f82d62635f4](.artifacts/records/project__check-run/rec-9a9ebe03-930a-4f4c-943f-3f82d62635f4.md))_

## audit-probes-claimed

### Acceptance
- **audit-probes-claimed**: tdd; evidence-layer; python3 -m pytest tests/test_audit_probes.py::test_r2_audit_reports_unclaimed_probe_difference -q _(id: [rec-841b4a3f-f2d6-40c0-b73f-b4af1186f1e8](.artifacts/records/project__acceptance/rec-841b4a3f-f2d6-40c0-b73f-b4af1186f1e8.md))_

### Check
- **audit-probes-claimed**: rec-841b4a3f-f2d6-40c0-b73f-b4af1186f1e8; a12a5f17c1f2cc53ffcb08848fe4cd3f60723658; fail; tdd _(id: [rec-0bfaef1d-fd57-4ca7-bce2-971fa39f286b](.artifacts/records/project__check-run/rec-0bfaef1d-fd57-4ca7-bce2-971fa39f286b.md))_
- **audit-probes-claimed**: rec-841b4a3f-f2d6-40c0-b73f-b4af1186f1e8; 846120fa770a16408c4425dc2d61a0ddacd08005; pass; tdd _(id: [rec-3a946cfc-304a-4537-b3e8-082c0747582b](.artifacts/records/project__check-run/rec-3a946cfc-304a-4537-b3e8-082c0747582b.md))_
- **audit-probes-claimed**: rec-841b4a3f-f2d6-40c0-b73f-b4af1186f1e8; dirty; fail; tdd _(id: [rec-68e6bfb9-a027-4d75-b276-0a5c2a8b1688](.artifacts/records/project__check-run/rec-68e6bfb9-a027-4d75-b276-0a5c2a8b1688.md))_
- **audit-probes-claimed**: rec-841b4a3f-f2d6-40c0-b73f-b4af1186f1e8; 62a8bf14f65eff352375e1679a7380c384abe17f; pass; tdd _(id: [rec-ba987cb7-7d39-4ec9-bc51-752df10d896f](.artifacts/records/project__check-run/rec-ba987cb7-7d39-4ec9-bc51-752df10d896f.md))_

## audit-probes-covered

### Acceptance
- **audit-probes-covered**: tdd; evidence-layer; python3 -m pytest tests/test_audit_probes.py::test_r3_audit_suppresses_diff_covered_by_cited_claim -q _(id: [rec-72c29ed5-5ed2-4a78-8847-bc5f73acee3a](.artifacts/records/project__acceptance/rec-72c29ed5-5ed2-4a78-8847-bc5f73acee3a.md))_

### Check
- **audit-probes-covered**: rec-72c29ed5-5ed2-4a78-8847-bc5f73acee3a; 62a8bf14f65eff352375e1679a7380c384abe17f; pass; tdd _(id: [rec-4c3f5c49-b797-423b-b2d9-8a2253243c78](.artifacts/records/project__check-run/rec-4c3f5c49-b797-423b-b2d9-8a2253243c78.md))_
- **audit-probes-covered**: rec-72c29ed5-5ed2-4a78-8847-bc5f73acee3a; a12a5f17c1f2cc53ffcb08848fe4cd3f60723658; fail; tdd _(id: [rec-5cc85bcf-3862-4194-af07-083c4f512c43](.artifacts/records/project__check-run/rec-5cc85bcf-3862-4194-af07-083c4f512c43.md))_
- **audit-probes-covered**: rec-72c29ed5-5ed2-4a78-8847-bc5f73acee3a; 846120fa770a16408c4425dc2d61a0ddacd08005; pass; tdd _(id: [rec-5f4655ab-3eb1-48d2-8133-41f1d8fdbd5a](.artifacts/records/project__check-run/rec-5f4655ab-3eb1-48d2-8133-41f1d8fdbd5a.md))_
- **audit-probes-covered**: rec-72c29ed5-5ed2-4a78-8847-bc5f73acee3a; dirty; fail; tdd _(id: [rec-cd787b8c-10e7-4100-a4d3-8a16bee2f46d](.artifacts/records/project__check-run/rec-cd787b8c-10e7-4100-a4d3-8a16bee2f46d.md))_

## audit-unclaimed-range

### Acceptance
- **audit-unclaimed-range**: tdd; evidence-layer; python3 -m pytest tests/test_audit_probes_range.py::test_r4_audit_reports_unclaimed_tdd_revision_relaxation -q _(id: [rec-04aba49b-468d-4d98-a837-9df3b7b5e7e7](.artifacts/records/project__acceptance/rec-04aba49b-468d-4d98-a837-9df3b7b5e7e7.md))_

### Check
- **audit-unclaimed-range**: rec-04aba49b-468d-4d98-a837-9df3b7b5e7e7; 780b98ed03d068aea39f95a1974c5294a2b1bfe9; pass; tdd _(id: [rec-9dc8bd8e-b3d0-4832-b16e-b179bf3de4c0](.artifacts/records/project__check-run/rec-9dc8bd8e-b3d0-4832-b16e-b179bf3de4c0.md))_
- **audit-unclaimed-range**: rec-04aba49b-468d-4d98-a837-9df3b7b5e7e7; dirty; fail; tdd _(id: [rec-d5698743-11ed-4e68-94b3-250ec65ec130](.artifacts/records/project__check-run/rec-d5698743-11ed-4e68-94b3-250ec65ec130.md))_

## ci-fixture-builder

### Acceptance
- **ci-fixture-builder**: check; evidence-layer; test -f tests/fixtures/verdict-repo/app.py && test -f tests/fixtures/verdict-repo/app.red.py && test -f tests/fixtures/verdict-repo/tests/test_widget.py && test -f tests/fixtures/verdict-repo/.affidavit/manifest.json && rg -q claim-widget tests/fixtures/verdict-repo/.affidavit/manifest.json && rg -q "verdict-repo/\.git" .gitignore _(id: [rec-b507fca2-1156-494c-a9c2-8ecab88e5368](.artifacts/records/project__acceptance/rec-b507fca2-1156-494c-a9c2-8ecab88e5368.md))_

### Check
- **ci-fixture-builder**: rec-b507fca2-1156-494c-a9c2-8ecab88e5368; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; check _(id: [rec-9879dd8f-d50a-491f-8d87-23c72b40602f](.artifacts/records/project__check-run/rec-9879dd8f-d50a-491f-8d87-23c72b40602f.md))_
- **ci-fixture-builder**: rec-b507fca2-1156-494c-a9c2-8ecab88e5368; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; check _(id: [rec-ec41e557-47d9-4d3f-91e7-cbba1864830f](.artifacts/records/project__check-run/rec-ec41e557-47d9-4d3f-91e7-cbba1864830f.md))_

## ci-fixture-builder-pytest

### Acceptance
- **ci-fixture-builder-pytest**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_ci_workflow_runs_verdict_and_attest -q _(id: [rec-4ac56f49-8e3e-4d6f-9504-aacf0f8950e1](.artifacts/records/project__acceptance/rec-4ac56f49-8e3e-4d6f-9504-aacf0f8950e1.md))_

### Check
- **ci-fixture-builder-pytest**: rec-4ac56f49-8e3e-4d6f-9504-aacf0f8950e1; dirty; fail; tdd _(id: [rec-734a65dc-b599-4d43-82c2-def27ed9cdcd](.artifacts/records/project__check-run/rec-734a65dc-b599-4d43-82c2-def27ed9cdcd.md))_
- **ci-fixture-builder-pytest**: rec-4ac56f49-8e3e-4d6f-9504-aacf0f8950e1; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; tdd _(id: [rec-8a1743fa-9310-4124-9b72-bccfa3c4e4b4](.artifacts/records/project__check-run/rec-8a1743fa-9310-4124-9b72-bccfa3c4e4b4.md))_

## ci-fixture-builder-verdict

### Acceptance
- **ci-fixture-builder-verdict**: check; evidence-layer; bash tests/fixtures/build_verdict_repo.sh && BASE=$(git -C tests/fixtures/verdict-repo rev-parse HEAD~1) && HEAD=$(git -C tests/fixtures/verdict-repo rev-parse HEAD) && bin/aff verdict --cwd tests/fixtures/verdict-repo --base "$BASE" --at "$HEAD" claim-widget | tee /tmp/verdict-fixture.json && python3 -c "import json; assert json.load(open(\"/tmp/verdict-fixture.json\"))[\"result\"]==\"pass\"" _(id: [rec-9557c1ab-c5e5-44ba-b992-20eac0a1098a](.artifacts/records/project__acceptance/rec-9557c1ab-c5e5-44ba-b992-20eac0a1098a.md))_

### Check
- **ci-fixture-builder-verdict**: rec-9557c1ab-c5e5-44ba-b992-20eac0a1098a; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; check _(id: [rec-a8152a20-71e9-44dc-bc98-ca52fe583495](.artifacts/records/project__check-run/rec-a8152a20-71e9-44dc-bc98-ca52fe583495.md))_

## ci-fixture-builder-workflow

### Acceptance
- **ci-fixture-builder-workflow**: check; evidence-layer; rg -n build_verdict_repo .github/workflows/affidavit-verdict.yml _(id: [rec-3d5bfc07-0ef7-4ed8-9f5b-746ff634bf45](.artifacts/records/project__acceptance/rec-3d5bfc07-0ef7-4ed8-9f5b-746ff634bf45.md))_

### Check
- **ci-fixture-builder-workflow**: rec-3d5bfc07-0ef7-4ed8-9f5b-746ff634bf45; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; check _(id: [rec-5f7e95be-a98b-4ad7-93e4-b37923847cc2](.artifacts/records/project__check-run/rec-5f7e95be-a98b-4ad7-93e4-b37923847cc2.md))_

## ci-verdict-fixture-review

### Check
- **ci-verdict-fixture-review**: ci-verdict-fixture-review; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; review; parent _(id: [rec-feea8042-f8d7-4a6d-9cc6-4b8428d28d4a](.artifacts/records/project__check-run/rec-feea8042-f8d7-4a6d-9cc6-4b8428d28d4a.md))_

## ci-verdict-fixture-suite

### Check
- **ci-verdict-fixture-suite**: ci-verdict-fixture-suite; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; fail; check _(id: [rec-dc09c80d-ea5b-45af-92a3-08dfe84f3a20](.artifacts/records/project__check-run/rec-dc09c80d-ea5b-45af-92a3-08dfe84f3a20.md))_

## claim-cli

### Acceptance
- **claim-cli**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r1_claim_add_writes_manifest_entry_standalone -q _(id: [rec-75798857-63f7-4bf9-ba62-1702b7d62da3](.artifacts/records/project__acceptance/rec-75798857-63f7-4bf9-ba62-1702b7d62da3.md))_

### Check
- **claim-cli**: rec-75798857-63f7-4bf9-ba62-1702b7d62da3; dirty; fail; tdd _(id: [rec-4c8b7ae1-dffd-4acd-90bf-2463c0c524e8](.artifacts/records/project__check-run/rec-4c8b7ae1-dffd-4acd-90bf-2463c0c524e8.md))_
- **claim-cli**: rec-75798857-63f7-4bf9-ba62-1702b7d62da3; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; tdd _(id: [rec-7d59e8f4-c6a1-47f2-80e7-487d8414d095](.artifacts/records/project__check-run/rec-7d59e8f4-c6a1-47f2-80e7-487d8414d095.md))_

## claim-cli-freeze

### Acceptance
- **claim-cli-freeze**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r2_freeze_records_exact_oracle_hashes tests/test_claim_authoring.py::test_r2_standalone_add_freeze_verdict_passes -q _(id: [rec-181f850e-452a-4386-a7c0-f2e5785394fa](.artifacts/records/project__acceptance/rec-181f850e-452a-4386-a7c0-f2e5785394fa.md))_

### Check
- **claim-cli-freeze**: rec-181f850e-452a-4386-a7c0-f2e5785394fa; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; tdd _(id: [rec-002dedc8-550c-4da7-9fb2-f03834ecb8da](.artifacts/records/project__check-run/rec-002dedc8-550c-4da7-9fb2-f03834ecb8da.md))_
- **claim-cli-freeze**: rec-181f850e-452a-4386-a7c0-f2e5785394fa; dirty; fail; tdd _(id: [rec-341e5450-1dbe-4091-8c1a-ba7ff112137d](.artifacts/records/project__check-run/rec-341e5450-1dbe-4091-8c1a-ba7ff112137d.md))_

## claim-cli-lint

### Acceptance
- **claim-cli-lint**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r3_lint_claims_reports_compound_claim -q _(id: [rec-253cbc9c-3aa1-417e-809e-11f3ae8f76c3](.artifacts/records/project__acceptance/rec-253cbc9c-3aa1-417e-809e-11f3ae8f76c3.md))_

### Check
- **claim-cli-lint**: rec-253cbc9c-3aa1-417e-809e-11f3ae8f76c3; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; tdd _(id: [rec-80c826c0-7439-46a7-8130-f6df23aaaeeb](.artifacts/records/project__check-run/rec-80c826c0-7439-46a7-8130-f6df23aaaeeb.md))_
- **claim-cli-lint**: rec-253cbc9c-3aa1-417e-809e-11f3ae8f76c3; dirty; fail; tdd _(id: [rec-b9d3df22-f84e-409e-8577-afbee7a17cc9](.artifacts/records/project__check-run/rec-b9d3df22-f84e-409e-8577-afbee7a17cc9.md))_

## claims-manifest-review

### Check
- **claims-manifest-review**: claims-manifest-review; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; fail; review _(id: [rec-0ddf91ca-e2b7-4a47-8ffb-982b0370877c](.artifacts/records/project__check-run/rec-0ddf91ca-e2b7-4a47-8ffb-982b0370877c.md))_
- **claims-manifest-review**: claims-manifest-review; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; review _(id: [rec-7524315e-b14a-415e-a8cb-ee76110c7dfe](.artifacts/records/project__check-run/rec-7524315e-b14a-415e-a8cb-ee76110c7dfe.md))_

## claims-manifest-suite

### Check
- **claims-manifest-suite**: claims-manifest-suite; f84f89b913b54f21f1e426c7201c49b2e62347ef; fail; check _(id: [rec-20c9e846-1a92-4206-90ae-68814427a9a5](.artifacts/records/project__check-run/rec-20c9e846-1a92-4206-90ae-68814427a9a5.md))_

## conventional-commits

### Acceptance
- **conventional-commits**: execute-phase shows a per-task commit, a phase-branch commit, and a store commit whose subject matches type(scope): summary and whose body is one or two sentences; a task commit names the task slug; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_task_commit.py -q _(id: [rec-325e52d1-3740-4543-8f5c-47e640bf5b84](.artifacts/records/project__acceptance/rec-325e52d1-3740-4543-8f5c-47e640bf5b84.md))_

### Check
- **conventional-commits**: rec-325e52d1-3740-4543-8f5c-47e640bf5b84; 40386351dd0a5d62619ef4be64070aefb986ff30; pass; tdd _(id: [rec-87e9eb85-7b20-4dd2-bcff-57a0c0392c01](.artifacts/records/project__check-run/rec-87e9eb85-7b20-4dd2-bcff-57a0c0392c01.md))_
- **conventional-commits**: rec-325e52d1-3740-4543-8f5c-47e640bf5b84; db859dbb0aa06cdaedbd5cffe24e04ca611eb463; fail; tdd _(id: [rec-f37381b1-3c16-4b7a-b2ed-3e18bbfc1a65](.artifacts/records/project__check-run/rec-f37381b1-3c16-4b7a-b2ed-3e18bbfc1a65.md))_

## env-freeze

### Acceptance
- **env-freeze**: tdd; evidence-layer; python3 -m pytest tests/test_verdict.py::test_verdict_refuses_support_file_drift_without_amendment tests/test_verdict.py::test_verdict_refuses_claim_support_file_drift_without_amendment -q _(id: [rec-3bff17d7-9d75-4d11-a504-9a5b8d66f551](.artifacts/records/project__acceptance/rec-3bff17d7-9d75-4d11-a504-9a5b8d66f551.md))_

### Check
- **env-freeze**: rec-3bff17d7-9d75-4d11-a504-9a5b8d66f551; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; tdd _(id: [rec-011ad8ec-76bc-4c1e-8a45-b683b5e8ab7d](.artifacts/records/project__check-run/rec-011ad8ec-76bc-4c1e-8a45-b683b5e8ab7d.md))_
- **env-freeze**: rec-3bff17d7-9d75-4d11-a504-9a5b8d66f551; dirty; fail; tdd _(id: [rec-3340ee1f-c1e9-48d2-9dcf-5117f8e7cb99](.artifacts/records/project__check-run/rec-3340ee1f-c1e9-48d2-9dcf-5117f8e7cb99.md))_

## env-freeze-runner

### Acceptance
- **env-freeze-runner**: tdd; evidence-layer; python3 -m pytest tests/test_verdict.py::test_verdict_refuses_runner_digest_drift_without_amendment -q _(id: [rec-6a082c2e-8500-4178-b517-9d57ef09d9c7](.artifacts/records/project__acceptance/rec-6a082c2e-8500-4178-b517-9d57ef09d9c7.md))_

### Check
- **env-freeze-runner**: rec-6a082c2e-8500-4178-b517-9d57ef09d9c7; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; tdd _(id: [rec-9171ecef-c36f-4248-a180-cd2652ca6d27](.artifacts/records/project__check-run/rec-9171ecef-c36f-4248-a180-cd2652ca6d27.md))_
- **env-freeze-runner**: rec-6a082c2e-8500-4178-b517-9d57ef09d9c7; dirty; fail; tdd _(id: [rec-b4531302-dc52-4fba-8fb5-694e65842764](.artifacts/records/project__check-run/rec-b4531302-dc52-4fba-8fb5-694e65842764.md))_

## evidence-interface-review

### Check
- **evidence-interface-review**: evidence-interface-review; a655bf41071f6783be3049a8107ac8e28c54ee55; pass; review _(id: [rec-4ced2e1e-89e8-44b3-a011-5ec97e463cc2](.artifacts/records/project__check-run/rec-4ced2e1e-89e8-44b3-a011-5ec97e463cc2.md))_
- **evidence-interface-review**: evidence-interface-review; a655bf41071f6783be3049a8107ac8e28c54ee55; pass; review; parent _(id: [rec-6e9d124f-7c0d-447c-8309-b39d6d6df1c1](.artifacts/records/project__check-run/rec-6e9d124f-7c0d-447c-8309-b39d6d6df1c1.md))_

## evidence-interface-suite

### Check
- **evidence-interface-suite**: evidence-interface-suite; a655bf41071f6783be3049a8107ac8e28c54ee55; fail; check _(id: [rec-3bfc1262-c7f7-4f31-ace6-a8936cfaaa2c](.artifacts/records/project__check-run/rec-3bfc1262-c7f7-4f31-ace6-a8936cfaaa2c.md))_

## extract-store-binding

### Acceptance
- **extract-store-binding**: affidavit.aa imports StoreBindingError and resolve from affidavit.aa_resolve, affidavit/aa.py does not mention dashboard, and the aa tests pass; tdd; evidence-layer; python3 -m pytest tests/test_affidavit_aa.py tests/test_aa_resolve.py -q _(id: [rec-4f47fdf2-e4c8-436a-ad8b-c1d6be8c51b8](.artifacts/records/project__acceptance/rec-4f47fdf2-e4c8-436a-ad8b-c1d6be8c51b8.md))_

### Check
- **extract-store-binding**: rec-4f47fdf2-e4c8-436a-ad8b-c1d6be8c51b8; ff6130b7e719fa6733288f28eda5e7317a80ecfa; pass; tdd _(id: [rec-3541dbb2-1f13-410f-87b2-4f1af6c81ab0](.artifacts/records/project__check-run/rec-3541dbb2-1f13-410f-87b2-4f1af6c81ab0.md))_
- **extract-store-binding**: rec-4f47fdf2-e4c8-436a-ad8b-c1d6be8c51b8; 6832daa9854bb94be1e61e06590cae1a4d189fb7; fail; tdd _(id: [rec-b4a7696b-a902-4555-be8b-7b4e57a6d872](.artifacts/records/project__check-run/rec-b4a7696b-a902-4555-be8b-7b4e57a6d872.md))_

## fix-agent-docs

### Acceptance
- **fix-agent-docs**: AGENTS.md, README.md, and CLAUDE.md describe this repo as the evidence layer and send skills, the dashboard, scripts, and agents to ~/orchestra; tdd; evidence-layer; python3 -m pytest tests/test_evidence_layout.py::test_protocol_docs_describe_the_evidence_layer -q _(id: [rec-f9615bc0-d2d4-4b1a-9bf5-b7226656ae8f](.artifacts/records/project__acceptance/rec-f9615bc0-d2d4-4b1a-9bf5-b7226656ae8f.md))_

### Check
- **fix-agent-docs**: rec-f9615bc0-d2d4-4b1a-9bf5-b7226656ae8f; 43bb26ec008e43d3c149f7d9fee38249e7a5d8c8; pass; tdd _(id: [rec-1a0b4244-ac0b-4288-9634-bb672b5cee54](.artifacts/records/project__check-run/rec-1a0b4244-ac0b-4288-9634-bb672b5cee54.md))_
- **fix-agent-docs**: rec-f9615bc0-d2d4-4b1a-9bf5-b7226656ae8f; ce104cd41dba89271999636ccc23f0011628bf0c; fail; tdd _(id: [rec-7a30b9de-199c-412e-a185-86e1cf05cdee](.artifacts/records/project__check-run/rec-7a30b9de-199c-412e-a185-86e1cf05cdee.md))_

## fix-orchestra-help-tests

### Acceptance
- **fix-orchestra-help-tests**: a pytest runs bin/orchestra check --help and bin/orchestra close-batch --help and each exits 0; check; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_affidavit_check.py -q -k orchestra_subcommand_help _(id: [rec-be84a29b-7214-4ca2-a94d-2d51ec2dc6ab](.artifacts/records/project__acceptance/rec-be84a29b-7214-4ca2-a94d-2d51ec2dc6ab.md))_

### Check
- **fix-orchestra-help-tests**: rec-be84a29b-7214-4ca2-a94d-2d51ec2dc6ab; 2f2054aeccef9db20ac96d84d3c7f09d2647adfd; pass; check _(id: [rec-c8aef260-6848-49ce-82d6-5c1c8c790e62](.artifacts/records/project__check-run/rec-c8aef260-6848-49ce-82d6-5c1c8c790e62.md))_

## fix-readme-check-phrase

### Acceptance
- **fix-readme-check-phrase**: the moved orchestra check, close-batch, and store-client tests pass, including the README entry assertion; check; evidence-layer; cd "$HOME/orchestra" && bin/orchestra check --help && bin/orchestra close-batch --help && python3 -m pytest tests/test_affidavit_check.py tests/test_close_batch.py tests/test_affidavit_aa.py tests/test_aa_resolve.py -q _(id: [rec-25664c07-1863-4dac-a754-0836105f1fc3](.artifacts/records/project__acceptance/rec-25664c07-1863-4dac-a754-0836105f1fc3.md))_

### Check
- **fix-readme-check-phrase**: rec-25664c07-1863-4dac-a754-0836105f1fc3; 50b2cd0b0360e6cbca7bdbfe3cda1dfaab46648c; pass; check _(id: [rec-4894e12a-a446-4400-8f5f-e880f9ec2368](.artifacts/records/project__check-run/rec-4894e12a-a446-4400-8f5f-e880f9ec2368.md))_
- **fix-readme-check-phrase**: rec-25664c07-1863-4dac-a754-0836105f1fc3; 2f2054aeccef9db20ac96d84d3c7f09d2647adfd; pass; check _(id: [rec-93fd20c9-4e48-4fe5-ba7c-c8ae87415ff5](.artifacts/records/project__check-run/rec-93fd20c9-4e48-4fe5-ba7c-c8ae87415ff5.md))_

## fix-verdict-exit

### Acceptance
- **fix-verdict-exit**: aff verdict fails a claim when pytest at --at exits non-zero, accepts a verified signed amendment, and rejects a hash or test-id change with no covering amendment; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "signed_amendment or head_failure or missing_amendment" _(id: [rec-cd3fb645-b979-440d-ad25-158586f29fe1](.artifacts/records/project__acceptance/rec-cd3fb645-b979-440d-ad25-158586f29fe1.md))_

### Check
- **fix-verdict-exit**: rec-cd3fb645-b979-440d-ad25-158586f29fe1; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-8d5219fa-dc90-4a3e-bb1a-7d919fba521f](.artifacts/records/project__check-run/rec-8d5219fa-dc90-4a3e-bb1a-7d919fba521f.md))_
- **fix-verdict-exit**: rec-cd3fb645-b979-440d-ad25-158586f29fe1; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; fail; tdd _(id: [rec-d29c2681-a1d9-49fe-a8b4-de9aea3f9413](.artifacts/records/project__check-run/rec-d29c2681-a1d9-49fe-a8b4-de9aea3f9413.md))_

## fix-verdict-help-test

### Acceptance
- **fix-verdict-help-test**: a pytest runs bin/aff verdict --help and asserts exit 0; check; evidence-layer; python3 -m pytest tests/test_standalone_cli.py -q -k verdict_help _(id: [rec-17932b62-b463-479e-8071-f17cc13eff09](.artifacts/records/project__acceptance/rec-17932b62-b463-479e-8071-f17cc13eff09.md))_

### Check
- **fix-verdict-help-test**: rec-17932b62-b463-479e-8071-f17cc13eff09; 95816892f1208fd6b13723e6f89a959d6736da44; pass; check _(id: [rec-5b05faaa-9341-43a8-80d7-58984955161b](.artifacts/records/project__check-run/rec-5b05faaa-9341-43a8-80d7-58984955161b.md))_

## frozen-environment-review

### Check
- **frozen-environment-review**: frozen-environment-review; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; review _(id: [rec-61b8fdef-0c25-404a-a218-80b04c22dc02](.artifacts/records/project__check-run/rec-61b8fdef-0c25-404a-a218-80b04c22dc02.md))_

## human-claim

### Acceptance
- **human-claim**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r4_verdict_accepts_valid_human_signature -q _(id: [rec-bb995342-c16f-481e-9fff-8a39171dd49c](.artifacts/records/project__acceptance/rec-bb995342-c16f-481e-9fff-8a39171dd49c.md))_

### Check
- **human-claim**: rec-bb995342-c16f-481e-9fff-8a39171dd49c; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; tdd _(id: [rec-096abc07-0834-435b-b55c-030dfe879493](.artifacts/records/project__check-run/rec-096abc07-0834-435b-b55c-030dfe879493.md))_
- **human-claim**: rec-bb995342-c16f-481e-9fff-8a39171dd49c; dirty; fail; tdd _(id: [rec-34a88d8e-4039-45cb-bc77-530dcad4076d](.artifacts/records/project__check-run/rec-34a88d8e-4039-45cb-bc77-530dcad4076d.md))_

## human-claim-reject

### Acceptance
- **human-claim-reject**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r5_verdict_rejects_missing_human_signature tests/test_claim_authoring.py::test_r5_verdict_rejects_invalid_human_signature -q _(id: [rec-02ad65e6-5b73-4781-ad50-2ceac314dd59](.artifacts/records/project__acceptance/rec-02ad65e6-5b73-4781-ad50-2ceac314dd59.md))_

### Check
- **human-claim-reject**: rec-02ad65e6-5b73-4781-ad50-2ceac314dd59; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; tdd _(id: [rec-1a1eda4d-30e7-4bc6-8f50-871d57e11f86](.artifacts/records/project__check-run/rec-1a1eda4d-30e7-4bc6-8f50-871d57e11f86.md))_
- **human-claim-reject**: rec-02ad65e6-5b73-4781-ad50-2ceac314dd59; dirty; fail; tdd _(id: [rec-c9c47b43-90bb-4bd8-a608-d5a10c203cdb](.artifacts/records/project__check-run/rec-c9c47b43-90bb-4bd8-a608-d5a10c203cdb.md))_

## junit-run-tests

### Acceptance
- **junit-run-tests**: run_tests returns one outcome per requested id from the JUnit file the command wrote; tdd; evidence-layer; python3 -m pytest tests/test_runner.py -q -k returns_id_outcomes _(id: [rec-63cf9023-9285-4f13-8e47-c12c9961223e](.artifacts/records/project__acceptance/rec-63cf9023-9285-4f13-8e47-c12c9961223e.md))_

### Check
- **junit-run-tests**: rec-63cf9023-9285-4f13-8e47-c12c9961223e; 4fb7199c6f71c99d2def7049ac7e57f67f36e641; fail; tdd _(id: [rec-5c8684a0-19d0-4b45-a3ce-73c70b79ef8d](.artifacts/records/project__check-run/rec-5c8684a0-19d0-4b45-a3ce-73c70b79ef8d.md))_
- **junit-run-tests**: rec-63cf9023-9285-4f13-8e47-c12c9961223e; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; tdd _(id: [rec-5d6717bd-5e9e-4dd7-ae37-7746655e21cd](.artifacts/records/project__check-run/rec-5d6717bd-5e9e-4dd7-ae37-7746655e21cd.md))_
- **junit-run-tests**: rec-63cf9023-9285-4f13-8e47-c12c9961223e; a94b0e1ff8123fa7b773abc5b868a7c1d69db96f; pass; tdd _(id: [rec-b61e5830-b95b-4ccb-b255-89aedc827f77](.artifacts/records/project__check-run/rec-b61e5830-b95b-4ccb-b255-89aedc827f77.md))_

## junit-run-tests-join

### Acceptance
- **junit-run-tests-join**: A case matches a witness id by name, or by file plus the classname segments after the file stem; tdd; evidence-layer; python3 -m pytest tests/test_runner.py -q -k joins_name_or_file _(id: [rec-433330be-3e4d-4928-9af1-1a2aa7d1719c](.artifacts/records/project__acceptance/rec-433330be-3e4d-4928-9af1-1a2aa7d1719c.md))_

### Check
- **junit-run-tests-join**: rec-433330be-3e4d-4928-9af1-1a2aa7d1719c; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; tdd _(id: [rec-2a9fb485-a172-4563-9432-6631409262ea](.artifacts/records/project__check-run/rec-2a9fb485-a172-4563-9432-6631409262ea.md))_
- **junit-run-tests-join**: rec-433330be-3e4d-4928-9af1-1a2aa7d1719c; a94b0e1ff8123fa7b773abc5b868a7c1d69db96f; pass; tdd _(id: [rec-5d6831a7-b363-4c24-adf7-29207215fe46](.artifacts/records/project__check-run/rec-5d6831a7-b363-4c24-adf7-29207215fe46.md))_
- **junit-run-tests-join**: rec-433330be-3e4d-4928-9af1-1a2aa7d1719c; 4fb7199c6f71c99d2def7049ac7e57f67f36e641; fail; tdd _(id: [rec-9d3ecd27-e1a2-47e3-b3dd-7d9736785b38](.artifacts/records/project__check-run/rec-9d3ecd27-e1a2-47e3-b3dd-7d9736785b38.md))_

## junit-run-tests-tags

### Acceptance
- **junit-run-tests-tags**: A JUnit failure is assertion_failed, an error is errored, a skip or a missing case is not_run, and a failure plus an error is errored; tdd; evidence-layer; python3 -m pytest tests/test_runner.py -q -k maps_failure_error_skipped _(id: [rec-cca4eb26-7518-47f2-9160-6f6480f68d02](.artifacts/records/project__acceptance/rec-cca4eb26-7518-47f2-9160-6f6480f68d02.md))_

### Check
- **junit-run-tests-tags**: rec-cca4eb26-7518-47f2-9160-6f6480f68d02; 4fb7199c6f71c99d2def7049ac7e57f67f36e641; fail; tdd _(id: [rec-11856921-9987-482f-aef3-ea054becd728](.artifacts/records/project__check-run/rec-11856921-9987-482f-aef3-ea054becd728.md))_
- **junit-run-tests-tags**: rec-cca4eb26-7518-47f2-9160-6f6480f68d02; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; tdd _(id: [rec-8470ebb5-d5d2-4b3a-a2d6-c25a0daeef37](.artifacts/records/project__check-run/rec-8470ebb5-d5d2-4b3a-a2d6-c25a0daeef37.md))_
- **junit-run-tests-tags**: rec-cca4eb26-7518-47f2-9160-6f6480f68d02; a94b0e1ff8123fa7b773abc5b868a7c1d69db96f; pass; tdd _(id: [rec-90e8cdf1-d4c0-4e10-b4dd-344b3f18261f](.artifacts/records/project__check-run/rec-90e8cdf1-d4c0-4e10-b4dd-344b3f18261f.md))_

## kind-enforcement

### Acceptance
- **kind-enforcement**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r1_manifest_claim_may_declare_evidence_kind -q _(id: [rec-1ef835e4-41dc-4aeb-8462-c21de870e1f1](.artifacts/records/project__acceptance/rec-1ef835e4-41dc-4aeb-8462-c21de870e1f1.md))_

### Check
- **kind-enforcement**: rec-1ef835e4-41dc-4aeb-8462-c21de870e1f1; 2c6d4575f86acb22f0e6af5f4ce60051888bcb2d; pass; tdd _(id: [rec-76ec6658-1903-4b6b-b74f-f8c4497e3985](.artifacts/records/project__check-run/rec-76ec6658-1903-4b6b-b74f-f8c4497e3985.md))_
- **kind-enforcement**: rec-1ef835e4-41dc-4aeb-8462-c21de870e1f1; dirty; fail; tdd _(id: [rec-8e9f1f73-e54b-45f8-bf73-6390a71ee4a0](.artifacts/records/project__check-run/rec-8e9f1f73-e54b-45f8-bf73-6390a71ee4a0.md))_

## kind-enforcement-r2

### Acceptance
- **kind-enforcement-r2**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r2_interaction_claim_fails_under_default_unit_runner -q _(id: [rec-6e679668-c104-4f8b-af4e-0ec2fdf06601](.artifacts/records/project__acceptance/rec-6e679668-c104-4f8b-af4e-0ec2fdf06601.md))_

### Check
- **kind-enforcement-r2**: rec-6e679668-c104-4f8b-af4e-0ec2fdf06601; 2c6d4575f86acb22f0e6af5f4ce60051888bcb2d; pass; tdd _(id: [rec-ab148b15-5a25-4c9c-a52e-0e10bd8bcf77](.artifacts/records/project__check-run/rec-ab148b15-5a25-4c9c-a52e-0e10bd8bcf77.md))_
- **kind-enforcement-r2**: rec-6e679668-c104-4f8b-af4e-0ec2fdf06601; dirty; fail; tdd _(id: [rec-f78b9e79-c33b-48d5-b794-1d65a2b30768](.artifacts/records/project__check-run/rec-f78b9e79-c33b-48d5-b794-1d65a2b30768.md))_

## kind-enforcement-r3

### Acceptance
- **kind-enforcement-r3**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r3_interaction_claim_passes_under_interaction_runner -q _(id: [rec-4a04e8e2-2dd3-40ef-aa2b-6466115aa6bd](.artifacts/records/project__acceptance/rec-4a04e8e2-2dd3-40ef-aa2b-6466115aa6bd.md))_

### Check
- **kind-enforcement-r3**: rec-4a04e8e2-2dd3-40ef-aa2b-6466115aa6bd; dirty; fail; tdd _(id: [rec-49f849a9-94c6-4270-955b-b5ea1f17c804](.artifacts/records/project__check-run/rec-49f849a9-94c6-4270-955b-b5ea1f17c804.md))_
- **kind-enforcement-r3**: rec-4a04e8e2-2dd3-40ef-aa2b-6466115aa6bd; 2c6d4575f86acb22f0e6af5f4ce60051888bcb2d; pass; tdd _(id: [rec-666544f2-57b7-476a-8821-17627661536f](.artifacts/records/project__check-run/rec-666544f2-57b7-476a-8821-17627661536f.md))_

## move-effort-records

### Acceptance
- **move-effort-records**: Both stores validate; the active goal here is evidence-layer; the active goals in orchestra are dashboard, workflow-loop, packaging, session-analysis, and test-suite-speed; check; evidence-layer; adaptive-artifacts validate && adaptive-artifacts --store "$HOME/orchestra/.artifacts" validate && python3 -c 'import json,os,subprocess
def goals(store):
 out=subprocess.check_output(["adaptive-artifacts","--store",store,"list","--type","project:active-goal","--state","active"],text=True)
 return sorted(r["subject"] for r in json.loads(out)["records"] if r.get("payload",{}).get("status")!="closed")
assert goals(".artifacts")==["evidence-layer"]
assert goals(os.path.expanduser("~/orchestra/.artifacts"))==["dashboard","packaging","session-analysis","test-suite-speed","workflow-loop"]' _(id: [rec-119ad93e-8886-4e96-912f-4ca9268d5971](.artifacts/records/project__acceptance/rec-119ad93e-8886-4e96-912f-4ca9268d5971.md))_

### Check
- **move-effort-records**: rec-119ad93e-8886-4e96-912f-4ca9268d5971; dirty; pass; check _(id: [rec-e14e624e-3966-4a60-b00a-d4da7de10dc0](.artifacts/records/project__check-run/rec-e14e624e-3966-4a60-b00a-d4da7de10dc0.md))_

## move-store-client

### Acceptance
- **move-store-client**: bin/orchestra check and close-batch --help exit 0, and the moved check, close-batch, and store-client tests pass in ~/orchestra; check; evidence-layer; cd "$HOME/orchestra" && bin/orchestra check --help && bin/orchestra close-batch --help && python3 -m pytest tests/test_affidavit_check.py tests/test_close_batch.py tests/test_affidavit_aa.py tests/test_aa_resolve.py -q _(id: [rec-d0a726bc-62cc-4cb2-a95c-f4dd36e50532](.artifacts/records/project__acceptance/rec-d0a726bc-62cc-4cb2-a95c-f4dd36e50532.md))_

### Check
- **move-store-client**: rec-d0a726bc-62cc-4cb2-a95c-f4dd36e50532; 2483da2da2ad4929ad5853978d57335072ff577a; pass; check _(id: [rec-7f080418-07e4-4fac-9f36-4c6c9956e056](.artifacts/records/project__check-run/rec-7f080418-07e4-4fac-9f36-4c6c9956e056.md))_
- **move-store-client**: rec-d0a726bc-62cc-4cb2-a95c-f4dd36e50532; 2f2054aeccef9db20ac96d84d3c7f09d2647adfd; pass; check _(id: [rec-de9391cb-a21a-45de-b4d1-1c58bff90f11](.artifacts/records/project__check-run/rec-de9391cb-a21a-45de-b4d1-1c58bff90f11.md))_

### Finding
- **move-store-client**: move-store-client closed done with a tdd pass that has no prior red check-run; aff check rec-e02d9d80-9036-481f-acec-0cc6f8f8c321 passed at 2483da2da2ad4929ad5853978d57335072ff577a. The executor committed tests/test_affidavit_import_boundary.py and the implementation in that same commit, so no runner-produced fail precedes the green.; a runner-produced fail for acceptance rec-bcc3412b-e7c6-4c97-988b-ea215bcb0c94 has a revision that is an ancestor of the green, or a human accepts this pass without red-first evidence; none _(id: [rec-7f5b80b9-cd8d-4376-9994-3553c0434f71](.artifacts/records/project__finding/rec-7f5b80b9-cd8d-4376-9994-3553c0434f71.md))_

## move-store-client-imports

### Acceptance
- **move-store-client-imports**: orchestra imports affidavit.oracle_red from the close path and does not import affidavit.aa, affidavit.aa_resolve, affidavit.check, affidavit.policy, or affidavit.verdict; tdd; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_affidavit_import_boundary.py -q _(id: [rec-bcc3412b-e7c6-4c97-988b-ea215bcb0c94](.artifacts/records/project__acceptance/rec-bcc3412b-e7c6-4c97-988b-ea215bcb0c94.md))_

### Check
- **move-store-client-imports**: rec-bcc3412b-e7c6-4c97-988b-ea215bcb0c94; 2f2054aeccef9db20ac96d84d3c7f09d2647adfd; pass; tdd _(id: [rec-62bca6f5-68b8-44e4-93ac-4b2863b8c243](.artifacts/records/project__check-run/rec-62bca6f5-68b8-44e4-93ac-4b2863b8c243.md))_
- **move-store-client-imports**: rec-bcc3412b-e7c6-4c97-988b-ea215bcb0c94; 2483da2da2ad4929ad5853978d57335072ff577a; pass; tdd _(id: [rec-e02d9d80-9036-481f-acec-0cc6f8f8c321](.artifacts/records/project__check-run/rec-e02d9d80-9036-481f-acec-0cc6f8f8c321.md))_

## observation-cli

### Acceptance
- **observation-cli**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_interface.py::test_r2_verdict_records_one_evidence_observation tests/test_evidence_interface.py::test_r2_verdict_without_store_matches_prephase_semantics -q _(id: [rec-e112515b-ee14-470f-a980-8a4943bec4a1](.artifacts/records/project__acceptance/rec-e112515b-ee14-470f-a980-8a4943bec4a1.md))_

### Check
- **observation-cli**: rec-e112515b-ee14-470f-a980-8a4943bec4a1; a655bf41071f6783be3049a8107ac8e28c54ee55; pass; tdd _(id: [rec-73d3effe-33d4-4038-a508-3c64a8c26df9](.artifacts/records/project__check-run/rec-73d3effe-33d4-4038-a508-3c64a8c26df9.md))_
- **observation-cli**: rec-e112515b-ee14-470f-a980-8a4943bec4a1; dirty; fail; tdd _(id: [rec-ceb6c592-0153-4691-ab00-f11cff6ec162](.artifacts/records/project__check-run/rec-ceb6c592-0153-4691-ab00-f11cff6ec162.md))_

## observation-cli-trail

### Acceptance
- **observation-cli-trail**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_interface.py::test_r3_aff_trail_lists_observations_as_json -q _(id: [rec-16b9050f-19e0-4ed7-af49-b2294f2cc62f](.artifacts/records/project__acceptance/rec-16b9050f-19e0-4ed7-af49-b2294f2cc62f.md))_

### Check
- **observation-cli-trail**: rec-16b9050f-19e0-4ed7-af49-b2294f2cc62f; a655bf41071f6783be3049a8107ac8e28c54ee55; pass; tdd _(id: [rec-18a40637-35ff-4c76-b989-21c7df512646](.artifacts/records/project__check-run/rec-18a40637-35ff-4c76-b989-21c7df512646.md))_
- **observation-cli-trail**: rec-16b9050f-19e0-4ed7-af49-b2294f2cc62f; dirty; fail; tdd _(id: [rec-411abc6c-cc0d-4610-af28-fe91f9503c79](.artifacts/records/project__check-run/rec-411abc6c-cc0d-4610-af28-fe91f9503c79.md))_

## observation-contract

### Acceptance
- **observation-contract**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_interface.py::test_r1_contract_defines_evidence_observation -q _(id: [rec-8d9025b0-5c74-4542-b5dc-4b41890bc5a1](.artifacts/records/project__acceptance/rec-8d9025b0-5c74-4542-b5dc-4b41890bc5a1.md))_

### Check
- **observation-contract**: rec-8d9025b0-5c74-4542-b5dc-4b41890bc5a1; 15064f44e70cf6f7ec5729946fbc7df9ca23f3cb; pass; tdd _(id: [rec-6c8d22f5-9cd7-4c4d-8935-182e1fe484ae](.artifacts/records/project__check-run/rec-6c8d22f5-9cd7-4c4d-8935-182e1fe484ae.md))_
- **observation-contract**: rec-8d9025b0-5c74-4542-b5dc-4b41890bc5a1; dirty; fail; tdd _(id: [rec-f67f556d-2f4f-4215-8312-cb047577b18d](.artifacts/records/project__check-run/rec-f67f556d-2f4f-4215-8312-cb047577b18d.md))_

## orchestration-split-review

### Check
- **orchestration-split-review**: orchestration-split-review; f67741737facb4a494ede2a0d4132b1a451f3c5c; fail; review _(id: [rec-b543e571-50db-40ce-893b-0732b05b3057](.artifacts/records/project__check-run/rec-b543e571-50db-40ce-893b-0732b05b3057.md))_
- **orchestration-split-review**: orchestration-split-review; 43bb26ec008e43d3c149f7d9fee38249e7a5d8c8; pass; review _(id: [rec-e353005b-becd-409a-b2eb-0172cc40772a](.artifacts/records/project__check-run/rec-e353005b-becd-409a-b2eb-0172cc40772a.md))_

## parse-manifest-runner

### Acceptance
- **parse-manifest-runner**: An absent runner loads as the shipped pytest template, and a runner that is not an argv list with {tests} and {report} fails manifest load; tdd; evidence-layer; python3 -m pytest tests/test_manifest.py -q -k "runner_absent or runner_invalid" _(id: [rec-2f6be402-8d78-4007-b3a4-e2a0ac1eec4a](.artifacts/records/project__acceptance/rec-2f6be402-8d78-4007-b3a4-e2a0ac1eec4a.md))_

### Check
- **parse-manifest-runner**: rec-2f6be402-8d78-4007-b3a4-e2a0ac1eec4a; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; tdd _(id: [rec-2ed9bd31-6008-400b-87e6-f8cfe7bebd78](.artifacts/records/project__check-run/rec-2ed9bd31-6008-400b-87e6-f8cfe7bebd78.md))_
- **parse-manifest-runner**: rec-2f6be402-8d78-4007-b3a4-e2a0ac1eec4a; a94b0e1ff8123fa7b773abc5b868a7c1d69db96f; pass; tdd _(id: [rec-3c7d4870-8a69-406a-b076-0ad19a8790e5](.artifacts/records/project__check-run/rec-3c7d4870-8a69-406a-b076-0ad19a8790e5.md))_
- **parse-manifest-runner**: rec-2f6be402-8d78-4007-b3a4-e2a0ac1eec4a; 4fb7199c6f71c99d2def7049ac7e57f67f36e641; fail; tdd _(id: [rec-4d9aa6ea-7e5a-4f14-98cd-138987a79db4](.artifacts/records/project__check-run/rec-4d9aa6ea-7e5a-4f14-98cd-138987a79db4.md))_

## provenance-check

### Acceptance
- **provenance-check**: tdd; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r1_oracle_after_implementation_fails -q _(id: [rec-0f86bd5c-0f8d-4e98-b84d-cc6ac1721055](.artifacts/records/project__acceptance/rec-0f86bd5c-0f8d-4e98-b84d-cc6ac1721055.md))_

### Check
- **provenance-check**: rec-0f86bd5c-0f8d-4e98-b84d-cc6ac1721055; 62db733ebc97851acd532d5103e2ae04130945cb; pass; tdd _(id: [rec-0c4a2630-4fc6-43a3-a874-d533da39a8f3](.artifacts/records/project__check-run/rec-0c4a2630-4fc6-43a3-a874-d533da39a8f3.md))_
- **provenance-check**: rec-0f86bd5c-0f8d-4e98-b84d-cc6ac1721055; dirty; fail; tdd _(id: [rec-31007f49-a6da-4701-a887-6c4ab8ecd18f](.artifacts/records/project__check-run/rec-31007f49-a6da-4701-a887-6c4ab8ecd18f.md))_

## provenance-check-pass

### Acceptance
- **provenance-check-pass**: tdd; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r4_ordered_oracle_only_distinct_signers_passes -q _(id: [rec-4cd9610f-2e6d-4690-97d8-507039b477dd](.artifacts/records/project__acceptance/rec-4cd9610f-2e6d-4690-97d8-507039b477dd.md))_

### Check
- **provenance-check-pass**: rec-4cd9610f-2e6d-4690-97d8-507039b477dd; 62db733ebc97851acd532d5103e2ae04130945cb; pass; tdd _(id: [rec-368628d9-364e-4f62-98b6-25aebaf9dcbf](.artifacts/records/project__check-run/rec-368628d9-364e-4f62-98b6-25aebaf9dcbf.md))_
- **provenance-check-pass**: rec-4cd9610f-2e6d-4690-97d8-507039b477dd; dirty; fail; tdd _(id: [rec-70efa345-56d1-4b40-a398-5afd77569367](.artifacts/records/project__check-run/rec-70efa345-56d1-4b40-a398-5afd77569367.md))_

## provenance-check-paths

### Acceptance
- **provenance-check-paths**: tdd; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r2_oracle_commit_touches_non_oracle_paths_fails -q _(id: [rec-b7c8c328-c343-43d3-aa47-68e0f1a43c2a](.artifacts/records/project__acceptance/rec-b7c8c328-c343-43d3-aa47-68e0f1a43c2a.md))_

### Check
- **provenance-check-paths**: rec-b7c8c328-c343-43d3-aa47-68e0f1a43c2a; dirty; fail; tdd _(id: [rec-1318166f-4cc7-4cf8-824a-05752f5712a2](.artifacts/records/project__check-run/rec-1318166f-4cc7-4cf8-824a-05752f5712a2.md))_
- **provenance-check-paths**: rec-b7c8c328-c343-43d3-aa47-68e0f1a43c2a; 62db733ebc97851acd532d5103e2ae04130945cb; pass; tdd _(id: [rec-7faccc65-f80f-491f-90b9-40b0ce155e05](.artifacts/records/project__check-run/rec-7faccc65-f80f-491f-90b9-40b0ce155e05.md))_

## provenance-check-signer

### Acceptance
- **provenance-check-signer**: tdd; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r3_shared_signer_fails -q _(id: [rec-d58ef0da-0be5-47e0-8ed8-140bd9cc586e](.artifacts/records/project__acceptance/rec-d58ef0da-0be5-47e0-8ed8-140bd9cc586e.md))_

### Check
- **provenance-check-signer**: rec-d58ef0da-0be5-47e0-8ed8-140bd9cc586e; 62db733ebc97851acd532d5103e2ae04130945cb; pass; tdd _(id: [rec-379d141f-41de-4635-8e45-788db8f75614](.artifacts/records/project__check-run/rec-379d141f-41de-4635-8e45-788db8f75614.md))_
- **provenance-check-signer**: rec-d58ef0da-0be5-47e0-8ed8-140bd9cc586e; dirty; fail; tdd _(id: [rec-b72065a0-66fc-4e63-818e-1f31db04f76c](.artifacts/records/project__check-run/rec-b72065a0-66fc-4e63-818e-1f31db04f76c.md))_

## review-move-effort-records-spec-gap

### Finding
- **review-move-effort-records-spec-gap**: spec-gap on move-effort-records: the phase-head store still holds every effort; Reviewer read .artifacts at f677417, the pre-split snapshot on the phase branch; a passing review at the phase head accepts the live stores on main and in ~/orchestra, or the human clears this finding; none _(id: [rec-6a11bf68-24f1-46c3-86f3-a154d4fe8a8b](.artifacts/records/project__finding/rec-6a11bf68-24f1-46c3-86f3-a154d4fe8a8b.md))_

## review-move-store-client-missing-test

### Finding
- **review-move-store-client-missing-test**: missing-test on move-store-client: bin/orchestra check and close-batch --help exit 0; test_bin_affidavit_entry only runs bin/orchestra --help; fix lands and reviewer re-run passes, or human clears; none _(id: [rec-d65b54e0-2ae7-47b1-abaa-892727231b09](.artifacts/records/project__finding/rec-d65b54e0-2ae7-47b1-abaa-892727231b09.md))_

## review-phase-missing-test-amendment

### Finding
- **review-phase-missing-test-amendment**: missing-test on phase: aff verdict must exit 0 when a test-id or hash delta is covered by a verified amendment and the allowlist is unchanged; tests/test_verdict.py has no subprocess test where a valid signed amendment makes an oracle or hash change pass; fix lands and reviewer re-run passes, or human clears; none _(id: [rec-0fcac021-f6ba-4d23-802e-999a1f6e2d1d](.artifacts/records/project__finding/rec-0fcac021-f6ba-4d23-802e-999a1f6e2d1d.md))_

## review-phase-missing-test-head-fail

### Finding
- **review-phase-missing-test-head-fail**: missing-test on phase: aff verdict must exit non-zero when oracle tests fail at --at; tests/test_verdict.py does not assert exit 1 and reason tests failed for a failing head run; fix lands and reviewer re-run passes, or human clears; none _(id: [rec-a708259b-4d9b-466b-97b3-33c8b2b345c2](.artifacts/records/project__finding/rec-a708259b-4d9b-466b-97b3-33c8b2b345c2.md))_

## review-phase-missing-test-missing-step

### Finding
- **review-phase-missing-test-missing-step**: missing-test on phase: aff verdict must exit non-zero when test ids or hashes differ without a covering amendment chain; missing step is only covered in tests/test_amendment.py; tests/test_verdict.py has no CLI case for a manifest delta with no amendment; fix lands and reviewer re-run passes, or human clears; none _(id: [rec-f5ae5085-839d-47e7-ac68-ea6ef1cb6107](.artifacts/records/project__finding/rec-f5ae5085-839d-47e7-ac68-ea6ef1cb6107.md))_

## review-phase-missing-test-verdict-help

### Finding
- **review-phase-missing-test-verdict-help**: missing-test on phase: bin/aff verdict --help exits 0; tests/test_standalone_cli.py does not assert verdict --help exit 0; fix lands and reviewer re-run passes, or human clears; none _(id: [rec-32467d43-dc9b-4815-a5a7-e97098dc5552](.artifacts/records/project__finding/rec-32467d43-dc9b-4815-a5a7-e97098dc5552.md))_

## review-strip-affidavit-spec-gap

### Finding
- **review-strip-affidavit-spec-gap**: spec-gap on strip-affidavit: AGENTS.md and README.md still describe the full plugin; Reviewer compared the stripped tree with AGENTS.md and README.md at f677417; docs match the evidence-layer tree and a review re-run passes, or the human clears this finding; none _(id: [rec-0588c8c0-26e7-40d6-a78f-1264bf16a271](.artifacts/records/project__finding/rec-0588c8c0-26e7-40d6-a78f-1264bf16a271.md))_

## review-verdict-command-behavior-bug

### Finding
- **review-verdict-command-behavior-bug**: behavior-bug on verdict-command: R2 requires pytest exit code 0 at --at for each claim's oracle tests; _head_passed returns true when exit_code != 0 if no FAILED/ERROR line matches the claim's node ids; fix lands and reviewer re-run passes, or human clears; none _(id: [rec-76d3d72d-c672-4634-8aea-560a2d2d4e7e](.artifacts/records/project__finding/rec-76d3d72d-c672-4634-8aea-560a2d2d4e7e.md))_

## rewrite-project-field

### Acceptance
- **rewrite-project-field**: A fixture whose project is affidavit is rewritten to orchestra, a fixture whose project is another name is unchanged, and the bundled contract project is orchestra; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_ensure_store_project.py -q _(id: [rec-80579791-d24b-4717-8664-25dbb29e89b9](.artifacts/records/project__acceptance/rec-80579791-d24b-4717-8664-25dbb29e89b9.md))_

### Check
- **rewrite-project-field**: rec-80579791-d24b-4717-8664-25dbb29e89b9; b4f59462fd054c0f266e3e1b7872a46472587286; fail; tdd _(id: [rec-41b87bf9-c902-4143-bb92-8483e4982661](.artifacts/records/project__check-run/rec-41b87bf9-c902-4143-bb92-8483e4982661.md))_
- **rewrite-project-field**: rec-80579791-d24b-4717-8664-25dbb29e89b9; 4cee07f421cc4a3de7996e5e02879cbc41b7a2ed; pass; tdd _(id: [rec-5d763c3d-7047-4530-a4e0-c869e984782e](.artifacts/records/project__check-run/rec-5d763c3d-7047-4530-a4e0-c869e984782e.md))_

## runner-adapter-review

### Check
- **runner-adapter-review**: runner-adapter-review; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; review _(id: [rec-86ed0a51-274d-454b-986d-8eb915664d2b](.artifacts/records/project__check-run/rec-86ed0a51-274d-454b-986d-8eb915664d2b.md))_

## scaffold-orchestra

### Acceptance
- **scaffold-orchestra**: orchestra.reviewer and orchestra.suite import, orchestra.tier2 does not, and affidavit/tier2.py is absent from ~/orchestra; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_orchestra_package.py -q _(id: [rec-85630b31-3c07-4f31-9cd9-6c4b31419fc9](.artifacts/records/project__acceptance/rec-85630b31-3c07-4f31-9cd9-6c4b31419fc9.md))_

### Check
- **scaffold-orchestra**: rec-85630b31-3c07-4f31-9cd9-6c4b31419fc9; de92a579897aa1aa1f2e8788d47697a74bc58513; pass; tdd _(id: [rec-15fdb7bb-8cf8-4323-9da0-652aff73c7b2](.artifacts/records/project__check-run/rec-15fdb7bb-8cf8-4323-9da0-652aff73c7b2.md))_
- **scaffold-orchestra**: rec-85630b31-3c07-4f31-9cd9-6c4b31419fc9; dcbe257640b906280cb8cdc8a72c531dc1c4cee0; fail; tdd _(id: [rec-fde41e1f-0069-45a5-a005-cadfbb9769ea](.artifacts/records/project__check-run/rec-fde41e1f-0069-45a5-a005-cadfbb9769ea.md))_

## scaffold-orchestra-layout

### Acceptance
- **scaffold-orchestra-layout**: ~/orchestra contains the seven skill directories and dashboard/, and both plugin manifests are named orchestra; check; evidence-layer; cd ~/orchestra && test -d skills/engage && test -d skills/discuss && test -d skills/plan-phase && test -d skills/execute-phase && test -d skills/verify-work && test -d skills/init && test -d skills/analyze-sessions && test -d dashboard && python3 -c "import json; from pathlib import Path; names=[json.loads(Path(p).read_text())[\"name\"] for p in [\".cursor-plugin/plugin.json\",\".claude-plugin/plugin.json\"]]; assert names==[\"orchestra\",\"orchestra\"]" _(id: [rec-bb8fcfec-3f8c-49dd-a274-6f88e947c6c4](.artifacts/records/project__acceptance/rec-bb8fcfec-3f8c-49dd-a274-6f88e947c6c4.md))_

### Check
- **scaffold-orchestra-layout**: rec-bb8fcfec-3f8c-49dd-a274-6f88e947c6c4; de92a579897aa1aa1f2e8788d47697a74bc58513; pass; check _(id: [rec-b905a6d5-a097-4b18-9666-9831281ea720](.artifacts/records/project__check-run/rec-b905a6d5-a097-4b18-9666-9831281ea720.md))_

## skill-command-names

### Acceptance
- **skill-command-names**: orchestra skills run orchestra check and orchestra close-batch, and still run aff verdict for a manifest claim; tdd; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_orchestra_commands.py -q _(id: [rec-4d363eb6-fdda-45d0-a8ba-65a04506823c](.artifacts/records/project__acceptance/rec-4d363eb6-fdda-45d0-a8ba-65a04506823c.md))_

### Check
- **skill-command-names**: rec-4d363eb6-fdda-45d0-a8ba-65a04506823c; cac5247ddb6774f9a490bf7f3c5593a36a790b09; pass; tdd _(id: [rec-2cf353e2-93e1-416d-b3f8-fb1b472a6c63](.artifacts/records/project__check-run/rec-2cf353e2-93e1-416d-b3f8-fb1b472a6c63.md))_
- **skill-command-names**: rec-4d363eb6-fdda-45d0-a8ba-65a04506823c; bb08d79c18804473fea229fb2eb1bfa8ec3ec6f7; fail; tdd _(id: [rec-579cbf13-4c6e-4d50-a835-6f1ebaf610ce](.artifacts/records/project__check-run/rec-579cbf13-4c6e-4d50-a835-6f1ebaf610ce.md))_
- **skill-command-names**: rec-4d363eb6-fdda-45d0-a8ba-65a04506823c; 2f2054aeccef9db20ac96d84d3c7f09d2647adfd; pass; tdd _(id: [rec-a1628187-6e4b-4413-a2e3-3c99499d3dd0](.artifacts/records/project__check-run/rec-a1628187-6e4b-4413-a2e3-3c99499d3dd0.md))_

## skill-evidence-boundary

### Acceptance
- **skill-evidence-boundary**: The boundary test fails on a fixture skill that creates a tdd check-run or a project:oracle-amendment, and passes on the migrated skills; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_skill_evidence_boundary.py -q -k "not verdict" _(id: [rec-3b292b01-e0a5-4159-addb-fcd87fe76d35](.artifacts/records/project__acceptance/rec-3b292b01-e0a5-4159-addb-fcd87fe76d35.md))_

### Check
- **skill-evidence-boundary**: rec-3b292b01-e0a5-4159-addb-fcd87fe76d35; 2df7598d15159946435617cd150ab4d4dd9329c8; fail; tdd _(id: [rec-7de63769-f16f-4201-9bd7-691885ea4120](.artifacts/records/project__check-run/rec-7de63769-f16f-4201-9bd7-691885ea4120.md))_
- **skill-evidence-boundary**: rec-3b292b01-e0a5-4159-addb-fcd87fe76d35; dae249d5636867d70f13c91d0e3710fcb4d39991; pass; tdd _(id: [rec-a967eb4d-4395-4b69-9ba0-40ff5dd889c0](.artifacts/records/project__check-run/rec-a967eb4d-4395-4b69-9ba0-40ff5dd889c0.md))_

## skill-evidence-boundary-verdict

### Acceptance
- **skill-evidence-boundary-verdict**: execute-phase and verify-work run aff verdict for a claim in the manifest and treat a non-zero exit as not done; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_skill_evidence_boundary.py -q -k verdict _(id: [rec-157b8a77-5bd4-4462-a516-cfed02b4ef1a](.artifacts/records/project__acceptance/rec-157b8a77-5bd4-4462-a516-cfed02b4ef1a.md))_

### Check
- **skill-evidence-boundary-verdict**: rec-157b8a77-5bd4-4462-a516-cfed02b4ef1a; dae249d5636867d70f13c91d0e3710fcb4d39991; pass; tdd _(id: [rec-03198204-22cb-4928-b7ba-a3cecbb55c0a](.artifacts/records/project__check-run/rec-03198204-22cb-4928-b7ba-a3cecbb55c0a.md))_
- **skill-evidence-boundary-verdict**: rec-157b8a77-5bd4-4462-a516-cfed02b4ef1a; 2df7598d15159946435617cd150ab4d4dd9329c8; fail; tdd _(id: [rec-cadc74d5-035f-4bda-a98e-cc74e02414e6](.artifacts/records/project__check-run/rec-cadc74d5-035f-4bda-a98e-cc74e02414e6.md))_

## standalone-aff-review

### Check
- **standalone-aff-review**: standalone-aff-review; 2c7dd552e6012ffb8626c635806214073168ba60; fail; review _(id: [rec-766a0816-5356-4a67-9d1b-729a569dd1fc](.artifacts/records/project__check-run/rec-766a0816-5356-4a67-9d1b-729a569dd1fc.md))_
- **standalone-aff-review**: standalone-aff-review; 95816892f1208fd6b13723e6f89a959d6736da44; pass; review _(id: [rec-e96ca8ec-342d-47cf-9fb9-50422b0e9814](.artifacts/records/project__check-run/rec-e96ca8ec-342d-47cf-9fb9-50422b0e9814.md))_

## standalone-aff-suite

### Check
- **standalone-aff-suite**: standalone-aff-suite; 95816892f1208fd6b13723e6f89a959d6736da44; fail; check _(id: [rec-15ca319e-d0bf-4a3a-8c96-c3652b0ea33c](.artifacts/records/project__check-run/rec-15ca319e-d0bf-4a3a-8c96-c3652b0ea33c.md))_

## strip-aff-verbs

### Acceptance
- **strip-aff-verbs**: bin/aff verdict passes with adaptive-artifacts off PATH, and bin/aff check and close-batch are rejected; tdd; evidence-layer; python3 -m pytest tests/test_standalone_cli.py -q _(id: [rec-e054ab1c-dd4a-4324-b7ed-cf3433b2d70f](.artifacts/records/project__acceptance/rec-e054ab1c-dd4a-4324-b7ed-cf3433b2d70f.md))_

### Check
- **strip-aff-verbs**: rec-e054ab1c-dd4a-4324-b7ed-cf3433b2d70f; 2c7dd552e6012ffb8626c635806214073168ba60; pass; tdd _(id: [rec-5fe28fea-fa80-4852-9393-d38a1005266a](.artifacts/records/project__check-run/rec-5fe28fea-fa80-4852-9393-d38a1005266a.md))_
- **strip-aff-verbs**: rec-e054ab1c-dd4a-4324-b7ed-cf3433b2d70f; 95816892f1208fd6b13723e6f89a959d6736da44; pass; tdd _(id: [rec-8405ce98-c548-4e87-a68e-5b71e5e67140](.artifacts/records/project__check-run/rec-8405ce98-c548-4e87-a68e-5b71e5e67140.md))_
- **strip-aff-verbs**: rec-e054ab1c-dd4a-4324-b7ed-cf3433b2d70f; b27be0ba1a99215aacda097f66d3c2b7454b1f13; fail; tdd _(id: [rec-af61f89f-7b84-4483-952d-bba736346c4f](.artifacts/records/project__check-run/rec-af61f89f-7b84-4483-952d-bba736346c4f.md))_

## strip-aff-verbs-boundary

### Acceptance
- **strip-aff-verbs-boundary**: a test fails when any module under affidavit/ contains project:, SE_WORKFLOW_STORE, store-binding.json, or adaptive-artifacts; tdd; evidence-layer; python3 -m pytest tests/test_evidence_layout.py -q -k no_store_tokens _(id: [rec-243ce423-ece2-440a-b36b-826ea9b47660](.artifacts/records/project__acceptance/rec-243ce423-ece2-440a-b36b-826ea9b47660.md))_

### Check
- **strip-aff-verbs-boundary**: rec-243ce423-ece2-440a-b36b-826ea9b47660; 2c7dd552e6012ffb8626c635806214073168ba60; pass; tdd _(id: [rec-1688c984-ffeb-47a3-b8fa-01f423ca3af1](.artifacts/records/project__check-run/rec-1688c984-ffeb-47a3-b8fa-01f423ca3af1.md))_
- **strip-aff-verbs-boundary**: rec-243ce423-ece2-440a-b36b-826ea9b47660; 95816892f1208fd6b13723e6f89a959d6736da44; pass; tdd _(id: [rec-16cca746-2a17-4a50-8b53-abe392058849](.artifacts/records/project__check-run/rec-16cca746-2a17-4a50-8b53-abe392058849.md))_
- **strip-aff-verbs-boundary**: rec-243ce423-ece2-440a-b36b-826ea9b47660; b27be0ba1a99215aacda097f66d3c2b7454b1f13; fail; tdd _(id: [rec-af832c74-9d5a-457b-b316-e775684bdfb3](.artifacts/records/project__check-run/rec-af832c74-9d5a-457b-b316-e775684bdfb3.md))_

## strip-affidavit

### Acceptance
- **strip-affidavit**: With skills/, dashboard/, scripts/, and agents/ absent, bin/aff check, close-batch, and verdict --help exit 0 and the remaining verb tests pass; tdd; evidence-layer; test ! -d skills && test ! -d dashboard && test ! -d scripts && test ! -d agents && bin/aff check --help && bin/aff close-batch --help && bin/aff verdict --help && python3 -m pytest tests/test_evidence_layout.py tests/test_affidavit_check.py tests/test_close_batch.py tests/test_verdict.py tests/test_manifest.py tests/test_amendment.py tests/test_oracle_red.py tests/test_affidavit_aa.py -q _(id: [rec-2badfd8f-ce40-4a92-bc85-6f8fa36c4e01](.artifacts/records/project__acceptance/rec-2badfd8f-ce40-4a92-bc85-6f8fa36c4e01.md))_

### Check
- **strip-affidavit**: rec-2badfd8f-ce40-4a92-bc85-6f8fa36c4e01; f67741737facb4a494ede2a0d4132b1a451f3c5c; pass; tdd _(id: [rec-3ae95d5d-b49b-4c8d-883a-98cf24915b88](.artifacts/records/project__check-run/rec-3ae95d5d-b49b-4c8d-883a-98cf24915b88.md))_
- **strip-affidavit**: rec-2badfd8f-ce40-4a92-bc85-6f8fa36c4e01; fb04f75e57717be91f194736650c437810bbcd5b; fail; tdd _(id: [rec-85a9aafc-7a96-40a3-b042-a1fbd984e050](.artifacts/records/project__check-run/rec-85a9aafc-7a96-40a3-b042-a1fbd984e050.md))_

## suite-advisory-ci-verdict-fixture

### Finding
- **suite-advisory-ci-verdict-fixture**: advisory suite fail for ci-verdict-fixture-suite; exit_code 1; fixture oracle collected by pytest; claim_authoring flaked under xdist; suite check-run passes at phase head, or human clears; none _(id: [rec-be525209-270c-4097-81c6-2883a2451309](.artifacts/records/project__finding/rec-be525209-270c-4097-81c6-2883a2451309.md))_

## suite-advisory-claims-manifest

### Finding
- **suite-advisory-claims-manifest**: advisory suite fail for claims-manifest-suite; exit_code 1; failing node tests/test_dashboard_journal.py::test_journal_detail_pager_pages_record_with_stub; suite check-run passes at phase head, or human clears; none _(id: [rec-43ce266c-c2ac-4895-99e2-e039eac06a4f](.artifacts/records/project__finding/rec-43ce266c-c2ac-4895-99e2-e039eac06a4f.md))_

## suite-advisory-evidence-interface

### Finding
- **suite-advisory-evidence-interface**: advisory suite fail for evidence-interface-suite; exit_code 1; failing_node_ids include tests/test_claim_authoring.py::test_r2_standalone_add_freeze_verdict_passes (JUnit ParseError flake); suite check-run passes at phase head, or human clears; none _(id: [rec-719631ea-8759-4173-bdab-2abe0b0f1ff2](.artifacts/records/project__finding/rec-719631ea-8759-4173-bdab-2abe0b0f1ff2.md))_

## suite-advisory-standalone-aff

### Finding
- **suite-advisory-standalone-aff**: advisory suite fail for standalone-aff-suite; exit_code=5; failing node ids: none (pytest collected no tmux tests); suite check-run passes at phase head, or human clears; none _(id: [rec-741cb0e6-238f-43c3-a038-2dfc5efa7913](.artifacts/records/project__finding/rec-741cb0e6-238f-43c3-a038-2dfc5efa7913.md))_

## verdict-command

### Acceptance
- **verdict-command**: bin/aff verdict exits 0 only when oracle hashes match, the base pytest failure is assertion-level, and the tests pass at head; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or not_assertion" _(id: [rec-39a10c5a-3bf3-4872-8e98-cb5e1082d5fb](.artifacts/records/project__acceptance/rec-39a10c5a-3bf3-4872-8e98-cb5e1082d5fb.md))_

### Check
- **verdict-command**: rec-39a10c5a-3bf3-4872-8e98-cb5e1082d5fb; 512796fda9f16f54a5848fdca999755a8e48eb27; fail; tdd _(id: [rec-472fee89-9dd0-4d3f-9428-60c162d31312](.artifacts/records/project__check-run/rec-472fee89-9dd0-4d3f-9428-60c162d31312.md))_
- **verdict-command**: rec-39a10c5a-3bf3-4872-8e98-cb5e1082d5fb; 512796fda9f16f54a5848fdca999755a8e48eb27; fail; tdd _(id: [rec-9d2aa199-dba5-4711-9c83-1ae38b040ae2](.artifacts/records/project__check-run/rec-9d2aa199-dba5-4711-9c83-1ae38b040ae2.md))_
- **verdict-command**: rec-39a10c5a-3bf3-4872-8e98-cb5e1082d5fb; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-de4e4041-4f98-4318-8c7a-29f76891473c](.artifacts/records/project__check-run/rec-de4e4041-4f98-4318-8c7a-29f76891473c.md))_
- **verdict-command**: rec-39a10c5a-3bf3-4872-8e98-cb5e1082d5fb; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; pass; tdd _(id: [rec-f9e29020-10b3-4a6a-883e-33705cf0be98](.artifacts/records/project__check-run/rec-f9e29020-10b3-4a6a-883e-33705cf0be98.md))_

## verdict-command-cli

### Acceptance
- **verdict-command-cli**: bin/aff verdict subprocess tests refuse a bad amendment signature and an allowlist change, and pass with --cwd pointed at a phase worktree; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "bad_signature or allowlist or cwd_phase" _(id: [rec-7839468b-6ae7-4fe1-a2f7-9c2fcef70187](.artifacts/records/project__acceptance/rec-7839468b-6ae7-4fe1-a2f7-9c2fcef70187.md))_

### Check
- **verdict-command-cli**: rec-7839468b-6ae7-4fe1-a2f7-9c2fcef70187; 512796fda9f16f54a5848fdca999755a8e48eb27; fail; tdd _(id: [rec-6399fbed-fdee-4ace-9686-57ad579d7fc8](.artifacts/records/project__check-run/rec-6399fbed-fdee-4ace-9686-57ad579d7fc8.md))_
- **verdict-command-cli**: rec-7839468b-6ae7-4fe1-a2f7-9c2fcef70187; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-e3f5a0b2-504c-4732-961b-8395364e2c96](.artifacts/records/project__check-run/rec-e3f5a0b2-504c-4732-961b-8395364e2c96.md))_
- **verdict-command-cli**: rec-7839468b-6ae7-4fe1-a2f7-9c2fcef70187; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; pass; tdd _(id: [rec-fe44434d-e52b-49f7-bc0a-5853504a522d](.artifacts/records/project__check-run/rec-fe44434d-e52b-49f7-bc0a-5853504a522d.md))_

## verdict-command-store

### Acceptance
- **verdict-command-store**: A forged project:check-run under .artifacts does not change a passing or a failing bin/aff verdict; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k forged_check_run _(id: [rec-ad7115bc-82ff-4215-a410-0883b5434294](.artifacts/records/project__acceptance/rec-ad7115bc-82ff-4215-a410-0883b5434294.md))_

### Check
- **verdict-command-store**: rec-ad7115bc-82ff-4215-a410-0883b5434294; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-46f6a508-fe1d-421a-bed9-1878dc767be4](.artifacts/records/project__check-run/rec-46f6a508-fe1d-421a-bed9-1878dc767be4.md))_
- **verdict-command-store**: rec-ad7115bc-82ff-4215-a410-0883b5434294; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; pass; tdd _(id: [rec-b7c634e7-4fa8-4795-9239-0130c5afd053](.artifacts/records/project__check-run/rec-b7c634e7-4fa8-4795-9239-0130c5afd053.md))_
- **verdict-command-store**: rec-ad7115bc-82ff-4215-a410-0883b5434294; 512796fda9f16f54a5848fdca999755a8e48eb27; fail; tdd _(id: [rec-ea18b090-b3ce-49c3-b975-adfbe9401123](.artifacts/records/project__check-run/rec-ea18b090-b3ce-49c3-b975-adfbe9401123.md))_

## verdict-manifest

### Acceptance
- **verdict-manifest**: git show of a revision yields the manifest claims, the allowlist bytes, and oracle file hashes; a dirty worktree and a non-commit revision do not; tdd; evidence-layer; python3 -m pytest tests/test_manifest.py -q _(id: [rec-a5646067-6c51-44b0-8302-bfae12644013](.artifacts/records/project__acceptance/rec-a5646067-6c51-44b0-8302-bfae12644013.md))_

### Check
- **verdict-manifest**: rec-a5646067-6c51-44b0-8302-bfae12644013; 86c5ca7847a05fa40cadb02bfe61dd5736b1a33c; fail; tdd _(id: [rec-52963144-3566-4337-8842-2267faaf7472](.artifacts/records/project__check-run/rec-52963144-3566-4337-8842-2267faaf7472.md))_
- **verdict-manifest**: rec-a5646067-6c51-44b0-8302-bfae12644013; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; pass; tdd _(id: [rec-67039a81-7afb-4f63-8308-e077ad7a1a15](.artifacts/records/project__check-run/rec-67039a81-7afb-4f63-8308-e077ad7a1a15.md))_
- **verdict-manifest**: rec-a5646067-6c51-44b0-8302-bfae12644013; 512796fda9f16f54a5848fdca999755a8e48eb27; pass; tdd _(id: [rec-d123be01-a6c5-4d46-a330-df7ae9819fe8](.artifacts/records/project__check-run/rec-d123be01-a6c5-4d46-a330-df7ae9819fe8.md))_
- **verdict-manifest**: rec-a5646067-6c51-44b0-8302-bfae12644013; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-fa7d1356-8b6d-4c5a-bea8-ce0837dbc846](.artifacts/records/project__check-run/rec-fa7d1356-8b6d-4c5a-bea8-ce0837dbc846.md))_

## verdict-through-runner

### Acceptance
- **verdict-through-runner**: aff verdict keeps pass, hash-mismatch, and collection-error results, and verdict.py does not scrape pytest stdout; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or not_assertion or ignores_pytest_stdout" _(id: [rec-11e21744-5979-4d98-a4fe-bb5dc3b0c834](.artifacts/records/project__acceptance/rec-11e21744-5979-4d98-a4fe-bb5dc3b0c834.md))_

### Check
- **verdict-through-runner**: rec-11e21744-5979-4d98-a4fe-bb5dc3b0c834; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; tdd _(id: [rec-5e0f22c6-0ca7-4967-b34f-f9c4ad73356d](.artifacts/records/project__check-run/rec-5e0f22c6-0ca7-4967-b34f-f9c4ad73356d.md))_
- **verdict-through-runner**: rec-11e21744-5979-4d98-a4fe-bb5dc3b0c834; 7a3dd0a507dd61c7137957b1e1a4bc3e7a26e42d; fail; tdd _(id: [rec-9916769a-4965-4252-9e31-ec533ee2239f](.artifacts/records/project__check-run/rec-9916769a-4965-4252-9e31-ec533ee2239f.md))_

## verdict-through-runner-fixture

### Acceptance
- **verdict-through-runner-fixture**: A fixture command that emits JUnit XML is judged pass, not assertion, or tests failed with no new module under affidavit/; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k fixture_junit _(id: [rec-7c5ba8b7-65f1-43b8-ae07-bdefbe64c545](.artifacts/records/project__acceptance/rec-7c5ba8b7-65f1-43b8-ae07-bdefbe64c545.md))_

### Check
- **verdict-through-runner-fixture**: rec-7c5ba8b7-65f1-43b8-ae07-bdefbe64c545; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; tdd _(id: [rec-0866201b-ce0b-462a-b453-da03cae6ddf1](.artifacts/records/project__check-run/rec-0866201b-ce0b-462a-b453-da03cae6ddf1.md))_
- **verdict-through-runner-fixture**: rec-7c5ba8b7-65f1-43b8-ae07-bdefbe64c545; 7a3dd0a507dd61c7137957b1e1a4bc3e7a26e42d; fail; tdd _(id: [rec-40057722-48e8-4adb-928e-ee6cedef12ff](.artifacts/records/project__check-run/rec-40057722-48e8-4adb-928e-ee6cedef12ff.md))_

## verdict-through-runner-unstable

### Acceptance
- **verdict-through-runner-unstable**: A disagreeing confirmation yields unstable and a non-zero exit, and a failed first run is not confirmed; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "unstable_when_confirmation or skips_confirmation" _(id: [rec-ca86ff79-3d6b-4441-91b8-e3e0abd9cdfa](.artifacts/records/project__acceptance/rec-ca86ff79-3d6b-4441-91b8-e3e0abd9cdfa.md))_

### Check
- **verdict-through-runner-unstable**: rec-ca86ff79-3d6b-4441-91b8-e3e0abd9cdfa; 7a3dd0a507dd61c7137957b1e1a4bc3e7a26e42d; fail; tdd _(id: [rec-93bc5ec4-3fbd-4b7b-bec2-1c87662c54be](.artifacts/records/project__check-run/rec-93bc5ec4-3fbd-4b7b-bec2-1c87662c54be.md))_
- **verdict-through-runner-unstable**: rec-ca86ff79-3d6b-4441-91b8-e3e0abd9cdfa; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; tdd _(id: [rec-bd98a4ac-4f41-4ff0-87b9-b2e47f6fce30](.artifacts/records/project__check-run/rec-bd98a4ac-4f41-4ff0-87b9-b2e47f6fce30.md))_

## verify-audit-differential

### Acceptance
- **verify-audit-differential**: check; evidence-layer; python3 -m pytest tests/test_audit_probes.py::test_r1_audit_runs_declared_probes_at_base_and_head -q _(id: [rec-13f0f1fa-e76f-4aa3-8bb5-fe61cfcf603c](.artifacts/records/project__acceptance/rec-13f0f1fa-e76f-4aa3-8bb5-fe61cfcf603c.md))_

### Check
- **verify-audit-differential**: rec-13f0f1fa-e76f-4aa3-8bb5-fe61cfcf603c; 780b98ed03d068aea39f95a1974c5294a2b1bfe9; pass; check _(id: [rec-34a2e6a9-b0a3-4adb-95aa-05e5e73d5555](.artifacts/records/project__check-run/rec-34a2e6a9-b0a3-4adb-95aa-05e5e73d5555.md))_

## verify-audit-differential-claimed

### Acceptance
- **verify-audit-differential-claimed**: check; evidence-layer; python3 -m pytest tests/test_audit_probes.py::test_r2_audit_reports_unclaimed_probe_difference -q _(id: [rec-fddcc59a-aa67-4ce0-95be-bc32e2819a90](.artifacts/records/project__acceptance/rec-fddcc59a-aa67-4ce0-95be-bc32e2819a90.md))_

### Check
- **verify-audit-differential-claimed**: rec-fddcc59a-aa67-4ce0-95be-bc32e2819a90; 780b98ed03d068aea39f95a1974c5294a2b1bfe9; pass; check _(id: [rec-49f97b1a-0545-4d0f-97a5-2000abd98d52](.artifacts/records/project__check-run/rec-49f97b1a-0545-4d0f-97a5-2000abd98d52.md))_

## verify-audit-differential-covered

### Acceptance
- **verify-audit-differential-covered**: check; evidence-layer; python3 -m pytest tests/test_audit_probes.py::test_r3_audit_suppresses_diff_covered_by_cited_claim -q _(id: [rec-77c1f1df-68b6-4338-858d-abb1e844db65](.artifacts/records/project__acceptance/rec-77c1f1df-68b6-4338-858d-abb1e844db65.md))_

### Check
- **verify-audit-differential-covered**: rec-77c1f1df-68b6-4338-858d-abb1e844db65; 780b98ed03d068aea39f95a1974c5294a2b1bfe9; pass; check _(id: [rec-606eb94b-ce55-4b59-80e4-3ec5a9fa9927](.artifacts/records/project__check-run/rec-606eb94b-ce55-4b59-80e4-3ec5a9fa9927.md))_

## verify-audit-differential-range

### Acceptance
- **verify-audit-differential-range**: check; evidence-layer; python3 -m pytest tests/test_audit_probes_range.py::test_r4_audit_reports_unclaimed_tdd_revision_relaxation -q _(id: [rec-dfd72358-f289-4f8c-8835-19e7523701f8](.artifacts/records/project__acceptance/rec-dfd72358-f289-4f8c-8835-19e7523701f8.md))_

### Check
- **verify-audit-differential-range**: rec-dfd72358-f289-4f8c-8835-19e7523701f8; 780b98ed03d068aea39f95a1974c5294a2b1bfe9; pass; check _(id: [rec-a0934f91-db70-42ca-a22f-cb6629bf2366](.artifacts/records/project__check-run/rec-a0934f91-db70-42ca-a22f-cb6629bf2366.md))_

## verify-ci-verdict-fixture

### Acceptance
- **verify-ci-verdict-fixture**: check; evidence-layer; bash tests/fixtures/dry_run_verdict_attest.sh _(id: [rec-01ad59dd-8f29-42c3-989f-ee2b9c915d3e](.artifacts/records/project__acceptance/rec-01ad59dd-8f29-42c3-989f-ee2b9c915d3e.md))_

### Check
- **verify-ci-verdict-fixture**: rec-01ad59dd-8f29-42c3-989f-ee2b9c915d3e; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; check _(id: [rec-3a08f637-9371-4514-8086-37902896d692](.artifacts/records/project__check-run/rec-3a08f637-9371-4514-8086-37902896d692.md))_

## verify-ci-verdict-fixture-pytest

### Acceptance
- **verify-ci-verdict-fixture-pytest**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_ci_workflow_runs_verdict_and_attest -q _(id: [rec-749c9954-a57a-4714-9ed0-d90250c028e3](.artifacts/records/project__acceptance/rec-749c9954-a57a-4714-9ed0-d90250c028e3.md))_

### Check
- **verify-ci-verdict-fixture-pytest**: rec-749c9954-a57a-4714-9ed0-d90250c028e3; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; tdd _(id: [rec-039ce4ae-9673-4210-ae6a-bf21922a1134](.artifacts/records/project__check-run/rec-039ce4ae-9673-4210-ae6a-bf21922a1134.md))_
- **verify-ci-verdict-fixture-pytest**: rec-749c9954-a57a-4714-9ed0-d90250c028e3; dirty; pass; tdd _(id: [rec-15f45303-41df-4da3-8963-c3b5d440cfec](.artifacts/records/project__check-run/rec-15f45303-41df-4da3-8963-c3b5d440cfec.md))_
- **verify-ci-verdict-fixture-pytest**: rec-749c9954-a57a-4714-9ed0-d90250c028e3; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; tdd _(id: [rec-6d19b780-e0f8-4e0b-b2c9-65e1fd40376d](.artifacts/records/project__check-run/rec-6d19b780-e0f8-4e0b-b2c9-65e1fd40376d.md))_
- **verify-ci-verdict-fixture-pytest**: rec-749c9954-a57a-4714-9ed0-d90250c028e3; dirty; fail; tdd _(id: [rec-b214db77-c1b1-4504-aaee-be7a76a321b9](.artifacts/records/project__check-run/rec-b214db77-c1b1-4504-aaee-be7a76a321b9.md))_
- **verify-ci-verdict-fixture-pytest**: rec-749c9954-a57a-4714-9ed0-d90250c028e3; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; tdd _(id: [rec-d497de41-8999-4b88-8ceb-a51d7050a4d7](.artifacts/records/project__check-run/rec-d497de41-8999-4b88-8ceb-a51d7050a4d7.md))_

## verify-ci-verdict-fixture-templates

### Acceptance
- **verify-ci-verdict-fixture-templates**: check; evidence-layer; test -f tests/fixtures/build_verdict_repo.sh && test -f tests/fixtures/verdict-repo/app.py && test -f tests/fixtures/verdict-repo/.affidavit/manifest.json && rg -q "verdict-repo/\.git" .gitignore _(id: [rec-bd904456-5b0e-428c-b743-afb539f03876](.artifacts/records/project__acceptance/rec-bd904456-5b0e-428c-b743-afb539f03876.md))_

### Check
- **verify-ci-verdict-fixture-templates**: rec-bd904456-5b0e-428c-b743-afb539f03876; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; check _(id: [rec-1cc38ec9-87fc-4706-863a-1477ab306660](.artifacts/records/project__check-run/rec-1cc38ec9-87fc-4706-863a-1477ab306660.md))_

## verify-ci-verdict-fixture-workflow

### Acceptance
- **verify-ci-verdict-fixture-workflow**: check; evidence-layer; rg -n build_verdict_repo .github/workflows/affidavit-verdict.yml _(id: [rec-9b25f2d6-f94c-4037-b11d-f3c3e1b98572](.artifacts/records/project__acceptance/rec-9b25f2d6-f94c-4037-b11d-f3c3e1b98572.md))_

### Check
- **verify-ci-verdict-fixture-workflow**: rec-9b25f2d6-f94c-4037-b11d-f3c3e1b98572; 65c76f72f5c5b4c12db8ed4961d8d5fb50adbdc2; pass; check _(id: [rec-f5614ea0-f137-4ad3-9c8a-1a717d9a79f0](.artifacts/records/project__check-run/rec-f5614ea0-f137-4ad3-9c8a-1a717d9a79f0.md))_

## verify-claim-authoring

### Acceptance
- **verify-claim-authoring**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r1_claim_add_writes_manifest_entry_standalone -q _(id: [rec-3ba8b3a4-946b-45b9-ad43-80a95fab5a9a](.artifacts/records/project__acceptance/rec-3ba8b3a4-946b-45b9-ad43-80a95fab5a9a.md))_

### Check
- **verify-claim-authoring**: rec-3ba8b3a4-946b-45b9-ad43-80a95fab5a9a; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; check _(id: [rec-21d68f2f-43e6-4a5e-a30e-e3f014d2ecf6](.artifacts/records/project__check-run/rec-21d68f2f-43e6-4a5e-a30e-e3f014d2ecf6.md))_

## verify-claim-authoring-freeze

### Acceptance
- **verify-claim-authoring-freeze**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r2_freeze_records_exact_oracle_hashes tests/test_claim_authoring.py::test_r2_standalone_add_freeze_verdict_passes -q _(id: [rec-c04a807b-31ff-475f-9acf-33a49952d72f](.artifacts/records/project__acceptance/rec-c04a807b-31ff-475f-9acf-33a49952d72f.md))_

### Check
- **verify-claim-authoring-freeze**: rec-c04a807b-31ff-475f-9acf-33a49952d72f; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; check _(id: [rec-657415ed-2cf3-4c4f-bf06-647fea7fdbb6](.artifacts/records/project__check-run/rec-657415ed-2cf3-4c4f-bf06-647fea7fdbb6.md))_

## verify-claim-authoring-lint

### Acceptance
- **verify-claim-authoring-lint**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r3_lint_claims_reports_compound_claim -q _(id: [rec-9d812846-4080-4211-876b-31734708a995](.artifacts/records/project__acceptance/rec-9d812846-4080-4211-876b-31734708a995.md))_

### Check
- **verify-claim-authoring-lint**: rec-9d812846-4080-4211-876b-31734708a995; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; check _(id: [rec-f9d78f7e-4a6b-4719-b917-107a016b1454](.artifacts/records/project__check-run/rec-f9d78f7e-4a6b-4719-b917-107a016b1454.md))_

## verify-claim-authoring-reject

### Acceptance
- **verify-claim-authoring-reject**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r5_verdict_rejects_missing_human_signature tests/test_claim_authoring.py::test_r5_verdict_rejects_invalid_human_signature -q _(id: [rec-55b8c272-23dc-43b4-97ac-0ac7bb74dda7](.artifacts/records/project__acceptance/rec-55b8c272-23dc-43b4-97ac-0ac7bb74dda7.md))_

### Check
- **verify-claim-authoring-reject**: rec-55b8c272-23dc-43b4-97ac-0ac7bb74dda7; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; check _(id: [rec-a815429b-3b59-4b6d-9cc9-f2a1f61b79ed](.artifacts/records/project__check-run/rec-a815429b-3b59-4b6d-9cc9-f2a1f61b79ed.md))_

## verify-claim-authoring-signed

### Acceptance
- **verify-claim-authoring-signed**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r4_verdict_accepts_valid_human_signature -q _(id: [rec-95ddfb5c-0a5b-43f3-9b6d-34079130a087](.artifacts/records/project__acceptance/rec-95ddfb5c-0a5b-43f3-9b6d-34079130a087.md))_

### Check
- **verify-claim-authoring-signed**: rec-95ddfb5c-0a5b-43f3-9b6d-34079130a087; 7dcfa7106a7e680f22920adee66cbd0206d49976; pass; check _(id: [rec-a3ebf848-4a3e-4c63-853d-9e86033311fa](.artifacts/records/project__check-run/rec-a3ebf848-4a3e-4c63-853d-9e86033311fa.md))_

## verify-claims-manifest

### Acceptance
- **verify-claims-manifest**: aff verdict exits 0 only when manifest hashes match the tree at --at, the oracle tests fail at --base on an assertion, and they pass at --at; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or not_assertion" _(id: [rec-f25d51ef-6c72-4a13-b9d6-4e9ec7a177b3](.artifacts/records/project__acceptance/rec-f25d51ef-6c72-4a13-b9d6-4e9ec7a177b3.md))_

### Check
- **verify-claims-manifest**: rec-f25d51ef-6c72-4a13-b9d6-4e9ec7a177b3; 512796fda9f16f54a5848fdca999755a8e48eb27; fail; tdd _(id: [rec-6db90d14-4fe2-454b-9a65-286bfb6f2ff9](.artifacts/records/project__check-run/rec-6db90d14-4fe2-454b-9a65-286bfb6f2ff9.md))_
- **verify-claims-manifest**: rec-f25d51ef-6c72-4a13-b9d6-4e9ec7a177b3; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; pass; tdd _(id: [rec-72796c03-48e7-490c-998b-cb56960549cc](.artifacts/records/project__check-run/rec-72796c03-48e7-490c-998b-cb56960549cc.md))_
- **verify-claims-manifest**: rec-f25d51ef-6c72-4a13-b9d6-4e9ec7a177b3; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-ebe28027-b90a-41b5-a853-04c14198365c](.artifacts/records/project__check-run/rec-ebe28027-b90a-41b5-a853-04c14198365c.md))_

## verify-claims-manifest-forge

### Acceptance
- **verify-claims-manifest-forge**: A forged stored check-run does not change the verdict; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k forged_check_run _(id: [rec-1aaa8c5e-adec-4df2-bc30-d09600c12903](.artifacts/records/project__acceptance/rec-1aaa8c5e-adec-4df2-bc30-d09600c12903.md))_

### Check
- **verify-claims-manifest-forge**: rec-1aaa8c5e-adec-4df2-bc30-d09600c12903; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-72e7af45-11c8-4228-993f-14b32c3bc0c4](.artifacts/records/project__check-run/rec-72e7af45-11c8-4228-993f-14b32c3bc0c4.md))_
- **verify-claims-manifest-forge**: rec-1aaa8c5e-adec-4df2-bc30-d09600c12903; 512796fda9f16f54a5848fdca999755a8e48eb27; fail; tdd _(id: [rec-ade425ff-2696-4dc8-8808-c73db83a5329](.artifacts/records/project__check-run/rec-ade425ff-2696-4dc8-8808-c73db83a5329.md))_
- **verify-claims-manifest-forge**: rec-1aaa8c5e-adec-4df2-bc30-d09600c12903; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; pass; tdd _(id: [rec-ceeb6cf1-2767-4045-a223-d54917424c6d](.artifacts/records/project__check-run/rec-ceeb6cf1-2767-4045-a223-d54917424c6d.md))_

## verify-claims-manifest-suite

### Acceptance
- **verify-claims-manifest-suite**: CLI subprocess tests cover the pass, a hash mismatch, a missing or invalid amendment signature, an allowlist change, and a --cwd pointed at a phase worktree other than the store checkout; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or bad_signature or allowlist or cwd_phase" _(id: [rec-27b93db5-292e-4864-8bc9-ac743955d861](.artifacts/records/project__acceptance/rec-27b93db5-292e-4864-8bc9-ac743955d861.md))_

### Check
- **verify-claims-manifest-suite**: rec-27b93db5-292e-4864-8bc9-ac743955d861; 512796fda9f16f54a5848fdca999755a8e48eb27; fail; tdd _(id: [rec-a2082b3e-966f-4582-ad33-99064849cb1a](.artifacts/records/project__check-run/rec-a2082b3e-966f-4582-ad33-99064849cb1a.md))_
- **verify-claims-manifest-suite**: rec-27b93db5-292e-4864-8bc9-ac743955d861; f84f89b913b54f21f1e426c7201c49b2e62347ef; pass; tdd _(id: [rec-e0a361c5-0c08-41b2-8dc0-07c6e326b849](.artifacts/records/project__check-run/rec-e0a361c5-0c08-41b2-8dc0-07c6e326b849.md))_
- **verify-claims-manifest-suite**: rec-27b93db5-292e-4864-8bc9-ac743955d861; 18e88e48fdb1fefea4bd0ab01e8bf1454364d16a; pass; tdd _(id: [rec-eb6538b1-57ce-4eba-8971-d89d7e714ce2](.artifacts/records/project__check-run/rec-eb6538b1-57ce-4eba-8971-d89d7e714ce2.md))_

## verify-evidence-interface

### Acceptance
- **verify-evidence-interface**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_interface.py::test_r4_verdict_trail_and_subsequent_verdict_pass -q _(id: [rec-7a536e2e-56fe-418d-9f76-ee4819ffc972](.artifacts/records/project__acceptance/rec-7a536e2e-56fe-418d-9f76-ee4819ffc972.md))_

### Check
- **verify-evidence-interface**: rec-7a536e2e-56fe-418d-9f76-ee4819ffc972; dirty; fail; tdd _(id: [rec-910efe84-10bd-45fe-a0ef-fbac6ceed70c](.artifacts/records/project__check-run/rec-910efe84-10bd-45fe-a0ef-fbac6ceed70c.md))_
- **verify-evidence-interface**: rec-7a536e2e-56fe-418d-9f76-ee4819ffc972; a655bf41071f6783be3049a8107ac8e28c54ee55; pass; tdd _(id: [rec-9c77593c-5482-4b44-9386-f49e215b3c67](.artifacts/records/project__check-run/rec-9c77593c-5482-4b44-9386-f49e215b3c67.md))_

## verify-evidence-interface-contract

### Acceptance
- **verify-evidence-interface-contract**: check; evidence-layer; python3 -m pytest tests/test_evidence_interface.py::test_r1_contract_defines_evidence_observation -q _(id: [rec-f4bd77f2-9d08-4e1a-9856-8ed3f967d3b7](.artifacts/records/project__acceptance/rec-f4bd77f2-9d08-4e1a-9856-8ed3f967d3b7.md))_

### Check
- **verify-evidence-interface-contract**: rec-f4bd77f2-9d08-4e1a-9856-8ed3f967d3b7; a655bf41071f6783be3049a8107ac8e28c54ee55; pass; check _(id: [rec-f06afe0b-49a0-40ea-9794-93c5d1ef770a](.artifacts/records/project__check-run/rec-f06afe0b-49a0-40ea-9794-93c5d1ef770a.md))_

## verify-evidence-interface-record

### Acceptance
- **verify-evidence-interface-record**: check; evidence-layer; python3 -m pytest tests/test_evidence_interface.py::test_r2_verdict_records_one_evidence_observation tests/test_evidence_interface.py::test_r2_verdict_without_store_matches_prephase_semantics -q _(id: [rec-36098ded-eb47-4b64-b5d5-f64dba0295cd](.artifacts/records/project__acceptance/rec-36098ded-eb47-4b64-b5d5-f64dba0295cd.md))_

### Check
- **verify-evidence-interface-record**: rec-36098ded-eb47-4b64-b5d5-f64dba0295cd; a655bf41071f6783be3049a8107ac8e28c54ee55; pass; check _(id: [rec-70a061d3-1241-4d57-b2d1-c317bcc755da](.artifacts/records/project__check-run/rec-70a061d3-1241-4d57-b2d1-c317bcc755da.md))_

## verify-evidence-interface-trail

### Acceptance
- **verify-evidence-interface-trail**: check; evidence-layer; python3 -m pytest tests/test_evidence_interface.py::test_r3_aff_trail_lists_observations_as_json -q _(id: [rec-cb193838-6640-40f2-a632-be392af0cd68](.artifacts/records/project__acceptance/rec-cb193838-6640-40f2-a632-be392af0cd68.md))_

### Check
- **verify-evidence-interface-trail**: rec-cb193838-6640-40f2-a632-be392af0cd68; a655bf41071f6783be3049a8107ac8e28c54ee55; pass; check _(id: [rec-e0aa8f7a-87fc-49e8-a093-5f2e5a77b3a8](.artifacts/records/project__check-run/rec-e0aa8f7a-87fc-49e8-a093-5f2e5a77b3a8.md))_

## verify-evidence-kind

### Acceptance
- **verify-evidence-kind**: check; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r1_manifest_claim_may_declare_evidence_kind -q _(id: [rec-31329697-17c1-4cef-927e-b2bba4675d35](.artifacts/records/project__acceptance/rec-31329697-17c1-4cef-927e-b2bba4675d35.md))_

### Check
- **verify-evidence-kind**: rec-31329697-17c1-4cef-927e-b2bba4675d35; 2c6d4575f86acb22f0e6af5f4ce60051888bcb2d; pass; check _(id: [rec-e800ecec-b5fc-4361-8662-863f14e3d4c0](.artifacts/records/project__check-run/rec-e800ecec-b5fc-4361-8662-863f14e3d4c0.md))_

## verify-evidence-kind-r2

### Acceptance
- **verify-evidence-kind-r2**: check; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r2_interaction_claim_fails_under_default_unit_runner -q _(id: [rec-7869f8d0-e7d5-4a7c-9c8c-aa0507b6cd7a](.artifacts/records/project__acceptance/rec-7869f8d0-e7d5-4a7c-9c8c-aa0507b6cd7a.md))_

### Check
- **verify-evidence-kind-r2**: rec-7869f8d0-e7d5-4a7c-9c8c-aa0507b6cd7a; 2c6d4575f86acb22f0e6af5f4ce60051888bcb2d; pass; check _(id: [rec-95e409e2-ca57-49c7-86b6-b3f3970bd4d6](.artifacts/records/project__check-run/rec-95e409e2-ca57-49c7-86b6-b3f3970bd4d6.md))_

## verify-evidence-kind-r3

### Acceptance
- **verify-evidence-kind-r3**: check; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r3_interaction_claim_passes_under_interaction_runner -q _(id: [rec-35c32ec7-df9d-44ae-9d4b-1da771b510ef](.artifacts/records/project__acceptance/rec-35c32ec7-df9d-44ae-9d4b-1da771b510ef.md))_

### Check
- **verify-evidence-kind-r3**: rec-35c32ec7-df9d-44ae-9d4b-1da771b510ef; 2c6d4575f86acb22f0e6af5f4ce60051888bcb2d; pass; check _(id: [rec-88df46a1-74ad-40f3-bd7e-048726a20e4c](.artifacts/records/project__check-run/rec-88df46a1-74ad-40f3-bd7e-048726a20e4c.md))_

## verify-frozen-environment

### Acceptance
- **verify-frozen-environment**: check; evidence-layer; python3 -m pytest tests/test_verdict.py::test_verdict_refuses_support_file_drift_without_amendment tests/test_verdict.py::test_verdict_refuses_claim_support_file_drift_without_amendment -q _(id: [rec-f83f8a6d-4589-43b7-9853-95d904d92b14](.artifacts/records/project__acceptance/rec-f83f8a6d-4589-43b7-9853-95d904d92b14.md))_

### Check
- **verify-frozen-environment**: rec-f83f8a6d-4589-43b7-9853-95d904d92b14; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; check _(id: [rec-f9a1c5b1-ab24-4306-935e-bce5c8353c7b](.artifacts/records/project__check-run/rec-f9a1c5b1-ab24-4306-935e-bce5c8353c7b.md))_

## verify-frozen-environment-lint

### Acceptance
- **verify-frozen-environment-lint**: check; evidence-layer; python3 -m pytest tests/test_lint.py::test_lint_reports_no_assert_witness -q _(id: [rec-55edf2d5-5ed9-49c2-aaef-10cdb45b875c](.artifacts/records/project__acceptance/rec-55edf2d5-5ed9-49c2-aaef-10cdb45b875c.md))_

### Check
- **verify-frozen-environment-lint**: rec-55edf2d5-5ed9-49c2-aaef-10cdb45b875c; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; check _(id: [rec-ffa6b5a3-b5cc-4781-838a-aa602636bf60](.artifacts/records/project__check-run/rec-ffa6b5a3-b5cc-4781-838a-aa602636bf60.md))_

## verify-frozen-environment-runner

### Acceptance
- **verify-frozen-environment-runner**: check; evidence-layer; python3 -m pytest tests/test_verdict.py::test_verdict_refuses_runner_digest_drift_without_amendment -q _(id: [rec-b9efb8a3-f48d-43a4-9733-78462fbe3a23](.artifacts/records/project__acceptance/rec-b9efb8a3-f48d-43a4-9733-78462fbe3a23.md))_

### Check
- **verify-frozen-environment-runner**: rec-b9efb8a3-f48d-43a4-9733-78462fbe3a23; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; check _(id: [rec-e002cbb6-edf5-47da-b80b-c3994bb0d231](.artifacts/records/project__check-run/rec-e002cbb6-edf5-47da-b80b-c3994bb0d231.md))_

## verify-frozen-environment-skips

### Acceptance
- **verify-frozen-environment-skips**: check; evidence-layer; python3 -m pytest tests/test_lint.py::test_lint_reports_new_skip_between_base_and_head -q _(id: [rec-64566959-1ab1-4de4-bca9-feb47da70a23](.artifacts/records/project__acceptance/rec-64566959-1ab1-4de4-bca9-feb47da70a23.md))_

### Check
- **verify-frozen-environment-skips**: rec-64566959-1ab1-4de4-bca9-feb47da70a23; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; check _(id: [rec-367f91dc-c4ed-477b-b288-e5f0df6587f2](.artifacts/records/project__check-run/rec-367f91dc-c4ed-477b-b288-e5f0df6587f2.md))_

## verify-oracle-provenance

### Acceptance
- **verify-oracle-provenance**: check; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r1_oracle_after_implementation_fails -q _(id: [rec-951a64c2-99ad-44da-95d4-4dc221012064](.artifacts/records/project__acceptance/rec-951a64c2-99ad-44da-95d4-4dc221012064.md))_

### Check
- **verify-oracle-provenance**: rec-951a64c2-99ad-44da-95d4-4dc221012064; 62db733ebc97851acd532d5103e2ae04130945cb; pass; check _(id: [rec-32ddd5b1-837b-4926-93b0-ee507ebdd8f3](.artifacts/records/project__check-run/rec-32ddd5b1-837b-4926-93b0-ee507ebdd8f3.md))_

## verify-oracle-provenance-pass

### Acceptance
- **verify-oracle-provenance-pass**: check; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r4_ordered_oracle_only_distinct_signers_passes -q _(id: [rec-64af228c-7e2c-443d-a84b-b391e3351926](.artifacts/records/project__acceptance/rec-64af228c-7e2c-443d-a84b-b391e3351926.md))_

### Check
- **verify-oracle-provenance-pass**: rec-64af228c-7e2c-443d-a84b-b391e3351926; 62db733ebc97851acd532d5103e2ae04130945cb; pass; check _(id: [rec-df3ee7c8-f75b-44d2-8629-2cb492fa6dde](.artifacts/records/project__check-run/rec-df3ee7c8-f75b-44d2-8629-2cb492fa6dde.md))_

## verify-oracle-provenance-paths

### Acceptance
- **verify-oracle-provenance-paths**: check; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r2_oracle_commit_touches_non_oracle_paths_fails -q _(id: [rec-068c0dd0-35ca-4d48-92d7-9df3837832ff](.artifacts/records/project__acceptance/rec-068c0dd0-35ca-4d48-92d7-9df3837832ff.md))_

### Check
- **verify-oracle-provenance-paths**: rec-068c0dd0-35ca-4d48-92d7-9df3837832ff; 62db733ebc97851acd532d5103e2ae04130945cb; pass; check _(id: [rec-6f68b29e-890d-4278-8275-fb80d029c136](.artifacts/records/project__check-run/rec-6f68b29e-890d-4278-8275-fb80d029c136.md))_

## verify-oracle-provenance-signer

### Acceptance
- **verify-oracle-provenance-signer**: check; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r3_shared_signer_fails -q _(id: [rec-fbe22f64-aab1-4d71-a9e9-424741e6234b](.artifacts/records/project__acceptance/rec-fbe22f64-aab1-4d71-a9e9-424741e6234b.md))_

### Check
- **verify-oracle-provenance-signer**: rec-fbe22f64-aab1-4d71-a9e9-424741e6234b; 62db733ebc97851acd532d5103e2ae04130945cb; pass; check _(id: [rec-e5bb1e4b-f44e-45ca-a3bb-fa478ad488ca](.artifacts/records/project__check-run/rec-e5bb1e4b-f44e-45ca-a3bb-fa478ad488ca.md))_

## verify-orchestration-split

### Acceptance
- **verify-orchestration-split**: bin/aff check, close-batch, and verdict --help exit 0, and the remaining pytest files pass with skills/, dashboard/, scripts/, and agents/ absent; check; evidence-layer; test ! -d skills && test ! -d dashboard && test ! -d scripts && test ! -d agents && bin/aff check --help && bin/aff close-batch --help && bin/aff verdict --help && python3 -m pytest tests/test_evidence_layout.py tests/test_affidavit_check.py tests/test_close_batch.py tests/test_verdict.py tests/test_manifest.py tests/test_amendment.py tests/test_oracle_red.py tests/test_affidavit_aa.py -q _(id: [rec-c590714e-be3c-4c72-9fd2-cd7d966f4ef0](.artifacts/records/project__acceptance/rec-c590714e-be3c-4c72-9fd2-cd7d966f4ef0.md))_

### Check
- **verify-orchestration-split**: rec-c590714e-be3c-4c72-9fd2-cd7d966f4ef0; f67741737facb4a494ede2a0d4132b1a451f3c5c; pass; check _(id: [rec-fddae680-a700-4355-89b2-f3e269c704e8](.artifacts/records/project__check-run/rec-fddae680-a700-4355-89b2-f3e269c704e8.md))_

## verify-orchestration-split-boundary

### Acceptance
- **verify-orchestration-split-boundary**: The orchestra boundary test fails on a fixture skill that creates a tdd or check check-run or a project:oracle-amendment, and passes on the migrated skills; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_skill_evidence_boundary.py -q -k 'not verdict' _(id: [rec-29938747-c59e-4421-838e-0a6c7573a4cb](.artifacts/records/project__acceptance/rec-29938747-c59e-4421-838e-0a6c7573a4cb.md))_

### Check
- **verify-orchestration-split-boundary**: rec-29938747-c59e-4421-838e-0a6c7573a4cb; 2df7598d15159946435617cd150ab4d4dd9329c8; fail; tdd _(id: [rec-48c1ac8c-5680-44bd-afe4-02fa5328deff](.artifacts/records/project__check-run/rec-48c1ac8c-5680-44bd-afe4-02fa5328deff.md))_
- **verify-orchestration-split-boundary**: rec-29938747-c59e-4421-838e-0a6c7573a4cb; 40386351dd0a5d62619ef4be64070aefb986ff30; pass; tdd _(id: [rec-ac98083f-b6b6-4e1b-ad4b-102910d293cd](.artifacts/records/project__check-run/rec-ac98083f-b6b6-4e1b-ad4b-102910d293cd.md))_
- **verify-orchestration-split-boundary**: rec-29938747-c59e-4421-838e-0a6c7573a4cb; 2df7598d15159946435617cd150ab4d4dd9329c8; fail; tdd _(id: [rec-d358fb0e-50e9-441e-9c7b-40fc2f3f01fa](.artifacts/records/project__check-run/rec-d358fb0e-50e9-441e-9c7b-40fc2f3f01fa.md))_

## verify-orchestration-split-commits

### Acceptance
- **verify-orchestration-split-commits**: execute-phase shows a per-task commit, a phase-branch commit, and a store commit whose subject matches type(scope): summary and whose body is one or two sentences; a task commit names the task slug; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_task_commit.py -q _(id: [rec-552c3f36-62a8-4868-b00c-e380bb8449bc](.artifacts/records/project__acceptance/rec-552c3f36-62a8-4868-b00c-e380bb8449bc.md))_

### Check
- **verify-orchestration-split-commits**: rec-552c3f36-62a8-4868-b00c-e380bb8449bc; db859dbb0aa06cdaedbd5cffe24e04ca611eb463; fail; tdd _(id: [rec-36997604-4489-425b-9935-c78b391a5df6](.artifacts/records/project__check-run/rec-36997604-4489-425b-9935-c78b391a5df6.md))_
- **verify-orchestration-split-commits**: rec-552c3f36-62a8-4868-b00c-e380bb8449bc; 40386351dd0a5d62619ef4be64070aefb986ff30; pass; tdd _(id: [rec-8293ea2b-b3fa-43c8-9832-15280cc4ee29](.artifacts/records/project__check-run/rec-8293ea2b-b3fa-43c8-9832-15280cc4ee29.md))_
- **verify-orchestration-split-commits**: rec-552c3f36-62a8-4868-b00c-e380bb8449bc; db859dbb0aa06cdaedbd5cffe24e04ca611eb463; fail; tdd _(id: [rec-c186d002-e61d-4da0-8074-af241b41f174](.artifacts/records/project__check-run/rec-c186d002-e61d-4da0-8074-af241b41f174.md))_

## verify-orchestration-split-layout

### Acceptance
- **verify-orchestration-split-layout**: ~/orchestra contains the seven skill directories and dashboard/, and orchestra.reviewer and orchestra.suite import with no tier2 module; check; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_orchestra_package.py -q && test -d skills/engage && test -d skills/discuss && test -d skills/plan-phase && test -d skills/execute-phase && test -d skills/verify-work && test -d skills/init && test -d skills/analyze-sessions && test -d dashboard _(id: [rec-5330ace0-1772-4d24-9d1a-f4e7b74a8fe0](.artifacts/records/project__acceptance/rec-5330ace0-1772-4d24-9d1a-f4e7b74a8fe0.md))_

### Check
- **verify-orchestration-split-layout**: rec-5330ace0-1772-4d24-9d1a-f4e7b74a8fe0; 40386351dd0a5d62619ef4be64070aefb986ff30; pass; check _(id: [rec-9f69431d-ea7d-465f-a656-1a000291adf5](.artifacts/records/project__check-run/rec-9f69431d-ea7d-465f-a656-1a000291adf5.md))_
- **verify-orchestration-split-layout**: rec-5330ace0-1772-4d24-9d1a-f4e7b74a8fe0; 40386351dd0a5d62619ef4be64070aefb986ff30; fail; check _(id: [rec-be1ef493-a60e-4e78-b6a0-4de1a3427c6b](.artifacts/records/project__check-run/rec-be1ef493-a60e-4e78-b6a0-4de1a3427c6b.md))_

## verify-orchestration-split-project

### Acceptance
- **verify-orchestration-split-project**: A fixture store whose project is affidavit is rewritten to orchestra, and a fixture whose project is any other name is left unchanged; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_ensure_store_project.py -q _(id: [rec-1c20c26a-415f-4af9-8b85-1041500bed92](.artifacts/records/project__acceptance/rec-1c20c26a-415f-4af9-8b85-1041500bed92.md))_

### Check
- **verify-orchestration-split-project**: rec-1c20c26a-415f-4af9-8b85-1041500bed92; b4f59462fd054c0f266e3e1b7872a46472587286; fail; tdd _(id: [rec-2e7bcaa8-8767-4815-9eee-68cdc28291c4](.artifacts/records/project__check-run/rec-2e7bcaa8-8767-4815-9eee-68cdc28291c4.md))_
- **verify-orchestration-split-project**: rec-1c20c26a-415f-4af9-8b85-1041500bed92; 40386351dd0a5d62619ef4be64070aefb986ff30; pass; tdd _(id: [rec-6525b694-bb36-4945-af87-e394aba7e53b](.artifacts/records/project__check-run/rec-6525b694-bb36-4945-af87-e394aba7e53b.md))_
- **verify-orchestration-split-project**: rec-1c20c26a-415f-4af9-8b85-1041500bed92; b4f59462fd054c0f266e3e1b7872a46472587286; fail; tdd _(id: [rec-6ce105c0-c0a7-43e0-b2df-cae14cf90a0e](.artifacts/records/project__check-run/rec-6ce105c0-c0a7-43e0-b2df-cae14cf90a0e.md))_

## verify-orchestration-split-stores

### Acceptance
- **verify-orchestration-split-stores**: Both stores validate; the active goal here is evidence-layer; the active goals in orchestra are dashboard, workflow-loop, packaging, session-analysis, and test-suite-speed; check; evidence-layer; adaptive-artifacts validate && adaptive-artifacts --store "$HOME/orchestra/.artifacts" validate && python3 -c 'import json,os,subprocess
def goals(store):
 out=subprocess.check_output(["adaptive-artifacts","--store",store,"list","--type","project:active-goal","--state","active"],text=True)
 return sorted(r["subject"] for r in json.loads(out)["records"] if r.get("payload",{}).get("status")!="closed")
assert goals(".artifacts")==["evidence-layer"]
assert goals(os.path.expanduser("~/orchestra/.artifacts"))==["dashboard","packaging","session-analysis","test-suite-speed","workflow-loop"]' _(id: [rec-e88d2262-2f38-4ef4-a3c1-59032762980f](.artifacts/records/project__acceptance/rec-e88d2262-2f38-4ef4-a3c1-59032762980f.md))_

### Check
- **verify-orchestration-split-stores**: rec-e88d2262-2f38-4ef4-a3c1-59032762980f; dirty; fail; check _(id: [rec-1dd3c10a-215d-4516-91ec-61923b6722d0](.artifacts/records/project__check-run/rec-1dd3c10a-215d-4516-91ec-61923b6722d0.md))_
- **verify-orchestration-split-stores**: rec-e88d2262-2f38-4ef4-a3c1-59032762980f; dirty; pass; check _(id: [rec-6e23a448-aef0-4c26-92af-0012c8eca066](.artifacts/records/project__check-run/rec-6e23a448-aef0-4c26-92af-0012c8eca066.md))_

## verify-orchestration-split-verdict

### Acceptance
- **verify-orchestration-split-verdict**: execute-phase and verify-work run aff verdict for a claim in the manifest and treat a non-zero exit as not done; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_skill_evidence_boundary.py -q -k verdict _(id: [rec-167feb75-1bd7-4db4-ad7c-05b50da84dae](.artifacts/records/project__acceptance/rec-167feb75-1bd7-4db4-ad7c-05b50da84dae.md))_

### Check
- **verify-orchestration-split-verdict**: rec-167feb75-1bd7-4db4-ad7c-05b50da84dae; 2df7598d15159946435617cd150ab4d4dd9329c8; fail; tdd _(id: [rec-13197abe-10a5-44e1-9437-a436982f2cbc](.artifacts/records/project__check-run/rec-13197abe-10a5-44e1-9437-a436982f2cbc.md))_
- **verify-orchestration-split-verdict**: rec-167feb75-1bd7-4db4-ad7c-05b50da84dae; 40386351dd0a5d62619ef4be64070aefb986ff30; pass; tdd _(id: [rec-72851342-8ebf-4547-93b6-557ff9464558](.artifacts/records/project__check-run/rec-72851342-8ebf-4547-93b6-557ff9464558.md))_
- **verify-orchestration-split-verdict**: rec-167feb75-1bd7-4db4-ad7c-05b50da84dae; 2df7598d15159946435617cd150ab4d4dd9329c8; fail; tdd _(id: [rec-97a0c1d1-39d9-4829-8e8f-2823b8ca594d](.artifacts/records/project__check-run/rec-97a0c1d1-39d9-4829-8e8f-2823b8ca594d.md))_

## verify-phase-end-evidence

### Acceptance
- **verify-phase-end-evidence**: check; evidence-layer; python3 -m pytest tests/test_audit.py::test_r1_audit_labels_each_source_block tests/test_audit.py::test_r1_audit_reads_claim_tests_from_manifest -q _(id: [rec-6309e3d9-876f-42ce-877b-70b6e54e95d0](.artifacts/records/project__acceptance/rec-6309e3d9-876f-42ce-877b-70b6e54e95d0.md))_

### Check
- **verify-phase-end-evidence**: rec-6309e3d9-876f-42ce-877b-70b6e54e95d0; 5bbd8cb571d2ad193b61f35159e3648c5adfd0f0; pass; check _(id: [rec-c23ad25f-719f-4e66-b730-dd7115c56e8a](.artifacts/records/project__check-run/rec-c23ad25f-719f-4e66-b730-dd7115c56e8a.md))_

## verify-phase-end-evidence-mutants

### Acceptance
- **verify-phase-end-evidence-mutants**: check; evidence-layer; python3 -m pytest tests/test_audit.py::test_r4_audit_plants_mutants_only_in_noticed_blocks -q _(id: [rec-e5c480a3-7f7b-4ab0-983d-4f1330b2d9c3](.artifacts/records/project__acceptance/rec-e5c480a3-7f7b-4ab0-983d-4f1330b2d9c3.md))_

### Check
- **verify-phase-end-evidence-mutants**: rec-e5c480a3-7f7b-4ab0-983d-4f1330b2d9c3; 5bbd8cb571d2ad193b61f35159e3648c5adfd0f0; pass; check _(id: [rec-76ff878e-85c6-4035-b11e-481583c50af5](.artifacts/records/project__check-run/rec-76ff878e-85c6-4035-b11e-481583c50af5.md))_

## verify-phase-end-evidence-range

### Acceptance
- **verify-phase-end-evidence-range**: check; evidence-layer; python3 -m pytest tests/test_audit.py::test_r3_audit_reports_unnoticed_build_batch_cwd_block -q _(id: [rec-80780e36-123f-4019-8dcc-1f4f096858a6](.artifacts/records/project__acceptance/rec-80780e36-123f-4019-8dcc-1f4f096858a6.md))_

### Check
- **verify-phase-end-evidence-range**: rec-80780e36-123f-4019-8dcc-1f4f096858a6; 5bbd8cb571d2ad193b61f35159e3648c5adfd0f0; pass; check _(id: [rec-2600bb37-d06e-4f6d-987c-e50de4b6ec96](.artifacts/records/project__check-run/rec-2600bb37-d06e-4f6d-987c-e50de4b6ec96.md))_

## verify-phase-end-evidence-tests

### Acceptance
- **verify-phase-end-evidence-tests**: check; evidence-layer; python3 -m pytest tests/test_audit.py::test_r2_audit_never_reports_test_file_blocks -q _(id: [rec-844c2281-213a-49a8-bb8e-f67e05319f6d](.artifacts/records/project__acceptance/rec-844c2281-213a-49a8-bb8e-f67e05319f6d.md))_

### Check
- **verify-phase-end-evidence-tests**: rec-844c2281-213a-49a8-bb8e-f67e05319f6d; 5bbd8cb571d2ad193b61f35159e3648c5adfd0f0; pass; check _(id: [rec-e7dd00b5-536c-467a-8bb9-8a96391c25a4](.artifacts/records/project__check-run/rec-e7dd00b5-536c-467a-8bb9-8a96391c25a4.md))_

## verify-runner-adapter

### Acceptance
- **verify-runner-adapter**: aff verdict judges a claim through run_tests with no pytest stdout regex, and existing pass, hash-mismatch, and collection-error cases keep their results; check; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or not_assertion or ignores_pytest_stdout" _(id: [rec-1806d506-b116-4a6d-8c3f-005d61f39cc2](.artifacts/records/project__acceptance/rec-1806d506-b116-4a6d-8c3f-005d61f39cc2.md))_

### Check
- **verify-runner-adapter**: rec-1806d506-b116-4a6d-8c3f-005d61f39cc2; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; check _(id: [rec-779f7de7-4ea6-4e63-99d0-3064cc3ed3da](.artifacts/records/project__check-run/rec-779f7de7-4ea6-4e63-99d0-3064cc3ed3da.md))_

## verify-runner-adapter-fixture

### Acceptance
- **verify-runner-adapter-fixture**: A fixture command that emits JUnit XML is judged through bin/aff verdict with no change under affidavit/; check; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k fixture_junit _(id: [rec-db6fa367-1432-40ad-8bc8-9f88d61f6eed](.artifacts/records/project__acceptance/rec-db6fa367-1432-40ad-8bc8-9f88d61f6eed.md))_

### Check
- **verify-runner-adapter-fixture**: rec-db6fa367-1432-40ad-8bc8-9f88d61f6eed; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; check _(id: [rec-4793736b-e0c3-41b0-94a0-8dbf323013e4](.artifacts/records/project__check-run/rec-4793736b-e0c3-41b0-94a0-8dbf323013e4.md))_

## verify-runner-adapter-template

### Acceptance
- **verify-runner-adapter-template**: An absent runner uses the shipped pytest template, and a runner that is not an argv list with {tests} and {report} fails manifest load; check; evidence-layer; python3 -m pytest tests/test_manifest.py -q -k "runner_absent or runner_invalid" _(id: [rec-84963c29-53ed-4d7d-a04b-d2d0d5b0c25a](.artifacts/records/project__acceptance/rec-84963c29-53ed-4d7d-a04b-d2d0d5b0c25a.md))_

### Check
- **verify-runner-adapter-template**: rec-84963c29-53ed-4d7d-a04b-d2d0d5b0c25a; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; check _(id: [rec-019b15ab-932f-4af9-abec-e84554a2580d](.artifacts/records/project__check-run/rec-019b15ab-932f-4af9-abec-e84554a2580d.md))_

## verify-runner-adapter-unstable

### Acceptance
- **verify-runner-adapter-unstable**: A witness that is assertion_failed on the first base run and passed on the confirmation run yields unstable and a non-zero exit; check; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k unstable_when_confirmation _(id: [rec-81acd29f-17af-42a1-b0be-374190e321dd](.artifacts/records/project__acceptance/rec-81acd29f-17af-42a1-b0be-374190e321dd.md))_

### Check
- **verify-runner-adapter-unstable**: rec-81acd29f-17af-42a1-b0be-374190e321dd; 37d326c5eb4085075b3b363aba49f17cc5e7d534; pass; check _(id: [rec-d612b645-12a5-4429-a014-9003f798e2b2](.artifacts/records/project__check-run/rec-d612b645-12a5-4429-a014-9003f798e2b2.md))_

## verify-signed-verdict

### Acceptance
- **verify-signed-verdict**: check; evidence-layer; python3 -m pytest tests/test_attestation.py::test_emit_signed_attestation_includes_commit_manifest_runner_and_claims -q _(id: [rec-02f5f1e1-da0e-4c60-b62f-9cea163b3ef3](.artifacts/records/project__acceptance/rec-02f5f1e1-da0e-4c60-b62f-9cea163b3ef3.md))_

### Check
- **verify-signed-verdict**: rec-02f5f1e1-da0e-4c60-b62f-9cea163b3ef3; 678568be6e44d42569de8196f94b55bca3b5f912; pass; check _(id: [rec-5aa2f0cf-3e18-4145-85b9-b754dc42730e](.artifacts/records/project__check-run/rec-5aa2f0cf-3e18-4145-85b9-b754dc42730e.md))_

## verify-signed-verdict-bind

### Acceptance
- **verify-signed-verdict-bind**: check; evidence-layer; python3 -m pytest tests/test_attestation.py::test_verify_rejects_wrong_commit tests/test_attestation.py::test_verify_rejects_bind_mismatch_on_manifest_hash -q _(id: [rec-3fa6eb8b-9b79-4ba8-a95f-c731281ab225](.artifacts/records/project__acceptance/rec-3fa6eb8b-9b79-4ba8-a95f-c731281ab225.md))_

### Check
- **verify-signed-verdict-bind**: rec-3fa6eb8b-9b79-4ba8-a95f-c731281ab225; 678568be6e44d42569de8196f94b55bca3b5f912; pass; check _(id: [rec-e09c6e68-57ef-4acb-a892-6ad64c813562](.artifacts/records/project__check-run/rec-e09c6e68-57ef-4acb-a892-6ad64c813562.md))_

## verify-signed-verdict-ci

### Acceptance
- **verify-signed-verdict-ci**: check; evidence-layer; python3 -m pytest tests/test_attestation.py::test_ci_workflow_runs_verdict_and_attest -q _(id: [rec-8d754ac2-188a-4162-8aac-2850522ce765](.artifacts/records/project__acceptance/rec-8d754ac2-188a-4162-8aac-2850522ce765.md))_

### Check
- **verify-signed-verdict-ci**: rec-8d754ac2-188a-4162-8aac-2850522ce765; 678568be6e44d42569de8196f94b55bca3b5f912; pass; check _(id: [rec-629e5c6f-9a9a-4a59-8bd5-924d206ccd68](.artifacts/records/project__check-run/rec-629e5c6f-9a9a-4a59-8bd5-924d206ccd68.md))_

## verify-signed-verdict-sig

### Acceptance
- **verify-signed-verdict-sig**: check; evidence-layer; python3 -m pytest tests/test_attestation.py::test_verify_rejects_bad_signature tests/test_attestation.py::test_verify_rejects_tampered_payload -q _(id: [rec-02cd8744-be8c-402c-9387-69c2c7e632d2](.artifacts/records/project__acceptance/rec-02cd8744-be8c-402c-9387-69c2c7e632d2.md))_

### Check
- **verify-signed-verdict-sig**: rec-02cd8744-be8c-402c-9387-69c2c7e632d2; 678568be6e44d42569de8196f94b55bca3b5f912; pass; check _(id: [rec-4e37b84f-5b7a-4ba0-b692-b99244fda2cf](.artifacts/records/project__check-run/rec-4e37b84f-5b7a-4ba0-b692-b99244fda2cf.md))_

## verify-standalone-aff

### Acceptance
- **verify-standalone-aff**: A checkout of this repo, with no orchestra tree, no adaptive-artifacts on PATH, and no se-workflow store binding, still produces a verdict from the committed manifest; check; evidence-layer; python3 -m pytest tests/test_standalone_cli.py -q -k verdict_without_runtime _(id: [rec-ef30c56e-14a1-4897-9621-e3110af528c3](.artifacts/records/project__acceptance/rec-ef30c56e-14a1-4897-9621-e3110af528c3.md))_

### Check
- **verify-standalone-aff**: rec-ef30c56e-14a1-4897-9621-e3110af528c3; 95816892f1208fd6b13723e6f89a959d6736da44; pass; check _(id: [rec-2fd486e2-31d9-48fc-943a-340745664831](.artifacts/records/project__check-run/rec-2fd486e2-31d9-48fc-943a-340745664831.md))_
- **verify-standalone-aff**: rec-ef30c56e-14a1-4897-9621-e3110af528c3; 2c7dd552e6012ffb8626c635806214073168ba60; pass; check _(id: [rec-954cb5fa-9acd-4f28-ad54-2fd3cc067989](.artifacts/records/project__check-run/rec-954cb5fa-9acd-4f28-ad54-2fd3cc067989.md))_
- **verify-standalone-aff**: rec-ef30c56e-14a1-4897-9621-e3110af528c3; 2c7dd552e6012ffb8626c635806214073168ba60; pass; check _(id: [rec-c960a982-0a9b-472c-b9b3-b5ae8aff8b3a](.artifacts/records/project__check-run/rec-c960a982-0a9b-472c-b9b3-b5ae8aff8b3a.md))_

## verify-standalone-aff-boundary

### Acceptance
- **verify-standalone-aff-boundary**: A test fails while any module under affidavit/ contains project:, SE_WORKFLOW_STORE, store-binding.json, or adaptive-artifacts; check; evidence-layer; python3 -m pytest tests/test_evidence_layout.py -q -k no_store_tokens _(id: [rec-2b4379ce-c5cf-4276-8a31-359b82448f7e](.artifacts/records/project__acceptance/rec-2b4379ce-c5cf-4276-8a31-359b82448f7e.md))_

### Check
- **verify-standalone-aff-boundary**: rec-2b4379ce-c5cf-4276-8a31-359b82448f7e; 95816892f1208fd6b13723e6f89a959d6736da44; pass; check _(id: [rec-9699e44a-7a03-43e8-98e3-f01cfa995809](.artifacts/records/project__check-run/rec-9699e44a-7a03-43e8-98e3-f01cfa995809.md))_
- **verify-standalone-aff-boundary**: rec-2b4379ce-c5cf-4276-8a31-359b82448f7e; 2c7dd552e6012ffb8626c635806214073168ba60; pass; check _(id: [rec-d50f5df6-b725-407e-aa8f-efcaf33735e3](.artifacts/records/project__check-run/rec-d50f5df6-b725-407e-aa8f-efcaf33735e3.md))_
- **verify-standalone-aff-boundary**: rec-2b4379ce-c5cf-4276-8a31-359b82448f7e; 2c7dd552e6012ffb8626c635806214073168ba60; pass; check _(id: [rec-fb95847f-a88c-40c2-a8ce-4fd7c531a464](.artifacts/records/project__check-run/rec-fb95847f-a88c-40c2-a8ce-4fd7c531a464.md))_

## verify-standalone-aff-cli

### Acceptance
- **verify-standalone-aff-cli**: orchestra check and orchestra close-batch run from ~/orchestra, and the moved check, close-batch, and store-client tests pass there; check; evidence-layer; cd "$HOME/orchestra" && bin/orchestra check --help && bin/orchestra close-batch --help && python3 -m pytest tests/test_affidavit_check.py tests/test_close_batch.py tests/test_affidavit_aa.py tests/test_aa_resolve.py -q _(id: [rec-8f3850bd-9558-48f9-9bfe-a1245f4a1a1d](.artifacts/records/project__acceptance/rec-8f3850bd-9558-48f9-9bfe-a1245f4a1a1d.md))_

### Check
- **verify-standalone-aff-cli**: rec-8f3850bd-9558-48f9-9bfe-a1245f4a1a1d; 50b2cd0b0360e6cbca7bdbfe3cda1dfaab46648c; pass; check _(id: [rec-6803d947-f2f6-4e67-aa24-0f96109683df](.artifacts/records/project__check-run/rec-6803d947-f2f6-4e67-aa24-0f96109683df.md))_
- **verify-standalone-aff-cli**: rec-8f3850bd-9558-48f9-9bfe-a1245f4a1a1d; cac5247ddb6774f9a490bf7f3c5593a36a790b09; fail; check _(id: [rec-e20d9589-4948-450d-a8b0-f0cbfc457a98](.artifacts/records/project__check-run/rec-e20d9589-4948-450d-a8b0-f0cbfc457a98.md))_
- **verify-standalone-aff-cli**: rec-8f3850bd-9558-48f9-9bfe-a1245f4a1a1d; 2f2054aeccef9db20ac96d84d3c7f09d2647adfd; pass; check _(id: [rec-f2ace697-30ab-472c-9384-bd0114a080b0](.artifacts/records/project__check-run/rec-f2ace697-30ab-472c-9384-bd0114a080b0.md))_

## verify-standalone-aff-imports

### Acceptance
- **verify-standalone-aff-imports**: The close path imports affidavit.oracle_red, and no orchestra module imports affidavit.aa, affidavit.aa_resolve, affidavit.check, affidavit.policy, or affidavit.verdict; check; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_affidavit_import_boundary.py -q _(id: [rec-f6e74f3f-9cb0-4a01-aca2-9bb1f06f7e8d](.artifacts/records/project__acceptance/rec-f6e74f3f-9cb0-4a01-aca2-9bb1f06f7e8d.md))_

### Check
- **verify-standalone-aff-imports**: rec-f6e74f3f-9cb0-4a01-aca2-9bb1f06f7e8d; cac5247ddb6774f9a490bf7f3c5593a36a790b09; pass; check _(id: [rec-6ef153a4-3e1f-41e3-8e30-96358eae261b](.artifacts/records/project__check-run/rec-6ef153a4-3e1f-41e3-8e30-96358eae261b.md))_
- **verify-standalone-aff-imports**: rec-f6e74f3f-9cb0-4a01-aca2-9bb1f06f7e8d; 2f2054aeccef9db20ac96d84d3c7f09d2647adfd; pass; check _(id: [rec-a320e182-ebea-4df4-b762-9f2f7faaf886](.artifacts/records/project__check-run/rec-a320e182-ebea-4df4-b762-9f2f7faaf886.md))_
- **verify-standalone-aff-imports**: rec-f6e74f3f-9cb0-4a01-aca2-9bb1f06f7e8d; 50b2cd0b0360e6cbca7bdbfe3cda1dfaab46648c; pass; check _(id: [rec-ecafaffc-7064-43c8-bd52-ec8a4520defa](.artifacts/records/project__check-run/rec-ecafaffc-7064-43c8-bd52-ec8a4520defa.md))_

## verify-standalone-aff-skills

### Acceptance
- **verify-standalone-aff-skills**: Orchestra skills run orchestra check and orchestra close-batch for those steps, and aff verdict for a manifest claim; check; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_orchestra_commands.py -q _(id: [rec-ef59bc8a-f074-4b54-bb1b-4df4124cd65f](.artifacts/records/project__acceptance/rec-ef59bc8a-f074-4b54-bb1b-4df4124cd65f.md))_

### Check
- **verify-standalone-aff-skills**: rec-ef59bc8a-f074-4b54-bb1b-4df4124cd65f; 50b2cd0b0360e6cbca7bdbfe3cda1dfaab46648c; pass; check _(id: [rec-075547ef-42bc-4e29-86ab-ad1bf89384a0](.artifacts/records/project__check-run/rec-075547ef-42bc-4e29-86ab-ad1bf89384a0.md))_
- **verify-standalone-aff-skills**: rec-ef59bc8a-f074-4b54-bb1b-4df4124cd65f; cac5247ddb6774f9a490bf7f3c5593a36a790b09; pass; check _(id: [rec-19adaf2c-85a6-411c-a6b7-d0050747c489](.artifacts/records/project__check-run/rec-19adaf2c-85a6-411c-a6b7-d0050747c489.md))_
- **verify-standalone-aff-skills**: rec-ef59bc8a-f074-4b54-bb1b-4df4124cd65f; 2f2054aeccef9db20ac96d84d3c7f09d2647adfd; pass; check _(id: [rec-d18abc69-5244-432b-953a-5e95d1d2bc46](.artifacts/records/project__check-run/rec-d18abc69-5244-432b-953a-5e95d1d2bc46.md))_

## verify-standalone-aff-verbs

### Acceptance
- **verify-standalone-aff-verbs**: aff check and aff close-batch are not commands; check; evidence-layer; python3 -m pytest tests/test_standalone_cli.py -q -k rejects_store_commands _(id: [rec-2efc0852-17bc-4c58-b065-c929276d1962](.artifacts/records/project__acceptance/rec-2efc0852-17bc-4c58-b065-c929276d1962.md))_

### Check
- **verify-standalone-aff-verbs**: rec-2efc0852-17bc-4c58-b065-c929276d1962; 95816892f1208fd6b13723e6f89a959d6736da44; pass; check _(id: [rec-748e17a9-2216-4edc-8f43-a8dc410c4263](.artifacts/records/project__check-run/rec-748e17a9-2216-4edc-8f43-a8dc410c4263.md))_
- **verify-standalone-aff-verbs**: rec-2efc0852-17bc-4c58-b065-c929276d1962; 2c7dd552e6012ffb8626c635806214073168ba60; pass; check _(id: [rec-964ec978-2b03-421a-8938-ebb1630ebfeb](.artifacts/records/project__check-run/rec-964ec978-2b03-421a-8938-ebb1630ebfeb.md))_
- **verify-standalone-aff-verbs**: rec-2efc0852-17bc-4c58-b065-c929276d1962; 2c7dd552e6012ffb8626c635806214073168ba60; pass; check _(id: [rec-afbcc32b-488d-4e70-b3b5-5970cadf7736](.artifacts/records/project__check-run/rec-afbcc32b-488d-4e70-b3b5-5970cadf7736.md))_

## witness-lint

### Acceptance
- **witness-lint**: tdd; evidence-layer; python3 -m pytest tests/test_lint.py::test_lint_reports_no_assert_witness -q _(id: [rec-6f481c53-d452-4f5b-a691-0b1e2ca3bbcb](.artifacts/records/project__acceptance/rec-6f481c53-d452-4f5b-a691-0b1e2ca3bbcb.md))_

### Check
- **witness-lint**: rec-6f481c53-d452-4f5b-a691-0b1e2ca3bbcb; dirty; fail; tdd _(id: [rec-362d7125-88be-4052-9d53-d83edfdbc3ae](.artifacts/records/project__check-run/rec-362d7125-88be-4052-9d53-d83edfdbc3ae.md))_
- **witness-lint**: rec-6f481c53-d452-4f5b-a691-0b1e2ca3bbcb; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; tdd _(id: [rec-ffc303fe-9d25-49dd-8e69-440c3f238e35](.artifacts/records/project__check-run/rec-ffc303fe-9d25-49dd-8e69-440c3f238e35.md))_

## witness-lint-skips

### Acceptance
- **witness-lint-skips**: tdd; evidence-layer; python3 -m pytest tests/test_lint.py::test_lint_reports_new_skip_between_base_and_head -q _(id: [rec-6447ebae-ba32-4520-a868-be2e7c72dd2f](.artifacts/records/project__acceptance/rec-6447ebae-ba32-4520-a868-be2e7c72dd2f.md))_

### Check
- **witness-lint-skips**: rec-6447ebae-ba32-4520-a868-be2e7c72dd2f; 766765f555e67d9f50500fccbf116c16b855f3c0; pass; tdd _(id: [rec-09de0647-e452-4264-a1e4-1e93262f5ddb](.artifacts/records/project__check-run/rec-09de0647-e452-4264-a1e4-1e93262f5ddb.md))_
- **witness-lint-skips**: rec-6447ebae-ba32-4520-a868-be2e7c72dd2f; dirty; fail; tdd _(id: [rec-6f36cadd-b471-4f71-9c02-498c85123028](.artifacts/records/project__check-run/rec-6f36cadd-b471-4f71-9c02-498c85123028.md))_
