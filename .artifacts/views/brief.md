# Project Brief

> Derived view — not authoritative. Edit underlying records, not this file.
> Store state: sha256:21e4311e053ef419d396aa28709b723a6e10d183042c978803f0d4af13499a38

## amendment-sign

### Acceptance
- **amendment-sign**: A hash or test-id change is authorized only by a signature chain that verifies under the base allowlist; a changed allowlist, a bad signature, and a missing step are refused; tdd; evidence-layer; python3 -m pytest tests/test_amendment.py -q _(id: [rec-ea520f42-d62e-4b5d-879a-9dfd8ecc6d43](.artifacts/records/project__acceptance/rec-ea520f42-d62e-4b5d-879a-9dfd8ecc6d43.md))_

## attest-ci

### Acceptance
- **attest-ci**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_ci_workflow_runs_verdict_and_attest -q _(id: [rec-9d1b0910-9edf-4f6f-834f-bdc4a4eb650f](.artifacts/records/project__acceptance/rec-9d1b0910-9edf-4f6f-834f-bdc4a4eb650f.md))_

## attest-core

### Acceptance
- **attest-core**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_emit_signed_attestation_includes_commit_manifest_runner_and_claims -q _(id: [rec-2620c049-5db4-4593-b467-1f13191c8832](.artifacts/records/project__acceptance/rec-2620c049-5db4-4593-b467-1f13191c8832.md))_

## attest-core-bind

### Acceptance
- **attest-core-bind**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_verify_rejects_wrong_commit tests/test_attestation.py::test_verify_rejects_bind_mismatch_on_manifest_hash -q _(id: [rec-af4de5c3-440e-4e5f-9175-039d591a6fea](.artifacts/records/project__acceptance/rec-af4de5c3-440e-4e5f-9175-039d591a6fea.md))_

## attest-core-sig

### Acceptance
- **attest-core-sig**: tdd; evidence-layer; python3 -m pytest tests/test_attestation.py::test_verify_rejects_bad_signature tests/test_attestation.py::test_verify_rejects_tampered_payload -q _(id: [rec-27204235-9eb7-4d4e-a858-0c140858be15](.artifacts/records/project__acceptance/rec-27204235-9eb7-4d4e-a858-0c140858be15.md))_

## audit-blocks

### Work
- **audit-blocks**: aff audit labels hunk blocks noticed or not; phase-end-evidence; deliver; evidence-layer _(id: [rec-f2503a35-0a0a-407e-b8d7-a7ec9847d6cc](.artifacts/records/project__work-item/rec-f2503a35-0a0a-407e-b8d7-a7ec9847d6cc.md))_

### Acceptance
- **audit-blocks**: tdd; evidence-layer; python3 -m pytest tests/test_audit.py::test_r1_audit_labels_each_source_block tests/test_audit.py::test_r1_audit_reads_claim_tests_from_manifest -q _(id: [rec-4d99e4a9-8eed-4abf-bbfd-63d23ba1bf0e](.artifacts/records/project__acceptance/rec-4d99e4a9-8eed-4abf-bbfd-63d23ba1bf0e.md))_

## audit-blocks-range

### Acceptance
- **audit-blocks-range**: tdd; evidence-layer; python3 -m pytest tests/test_audit.py::test_r3_audit_reports_unnoticed_build_batch_cwd_block -q _(id: [rec-a402e4fe-db71-4c0b-9504-4bc345fe82fb](.artifacts/records/project__acceptance/rec-a402e4fe-db71-4c0b-9504-4bc345fe82fb.md))_

## audit-blocks-tests

### Acceptance
- **audit-blocks-tests**: tdd; evidence-layer; python3 -m pytest tests/test_audit.py::test_r2_audit_never_reports_test_file_blocks -q _(id: [rec-80251ecf-6081-4c0c-8ebb-aff653eb663a](.artifacts/records/project__acceptance/rec-80251ecf-6081-4c0c-8ebb-aff653eb663a.md))_

## audit-mutants

### Work
- **audit-mutants**: aff audit plants mutants in noticed blocks; phase-end-evidence; deliver; evidence-layer _(id: [rec-e68243cc-39af-4b77-abf6-4d9a191f1750](.artifacts/records/project__work-item/rec-e68243cc-39af-4b77-abf6-4d9a191f1750.md))_

### Acceptance
- **audit-mutants**: tdd; evidence-layer; python3 -m pytest tests/test_audit.py::test_r4_audit_plants_mutants_only_in_noticed_blocks -q _(id: [rec-1b284b3d-549e-44c3-9ebb-819ea7e633c0](.artifacts/records/project__acceptance/rec-1b284b3d-549e-44c3-9ebb-819ea7e633c0.md))_

## campaign-landing-automerge

### Constraint
- **campaign-landing-automerge**: For evidence-layer phases 5-11, Landing merges the phase branch into main and commits the store without asking; push is not a human stop; Landing close for evidence-layer phases frozen-environment through audit-differential; evidence-layer _(id: [rec-1c169abc-70e2-4610-a03b-aeee49a1257b](.artifacts/records/project__constraint/rec-1c169abc-70e2-4610-a03b-aeee49a1257b.md))_

## claim-cli

### Acceptance
- **claim-cli**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r1_claim_add_writes_manifest_entry_standalone -q _(id: [rec-75798857-63f7-4bf9-ba62-1702b7d62da3](.artifacts/records/project__acceptance/rec-75798857-63f7-4bf9-ba62-1702b7d62da3.md))_

## claim-cli-freeze

### Acceptance
- **claim-cli-freeze**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r2_freeze_records_exact_oracle_hashes tests/test_claim_authoring.py::test_r2_standalone_add_freeze_verdict_passes -q _(id: [rec-181f850e-452a-4386-a7c0-f2e5785394fa](.artifacts/records/project__acceptance/rec-181f850e-452a-4386-a7c0-f2e5785394fa.md))_

## claim-cli-lint

### Acceptance
- **claim-cli-lint**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r3_lint_claims_reports_compound_claim -q _(id: [rec-253cbc9c-3aa1-417e-809e-11f3ae8f76c3](.artifacts/records/project__acceptance/rec-253cbc9c-3aa1-417e-809e-11f3ae8f76c3.md))_

## conventional-commits

### Acceptance
- **conventional-commits**: execute-phase shows a per-task commit, a phase-branch commit, and a store commit whose subject matches type(scope): summary and whose body is one or two sentences; a task commit names the task slug; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_task_commit.py -q _(id: [rec-325e52d1-3740-4543-8f5c-47e640bf5b84](.artifacts/records/project__acceptance/rec-325e52d1-3740-4543-8f5c-47e640bf5b84.md))_

## env-freeze

### Acceptance
- **env-freeze**: tdd; evidence-layer; python3 -m pytest tests/test_verdict.py::test_verdict_refuses_support_file_drift_without_amendment tests/test_verdict.py::test_verdict_refuses_claim_support_file_drift_without_amendment -q _(id: [rec-3bff17d7-9d75-4d11-a504-9a5b8d66f551](.artifacts/records/project__acceptance/rec-3bff17d7-9d75-4d11-a504-9a5b8d66f551.md))_

## env-freeze-runner

### Acceptance
- **env-freeze-runner**: tdd; evidence-layer; python3 -m pytest tests/test_verdict.py::test_verdict_refuses_runner_digest_drift_without_amendment -q _(id: [rec-6a082c2e-8500-4178-b517-9d57ef09d9c7](.artifacts/records/project__acceptance/rec-6a082c2e-8500-4178-b517-9d57ef09d9c7.md))_

## evidence-layer

### Position
- **evidence-layer**: claim-authoring done; next up: phase-end-evidence; effort _(id: [rec-0c1b0959-7c23-496f-9474-082254eccf46](.artifacts/records/project__current-position/rec-0c1b0959-7c23-496f-9474-082254eccf46.md))_

## extract-store-binding

### Acceptance
- **extract-store-binding**: affidavit.aa imports StoreBindingError and resolve from affidavit.aa_resolve, affidavit/aa.py does not mention dashboard, and the aa tests pass; tdd; evidence-layer; python3 -m pytest tests/test_affidavit_aa.py tests/test_aa_resolve.py -q _(id: [rec-4f47fdf2-e4c8-436a-ad8b-c1d6be8c51b8](.artifacts/records/project__acceptance/rec-4f47fdf2-e4c8-436a-ad8b-c1d6be8c51b8.md))_

## fix-agent-docs

### Acceptance
- **fix-agent-docs**: AGENTS.md, README.md, and CLAUDE.md describe this repo as the evidence layer and send skills, the dashboard, scripts, and agents to ~/orchestra; tdd; evidence-layer; python3 -m pytest tests/test_evidence_layout.py::test_protocol_docs_describe_the_evidence_layer -q _(id: [rec-f9615bc0-d2d4-4b1a-9bf5-b7226656ae8f](.artifacts/records/project__acceptance/rec-f9615bc0-d2d4-4b1a-9bf5-b7226656ae8f.md))_

## fix-orchestra-help-tests

### Acceptance
- **fix-orchestra-help-tests**: a pytest runs bin/orchestra check --help and bin/orchestra close-batch --help and each exits 0; check; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_affidavit_check.py -q -k orchestra_subcommand_help _(id: [rec-be84a29b-7214-4ca2-a94d-2d51ec2dc6ab](.artifacts/records/project__acceptance/rec-be84a29b-7214-4ca2-a94d-2d51ec2dc6ab.md))_

## fix-readme-check-phrase

### Acceptance
- **fix-readme-check-phrase**: the moved orchestra check, close-batch, and store-client tests pass, including the README entry assertion; check; evidence-layer; cd "$HOME/orchestra" && bin/orchestra check --help && bin/orchestra close-batch --help && python3 -m pytest tests/test_affidavit_check.py tests/test_close_batch.py tests/test_affidavit_aa.py tests/test_aa_resolve.py -q _(id: [rec-25664c07-1863-4dac-a754-0836105f1fc3](.artifacts/records/project__acceptance/rec-25664c07-1863-4dac-a754-0836105f1fc3.md))_

## fix-verdict-exit

### Acceptance
- **fix-verdict-exit**: aff verdict fails a claim when pytest at --at exits non-zero, accepts a verified signed amendment, and rejects a hash or test-id change with no covering amendment; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "signed_amendment or head_failure or missing_amendment" _(id: [rec-cd3fb645-b979-440d-ad25-158586f29fe1](.artifacts/records/project__acceptance/rec-cd3fb645-b979-440d-ad25-158586f29fe1.md))_

## fix-verdict-help-test

### Acceptance
- **fix-verdict-help-test**: a pytest runs bin/aff verdict --help and asserts exit 0; check; evidence-layer; python3 -m pytest tests/test_standalone_cli.py -q -k verdict_help _(id: [rec-17932b62-b463-479e-8071-f17cc13eff09](.artifacts/records/project__acceptance/rec-17932b62-b463-479e-8071-f17cc13eff09.md))_

## human-claim

### Acceptance
- **human-claim**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r4_verdict_accepts_valid_human_signature -q _(id: [rec-bb995342-c16f-481e-9fff-8a39171dd49c](.artifacts/records/project__acceptance/rec-bb995342-c16f-481e-9fff-8a39171dd49c.md))_

## human-claim-reject

### Acceptance
- **human-claim-reject**: tdd; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r5_verdict_rejects_missing_human_signature tests/test_claim_authoring.py::test_r5_verdict_rejects_invalid_human_signature -q _(id: [rec-02ad65e6-5b73-4781-ad50-2ceac314dd59](.artifacts/records/project__acceptance/rec-02ad65e6-5b73-4781-ad50-2ceac314dd59.md))_

## junit-run-tests

### Acceptance
- **junit-run-tests**: run_tests returns one outcome per requested id from the JUnit file the command wrote; tdd; evidence-layer; python3 -m pytest tests/test_runner.py -q -k returns_id_outcomes _(id: [rec-63cf9023-9285-4f13-8e47-c12c9961223e](.artifacts/records/project__acceptance/rec-63cf9023-9285-4f13-8e47-c12c9961223e.md))_

## junit-run-tests-join

### Acceptance
- **junit-run-tests-join**: A case matches a witness id by name, or by file plus the classname segments after the file stem; tdd; evidence-layer; python3 -m pytest tests/test_runner.py -q -k joins_name_or_file _(id: [rec-433330be-3e4d-4928-9af1-1a2aa7d1719c](.artifacts/records/project__acceptance/rec-433330be-3e4d-4928-9af1-1a2aa7d1719c.md))_

## junit-run-tests-tags

### Acceptance
- **junit-run-tests-tags**: A JUnit failure is assertion_failed, an error is errored, a skip or a missing case is not_run, and a failure plus an error is errored; tdd; evidence-layer; python3 -m pytest tests/test_runner.py -q -k maps_failure_error_skipped _(id: [rec-cca4eb26-7518-47f2-9160-6f6480f68d02](.artifacts/records/project__acceptance/rec-cca4eb26-7518-47f2-9160-6f6480f68d02.md))_

## kind-enforcement

### Acceptance
- **kind-enforcement**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r1_manifest_claim_may_declare_evidence_kind -q _(id: [rec-1ef835e4-41dc-4aeb-8462-c21de870e1f1](.artifacts/records/project__acceptance/rec-1ef835e4-41dc-4aeb-8462-c21de870e1f1.md))_

## kind-enforcement-r2

### Acceptance
- **kind-enforcement-r2**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r2_interaction_claim_fails_under_default_unit_runner -q _(id: [rec-6e679668-c104-4f8b-af4e-0ec2fdf06601](.artifacts/records/project__acceptance/rec-6e679668-c104-4f8b-af4e-0ec2fdf06601.md))_

## kind-enforcement-r3

### Acceptance
- **kind-enforcement-r3**: tdd; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r3_interaction_claim_passes_under_interaction_runner -q _(id: [rec-4a04e8e2-2dd3-40ef-aa2b-6466115aa6bd](.artifacts/records/project__acceptance/rec-4a04e8e2-2dd3-40ef-aa2b-6466115aa6bd.md))_

## move-effort-records

### Acceptance
- **move-effort-records**: Both stores validate; the active goal here is evidence-layer; the active goals in orchestra are dashboard, workflow-loop, packaging, session-analysis, and test-suite-speed; check; evidence-layer; adaptive-artifacts validate && adaptive-artifacts --store "$HOME/orchestra/.artifacts" validate && python3 -c 'import json,os,subprocess
def goals(store):
 out=subprocess.check_output(["adaptive-artifacts","--store",store,"list","--type","project:active-goal","--state","active"],text=True)
 return sorted(r["subject"] for r in json.loads(out)["records"] if r.get("payload",{}).get("status")!="closed")
assert goals(".artifacts")==["evidence-layer"]
assert goals(os.path.expanduser("~/orchestra/.artifacts"))==["dashboard","packaging","session-analysis","test-suite-speed","workflow-loop"]' _(id: [rec-119ad93e-8886-4e96-912f-4ca9268d5971](.artifacts/records/project__acceptance/rec-119ad93e-8886-4e96-912f-4ca9268d5971.md))_

## move-store-client

### Acceptance
- **move-store-client**: bin/orchestra check and close-batch --help exit 0, and the moved check, close-batch, and store-client tests pass in ~/orchestra; check; evidence-layer; cd "$HOME/orchestra" && bin/orchestra check --help && bin/orchestra close-batch --help && python3 -m pytest tests/test_affidavit_check.py tests/test_close_batch.py tests/test_affidavit_aa.py tests/test_aa_resolve.py -q _(id: [rec-d0a726bc-62cc-4cb2-a95c-f4dd36e50532](.artifacts/records/project__acceptance/rec-d0a726bc-62cc-4cb2-a95c-f4dd36e50532.md))_

### Finding
- **move-store-client**: move-store-client closed done with a tdd pass that has no prior red check-run; aff check rec-e02d9d80-9036-481f-acec-0cc6f8f8c321 passed at 2483da2da2ad4929ad5853978d57335072ff577a. The executor committed tests/test_affidavit_import_boundary.py and the implementation in that same commit, so no runner-produced fail precedes the green.; a runner-produced fail for acceptance rec-bcc3412b-e7c6-4c97-988b-ea215bcb0c94 has a revision that is an ancestor of the green, or a human accepts this pass without red-first evidence; none _(id: [rec-7f5b80b9-cd8d-4376-9994-3553c0434f71](.artifacts/records/project__finding/rec-7f5b80b9-cd8d-4376-9994-3553c0434f71.md))_

## move-store-client-imports

### Acceptance
- **move-store-client-imports**: orchestra imports affidavit.oracle_red from the close path and does not import affidavit.aa, affidavit.aa_resolve, affidavit.check, affidavit.policy, or affidavit.verdict; tdd; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_affidavit_import_boundary.py -q _(id: [rec-bcc3412b-e7c6-4c97-988b-ea215bcb0c94](.artifacts/records/project__acceptance/rec-bcc3412b-e7c6-4c97-988b-ea215bcb0c94.md))_

## parse-manifest-runner

### Acceptance
- **parse-manifest-runner**: An absent runner loads as the shipped pytest template, and a runner that is not an argv list with {tests} and {report} fails manifest load; tdd; evidence-layer; python3 -m pytest tests/test_manifest.py -q -k "runner_absent or runner_invalid" _(id: [rec-2f6be402-8d78-4007-b3a4-e2a0ac1eec4a](.artifacts/records/project__acceptance/rec-2f6be402-8d78-4007-b3a4-e2a0ac1eec4a.md))_

## phase-end-evidence

### Position
- **phase-end-evidence**: phase-end-evidence planned: audit-blocks, audit-mutants + verify; phase _(id: [rec-fd218096-69fc-44f6-b89b-bcf0ff786453](.artifacts/records/project__current-position/rec-fd218096-69fc-44f6-b89b-bcf0ff786453.md))_

## phase-end-reviewer-milestones

### Constraint
- **phase-end-reviewer-milestones**: For evidence-layer phases 5-11, run the phase-end se-reviewer only on frozen-environment and audit-differential; skip reviewer, review check-run requirement, and integration-report on signed-verdict, oracle-provenance, evidence-kind, claim-authoring, and phase-end-evidence; execute-phase phase-end for evidence-layer phases frozen-environment through audit-differential; evidence-layer _(id: [rec-db3a1390-0ef9-4ba5-8d10-6ee334c90433](.artifacts/records/project__constraint/rec-db3a1390-0ef9-4ba5-8d10-6ee334c90433.md))_

## provenance-check

### Acceptance
- **provenance-check**: tdd; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r1_oracle_after_implementation_fails -q _(id: [rec-0f86bd5c-0f8d-4e98-b84d-cc6ac1721055](.artifacts/records/project__acceptance/rec-0f86bd5c-0f8d-4e98-b84d-cc6ac1721055.md))_

## provenance-check-pass

### Acceptance
- **provenance-check-pass**: tdd; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r4_ordered_oracle_only_distinct_signers_passes -q _(id: [rec-4cd9610f-2e6d-4690-97d8-507039b477dd](.artifacts/records/project__acceptance/rec-4cd9610f-2e6d-4690-97d8-507039b477dd.md))_

## provenance-check-paths

### Acceptance
- **provenance-check-paths**: tdd; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r2_oracle_commit_touches_non_oracle_paths_fails -q _(id: [rec-b7c8c328-c343-43d3-aa47-68e0f1a43c2a](.artifacts/records/project__acceptance/rec-b7c8c328-c343-43d3-aa47-68e0f1a43c2a.md))_

## provenance-check-signer

### Acceptance
- **provenance-check-signer**: tdd; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r3_shared_signer_fails -q _(id: [rec-d58ef0da-0be5-47e0-8ed8-140bd9cc586e](.artifacts/records/project__acceptance/rec-d58ef0da-0be5-47e0-8ed8-140bd9cc586e.md))_

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

## scaffold-orchestra

### Acceptance
- **scaffold-orchestra**: orchestra.reviewer and orchestra.suite import, orchestra.tier2 does not, and affidavit/tier2.py is absent from ~/orchestra; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_orchestra_package.py -q _(id: [rec-85630b31-3c07-4f31-9cd9-6c4b31419fc9](.artifacts/records/project__acceptance/rec-85630b31-3c07-4f31-9cd9-6c4b31419fc9.md))_

## scaffold-orchestra-layout

### Acceptance
- **scaffold-orchestra-layout**: ~/orchestra contains the seven skill directories and dashboard/, and both plugin manifests are named orchestra; check; evidence-layer; cd ~/orchestra && test -d skills/engage && test -d skills/discuss && test -d skills/plan-phase && test -d skills/execute-phase && test -d skills/verify-work && test -d skills/init && test -d skills/analyze-sessions && test -d dashboard && python3 -c "import json; from pathlib import Path; names=[json.loads(Path(p).read_text())[\"name\"] for p in [\".cursor-plugin/plugin.json\",\".claude-plugin/plugin.json\"]]; assert names==[\"orchestra\",\"orchestra\"]" _(id: [rec-bb8fcfec-3f8c-49dd-a274-6f88e947c6c4](.artifacts/records/project__acceptance/rec-bb8fcfec-3f8c-49dd-a274-6f88e947c6c4.md))_

## skill-command-names

### Acceptance
- **skill-command-names**: orchestra skills run orchestra check and orchestra close-batch, and still run aff verdict for a manifest claim; tdd; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_orchestra_commands.py -q _(id: [rec-4d363eb6-fdda-45d0-a8ba-65a04506823c](.artifacts/records/project__acceptance/rec-4d363eb6-fdda-45d0-a8ba-65a04506823c.md))_

## skill-evidence-boundary

### Acceptance
- **skill-evidence-boundary**: The boundary test fails on a fixture skill that creates a tdd check-run or a project:oracle-amendment, and passes on the migrated skills; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_skill_evidence_boundary.py -q -k "not verdict" _(id: [rec-3b292b01-e0a5-4159-addb-fcd87fe76d35](.artifacts/records/project__acceptance/rec-3b292b01-e0a5-4159-addb-fcd87fe76d35.md))_

## skill-evidence-boundary-verdict

### Acceptance
- **skill-evidence-boundary-verdict**: execute-phase and verify-work run aff verdict for a claim in the manifest and treat a non-zero exit as not done; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_skill_evidence_boundary.py -q -k verdict _(id: [rec-157b8a77-5bd4-4462-a516-cfed02b4ef1a](.artifacts/records/project__acceptance/rec-157b8a77-5bd4-4462-a516-cfed02b4ef1a.md))_

## strip-aff-verbs

### Acceptance
- **strip-aff-verbs**: bin/aff verdict passes with adaptive-artifacts off PATH, and bin/aff check and close-batch are rejected; tdd; evidence-layer; python3 -m pytest tests/test_standalone_cli.py -q _(id: [rec-e054ab1c-dd4a-4324-b7ed-cf3433b2d70f](.artifacts/records/project__acceptance/rec-e054ab1c-dd4a-4324-b7ed-cf3433b2d70f.md))_

## strip-aff-verbs-boundary

### Acceptance
- **strip-aff-verbs-boundary**: a test fails when any module under affidavit/ contains project:, SE_WORKFLOW_STORE, store-binding.json, or adaptive-artifacts; tdd; evidence-layer; python3 -m pytest tests/test_evidence_layout.py -q -k no_store_tokens _(id: [rec-243ce423-ece2-440a-b36b-826ea9b47660](.artifacts/records/project__acceptance/rec-243ce423-ece2-440a-b36b-826ea9b47660.md))_

## strip-affidavit

### Acceptance
- **strip-affidavit**: With skills/, dashboard/, scripts/, and agents/ absent, bin/aff check, close-batch, and verdict --help exit 0 and the remaining verb tests pass; tdd; evidence-layer; test ! -d skills && test ! -d dashboard && test ! -d scripts && test ! -d agents && bin/aff check --help && bin/aff close-batch --help && bin/aff verdict --help && python3 -m pytest tests/test_evidence_layout.py tests/test_affidavit_check.py tests/test_close_batch.py tests/test_verdict.py tests/test_manifest.py tests/test_amendment.py tests/test_oracle_red.py tests/test_affidavit_aa.py -q _(id: [rec-2badfd8f-ce40-4a92-bc85-6f8fa36c4e01](.artifacts/records/project__acceptance/rec-2badfd8f-ce40-4a92-bc85-6f8fa36c4e01.md))_

## suite-advisory-claims-manifest

### Finding
- **suite-advisory-claims-manifest**: advisory suite fail for claims-manifest-suite; exit_code 1; failing node tests/test_dashboard_journal.py::test_journal_detail_pager_pages_record_with_stub; suite check-run passes at phase head, or human clears; none _(id: [rec-43ce266c-c2ac-4895-99e2-e039eac06a4f](.artifacts/records/project__finding/rec-43ce266c-c2ac-4895-99e2-e039eac06a4f.md))_

## suite-advisory-standalone-aff

### Finding
- **suite-advisory-standalone-aff**: advisory suite fail for standalone-aff-suite; exit_code=5; failing node ids: none (pytest collected no tmux tests); suite check-run passes at phase head, or human clears; none _(id: [rec-741cb0e6-238f-43c3-a038-2dfc5efa7913](.artifacts/records/project__finding/rec-741cb0e6-238f-43c3-a038-2dfc5efa7913.md))_

## verdict-command

### Acceptance
- **verdict-command**: bin/aff verdict exits 0 only when oracle hashes match, the base pytest failure is assertion-level, and the tests pass at head; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or not_assertion" _(id: [rec-39a10c5a-3bf3-4872-8e98-cb5e1082d5fb](.artifacts/records/project__acceptance/rec-39a10c5a-3bf3-4872-8e98-cb5e1082d5fb.md))_

## verdict-command-cli

### Acceptance
- **verdict-command-cli**: bin/aff verdict subprocess tests refuse a bad amendment signature and an allowlist change, and pass with --cwd pointed at a phase worktree; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "bad_signature or allowlist or cwd_phase" _(id: [rec-7839468b-6ae7-4fe1-a2f7-9c2fcef70187](.artifacts/records/project__acceptance/rec-7839468b-6ae7-4fe1-a2f7-9c2fcef70187.md))_

## verdict-command-store

### Acceptance
- **verdict-command-store**: A forged project:check-run under .artifacts does not change a passing or a failing bin/aff verdict; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k forged_check_run _(id: [rec-ad7115bc-82ff-4215-a410-0883b5434294](.artifacts/records/project__acceptance/rec-ad7115bc-82ff-4215-a410-0883b5434294.md))_

## verdict-manifest

### Acceptance
- **verdict-manifest**: git show of a revision yields the manifest claims, the allowlist bytes, and oracle file hashes; a dirty worktree and a non-commit revision do not; tdd; evidence-layer; python3 -m pytest tests/test_manifest.py -q _(id: [rec-a5646067-6c51-44b0-8302-bfae12644013](.artifacts/records/project__acceptance/rec-a5646067-6c51-44b0-8302-bfae12644013.md))_

## verdict-through-runner

### Acceptance
- **verdict-through-runner**: aff verdict keeps pass, hash-mismatch, and collection-error results, and verdict.py does not scrape pytest stdout; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or not_assertion or ignores_pytest_stdout" _(id: [rec-11e21744-5979-4d98-a4fe-bb5dc3b0c834](.artifacts/records/project__acceptance/rec-11e21744-5979-4d98-a4fe-bb5dc3b0c834.md))_

### Amendment
- **verdict-through-runner**: verdict-through-runner; evidence-layer _(id: [rec-81bfee77-abca-4104-b427-c19683f55e79](.artifacts/records/project__assignment-amendment/rec-81bfee77-abca-4104-b427-c19683f55e79.md))_

## verdict-through-runner-fixture

### Acceptance
- **verdict-through-runner-fixture**: A fixture command that emits JUnit XML is judged pass, not assertion, or tests failed with no new module under affidavit/; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k fixture_junit _(id: [rec-7c5ba8b7-65f1-43b8-ae07-bdefbe64c545](.artifacts/records/project__acceptance/rec-7c5ba8b7-65f1-43b8-ae07-bdefbe64c545.md))_

## verdict-through-runner-unstable

### Acceptance
- **verdict-through-runner-unstable**: A disagreeing confirmation yields unstable and a non-zero exit, and a failed first run is not confirmed; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "unstable_when_confirmation or skips_confirmation" _(id: [rec-ca86ff79-3d6b-4441-91b8-e3e0abd9cdfa](.artifacts/records/project__acceptance/rec-ca86ff79-3d6b-4441-91b8-e3e0abd9cdfa.md))_

## verify-claim-authoring

### Acceptance
- **verify-claim-authoring**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r1_claim_add_writes_manifest_entry_standalone -q _(id: [rec-3ba8b3a4-946b-45b9-ad43-80a95fab5a9a](.artifacts/records/project__acceptance/rec-3ba8b3a4-946b-45b9-ad43-80a95fab5a9a.md))_

## verify-claim-authoring-freeze

### Acceptance
- **verify-claim-authoring-freeze**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r2_freeze_records_exact_oracle_hashes tests/test_claim_authoring.py::test_r2_standalone_add_freeze_verdict_passes -q _(id: [rec-c04a807b-31ff-475f-9acf-33a49952d72f](.artifacts/records/project__acceptance/rec-c04a807b-31ff-475f-9acf-33a49952d72f.md))_

## verify-claim-authoring-lint

### Acceptance
- **verify-claim-authoring-lint**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r3_lint_claims_reports_compound_claim -q _(id: [rec-9d812846-4080-4211-876b-31734708a995](.artifacts/records/project__acceptance/rec-9d812846-4080-4211-876b-31734708a995.md))_

## verify-claim-authoring-reject

### Acceptance
- **verify-claim-authoring-reject**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r5_verdict_rejects_missing_human_signature tests/test_claim_authoring.py::test_r5_verdict_rejects_invalid_human_signature -q _(id: [rec-55b8c272-23dc-43b4-97ac-0ac7bb74dda7](.artifacts/records/project__acceptance/rec-55b8c272-23dc-43b4-97ac-0ac7bb74dda7.md))_

## verify-claim-authoring-signed

### Acceptance
- **verify-claim-authoring-signed**: check; evidence-layer; python3 -m pytest tests/test_claim_authoring.py::test_r4_verdict_accepts_valid_human_signature -q _(id: [rec-95ddfb5c-0a5b-43f3-9b6d-34079130a087](.artifacts/records/project__acceptance/rec-95ddfb5c-0a5b-43f3-9b6d-34079130a087.md))_

## verify-claims-manifest

### Acceptance
- **verify-claims-manifest**: aff verdict exits 0 only when manifest hashes match the tree at --at, the oracle tests fail at --base on an assertion, and they pass at --at; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or not_assertion" _(id: [rec-f25d51ef-6c72-4a13-b9d6-4e9ec7a177b3](.artifacts/records/project__acceptance/rec-f25d51ef-6c72-4a13-b9d6-4e9ec7a177b3.md))_

## verify-claims-manifest-forge

### Acceptance
- **verify-claims-manifest-forge**: A forged stored check-run does not change the verdict; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k forged_check_run _(id: [rec-1aaa8c5e-adec-4df2-bc30-d09600c12903](.artifacts/records/project__acceptance/rec-1aaa8c5e-adec-4df2-bc30-d09600c12903.md))_

## verify-claims-manifest-suite

### Acceptance
- **verify-claims-manifest-suite**: CLI subprocess tests cover the pass, a hash mismatch, a missing or invalid amendment signature, an allowlist change, and a --cwd pointed at a phase worktree other than the store checkout; tdd; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or bad_signature or allowlist or cwd_phase" _(id: [rec-27b93db5-292e-4864-8bc9-ac743955d861](.artifacts/records/project__acceptance/rec-27b93db5-292e-4864-8bc9-ac743955d861.md))_

## verify-evidence-kind

### Acceptance
- **verify-evidence-kind**: check; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r1_manifest_claim_may_declare_evidence_kind -q _(id: [rec-31329697-17c1-4cef-927e-b2bba4675d35](.artifacts/records/project__acceptance/rec-31329697-17c1-4cef-927e-b2bba4675d35.md))_

## verify-evidence-kind-r2

### Acceptance
- **verify-evidence-kind-r2**: check; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r2_interaction_claim_fails_under_default_unit_runner -q _(id: [rec-7869f8d0-e7d5-4a7c-9c8c-aa0507b6cd7a](.artifacts/records/project__acceptance/rec-7869f8d0-e7d5-4a7c-9c8c-aa0507b6cd7a.md))_

## verify-evidence-kind-r3

### Acceptance
- **verify-evidence-kind-r3**: check; evidence-layer; python3 -m pytest tests/test_evidence_kind.py::test_r3_interaction_claim_passes_under_interaction_runner -q _(id: [rec-35c32ec7-df9d-44ae-9d4b-1da771b510ef](.artifacts/records/project__acceptance/rec-35c32ec7-df9d-44ae-9d4b-1da771b510ef.md))_

## verify-frozen-environment

### Acceptance
- **verify-frozen-environment**: check; evidence-layer; python3 -m pytest tests/test_verdict.py::test_verdict_refuses_support_file_drift_without_amendment tests/test_verdict.py::test_verdict_refuses_claim_support_file_drift_without_amendment -q _(id: [rec-f83f8a6d-4589-43b7-9853-95d904d92b14](.artifacts/records/project__acceptance/rec-f83f8a6d-4589-43b7-9853-95d904d92b14.md))_

## verify-frozen-environment-lint

### Acceptance
- **verify-frozen-environment-lint**: check; evidence-layer; python3 -m pytest tests/test_lint.py::test_lint_reports_no_assert_witness -q _(id: [rec-55edf2d5-5ed9-49c2-aaef-10cdb45b875c](.artifacts/records/project__acceptance/rec-55edf2d5-5ed9-49c2-aaef-10cdb45b875c.md))_

## verify-frozen-environment-runner

### Acceptance
- **verify-frozen-environment-runner**: check; evidence-layer; python3 -m pytest tests/test_verdict.py::test_verdict_refuses_runner_digest_drift_without_amendment -q _(id: [rec-b9efb8a3-f48d-43a4-9733-78462fbe3a23](.artifacts/records/project__acceptance/rec-b9efb8a3-f48d-43a4-9733-78462fbe3a23.md))_

## verify-frozen-environment-skips

### Acceptance
- **verify-frozen-environment-skips**: check; evidence-layer; python3 -m pytest tests/test_lint.py::test_lint_reports_new_skip_between_base_and_head -q _(id: [rec-64566959-1ab1-4de4-bca9-feb47da70a23](.artifacts/records/project__acceptance/rec-64566959-1ab1-4de4-bca9-feb47da70a23.md))_

## verify-oracle-provenance

### Acceptance
- **verify-oracle-provenance**: check; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r1_oracle_after_implementation_fails -q _(id: [rec-951a64c2-99ad-44da-95d4-4dc221012064](.artifacts/records/project__acceptance/rec-951a64c2-99ad-44da-95d4-4dc221012064.md))_

## verify-oracle-provenance-pass

### Acceptance
- **verify-oracle-provenance-pass**: check; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r4_ordered_oracle_only_distinct_signers_passes -q _(id: [rec-64af228c-7e2c-443d-a84b-b391e3351926](.artifacts/records/project__acceptance/rec-64af228c-7e2c-443d-a84b-b391e3351926.md))_

## verify-oracle-provenance-paths

### Acceptance
- **verify-oracle-provenance-paths**: check; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r2_oracle_commit_touches_non_oracle_paths_fails -q _(id: [rec-068c0dd0-35ca-4d48-92d7-9df3837832ff](.artifacts/records/project__acceptance/rec-068c0dd0-35ca-4d48-92d7-9df3837832ff.md))_

## verify-oracle-provenance-signer

### Acceptance
- **verify-oracle-provenance-signer**: check; evidence-layer; python3 -m pytest tests/test_provenance.py::test_r3_shared_signer_fails -q _(id: [rec-fbe22f64-aab1-4d71-a9e9-424741e6234b](.artifacts/records/project__acceptance/rec-fbe22f64-aab1-4d71-a9e9-424741e6234b.md))_

## verify-orchestration-split

### Acceptance
- **verify-orchestration-split**: bin/aff check, close-batch, and verdict --help exit 0, and the remaining pytest files pass with skills/, dashboard/, scripts/, and agents/ absent; check; evidence-layer; test ! -d skills && test ! -d dashboard && test ! -d scripts && test ! -d agents && bin/aff check --help && bin/aff close-batch --help && bin/aff verdict --help && python3 -m pytest tests/test_evidence_layout.py tests/test_affidavit_check.py tests/test_close_batch.py tests/test_verdict.py tests/test_manifest.py tests/test_amendment.py tests/test_oracle_red.py tests/test_affidavit_aa.py -q _(id: [rec-c590714e-be3c-4c72-9fd2-cd7d966f4ef0](.artifacts/records/project__acceptance/rec-c590714e-be3c-4c72-9fd2-cd7d966f4ef0.md))_

## verify-orchestration-split-boundary

### Acceptance
- **verify-orchestration-split-boundary**: The orchestra boundary test fails on a fixture skill that creates a tdd or check check-run or a project:oracle-amendment, and passes on the migrated skills; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_skill_evidence_boundary.py -q -k 'not verdict' _(id: [rec-29938747-c59e-4421-838e-0a6c7573a4cb](.artifacts/records/project__acceptance/rec-29938747-c59e-4421-838e-0a6c7573a4cb.md))_

## verify-orchestration-split-commits

### Acceptance
- **verify-orchestration-split-commits**: execute-phase shows a per-task commit, a phase-branch commit, and a store commit whose subject matches type(scope): summary and whose body is one or two sentences; a task commit names the task slug; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_task_commit.py -q _(id: [rec-552c3f36-62a8-4868-b00c-e380bb8449bc](.artifacts/records/project__acceptance/rec-552c3f36-62a8-4868-b00c-e380bb8449bc.md))_

## verify-orchestration-split-layout

### Acceptance
- **verify-orchestration-split-layout**: ~/orchestra contains the seven skill directories and dashboard/, and orchestra.reviewer and orchestra.suite import with no tier2 module; check; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_orchestra_package.py -q && test -d skills/engage && test -d skills/discuss && test -d skills/plan-phase && test -d skills/execute-phase && test -d skills/verify-work && test -d skills/init && test -d skills/analyze-sessions && test -d dashboard _(id: [rec-5330ace0-1772-4d24-9d1a-f4e7b74a8fe0](.artifacts/records/project__acceptance/rec-5330ace0-1772-4d24-9d1a-f4e7b74a8fe0.md))_

## verify-orchestration-split-project

### Acceptance
- **verify-orchestration-split-project**: A fixture store whose project is affidavit is rewritten to orchestra, and a fixture whose project is any other name is left unchanged; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_ensure_store_project.py -q _(id: [rec-1c20c26a-415f-4af9-8b85-1041500bed92](.artifacts/records/project__acceptance/rec-1c20c26a-415f-4af9-8b85-1041500bed92.md))_

## verify-orchestration-split-stores

### Acceptance
- **verify-orchestration-split-stores**: Both stores validate; the active goal here is evidence-layer; the active goals in orchestra are dashboard, workflow-loop, packaging, session-analysis, and test-suite-speed; check; evidence-layer; adaptive-artifacts validate && adaptive-artifacts --store "$HOME/orchestra/.artifacts" validate && python3 -c 'import json,os,subprocess
def goals(store):
 out=subprocess.check_output(["adaptive-artifacts","--store",store,"list","--type","project:active-goal","--state","active"],text=True)
 return sorted(r["subject"] for r in json.loads(out)["records"] if r.get("payload",{}).get("status")!="closed")
assert goals(".artifacts")==["evidence-layer"]
assert goals(os.path.expanduser("~/orchestra/.artifacts"))==["dashboard","packaging","session-analysis","test-suite-speed","workflow-loop"]' _(id: [rec-e88d2262-2f38-4ef4-a3c1-59032762980f](.artifacts/records/project__acceptance/rec-e88d2262-2f38-4ef4-a3c1-59032762980f.md))_

## verify-orchestration-split-verdict

### Acceptance
- **verify-orchestration-split-verdict**: execute-phase and verify-work run aff verdict for a claim in the manifest and treat a non-zero exit as not done; tdd; evidence-layer; cd ~/orchestra && python3 -m pytest tests/test_skill_evidence_boundary.py -q -k verdict _(id: [rec-167feb75-1bd7-4db4-ad7c-05b50da84dae](.artifacts/records/project__acceptance/rec-167feb75-1bd7-4db4-ad7c-05b50da84dae.md))_

## verify-phase-end-evidence

### Work
- **verify-phase-end-evidence**: Verify phase-end evidence; phase-end-evidence; deliver; evidence-layer _(id: [rec-7f20d856-7d9c-4e47-8f58-3f3afebe34b0](.artifacts/records/project__work-item/rec-7f20d856-7d9c-4e47-8f58-3f3afebe34b0.md))_

### Acceptance
- **verify-phase-end-evidence**: check; evidence-layer; python3 -m pytest tests/test_audit.py::test_r1_audit_labels_each_source_block tests/test_audit.py::test_r1_audit_reads_claim_tests_from_manifest -q _(id: [rec-6309e3d9-876f-42ce-877b-70b6e54e95d0](.artifacts/records/project__acceptance/rec-6309e3d9-876f-42ce-877b-70b6e54e95d0.md))_

## verify-phase-end-evidence-mutants

### Acceptance
- **verify-phase-end-evidence-mutants**: check; evidence-layer; python3 -m pytest tests/test_audit.py::test_r4_audit_plants_mutants_only_in_noticed_blocks -q _(id: [rec-e5c480a3-7f7b-4ab0-983d-4f1330b2d9c3](.artifacts/records/project__acceptance/rec-e5c480a3-7f7b-4ab0-983d-4f1330b2d9c3.md))_

## verify-phase-end-evidence-range

### Acceptance
- **verify-phase-end-evidence-range**: check; evidence-layer; python3 -m pytest tests/test_audit.py::test_r3_audit_reports_unnoticed_build_batch_cwd_block -q _(id: [rec-80780e36-123f-4019-8dcc-1f4f096858a6](.artifacts/records/project__acceptance/rec-80780e36-123f-4019-8dcc-1f4f096858a6.md))_

## verify-phase-end-evidence-tests

### Acceptance
- **verify-phase-end-evidence-tests**: check; evidence-layer; python3 -m pytest tests/test_audit.py::test_r2_audit_never_reports_test_file_blocks -q _(id: [rec-844c2281-213a-49a8-bb8e-f67e05319f6d](.artifacts/records/project__acceptance/rec-844c2281-213a-49a8-bb8e-f67e05319f6d.md))_

## verify-runner-adapter

### Acceptance
- **verify-runner-adapter**: aff verdict judges a claim through run_tests with no pytest stdout regex, and existing pass, hash-mismatch, and collection-error cases keep their results; check; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k "pass_when or hash_mismatch or not_assertion or ignores_pytest_stdout" _(id: [rec-1806d506-b116-4a6d-8c3f-005d61f39cc2](.artifacts/records/project__acceptance/rec-1806d506-b116-4a6d-8c3f-005d61f39cc2.md))_

## verify-runner-adapter-fixture

### Acceptance
- **verify-runner-adapter-fixture**: A fixture command that emits JUnit XML is judged through bin/aff verdict with no change under affidavit/; check; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k fixture_junit _(id: [rec-db6fa367-1432-40ad-8bc8-9f88d61f6eed](.artifacts/records/project__acceptance/rec-db6fa367-1432-40ad-8bc8-9f88d61f6eed.md))_

## verify-runner-adapter-template

### Acceptance
- **verify-runner-adapter-template**: An absent runner uses the shipped pytest template, and a runner that is not an argv list with {tests} and {report} fails manifest load; check; evidence-layer; python3 -m pytest tests/test_manifest.py -q -k "runner_absent or runner_invalid" _(id: [rec-84963c29-53ed-4d7d-a04b-d2d0d5b0c25a](.artifacts/records/project__acceptance/rec-84963c29-53ed-4d7d-a04b-d2d0d5b0c25a.md))_

## verify-runner-adapter-unstable

### Acceptance
- **verify-runner-adapter-unstable**: A witness that is assertion_failed on the first base run and passed on the confirmation run yields unstable and a non-zero exit; check; evidence-layer; python3 -m pytest tests/test_verdict.py -q -k unstable_when_confirmation _(id: [rec-81acd29f-17af-42a1-b0be-374190e321dd](.artifacts/records/project__acceptance/rec-81acd29f-17af-42a1-b0be-374190e321dd.md))_

## verify-signed-verdict

### Acceptance
- **verify-signed-verdict**: check; evidence-layer; python3 -m pytest tests/test_attestation.py::test_emit_signed_attestation_includes_commit_manifest_runner_and_claims -q _(id: [rec-02f5f1e1-da0e-4c60-b62f-9cea163b3ef3](.artifacts/records/project__acceptance/rec-02f5f1e1-da0e-4c60-b62f-9cea163b3ef3.md))_

## verify-signed-verdict-bind

### Acceptance
- **verify-signed-verdict-bind**: check; evidence-layer; python3 -m pytest tests/test_attestation.py::test_verify_rejects_wrong_commit tests/test_attestation.py::test_verify_rejects_bind_mismatch_on_manifest_hash -q _(id: [rec-3fa6eb8b-9b79-4ba8-a95f-c731281ab225](.artifacts/records/project__acceptance/rec-3fa6eb8b-9b79-4ba8-a95f-c731281ab225.md))_

## verify-signed-verdict-ci

### Acceptance
- **verify-signed-verdict-ci**: check; evidence-layer; python3 -m pytest tests/test_attestation.py::test_ci_workflow_runs_verdict_and_attest -q _(id: [rec-8d754ac2-188a-4162-8aac-2850522ce765](.artifacts/records/project__acceptance/rec-8d754ac2-188a-4162-8aac-2850522ce765.md))_

## verify-signed-verdict-sig

### Acceptance
- **verify-signed-verdict-sig**: check; evidence-layer; python3 -m pytest tests/test_attestation.py::test_verify_rejects_bad_signature tests/test_attestation.py::test_verify_rejects_tampered_payload -q _(id: [rec-02cd8744-be8c-402c-9387-69c2c7e632d2](.artifacts/records/project__acceptance/rec-02cd8744-be8c-402c-9387-69c2c7e632d2.md))_

## verify-standalone-aff

### Acceptance
- **verify-standalone-aff**: A checkout of this repo, with no orchestra tree, no adaptive-artifacts on PATH, and no se-workflow store binding, still produces a verdict from the committed manifest; check; evidence-layer; python3 -m pytest tests/test_standalone_cli.py -q -k verdict_without_runtime _(id: [rec-ef30c56e-14a1-4897-9621-e3110af528c3](.artifacts/records/project__acceptance/rec-ef30c56e-14a1-4897-9621-e3110af528c3.md))_

### Amendment
- **verify-standalone-aff**: verify-standalone-aff; evidence-layer _(id: [rec-66bb4833-67fa-4c52-bdea-d7915f064a0b](.artifacts/records/project__assignment-amendment/rec-66bb4833-67fa-4c52-bdea-d7915f064a0b.md))_

## verify-standalone-aff-boundary

### Acceptance
- **verify-standalone-aff-boundary**: A test fails while any module under affidavit/ contains project:, SE_WORKFLOW_STORE, store-binding.json, or adaptive-artifacts; check; evidence-layer; python3 -m pytest tests/test_evidence_layout.py -q -k no_store_tokens _(id: [rec-2b4379ce-c5cf-4276-8a31-359b82448f7e](.artifacts/records/project__acceptance/rec-2b4379ce-c5cf-4276-8a31-359b82448f7e.md))_

## verify-standalone-aff-cli

### Acceptance
- **verify-standalone-aff-cli**: orchestra check and orchestra close-batch run from ~/orchestra, and the moved check, close-batch, and store-client tests pass there; check; evidence-layer; cd "$HOME/orchestra" && bin/orchestra check --help && bin/orchestra close-batch --help && python3 -m pytest tests/test_affidavit_check.py tests/test_close_batch.py tests/test_affidavit_aa.py tests/test_aa_resolve.py -q _(id: [rec-8f3850bd-9558-48f9-9bfe-a1245f4a1a1d](.artifacts/records/project__acceptance/rec-8f3850bd-9558-48f9-9bfe-a1245f4a1a1d.md))_

## verify-standalone-aff-imports

### Acceptance
- **verify-standalone-aff-imports**: The close path imports affidavit.oracle_red, and no orchestra module imports affidavit.aa, affidavit.aa_resolve, affidavit.check, affidavit.policy, or affidavit.verdict; check; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_affidavit_import_boundary.py -q _(id: [rec-f6e74f3f-9cb0-4a01-aca2-9bb1f06f7e8d](.artifacts/records/project__acceptance/rec-f6e74f3f-9cb0-4a01-aca2-9bb1f06f7e8d.md))_

## verify-standalone-aff-skills

### Acceptance
- **verify-standalone-aff-skills**: Orchestra skills run orchestra check and orchestra close-batch for those steps, and aff verdict for a manifest claim; check; evidence-layer; cd "$HOME/orchestra" && python3 -m pytest tests/test_orchestra_commands.py -q _(id: [rec-ef59bc8a-f074-4b54-bb1b-4df4124cd65f](.artifacts/records/project__acceptance/rec-ef59bc8a-f074-4b54-bb1b-4df4124cd65f.md))_

## verify-standalone-aff-verbs

### Acceptance
- **verify-standalone-aff-verbs**: aff check and aff close-batch are not commands; check; evidence-layer; python3 -m pytest tests/test_standalone_cli.py -q -k rejects_store_commands _(id: [rec-2efc0852-17bc-4c58-b065-c929276d1962](.artifacts/records/project__acceptance/rec-2efc0852-17bc-4c58-b065-c929276d1962.md))_

## witness-lint

### Acceptance
- **witness-lint**: tdd; evidence-layer; python3 -m pytest tests/test_lint.py::test_lint_reports_no_assert_witness -q _(id: [rec-6f481c53-d452-4f5b-a691-0b1e2ca3bbcb](.artifacts/records/project__acceptance/rec-6f481c53-d452-4f5b-a691-0b1e2ca3bbcb.md))_

## witness-lint-skips

### Acceptance
- **witness-lint-skips**: tdd; evidence-layer; python3 -m pytest tests/test_lint.py::test_lint_reports_new_skip_between_base_and_head -q _(id: [rec-6447ebae-ba32-4520-a868-be2e7c72dd2f](.artifacts/records/project__acceptance/rec-6447ebae-ba32-4520-a868-be2e7c72dd2f.md))_
