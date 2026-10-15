# Project Verification

> Derived view — not authoritative. Edit underlying records, not this file.
> Store state: sha256:d8f5544db236d8d53f0b88f94fef5eb73f5d942e820c43b8629b251a3393a079

## activity-failures

### Acceptance
- **activity-failures**: Model test sets failed for a failed check-run and a failed report only; pilot test shows a failed line in the error colour with ✗; the tests fail before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_app.py -q -k fail _(id: [rec-7d228e89-762a-4794-9c56-adfca651899a](.artifacts/records/project__acceptance/rec-7d228e89-762a-4794-9c56-adfca651899a.md))_

### Check
- **activity-failures**: rec-7d228e89-762a-4794-9c56-adfca651899a; 6c723d89c0a95f1c261cd940f48e51f9a731bfd1; pass; tdd _(id: [rec-2a089a7b-872b-465c-9b46-aaa8ae7f5812](.artifacts/records/project__check-run/rec-2a089a7b-872b-465c-9b46-aaa8ae7f5812.md))_

## add-dashboard-view

### Acceptance
- **add-dashboard-view**: The contract resolves with the dashboard view and passes the contract and skill consistency tests; tdd; dashboard; cd ~/se-workflow && python3 -m pytest tests -q _(id: [rec-b6ae7140-2e58-4194-9294-6cc47d132fb4](.artifacts/records/project__acceptance/rec-b6ae7140-2e58-4194-9294-6cc47d132fb4.md))_

### Check
- **add-dashboard-view**: rec-1dceda28-8bfd-43df-b3ca-53d3a7740286; c993c1b8159c0a5a28827c63e588a86f40a0971b; pass; tdd _(id: [rec-31267407-87d0-4234-b4bb-761394266851](.artifacts/records/project__check-run/rec-31267407-87d0-4234-b4bb-761394266851.md))_
- **add-dashboard-view**: rec-b6ae7140-2e58-4194-9294-6cc47d132fb4; c993c1b8159c0a5a28827c63e588a86f40a0971b; pass; tdd _(id: [rec-c2cd5a62-cd01-4fe9-9a3d-83ce6a3b6abc](.artifacts/records/project__check-run/rec-c2cd5a62-cd01-4fe9-9a3d-83ce6a3b6abc.md))_

## add-dashboard-view-render

### Acceptance
- **add-dashboard-view-render**: Against a seeded store with one record per section, view --id project:dashboard renders every section in order with labeled fields, and a done item older than 24h is absent; tdd; dashboard; cd ~/se-workflow && python3 -m pytest tests -q -k dashboard _(id: [rec-1dceda28-8bfd-43df-b3ca-53d3a7740286](.artifacts/records/project__acceptance/rec-1dceda28-8bfd-43df-b3ca-53d3a7740286.md))_

## ag-aggregate-cli

### Acceptance
- **ag-aggregate-cli**: On a fixture report the command prints valid JSON with efforts, tools, skills, outliers and caveats; on the real report it exits 0 and lists every effort that has a session.; tdd; session-analysis; python3 -m pytest -q tests/test_session_aggregate.py _(id: [rec-efaa257a-446d-4f97-a738-4d098747043f](.artifacts/records/project__acceptance/rec-efaa257a-446d-4f97-a738-4d098747043f.md))_

### Check
- **ag-aggregate-cli**: rec-efaa257a-446d-4f97-a738-4d098747043f; dirty; pass; tdd _(id: [rec-2d90d015-36ae-4873-a6d1-98bdecf0a0ec](.artifacts/records/project__check-run/rec-2d90d015-36ae-4873-a6d1-98bdecf0a0ec.md))_

## ag-effort-rollup

### Acceptance
- **ag-effort-rollup**: A fixture of three sessions and two efforts, one session touching both, yields exact per-effort totals with shared and exclusive cost split.; tdd; session-analysis; python3 -m pytest -q tests/test_effort_rollup.py _(id: [rec-d0cbaaf6-d767-45f6-aa4d-f32b9415b6bc](.artifacts/records/project__acceptance/rec-d0cbaaf6-d767-45f6-aa4d-f32b9415b6bc.md))_

### Check
- **ag-effort-rollup**: rec-d0cbaaf6-d767-45f6-aa4d-f32b9415b6bc; dirty; pass; tdd _(id: [rec-2a7118de-ad03-4568-9f13-c9f5b4c3be61](.artifacts/records/project__check-run/rec-2a7118de-ad03-4568-9f13-c9f5b4c3be61.md))_

## ag-outliers

### Acceptance
- **ag-outliers**: A fixture yields the top sessions per metric in the expected order, with references and values only, and fewer than top entries when there are fewer sessions.; tdd; session-analysis; python3 -m pytest -q tests/test_session_outliers.py _(id: [rec-4b4378e7-5443-435e-86ab-02ad515ebb4d](.artifacts/records/project__acceptance/rec-4b4378e7-5443-435e-86ab-02ad515ebb4d.md))_

### Check
- **ag-outliers**: rec-4b4378e7-5443-435e-86ab-02ad515ebb4d; dirty; pass; tdd _(id: [rec-46e8a5f9-0acc-4f97-8a6e-c630b856a816](.artifacts/records/project__check-run/rec-46e8a5f9-0acc-4f97-8a6e-c630b856a816.md))_

## ag-tool-skill-rollup

### Acceptance
- **ag-tool-skill-rollup**: A fixture yields exact per-tool calls, errors, error rate, retries and session counts, and per-skill invocation and session counts, in sorted order.; tdd; session-analysis; python3 -m pytest -q tests/test_tool_skill_rollup.py _(id: [rec-f283ff9c-78e6-439b-ae65-90ef88690304](.artifacts/records/project__acceptance/rec-f283ff9c-78e6-439b-ae65-90ef88690304.md))_

### Check
- **ag-tool-skill-rollup**: rec-f283ff9c-78e6-439b-ae65-90ef88690304; dirty; pass; tdd _(id: [rec-d83cb7ea-fdf5-43ff-963d-6a25570a2de5](.artifacts/records/project__check-run/rec-d83cb7ea-fdf5-43ff-963d-6a25570a2de5.md))_

## approval-confirm-ux

### Acceptance
- **approval-confirm-ux**: From the Needs-you list, d opens detail and does not write; a write requires detail plus confirm; cancel makes no CLI call; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'approval and (detail or confirm or cancel)' _(id: [rec-18701e87-22d6-4a86-add9-8b350996cbcf](.artifacts/records/project__acceptance/rec-18701e87-22d6-4a86-add9-8b350996cbcf.md))_

### Check
- **approval-confirm-ux**: rec-18701e87-22d6-4a86-add9-8b350996cbcf; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; tdd _(id: [rec-18a75883-bd92-4900-ba37-7f83f25bdb57](.artifacts/records/project__check-run/rec-18a75883-bd92-4900-ba37-7f83f25bdb57.md))_

## approval-confirm-ux-actions

### Acceptance
- **approval-confirm-ux-actions**: Plan-review Approve/Reject, manual Sign, and finding Accept risk behave as specified with note rules; Reject keeps the question open; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'approval and (approve or reject or sign or accept)' _(id: [rec-cfce9c2b-44e5-4324-913a-5bb887a7aa33](.artifacts/records/project__acceptance/rec-cfce9c2b-44e5-4324-913a-5bb887a7aa33.md))_

### Check
- **approval-confirm-ux-actions**: rec-cfce9c2b-44e5-4324-913a-5bb887a7aa33; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; tdd _(id: [rec-c31a38af-f997-4e0f-aee3-c5a16df0102f](.artifacts/records/project__check-run/rec-c31a38af-f997-4e0f-aee3-c5a16df0102f.md))_

## approval-confirm-ux-readme

### Acceptance
- **approval-confirm-ux-readme**: README key table documents detail-first d, confirm actions (Approve/Reject/Sign/Accept risk), and note rules; check; workflow-loop; grep -E 'Approve|Reject|Accept risk|Sign' README.md && grep -E 'Needs you|dismiss|confirm' README.md _(id: [rec-454294d0-2d0a-4652-92d3-ddfd22b795fd](.artifacts/records/project__acceptance/rec-454294d0-2d0a-4652-92d3-ddfd22b795fd.md))_

### Check
- **approval-confirm-ux-readme**: rec-454294d0-2d0a-4652-92d3-ddfd22b795fd; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; check _(id: [rec-bfbc3223-705a-45cc-b668-1664a79619e1](.artifacts/records/project__check-run/rec-bfbc3223-705a-45cc-b668-1664a79619e1.md))_

## approval-constraints

### Acceptance
- **approval-constraints**: dashboard-human-gate-writes is active with the human-gate write statement; no active constraint still claims the dashboard never writes; the three former read-only subjects are retired pointers to dashboard-human-gate-writes; check; workflow-loop; /home/andrewyin/adaptive-artifacts/bin/adaptive-artifacts --store /home/andrewyin/se-workflow/.artifacts list --type project:constraint --state active | python3 -c "import sys,json; d=json.load(sys.stdin); stmts=[(r['subject'], (r.get('payload') or {}).get('statement') or '') for r in d['records']]; assert any(s=='dashboard-human-gate-writes' for s,_ in stmts); hg=[t for s,t in stmts if s=='dashboard-human-gate-writes']; assert hg and ('human Needs-you' in hg[0] or 'human-gate' in hg[0].lower()); old={'dashboard-read-only','dashboard-read-only-dashboard-bugfix','dashboard-read-only-dashboard-features'}; assert not any('never writes' in t.lower() for s,t in stmts if s in old); assert all('Retired' in t or 'dashboard-human-gate-writes' in t for s,t in stmts if s in old)" _(id: [rec-7927a6c7-eea1-4224-b9a1-9d4800dce4b0](.artifacts/records/project__acceptance/rec-7927a6c7-eea1-4224-b9a1-9d4800dce4b0.md))_

### Check
- **approval-constraints**: rec-7927a6c7-eea1-4224-b9a1-9d4800dce4b0; dirty; pass; check _(id: [rec-da95e0a2-c3d9-4062-99f0-7d1b309b6a40](.artifacts/records/project__check-run/rec-da95e0a2-c3d9-4062-99f0-7d1b309b6a40.md))_

## approval-contract

### Acceptance
- **approval-contract**: Bundled contract resolves with optional answer, signed_note, and resolution_note on the gate types; skill↔contract consistency and contract self-consistency tests pass; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_contract_self_consistency.py -q -k approval_optional_payload_note_fields _(id: [rec-de3c1982-720c-4be7-90ef-54f23b74e65e](.artifacts/records/project__acceptance/rec-de3c1982-720c-4be7-90ef-54f23b74e65e.md))_

### Check
- **approval-contract**: rec-de3c1982-720c-4be7-90ef-54f23b74e65e; 74bd9a1d9af382217e652fb4eb3f7a23fb61a25d; pass; tdd _(id: [rec-03aaea29-4322-4cbd-a60e-77bed891d77c](.artifacts/records/project__check-run/rec-03aaea29-4322-4cbd-a60e-77bed891d77c.md))_
- **approval-contract**: rec-de3c1982-720c-4be7-90ef-54f23b74e65e; 99072b992cdbd1c45a11081d940de72e61022d3b; fail; tdd _(id: [rec-6e29f579-2087-4eb7-b762-3fb53abd21a4](.artifacts/records/project__check-run/rec-6e29f579-2087-4eb7-b762-3fb53abd21a4.md))_
- **approval-contract**: rec-de3c1982-720c-4be7-90ef-54f23b74e65e; 74bd9a1d9af382217e652fb4eb3f7a23fb61a25d; pass; tdd _(id: [rec-706b4c15-8743-4096-a7e7-23bdba2bd25d](.artifacts/records/project__check-run/rec-706b4c15-8743-4096-a7e7-23bdba2bd25d.md))_
- **approval-contract**: rec-de3c1982-720c-4be7-90ef-54f23b74e65e; 99072b992cdbd1c45a11081d940de72e61022d3b; pass; tdd _(id: [rec-970a0b83-b87f-4de8-a07c-dc081ef1c1e4](.artifacts/records/project__check-run/rec-970a0b83-b87f-4de8-a07c-dc081ef1c1e4.md))_

## approval-dismiss

### Acceptance
- **approval-dismiss**: dismiss_command uses displayed revision (never @current); Approve/Sign/Accept-risk payloads include note fields when provided; Reject creates a needs:human finding and does not answer the continuity-question; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py tests/test_dashboard_model.py -q -k 'approval and (dismiss or revision or reject)' _(id: [rec-6709bf08-2353-479f-ae3d-993edd2c640c](.artifacts/records/project__acceptance/rec-6709bf08-2353-479f-ae3d-993edd2c640c.md))_

### Check
- **approval-dismiss**: rec-6709bf08-2353-479f-ae3d-993edd2c640c; 83a192e629165f9377c23943ea7088c2ce53e3e4; pass; tdd _(id: [rec-d5d8e1a2-38b3-41a6-ad24-a3547b8c4d9e](.artifacts/records/project__check-run/rec-d5d8e1a2-38b3-41a6-ad24-a3547b8c4d9e.md))_

## approval-dismiss-stale

### Acceptance
- **approval-dismiss-stale**: When the CLI rejects a stale expected-revision, dismiss raises a clear error and does not retry with @current; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'approval and stale' _(id: [rec-5acd72b1-7099-4efa-a8b1-ac7f5c99ebd1](.artifacts/records/project__acceptance/rec-5acd72b1-7099-4efa-a8b1-ac7f5c99ebd1.md))_

### Check
- **approval-dismiss-stale**: rec-5acd72b1-7099-4efa-a8b1-ac7f5c99ebd1; 83a192e629165f9377c23943ea7088c2ce53e3e4; pass; tdd _(id: [rec-9071df4e-a52b-459d-81c4-e36f196f16da](.artifacts/records/project__check-run/rec-9071df4e-a52b-459d-81c4-e36f196f16da.md))_

## as-cost-null

### Acceptance
- **as-cost-null**: Every session whose transcript has a cost-state line with a numeric cost reports a non-null cost_usd, and a regression test covers the cause.; tdd; session-analysis; python3 -m pytest -q tests/test_session_fields.py _(id: [rec-36001c1e-b274-4757-b5b3-44fd1a44e292](.artifacts/records/project__acceptance/rec-36001c1e-b274-4757-b5b3-44fd1a44e292.md))_

### Check
- **as-cost-null**: rec-36001c1e-b274-4757-b5b3-44fd1a44e292; dirty; pass; tdd _(id: [rec-cdcd7553-bfa6-4461-8cc7-fb0bce6b615c](.artifacts/records/project__check-run/rec-cdcd7553-bfa6-4461-8cc7-fb0bce6b615c.md))_

### Finding
- **as-cost-null**: Null cost_usd on 140 of 247 sessions is a data gap: those transcripts have no cost-state line, so cost totals are a lower bound over 107 sessions.; Streamed all 140 null transcripts: 0 cost-state lines and 0 cost-named keys. The 107 non-null sessions parse correctly.; Claude Code starts writing cost-state lines for more sessions, or a different cost field appears in transcripts.; none _(id: [rec-8aa9b9e5-9088-4e73-a8ec-facffa2d3833](.artifacts/records/project__finding/rec-8aa9b9e5-9088-4e73-a8ec-facffa2d3833.md))_

## as-dry-run

### Acceptance
- **as-dry-run**: The dry run lists candidates that each cite a metric and a session reference, and the user accepts the list.; manual; session-analysis _(id: [rec-2fa1b9d2-53f0-4a38-bc7f-ace90efeb566](.artifacts/records/project__acceptance/rec-2fa1b9d2-53f0-4a38-bc7f-ace90efeb566.md))_

### Check
- **as-dry-run**: rec-2fa1b9d2-53f0-4a38-bc7f-ace90efeb566; dirty; pass; manual _(id: [rec-23dbd684-3ad1-481e-ac44-afd9f4a53263](.artifacts/records/project__check-run/rec-23dbd684-3ad1-481e-ac44-afd9f4a53263.md))_
- **as-dry-run**: rec-2fa1b9d2-53f0-4a38-bc7f-ace90efeb566; dirty; pass; manual; Andrew Yin _(id: [rec-37f7dd93-e369-4875-9188-d90fef4007c4](.artifacts/records/project__check-run/rec-37f7dd93-e369-4875-9188-d90fef4007c4.md))_
- **as-dry-run**: rec-2fa1b9d2-53f0-4a38-bc7f-ace90efeb566; dirty; pass; manual; andrewyin _(id: [rec-e3de74ac-ae4b-4d14-8bd4-af486373d840](.artifacts/records/project__check-run/rec-e3de74ac-ae4b-4d14-8bd4-af486373d840.md))_

### Finding
- **as-dry-run**: The analyze-sessions skill yields 4 specific, metric-backed candidates on real data, but it lacks rules the agent had to guess: temp directory, pattern and noise, severity, and tool-level session ids.; Dry run over 243 sessions: 4 candidates each with a metric, session references and a target; 4 patterns dropped; 6 of 7 done-when criteria met (step 7 deferred to the caller). I re-checked the Bash, jira_create_issue and error-outlier numbers against a fresh run and they match.; SKILL.md defines the missing rules and a second dry run needs no manual report.jsonl lookups.; none _(id: [rec-1e84d081-a11f-4cf3-b588-672c9f99d52b](.artifacts/records/project__finding/rec-1e84d081-a11f-4cf3-b588-672c9f99d52b.md))_

## as-dry-run-rerun

### Finding
- **as-dry-run-rerun**: After the rules fix the skill needs no guessed rules for pattern, noise, severity or tool-level session references, but two gaps remain: project identity for worktree paths, and candidate edits that need a transcript read.; Second dry run over 243 sessions: 2 candidates with full session ids and targets, 2 patterns dropped, 1 noise session. The agent named remaining gaps: worktree project strings, double counting of slots across patterns, edits that cannot be named from metrics, cost outliers with empty efforts have no target, cross-repo fix locations.; SKILL.md and targets.md state the project-identity, double counting, evidence-needed and cross-repo rules and a third run needs no guesses.; none _(id: [rec-b393a226-8a19-4952-abff-ecfaf8532b8b](.artifacts/records/project__finding/rec-b393a226-8a19-4952-abff-ecfaf8532b8b.md))_

## as-skill

### Acceptance
- **as-skill**: SKILL.md has name and a user-invoked flag, names both scripts at paths that exist, links targets.md, has no store-writing command, stays under 80 lines, and the skill contract consistency test passes.; tdd; session-analysis; python3 -m pytest -q tests/test_analyze_sessions_skill.py tests/test_skill_contract_consistency.py _(id: [rec-d186eb9e-852f-4f75-96aa-313e576c0f8b](.artifacts/records/project__acceptance/rec-d186eb9e-852f-4f75-96aa-313e576c0f8b.md))_

### Check
- **as-skill**: rec-d186eb9e-852f-4f75-96aa-313e576c0f8b; dirty; pass; tdd _(id: [rec-f0d0b94f-0628-4826-a559-1d534622f347](.artifacts/records/project__check-run/rec-f0d0b94f-0628-4826-a559-1d534622f347.md))_

## as-skill-rules

### Acceptance
- **as-skill-rules**: SKILL.md defines the temp directory, pattern, noise, severity, tool-level session references and bounded slices, stays under 80 lines, and the skill tests and the skill contract consistency test pass.; tdd; session-analysis; python3 -m pytest -q tests/test_analyze_sessions_skill.py tests/test_skill_contract_consistency.py _(id: [rec-f0c76da5-b91f-4660-bcc7-e221a00ac3e8](.artifacts/records/project__acceptance/rec-f0c76da5-b91f-4660-bcc7-e221a00ac3e8.md))_

### Check
- **as-skill-rules**: rec-f0c76da5-b91f-4660-bcc7-e221a00ac3e8; dirty; pass; tdd _(id: [rec-9b88c13a-abba-4c98-ba93-556c2280ccaa](.artifacts/records/project__check-run/rec-9b88c13a-abba-4c98-ba93-556c2280ccaa.md))_

## as-targets

### Acceptance
- **as-targets**: targets.md has one section per target and each section lists at least one pattern whose metric field names all exist in the real aggregate output.; tdd; session-analysis; python3 -m pytest -q tests/test_analyze_sessions_targets.py _(id: [rec-9c15a1e4-c392-4ce0-8482-7bea7dd7f367](.artifacts/records/project__acceptance/rec-9c15a1e4-c392-4ce0-8482-7bea7dd7f367.md))_

### Check
- **as-targets**: rec-9c15a1e4-c392-4ce0-8482-7bea7dd7f367; dirty; pass; tdd _(id: [rec-aeb76e26-4633-45f2-8afb-47c8a383a79c](.artifacts/records/project__check-run/rec-aeb76e26-4633-45f2-8afb-47c8a383a79c.md))_

## assess-route

### Acceptance
- **assess-route**: verify-work keeps level and next off the check-run, raises implementation to design only when a repeat adds no evidence, and writes release ready only when every requirement is verified. test_assess_routing.py passes.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_assess_routing.py -q _(id: [rec-fb7cdbf9-8de6-4066-a413-41f688ed3792](.artifacts/records/project__acceptance/rec-fb7cdbf9-8de6-4066-a413-41f688ed3792.md))_

### Check
- **assess-route**: rec-fb7cdbf9-8de6-4066-a413-41f688ed3792; dirty; pass; check _(id: [rec-41c4aff8-877d-449c-8d7d-a9f99470d5ac](.artifacts/records/project__check-run/rec-41c4aff8-877d-449c-8d7d-a9f99470d5ac.md))_

## backlog-lifecycle

### Acceptance
- **backlog-lifecycle**: Through adaptive-artifacts CLI on a seeded store, create open backlog-item with effort, list it by status=open, and reject create without effort; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_backlog_item.py -q _(id: [rec-fc666597-85d7-42c1-a7e9-3f67d996e0c2](.artifacts/records/project__acceptance/rec-fc666597-85d7-42c1-a7e9-3f67d996e0c2.md))_

### Check
- **backlog-lifecycle**: rec-fc666597-85d7-42c1-a7e9-3f67d996e0c2; 0f7181ef59251f8135db5a71258471f92a972e7c; pass; tdd _(id: [rec-2dd9b20c-e93b-47b5-bd83-b464826e2221](.artifacts/records/project__check-run/rec-2dd9b20c-e93b-47b5-bd83-b464826e2221.md))_

## backlog-lifecycle-promote

### Acceptance
- **backlog-lifecycle-promote**: Promote and dismiss paths use backlog-item supersede, not feedback; feedback create/list still works as an observation signal; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_backlog_item.py -q _(id: [rec-a19b9909-b798-4b7d-a0e1-c2eac876dc42](.artifacts/records/project__acceptance/rec-a19b9909-b798-4b7d-a0e1-c2eac876dc42.md))_

### Check
- **backlog-lifecycle-promote**: rec-a19b9909-b798-4b7d-a0e1-c2eac876dc42; 0f7181ef59251f8135db5a71258471f92a972e7c; pass; tdd _(id: [rec-9c7db177-6ef9-41d0-87e7-c2d124d1cd8d](.artifacts/records/project__check-run/rec-9c7db177-6ef9-41d0-87e7-c2d124d1cd8d.md))_

## backlog-lifecycle-status

### Acceptance
- **backlog-lifecycle-status**: CLI supersede to promoted and dismissed removes items from open lists while leaving active successors with the new status; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_backlog_item.py -q _(id: [rec-f5bbe8ab-d0e6-4929-9293-f23518096569](.artifacts/records/project__acceptance/rec-f5bbe8ab-d0e6-4929-9293-f23518096569.md))_

### Check
- **backlog-lifecycle-status**: rec-f5bbe8ab-d0e6-4929-9293-f23518096569; 0f7181ef59251f8135db5a71258471f92a972e7c; pass; tdd _(id: [rec-a90020f0-ba81-4c5a-8b9a-ed62eb58e42d](.artifacts/records/project__check-run/rec-a90020f0-ba81-4c5a-8b9a-ed62eb58e42d.md))_

## budget-instructions

### Acceptance
- **budget-instructions**: plan-phase writes verification acceptances from the phase exit criteria, including one integration check through the real entry point; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_budget.py -q -k plan_phase_limits _(id: [rec-b147b60a-bac3-473f-bff5-6ea8db7fe2e9](.artifacts/records/project__acceptance/rec-b147b60a-bac3-473f-bff5-6ea8db7fe2e9.md))_

### Check
- **budget-instructions**: rec-b147b60a-bac3-473f-bff5-6ea8db7fe2e9; dirty; pass; tdd _(id: [rec-6d98b2c8-3812-46a3-9f47-2fc4de4481b3](.artifacts/records/project__check-run/rec-6d98b2c8-3812-46a3-9f47-2fc4de4481b3.md))_
- **budget-instructions**: rec-b147b60a-bac3-473f-bff5-6ea8db7fe2e9; dirty; pass; tdd _(id: [rec-9c88f0a0-58dd-430d-a412-71eb101b857a](.artifacts/records/project__check-run/rec-9c88f0a0-58dd-430d-a412-71eb101b857a.md))_
- **budget-instructions**: rec-b147b60a-bac3-473f-bff5-6ea8db7fe2e9; dirty; fail; tdd _(id: [rec-e1f51bc9-28f4-4b19-8688-95beb25889da](.artifacts/records/project__check-run/rec-e1f51bc9-28f4-4b19-8688-95beb25889da.md))_

## budget-instructions-close

### Acceptance
- **budget-instructions-close**: AGENTS.md and CLAUDE.md tell a task to run its verify_command and do not tell it to run the full suite before close; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_budget.py -q -k close_instructions _(id: [rec-a12edd10-9c55-4760-b80f-7fc1177203da](.artifacts/records/project__acceptance/rec-a12edd10-9c55-4760-b80f-7fc1177203da.md))_

### Check
- **budget-instructions-close**: rec-a12edd10-9c55-4760-b80f-7fc1177203da; dirty; fail; tdd _(id: [rec-3159ba4a-f165-4735-af54-c4cdcfde42c7](.artifacts/records/project__check-run/rec-3159ba4a-f165-4735-af54-c4cdcfde42c7.md))_
- **budget-instructions-close**: rec-a12edd10-9c55-4760-b80f-7fc1177203da; dirty; pass; tdd _(id: [rec-c6f6deee-7dc9-4fc4-84fb-5eacb6fd6fe2](.artifacts/records/project__check-run/rec-c6f6deee-7dc9-4fc4-84fb-5eacb6fd6fe2.md))_

## budget-instructions-filter

### Acceptance
- **budget-instructions-filter**: plan-phase rejects a verification command that runs the whole tests tree or tests/test_dashboard_app.py without a -k filter for this phase; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_budget.py -q -k rejects_whole_suite _(id: [rec-61d66067-90f5-4d51-b24b-0afb76d408d1](.artifacts/records/project__acceptance/rec-61d66067-90f5-4d51-b24b-0afb76d408d1.md))_

### Check
- **budget-instructions-filter**: rec-61d66067-90f5-4d51-b24b-0afb76d408d1; dirty; fail; tdd _(id: [rec-8e14fedd-1a87-4a4e-be22-58e54814ed18](.artifacts/records/project__check-run/rec-8e14fedd-1a87-4a4e-be22-58e54814ed18.md))_
- **budget-instructions-filter**: rec-61d66067-90f5-4d51-b24b-0afb76d408d1; dirty; pass; tdd _(id: [rec-db43ba29-89a6-4655-b28b-22924b54d289](.artifacts/records/project__check-run/rec-db43ba29-89a6-4655-b28b-22924b54d289.md))_

## budget-instructions-stop

### Acceptance
- **budget-instructions-stop**: A failing verification returns fail without editing, and verify-work leaves the work-item in progress with assessment next execute; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_budget.py -q -k verification_failure _(id: [rec-4c85a8d1-dde4-448b-bfe6-aee86654a15e](.artifacts/records/project__acceptance/rec-4c85a8d1-dde4-448b-bfe6-aee86654a15e.md))_

### Check
- **budget-instructions-stop**: rec-4c85a8d1-dde4-448b-bfe6-aee86654a15e; dirty; pass; tdd _(id: [rec-0c637640-3452-4958-b7df-c94c2c43ca43](.artifacts/records/project__check-run/rec-0c637640-3452-4958-b7df-c94c2c43ca43.md))_
- **budget-instructions-stop**: rec-4c85a8d1-dde4-448b-bfe6-aee86654a15e; dirty; pass; tdd _(id: [rec-5a6a0868-84bc-4a9f-bc50-5d2304feb0dd](.artifacts/records/project__check-run/rec-5a6a0868-84bc-4a9f-bc50-5d2304feb0dd.md))_
- **budget-instructions-stop**: rec-4c85a8d1-dde4-448b-bfe6-aee86654a15e; dirty; fail; tdd _(id: [rec-ef3f591d-b275-455e-b7eb-4b4e227cdbc1](.artifacts/records/project__check-run/rec-ef3f591d-b275-455e-b7eb-4b4e227cdbc1.md))_

## check-run-contract

### Acceptance
- **check-run-contract**: Bundled contract declares enums for check-run.result and check-run/acceptance method, lists the optional runner fields, and contract self-consistency plus the flipped evidence-loop/assess-routing tests pass; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_contract_self_consistency.py tests/test_evidence_loop.py tests/test_assess_routing.py -q -k 'enum or result or method or contract' _(id: [rec-88363d0c-d058-4a0d-8c04-4a697bbe457d](.artifacts/records/project__acceptance/rec-88363d0c-d058-4a0d-8c04-4a697bbe457d.md))_

### Check
- **check-run-contract**: rec-88363d0c-d058-4a0d-8c04-4a697bbe457d; 16c24e78d806d5207ee2c37a9418e828521f8389; pass; tdd _(id: [rec-06babb10-72f2-4c7c-8ef8-285ebdef0f15](.artifacts/records/project__check-run/rec-06babb10-72f2-4c7c-8ef8-285ebdef0f15.md))_

## claude-shared-marketplace

### Acceptance
- **claude-shared-marketplace**: plugin.json declares adaptive-artifacts in dependencies and marketplace.json lists both plugins with AA via github source; claude plugin validate . exits 0; check; packaging; claude plugin validate . && python3 -c "import json;p=json.load(open('.claude-plugin/plugin.json'));d=p.get('dependencies',[]);assert 'adaptive-artifacts' in d or any(isinstance(x,dict) and x.get('name')=='adaptive-artifacts' for x in d);m=json.load(open('.claude-plugin/marketplace.json'));assert {x.get('name') for x in m['plugins']}>= {'se-workflow','adaptive-artifacts'}" _(id: [rec-a60c0f0a-abb6-4cfe-b569-657d0edb4722](.artifacts/records/project__acceptance/rec-a60c0f0a-abb6-4cfe-b569-657d0edb4722.md))_

### Check
- **claude-shared-marketplace**: rec-a60c0f0a-abb6-4cfe-b569-657d0edb4722; 40db2970236ac7ff04afd9eaf08292f072a912a2; pass; check _(id: [rec-133596a3-9698-4c2b-aeaa-ae7ab76e82f5](.artifacts/records/project__check-run/rec-133596a3-9698-4c2b-aeaa-ae7ab76e82f5.md))_

## claude-shared-marketplace-readme

### Acceptance
- **claude-shared-marketplace-readme**: README Claude install uses a single marketplace add for se-workflow; Cursor subsection does not claim dependency auto-install; check; packaging; grep -q 'claude plugin marketplace add andrewy1n/se-workflow' README.md && grep -qi Cursor README.md && ! grep -qiE 'Cursor.*(auto-?install|plugin dependenc).*adaptive-artifacts' README.md _(id: [rec-49384b6f-6de8-4e22-b43c-f27f3e8f06ad](.artifacts/records/project__acceptance/rec-49384b6f-6de8-4e22-b43c-f27f3e8f06ad.md))_

### Check
- **claude-shared-marketplace-readme**: rec-49384b6f-6de8-4e22-b43c-f27f3e8f06ad; 40db2970236ac7ff04afd9eaf08292f072a912a2; pass; check _(id: [rec-afd46d92-057c-4b40-8961-34c19871e95d](.artifacts/records/project__check-run/rec-afd46d92-057c-4b40-8961-34c19871e95d.md))_

## close-batch-cli

### Acceptance
- **close-batch-cli**: bin/se-workflow close-batch builds NDJSON batches and preserves red-first refusal exit codes through the CLI entry; tdd; packaging; uv run --with pytest python -m pytest tests/test_close_batch.py -q _(id: [rec-45b51bb0-0c79-4f85-9120-374742d1d297](.artifacts/records/project__acceptance/rec-45b51bb0-0c79-4f85-9120-374742d1d297.md))_

### Check
- **close-batch-cli**: rec-45b51bb0-0c79-4f85-9120-374742d1d297; dirty; fail; tdd _(id: [rec-644ce7a2-d954-465f-bb8c-f2899f253d92](.artifacts/records/project__check-run/rec-644ce7a2-d954-465f-bb8c-f2899f253d92.md))_
- **close-batch-cli**: rec-45b51bb0-0c79-4f85-9120-374742d1d297; 23c6f922d2a051135dc323f67924f2364b3788db; pass; tdd _(id: [rec-7637c340-cead-4240-9940-0a3c34093d3f](.artifacts/records/project__check-run/rec-7637c340-cead-4240-9940-0a3c34093d3f.md))_

## close-red-first

### Acceptance
- **close-red-first**: close_batch refuses pass-only tdd done without finding (exit 2, criterion named) and accepts fail→pass when red precedes green by git ancestry or dirty red with diff_sha256; wrong order/non-ancestor refused; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k red_first _(id: [rec-e7b02db3-cbf8-492f-8363-9844982d7753](.artifacts/records/project__acceptance/rec-e7b02db3-cbf8-492f-8363-9844982d7753.md))_

### Check
- **close-red-first**: rec-e7b02db3-cbf8-492f-8363-9844982d7753; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-518b386e-aa2c-42c3-a539-a7d1220f7051](.artifacts/records/project__check-run/rec-518b386e-aa2c-42c3-a539-a7d1220f7051.md))_
- **close-red-first**: rec-e7b02db3-cbf8-492f-8363-9844982d7753; 54181564b74027f0ec23a402a44df7dc009d42d2; pass; tdd _(id: [rec-7f23ed3b-5645-4eb2-a0e0-5378ea9acb2d](.artifacts/records/project__check-run/rec-7f23ed3b-5645-4eb2-a0e0-5378ea9acb2d.md))_

## close-red-first-escape

### Acceptance
- **close-red-first-escape**: Finding escape permits tdd done without red and forces needs human; check and manual criteria close without red_check_run_id; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k 'red_first_escape or red_first_other_methods' _(id: [rec-c8b5c4cd-99a6-4906-a91c-7b4385187029](.artifacts/records/project__acceptance/rec-c8b5c4cd-99a6-4906-a91c-7b4385187029.md))_

### Check
- **close-red-first-escape**: rec-c8b5c4cd-99a6-4906-a91c-7b4385187029; 54181564b74027f0ec23a402a44df7dc009d42d2; pass; tdd _(id: [rec-33825f2d-fc44-4516-905b-51032ccb78e2](.artifacts/records/project__check-run/rec-33825f2d-fc44-4516-905b-51032ccb78e2.md))_
- **close-red-first-escape**: rec-c8b5c4cd-99a6-4906-a91c-7b4385187029; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-eccd7ba2-0282-4e31-91bf-ef3c74080e73](.artifacts/records/project__check-run/rec-eccd7ba2-0282-4e31-91bf-ef3c74080e73.md))_

## close-red-first-methods

### Acceptance
- **close-red-first-methods**: check and manual done closes succeed without red_check_run_id; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k red_first_other_methods _(id: [rec-20f81a2f-2df9-4e5d-9eec-63da3defeec3](.artifacts/records/project__acceptance/rec-20f81a2f-2df9-4e5d-9eec-63da3defeec3.md))_

### Check
- **close-red-first-methods**: rec-20f81a2f-2df9-4e5d-9eec-63da3defeec3; 54181564b74027f0ec23a402a44df7dc009d42d2; pass; tdd _(id: [rec-7d303292-39e4-4fd7-b485-dc88c66ad0bb](.artifacts/records/project__check-run/rec-7d303292-39e4-4fd7-b485-dc88c66ad0bb.md))_
- **close-red-first-methods**: rec-20f81a2f-2df9-4e5d-9eec-63da3defeec3; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-bc6eeb64-10b5-4bca-a8d0-6b0d84553830](.artifacts/records/project__check-run/rec-bc6eeb64-10b5-4bca-a8d0-6b0d84553830.md))_

## close-red-first-order

### Acceptance
- **close-red-first-order**: Green SHA must be equal to or git-descendant of red SHA; dirty red accepted only with non-empty diff_sha256; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k red_first_order _(id: [rec-6e4d8f33-f843-4db1-a990-e3c5ea1abbd7](.artifacts/records/project__acceptance/rec-6e4d8f33-f843-4db1-a990-e3c5ea1abbd7.md))_

### Check
- **close-red-first-order**: rec-6e4d8f33-f843-4db1-a990-e3c5ea1abbd7; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-22236a02-24dc-4d28-8d2c-c5fed9959b77](.artifacts/records/project__check-run/rec-22236a02-24dc-4d28-8d2c-c5fed9959b77.md))_
- **close-red-first-order**: rec-6e4d8f33-f843-4db1-a990-e3c5ea1abbd7; 54181564b74027f0ec23a402a44df7dc009d42d2; pass; tdd _(id: [rec-5e39adba-823f-401d-ba69-558b1eba100d](.artifacts/records/project__check-run/rec-5e39adba-823f-401d-ba69-558b1eba100d.md))_

## close-red-first-request

### Acceptance
- **close-red-first-request**: close_batch validates request-carried red_check_run_id and copied red fields; it does not query the store for prior check-runs; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k red_first_request _(id: [rec-be6e5c30-7b5f-44e1-b497-7dcbccbea6ad](.artifacts/records/project__acceptance/rec-be6e5c30-7b5f-44e1-b497-7dcbccbea6ad.md))_

### Check
- **close-red-first-request**: rec-be6e5c30-7b5f-44e1-b497-7dcbccbea6ad; 54181564b74027f0ec23a402a44df7dc009d42d2; pass; tdd _(id: [rec-1ba03e59-6710-4afc-bafd-05f0555f3d77](.artifacts/records/project__check-run/rec-1ba03e59-6710-4afc-bafd-05f0555f3d77.md))_
- **close-red-first-request**: rec-be6e5c30-7b5f-44e1-b497-7dcbccbea6ad; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-6c63bc4a-319f-4ba9-9412-c689022b6183](.artifacts/records/project__check-run/rec-6c63bc4a-319f-4ba9-9412-c689022b6183.md))_

## close-step-skill

### Acceptance
- **close-step-skill**: execute-phase documents the close step with a payload the contract accepts; skill/contract consistency tests pass; tdd; workflow-loop; python3 -m pytest tests/test_skill_contract_consistency.py -q _(id: [rec-8bcac210-20bd-42a8-b0ea-953bd412937a](.artifacts/records/project__acceptance/rec-8bcac210-20bd-42a8-b0ea-953bd412937a.md))_

### Check
- **close-step-skill**: rec-8bcac210-20bd-42a8-b0ea-953bd412937a; 8f1c9bbbb89ef3dc90f3fa36d00c83b924f2a721; pass; tdd _(id: [rec-624fc8c3-8603-42f5-b7bb-ab21d051cbc3](.artifacts/records/project__check-run/rec-624fc8c3-8603-42f5-b7bb-ab21d051cbc3.md))_

## column-resize

### Acceptance
- **column-resize**: Resize 120 to 60 columns: the table shows status, task, wave with no reload; resize back: phase and assignee return; the test fails before the fix; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k resize _(id: [rec-4b32e614-7d7e-4a55-be85-301c98fe6ef9](.artifacts/records/project__acceptance/rec-4b32e614-7d7e-4a55-be85-301c98fe6ef9.md))_

### Check
- **column-resize**: rec-4b32e614-7d7e-4a55-be85-301c98fe6ef9; b104980765db3920237082612a4d1aa5eda6a5b7; pass; tdd _(id: [rec-92efe161-3980-4dc2-b0ce-32eca9e0f501](.artifacts/records/project__check-run/rec-92efe161-3980-4dc2-b0ce-32eca9e0f501.md))_

### Observation
- **column-resize**: On resize, DashboardApp.on_resize runs before App.size updates, so paint() used the old width; EffortPane.on_resize replayed the stored stale width. Columns stayed wide until reload.; dashboard-bugfix _(id: [rec-c526251e-c035-426f-abf2-b9604030e7fa](.artifacts/records/project__investigation-observation/rec-c526251e-c035-426f-abf2-b9604030e7fa.md))_

## commit-stat-width

### Acceptance
- **commit-stat-width**: A pilot test at 60 and 80 columns shows every stat line of a commit with a long path on one line; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q _(id: [rec-de68bee3-9f99-4495-8545-8aa7b453e373](.artifacts/records/project__acceptance/rec-de68bee3-9f99-4495-8545-8aa7b453e373.md))_

### Check
- **commit-stat-width**: rec-de68bee3-9f99-4495-8545-8aa7b453e373; da2d120; pass; tdd _(id: [rec-b7acff16-1849-4e7f-a841-2a9bd821afd0](.artifacts/records/project__check-run/rec-b7acff16-1849-4e7f-a841-2a9bd821afd0.md))_

## contract-backlog

### Acceptance
- **contract-backlog**: The bundled contract resolves project:backlog-item as current-status with status open|promoted|dismissed and effort required, still resolves project:feedback, and a generic create/read of backlog-item validates; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_contract_self_consistency.py -q _(id: [rec-23b30985-3712-43f6-b1e4-f9240d9a632c](.artifacts/records/project__acceptance/rec-23b30985-3712-43f6-b1e4-f9240d9a632c.md))_

### Check
- **contract-backlog**: rec-23b30985-3712-43f6-b1e4-f9240d9a632c; 150d4cf3ea0e2c0d34718cc9645613ed33a8430b; pass; check _(id: [rec-131906fa-23a5-4e07-9669-db912f63c0e2](.artifacts/records/project__check-run/rec-131906fa-23a5-4e07-9669-db912f63c0e2.md))_

## contract-backlog-effort

### Acceptance
- **contract-backlog-effort**: backlog-item payload requires effort; optional source and phase are declared; create without effort fails validation; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_contract_self_consistency.py -q _(id: [rec-1686fb83-3253-4571-8f6d-9b927f916c77](.artifacts/records/project__acceptance/rec-1686fb83-3253-4571-8f6d-9b927f916c77.md))_

### Check
- **contract-backlog-effort**: rec-1686fb83-3253-4571-8f6d-9b927f916c77; 150d4cf3ea0e2c0d34718cc9645613ed33a8430b; pass; check _(id: [rec-3dd98e54-6a65-4576-8783-42412165c962](.artifacts/records/project__check-run/rec-3dd98e54-6a65-4576-8783-42412165c962.md))_

## contract-backlog-status

### Acceptance
- **contract-backlog-status**: backlog-item status enum is open|promoted|dismissed and handoff selects only status equals open; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_contract_self_consistency.py -q _(id: [rec-7f83aff0-87bd-4dfa-9d94-12920f3a46aa](.artifacts/records/project__acceptance/rec-7f83aff0-87bd-4dfa-9d94-12920f3a46aa.md))_

### Check
- **contract-backlog-status**: rec-7f83aff0-87bd-4dfa-9d94-12920f3a46aa; 150d4cf3ea0e2c0d34718cc9645613ed33a8430b; pass; check _(id: [rec-c6be4c30-1d8a-4ecb-968a-7572136c150f](.artifacts/records/project__check-run/rec-c6be4c30-1d8a-4ecb-968a-7572136c150f.md))_

## contract-loop

### Acceptance
- **contract-loop**: The bundled contract resolves specification, design, integration-report, assessment, release, and feedback, and a check-run result of pass still validates.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_contract_self_consistency.py -q _(id: [rec-6d715e64-501c-42c0-b057-42d81bbb01b8](.artifacts/records/project__acceptance/rec-6d715e64-501c-42c0-b057-42d81bbb01b8.md))_

### Check
- **contract-loop**: rec-6d715e64-501c-42c0-b057-42d81bbb01b8; dirty; pass; check _(id: [rec-bc6527c5-0217-413e-a69f-4a2272e61b1d](.artifacts/records/project__check-run/rec-bc6527c5-0217-413e-a69f-4a2272e61b1d.md))_

## copy-and-commit-actions

### Acceptance
- **copy-and-commit-actions**: Pilot tests copy the selected slug from the dashboard and the detail screen, open the commit screen with the message and stat for a task's latest revision in a temp git repo, show a message for a dirty or unknown revision, and return on Esc; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q _(id: [rec-b0782695-b6a8-443a-b1ed-fd39a65b5de8](.artifacts/records/project__acceptance/rec-b0782695-b6a8-443a-b1ed-fd39a65b5de8.md))_

### Check
- **copy-and-commit-actions**: rec-b0782695-b6a8-443a-b1ed-fd39a65b5de8; 9822923; pass; tdd _(id: [rec-fb98930f-0a3a-4841-95db-46f171e68f36](.artifacts/records/project__check-run/rec-fb98930f-0a3a-4841-95db-46f171e68f36.md))_

## dashboard-app

### Acceptance
- **dashboard-app**: A Textual pilot test at 60 and 120 columns finds the goal, progress, tiles, task rows, needs-you items, and activity for a temp store, and sees a redraw after a store change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q _(id: [rec-607927c0-6e77-499d-ae1f-ee7a890cfd07](.artifacts/records/project__acceptance/rec-607927c0-6e77-499d-ae1f-ee7a890cfd07.md))_

### Check
- **dashboard-app**: rec-607927c0-6e77-499d-ae1f-ee7a890cfd07; f84a229; pass; tdd _(id: [rec-3b1bf0ad-45ab-4b9b-8c35-152bc2cd0bad](.artifacts/records/project__check-run/rec-3b1bf0ad-45ab-4b9b-8c35-152bc2cd0bad.md))_

## dashboard-approvals-review

### Check
- **dashboard-approvals-review**: dashboard-approvals-review; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; fail; review _(id: [rec-9b93df93-3d63-4d15-8eb1-f927c1beb724](.artifacts/records/project__check-run/rec-9b93df93-3d63-4d15-8eb1-f927c1beb724.md))_
- **dashboard-approvals-review**: dashboard-approvals-review; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; review _(id: [rec-a1ab248f-9e27-47ac-bce5-f732320cabba](.artifacts/records/project__check-run/rec-a1ab248f-9e27-47ac-bce5-f732320cabba.md))_

## dashboard-backlog

### Acceptance
- **dashboard-backlog**: EffortView / snapshot includes only open backlog-items for that effort; Needs you does not list them; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k backlog _(id: [rec-00466274-876f-4c8b-a54e-a8db1e61fbda](.artifacts/records/project__acceptance/rec-00466274-876f-4c8b-a54e-a8db1e61fbda.md))_

### Check
- **dashboard-backlog**: rec-00466274-876f-4c8b-a54e-a8db1e61fbda; 2ba3f658a6c7a374ef157640f4dd4a3024588e90; pass; tdd _(id: [rec-0adb36e3-2686-4672-81d9-8173f848bb8d](.artifacts/records/project__check-run/rec-0adb36e3-2686-4672-81d9-8173f848bb8d.md))_

## dashboard-backlog-actions

### Acceptance
- **dashboard-backlog-actions**: App pilots: Backlog panel shows open items; promote and dismiss call CLI supersede; promote copies an agent prompt; Needs you unchanged; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k backlog _(id: [rec-644805a3-42e4-4437-8ffc-cd772a363cea](.artifacts/records/project__acceptance/rec-644805a3-42e4-4437-8ffc-cd772a363cea.md))_

### Check
- **dashboard-backlog-actions**: rec-644805a3-42e4-4437-8ffc-cd772a363cea; 2ba3f658a6c7a374ef157640f4dd4a3024588e90; pass; tdd _(id: [rec-4b35e98c-e1c7-4fd6-9afa-664703d80eab](.artifacts/records/project__check-run/rec-4b35e98c-e1c7-4fd6-9afa-664703d80eab.md))_

## dashboard-closed-goals

### Acceptance
- **dashboard-closed-goals**: build_model leaves out an effort whose goal has status closed; tdd; workflow-loop; python3 -m pytest tests/test_dashboard_model.py -q _(id: [rec-f02ec3b2-3bd6-496f-933a-1506d3b4a877](.artifacts/records/project__acceptance/rec-f02ec3b2-3bd6-496f-933a-1506d3b4a877.md))_

### Check
- **dashboard-closed-goals**: rec-f02ec3b2-3bd6-496f-933a-1506d3b4a877; 8f1c9bbbb89ef3dc90f3fa36d00c83b924f2a721; pass; tdd _(id: [rec-d8041aec-d887-49ea-aa27-693636929bb6](.artifacts/records/project__check-run/rec-d8041aec-d887-49ea-aa27-693636929bb6.md))_

## dashboard-dismiss

### Acceptance
- **dashboard-dismiss**: Pilot: dismiss clears a question, a needs:human finding, and an unsigned manual check via CLI and removes them from Needs you; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k dismiss _(id: [rec-3399e692-0dd4-4842-9cb1-3ff2a3f95513](.artifacts/records/project__acceptance/rec-3399e692-0dd4-4842-9cb1-3ff2a3f95513.md))_

### Check
- **dashboard-dismiss**: rec-3399e692-0dd4-4842-9cb1-3ff2a3f95513; 8799ca930443a9a3144434eaf3b9e30e497adbce; pass; tdd _(id: [rec-1067db97-d173-4c6d-9703-51b875bfe369](.artifacts/records/project__check-run/rec-1067db97-d173-4c6d-9703-51b875bfe369.md))_

### Observation
- **dashboard-dismiss**: Needs you list/detail had no dismiss binding and never invoked adaptive-artifacts; workflow-loop _(id: [rec-ad0eb0da-1eac-4d9d-b81a-4b11e16bbe1b](.artifacts/records/project__investigation-observation/rec-ad0eb0da-1eac-4d9d-b81a-4b11e16bbe1b.md))_

### Finding
- **dashboard-dismiss**: Dashboard mirrored open human gates but never dismissed them via adaptive-artifacts CLI; pre-fix UI had no d-dismiss; pilots now pass for clear/refuse/CLI-fail; dismiss pilots fail or dashboard invents a local dismiss cache; none _(id: [rec-02f2b892-db35-4a29-8220-d89cbe33ab4c](.artifacts/records/project__finding/rec-02f2b892-db35-4a29-8220-d89cbe33ab4c.md))_

## dashboard-dismiss-refuse

### Acceptance
- **dashboard-dismiss-refuse**: Pilot: dismiss is refused for merge-branch (and other non-human kinds); CLI failure keeps the item and shows an error; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'dismiss and (refuse or fail or error)' _(id: [rec-76204de3-ed47-4406-9096-db2caa3f9d68](.artifacts/records/project__acceptance/rec-76204de3-ed47-4406-9096-db2caa3f9d68.md))_

### Check
- **dashboard-dismiss-refuse**: rec-76204de3-ed47-4406-9096-db2caa3f9d68; 8799ca930443a9a3144434eaf3b9e30e497adbce; pass; tdd _(id: [rec-232c063c-895e-42a5-b91a-55d0d1a6cad0](.artifacts/records/project__check-run/rec-232c063c-895e-42a5-b91a-55d0d1a6cad0.md))_

## dashboard-launcher

### Acceptance
- **dashboard-launcher**: Given a temp repo: with ~/.artifacts/<repo> it uses that store; with only <repo>/.artifacts it uses that; with none it prints a no-store message; with a store whose contract lacks project:dashboard it prints a missing-view message; ADAPTIVE_ARTIFACTS_BIN overrides the binary; tdd; dashboard; cd ~/se-workflow && python3 -m pytest tests -q _(id: [rec-e4e1b7a5-4c4b-45ce-8a02-bb12452e15ea](.artifacts/records/project__acceptance/rec-e4e1b7a5-4c4b-45ce-8a02-bb12452e15ea.md))_

### Check
- **dashboard-launcher**: rec-e4e1b7a5-4c4b-45ce-8a02-bb12452e15ea; f4cf9dc; pass; tdd _(id: [rec-c4dc7668-a282-42b6-bfa7-6669d2e8e89d](.artifacts/records/project__check-run/rec-c4dc7668-a282-42b6-bfa7-6669d2e8e89d.md))_

## dashboard-launcher-switch

### Acceptance
- **dashboard-launcher-switch**: Launcher and tmux tests pass with scripts/dashboard running the Textual app; tdd; dashboard; python3 -m pytest tests/test_dashboard_launcher.py tests/test_tmux_integration.py -q _(id: [rec-7fbf25bf-c639-424e-a4a2-66a5d640f23a](.artifacts/records/project__acceptance/rec-7fbf25bf-c639-424e-a4a2-66a5d640f23a.md))_

### Check
- **dashboard-launcher-switch**: rec-7fbf25bf-c639-424e-a4a2-66a5d640f23a; 3e52964; pass; tdd _(id: [rec-886e6cd6-162c-4c11-a70f-08b1d3cb20b9](.artifacts/records/project__check-run/rec-886e6cd6-162c-4c11-a70f-08b1d3cb20b9.md))_

## dashboard-snapshot

### Acceptance
- **dashboard-snapshot**: Tests against a temp store show the snapshot groups records per effort and classifies tasks, needs-you items, phase progress, and recent activity correctly; tdd; dashboard; python3 -m pytest tests/test_dashboard_model.py -q _(id: [rec-8f27fb0c-0113-4d37-9083-5f9767e2d6e6](.artifacts/records/project__acceptance/rec-8f27fb0c-0113-4d37-9083-5f9767e2d6e6.md))_

### Check
- **dashboard-snapshot**: rec-8f27fb0c-0113-4d37-9083-5f9767e2d6e6; 1e88c65; pass; tdd _(id: [rec-2bc92ccd-0454-477e-b1db-644874232b6c](.artifacts/records/project__check-run/rec-2bc92ccd-0454-477e-b1db-644874232b6c.md))_

## dashboard-status-segment

### Acceptance
- **dashboard-status-segment**: Against a seeded store the segment prints the correct running, ready and needs-you counts within 1 s; with no store it prints nothing and exits 0; tdd; dashboard; cd ~/se-workflow && python3 -m pytest tests -q _(id: [rec-e7e94ca1-9742-44b2-9fe1-7a014b58ef3d](.artifacts/records/project__acceptance/rec-e7e94ca1-9742-44b2-9fe1-7a014b58ef3d.md))_

### Check
- **dashboard-status-segment**: rec-e7e94ca1-9742-44b2-9fe1-7a014b58ef3d; 79fda7a; pass; tdd _(id: [rec-9b7aa254-a191-4196-a918-8e364893a451](.artifacts/records/project__check-run/rec-9b7aa254-a191-4196-a918-8e364893a451.md))_

## detail-redraw-race

### Acceptance
- **detail-redraw-race**: The root cause is named, and test_detail_screen_redraws_when_the_store_changes passes 30 times in a row alone and in two full-suite runs; check; dashboard; for i in $(seq 30); do uv run --with textual --with pytest python -m pytest 'tests/test_dashboard_app.py::test_detail_screen_redraws_when_the_store_changes' -q || exit 1; done _(id: [rec-c4742568-196f-4b86-89ea-4a12a7490978](.artifacts/records/project__acceptance/rec-c4742568-196f-4b86-89ea-4a12a7490978.md))_

### Check
- **detail-redraw-race**: rec-c4742568-196f-4b86-89ea-4a12a7490978; 03d561c; pass; check _(id: [rec-83577b2a-8ec0-4648-b7d9-2d706b7959bd](.artifacts/records/project__check-run/rec-83577b2a-8ec0-4648-b7d9-2d706b7959bd.md))_

### Observation
- **detail-redraw-race**: test_detail_screen_redraws_when_the_store_changes[size1] failed with NoMatches: No nodes match '#related' on TaskDetailScreen(); 1 of 2 full runs, 1 of 4 isolated runs; earlier it timed out under load in two other full runs; dashboard-ui _(id: [rec-cf05a87a-e78b-48fb-ad15-132bd63bb053](.artifacts/records/project__investigation-observation/rec-cf05a87a-e78b-48fb-ad15-132bd63bb053.md))_

### Finding
- **detail-redraw-race**: The detail screen paint queried #related after awaits without re-checking that the screen was still attached, so a poll-triggered redraw racing teardown raised NoMatches; Traceback apply -> paint query_one(#related) in 5 of 25 loaded runs; 30/30 loaded and 30/30 alone after re-checking is_attached after the awaits; The test fails again with NoMatches after 03d561c; none _(id: [rec-5018f385-7ec4-40ba-9736-d651d7b2af88](.artifacts/records/project__finding/rec-5018f385-7ec4-40ba-9736-d651d7b2af88.md))_

## discuss-skill

### Acceptance
- **discuss-skill**: skills/discuss/SKILL.md exists and every adaptive-artifacts invocation in it passes the skill/contract consistency test; tdd; workflow-loop; python3 -m pytest tests/test_skill_contract_consistency.py tests/test_discuss_skill.py -q _(id: [rec-29f17960-fd84-4c12-9d0b-9589e7b71980](.artifacts/records/project__acceptance/rec-29f17960-fd84-4c12-9d0b-9589e7b71980.md))_

### Check
- **discuss-skill**: rec-29f17960-fd84-4c12-9d0b-9589e7b71980; 8c697bc88db7147f17a058311b0323cd4a191fee; pass; tdd _(id: [rec-94e86670-ccc6-4d19-bc2f-38158169ceeb](.artifacts/records/project__check-run/rec-94e86670-ccc6-4d19-bc2f-38158169ceeb.md))_

## drop-row-waits-on

### Acceptance
- **drop-row-waits-on**: title_cell for a waiting task with unfinished deps has no waits on substring and still ends with the muted size/estimate/executor suffix; tests fail before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_tasks.py -q -k 'title_cell and waits' _(id: [rec-873b510b-7eeb-42da-a7e7-fc83684576e7](.artifacts/records/project__acceptance/rec-873b510b-7eeb-42da-a7e7-fc83684576e7.md))_

### Check
- **drop-row-waits-on**: rec-873b510b-7eeb-42da-a7e7-fc83684576e7; dirty; fail; tdd _(id: [rec-6d8ce709-787d-4d5d-8ecd-d092f017d26b](.artifacts/records/project__check-run/rec-6d8ce709-787d-4d5d-8ecd-d092f017d26b.md))_
- **drop-row-waits-on**: rec-873b510b-7eeb-42da-a7e7-fc83684576e7; 98bcbd8 dirty; pass; tdd _(id: [rec-c7ae8096-95aa-476a-9b82-1e919116029f](.artifacts/records/project__check-run/rec-c7ae8096-95aa-476a-9b82-1e919116029f.md))_

### Observation
- **drop-row-waits-on**: title_cell appended full unclipped waits on list; 8 long deps produced ~157-char title cell at widths 40/60/120; dashboard _(id: [rec-93f80c29-7ff5-4aa8-b53d-c92927d28a82](.artifacts/records/project__investigation-observation/rec-93f80c29-7ff5-4aa8-b53d-c92927d28a82.md))_

### Finding
- **drop-row-waits-on**: title_cell appended an unclipped waits-on dependency list that overflowed and wrapped task rows; code inspection of title_cell plus failing then passing TDD slice; title_cell again appends waits on text or detail loses Depends on links; none _(id: [rec-8a2bc307-f417-4d2f-a4b7-507724e2e977](.artifacts/records/project__finding/rec-8a2bc307-f417-4d2f-a4b7-507724e2e977.md))_

## drop-row-waits-on-detail

### Acceptance
- **drop-row-waits-on-detail**: Task detail for a blocked/waiting task still lists Depends on links for its dependencies after the row note is gone; regression holds; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'detail and (Depends or blocked or waiting)' _(id: [rec-d2f45e59-d643-45ff-97f9-72e4edd0debb](.artifacts/records/project__acceptance/rec-d2f45e59-d643-45ff-97f9-72e4edd0debb.md))_

### Check
- **drop-row-waits-on-detail**: rec-d2f45e59-d643-45ff-97f9-72e4edd0debb; dirty; fail; tdd _(id: [rec-59ffa822-2a79-460f-a77a-65666f6c920d](.artifacts/records/project__check-run/rec-59ffa822-2a79-460f-a77a-65666f6c920d.md))_
- **drop-row-waits-on-detail**: rec-d2f45e59-d643-45ff-97f9-72e4edd0debb; 98bcbd8 dirty; pass; tdd _(id: [rec-ab772415-e0aa-42a0-aa88-2a840c6d2471](.artifacts/records/project__check-run/rec-ab772415-e0aa-42a0-aa88-2a840c6d2471.md))_

## drop-row-waits-on-oneline

### Acceptance
- **drop-row-waits-on-oneline**: A waiting row with several unfinished dependencies stays one line (no waits on, no dependency-driven wrap) at 60 and 120 columns in the app pilot; fails before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'waiting_row' _(id: [rec-171c0948-9d2c-48a5-8622-a063778e21bf](.artifacts/records/project__acceptance/rec-171c0948-9d2c-48a5-8622-a063778e21bf.md))_

### Check
- **drop-row-waits-on-oneline**: rec-171c0948-9d2c-48a5-8622-a063778e21bf; dirty; fail; tdd _(id: [rec-0b41479e-16e0-417c-b615-a9f37fcdc0e1](.artifacts/records/project__check-run/rec-0b41479e-16e0-417c-b615-a9f37fcdc0e1.md))_
- **drop-row-waits-on-oneline**: rec-171c0948-9d2c-48a5-8622-a063778e21bf; 98bcbd8 dirty; pass; tdd _(id: [rec-c9806692-e2a6-4d50-81aa-936e7d9fbaae](.artifacts/records/project__check-run/rec-c9806692-e2a6-4d50-81aa-936e7d9fbaae.md))_

## e2e-real-execute-run

### Acceptance
- **e2e-real-execute-run**: The frame log shows task one go ready, running, done and task two go waiting, ready, running, done, driven by real subagent dispatch; the user signs after reading it; manual; dashboard _(id: [rec-70f9c43d-01d7-438e-8df6-ad97b7fd46ce](.artifacts/records/project__acceptance/rec-70f9c43d-01d7-438e-8df6-ad97b7fd46ce.md))_

### Check
- **e2e-real-execute-run**: rec-70f9c43d-01d7-438e-8df6-ad97b7fd46ce; dirty; pass; manual; ayin _(id: [rec-fd14f0b7-0adc-4394-8deb-14db551d0328](.artifacts/records/project__check-run/rec-fd14f0b7-0adc-4394-8deb-14db551d0328.md))_

## e2e-scripted-run

### Acceptance
- **e2e-scripted-run**: After each step the live side pane shows exactly the expected section map within 5 s and the status segment shows the matching counts; tdd; dashboard; cd ~/se-workflow && python3 -m pytest tests -q -k e2e _(id: [rec-5f7f36da-ec22-4619-b31b-8ff7fb3b85ee](.artifacts/records/project__acceptance/rec-5f7f36da-ec22-4619-b31b-8ff7fb3b85ee.md))_

### Check
- **e2e-scripted-run**: rec-5f7f36da-ec22-4619-b31b-8ff7fb3b85ee; a3b4ee2; pass; tdd _(id: [rec-0bb17e22-8556-465f-b71b-26bf65439808](.artifacts/records/project__check-run/rec-0bb17e22-8556-465f-b71b-26bf65439808.md))_

### Observation
- **e2e-scripted-run**: One of ten full-suite runs failed on the e2e test before the status check became a poll; likely cause is the dashboard-status 2 s view timeout under load, which makes the status line print nothing; watch-dashboard _(id: [rec-a77f0052-dde9-486a-8cd7-d29c9576f5a4](.artifacts/records/project__investigation-observation/rec-a77f0052-dde9-486a-8cd7-d29c9576f5a4.md))_

## effort-switch-focus

### Acceptance
- **effort-switch-focus**: Pilot test: with an effort-level question on a live effort, tab and shift+tab reach a finished effort and stay there; the test fails before the fix; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k switch _(id: [rec-768f3192-cdcf-45d9-9421-2282f78e8bef](.artifacts/records/project__acceptance/rec-768f3192-cdcf-45d9-9421-2282f78e8bef.md))_

### Check
- **effort-switch-focus**: rec-768f3192-cdcf-45d9-9421-2282f78e8bef; 9da847f3ed9909af06213792ab542bdd582422a3; pass; tdd _(id: [rec-f46731c5-7318-4e68-8d68-c07a955c4d00](.artifacts/records/project__check-run/rec-f46731c5-7318-4e68-8d68-c07a955c4d00.md))_

## estimate-chips

### Acceptance
- **estimate-chips**: test_estimate_view_chips fails before the change and passes after: at 60 columns the opened task shows chips for size when set, minutes when set including 0m, and executor inline or executor subagent.; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_estimate.py -q -k estimate_view_chips _(id: [rec-9151bd53-c190-48d4-a538-e887e6f192bd](.artifacts/records/project__acceptance/rec-9151bd53-c190-48d4-a538-e887e6f192bd.md))_

### Check
- **estimate-chips**: rec-9151bd53-c190-48d4-a538-e887e6f192bd; dirty; pass; tdd _(id: [rec-74c63806-81fe-44f6-a287-e830459e7a99](.artifacts/records/project__check-run/rec-74c63806-81fe-44f6-a287-e830459e7a99.md))_
- **estimate-chips**: rec-9151bd53-c190-48d4-a538-e887e6f192bd; dirty; fail; tdd _(id: [rec-fd0dc3b1-bc13-48e3-b1d4-ed18aab7da50](.artifacts/records/project__check-run/rec-fd0dc3b1-bc13-48e3-b1d4-ed18aab7da50.md))_

## estimate-contract

### Acceptance
- **estimate-contract**: contract/project-design.json lists optional size with enum XS, S, M, L, XL on project:work-item, and the phase record does not gain size.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_estimate_contract.py -q -k size _(id: [rec-1f969ece-cd7e-42c2-944a-899e5ff0f266](.artifacts/records/project__acceptance/rec-1f969ece-cd7e-42c2-944a-899e5ff0f266.md))_

### Check
- **estimate-contract**: rec-1f969ece-cd7e-42c2-944a-899e5ff0f266; dirty; pass; tdd _(id: [rec-d8d55808-f9b0-4f46-9cf1-d924a88ec0d6](.artifacts/records/project__check-run/rec-d8d55808-f9b0-4f46-9cf1-d924a88ec0d6.md))_
- **estimate-contract**: rec-1f969ece-cd7e-42c2-944a-899e5ff0f266; dirty; fail; tdd _(id: [rec-fa2dfc43-1ec4-4d0e-bc55-80fc987bb32b](.artifacts/records/project__check-run/rec-fa2dfc43-1ec4-4d0e-bc55-80fc987bb32b.md))_

## estimate-contract-minutes

### Acceptance
- **estimate-contract-minutes**: estimate_minutes is an optional work-item field and is not an enum, and the work-item has no minutes or hours field.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_estimate_contract.py -q -k minutes _(id: [rec-5a0f9f85-407d-497d-b412-1e314d15e91d](.artifacts/records/project__acceptance/rec-5a0f9f85-407d-497d-b412-1e314d15e91d.md))_

### Check
- **estimate-contract-minutes**: rec-5a0f9f85-407d-497d-b412-1e314d15e91d; dirty; pass; tdd _(id: [rec-81470571-0061-44e4-8e84-2e21746a65bd](.artifacts/records/project__check-run/rec-81470571-0061-44e4-8e84-2e21746a65bd.md))_
- **estimate-contract-minutes**: rec-5a0f9f85-407d-497d-b412-1e314d15e91d; dirty; fail; tdd _(id: [rec-fb3ae873-822c-4528-87f2-c10c122aa0b0](.artifacts/records/project__check-run/rec-fb3ae873-822c-4528-87f2-c10c122aa0b0.md))_

## estimate-model

### Acceptance
- **estimate-model**: test_estimate_view_sitting_phrase fails before the change and passes after: Size: more than one sitting returns more than one, Size: one sitting returns one sitting, and a body with no Size line returns empty.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_dashboard_model.py -q -k estimate_view_sitting_phrase _(id: [rec-7eabd5f4-5519-4834-b2f5-2330ed0ff75e](.artifacts/records/project__acceptance/rec-7eabd5f4-5519-4834-b2f5-2330ed0ff75e.md))_

### Check
- **estimate-model**: rec-7eabd5f4-5519-4834-b2f5-2330ed0ff75e; dirty; pass; tdd _(id: [rec-4ff68584-f3f2-42d5-a170-df4ced720bcd](.artifacts/records/project__check-run/rec-4ff68584-f3f2-42d5-a170-df4ced720bcd.md))_
- **estimate-model**: rec-7eabd5f4-5519-4834-b2f5-2330ed0ff75e; dirty; fail; tdd _(id: [rec-e5b84812-c7d4-4ea5-bfb2-4a89b28fcadc](.artifacts/records/project__check-run/rec-e5b84812-c7d4-4ea5-bfb2-4a89b28fcadc.md))_

## estimate-model-blank

### Acceptance
- **estimate-model-blank**: test_estimate_view_blank_executor fails before the change and passes after: a task with no size and no estimate_minutes still has executor subagent, an empty size, and no minutes.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_dashboard_model.py -q -k estimate_view_blank_executor _(id: [rec-910eed74-aa0f-4d5f-af8b-aa7323cf0f9a](.artifacts/records/project__acceptance/rec-910eed74-aa0f-4d5f-af8b-aa7323cf0f9a.md))_

### Check
- **estimate-model-blank**: rec-910eed74-aa0f-4d5f-af8b-aa7323cf0f9a; dirty; fail; tdd _(id: [rec-a401ce2e-b2b9-464b-a28c-dc6e140d68df](.artifacts/records/project__check-run/rec-a401ce2e-b2b9-464b-a28c-dc6e140d68df.md))_
- **estimate-model-blank**: rec-910eed74-aa0f-4d5f-af8b-aa7323cf0f9a; dirty; pass; tdd _(id: [rec-cb7813d1-d531-4b31-9efa-c3a57723f722](.artifacts/records/project__check-run/rec-cb7813d1-d531-4b31-9efa-c3a57723f722.md))_

## estimate-model-row

### Acceptance
- **estimate-model-row**: test_estimate_view_row_fields fails before the change and passes after: a phase row carries the sitting phrase and elapsed minutes, and a task row carries size, estimate_minutes, and executor from the work-item.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_dashboard_model.py -q -k estimate_view_row_fields _(id: [rec-18fd0fc9-9da2-4cc0-a5e1-a968d60dac73](.artifacts/records/project__acceptance/rec-18fd0fc9-9da2-4cc0-a5e1-a968d60dac73.md))_

### Check
- **estimate-model-row**: rec-18fd0fc9-9da2-4cc0-a5e1-a968d60dac73; dirty; pass; tdd _(id: [rec-88acb7c5-1acd-420f-b432-6a345415dbf4](.artifacts/records/project__check-run/rec-88acb7c5-1acd-420f-b432-6a345415dbf4.md))_
- **estimate-model-row**: rec-18fd0fc9-9da2-4cc0-a5e1-a968d60dac73; dirty; fail; tdd _(id: [rec-b532893c-2c49-4961-adfc-b72280078026](.artifacts/records/project__check-run/rec-b532893c-2c49-4961-adfc-b72280078026.md))_

## estimate-model-unset

### Acceptance
- **estimate-model-unset**: test_estimate_view_unset_count fails before the change and passes after: two counted tasks with no estimate_minutes yield an unset count of 2 beside a partial total, and a phase with no estimates returns no elapsed total.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_dashboard_model.py -q -k estimate_view_unset_count _(id: [rec-12a895aa-399e-41fb-9955-825515f54673](.artifacts/records/project__acceptance/rec-12a895aa-399e-41fb-9955-825515f54673.md))_

### Check
- **estimate-model-unset**: rec-12a895aa-399e-41fb-9955-825515f54673; dirty; pass; tdd _(id: [rec-8b80532f-21ea-4fa2-bac4-31df00fba144](.artifacts/records/project__check-run/rec-8b80532f-21ea-4fa2-bac4-31df00fba144.md))_
- **estimate-model-unset**: rec-12a895aa-399e-41fb-9955-825515f54673; dirty; fail; tdd _(id: [rec-d8de5685-1a44-49b0-9e5b-eb7ac24eb638](.artifacts/records/project__check-run/rec-d8de5685-1a44-49b0-9e5b-eb7ac24eb638.md))_

## estimate-model-wave

### Acceptance
- **estimate-model-wave**: test_estimate_view_wave_rule fails before the change and passes after: inline minutes in a wave add, a subagent wave contributes its longest estimate_minutes, blanks are skipped, zero counts, and those wave figures add.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_dashboard_model.py -q -k estimate_view_wave_rule _(id: [rec-70638ad0-75c0-4b42-8827-77ec817e3cfd](.artifacts/records/project__acceptance/rec-70638ad0-75c0-4b42-8827-77ec817e3cfd.md))_

### Check
- **estimate-model-wave**: rec-70638ad0-75c0-4b42-8827-77ec817e3cfd; dirty; pass; tdd _(id: [rec-16df7a56-5f25-4f8a-9481-039de8e0b7fb](.artifacts/records/project__check-run/rec-16df7a56-5f25-4f8a-9481-039de8e0b7fb.md))_
- **estimate-model-wave**: rec-70638ad0-75c0-4b42-8827-77ec817e3cfd; dirty; fail; tdd _(id: [rec-aa113976-91b5-4222-9b1b-28736ee0c3d7](.artifacts/records/project__check-run/rec-aa113976-91b5-4222-9b1b-28736ee0c3d7.md))_

## estimate-skill

### Acceptance
- **estimate-skill**: Every new work-item example in plan-phase includes size and estimate_minutes, and the skill states the five size meanings and that the minutes belong to the executor.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_estimate_skill.py -q -k write _(id: [rec-0106101c-dc9b-4060-bef9-b1dd59a2bd68](.artifacts/records/project__acceptance/rec-0106101c-dc9b-4060-bef9-b1dd59a2bd68.md))_

### Check
- **estimate-skill**: rec-0106101c-dc9b-4060-bef9-b1dd59a2bd68; dirty; fail; tdd _(id: [rec-0a6a2d7f-dec7-444e-901a-677678bf9194](.artifacts/records/project__check-run/rec-0a6a2d7f-dec7-444e-901a-677678bf9194.md))_
- **estimate-skill**: rec-0106101c-dc9b-4060-bef9-b1dd59a2bd68; dirty; pass; tdd _(id: [rec-2b63e40c-65b3-4e1c-b831-27c8382140d7](.artifacts/records/project__check-run/rec-2b63e40c-65b3-4e1c-b831-27c8382140d7.md))_

## estimate-skill-rollup

### Acceptance
- **estimate-skill-rollup**: The skill states that inline minutes in a wave add, a subagent wave uses the longest estimate_minutes, and phase elapsed time adds those wave figures in wave order, skipping blanks.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_estimate_skill.py -q -k rollup _(id: [rec-8ea82af0-405d-4dbb-bb7c-a73bdf063adf](.artifacts/records/project__acceptance/rec-8ea82af0-405d-4dbb-bb7c-a73bdf063adf.md))_

### Check
- **estimate-skill-rollup**: rec-8ea82af0-405d-4dbb-bb7c-a73bdf063adf; dirty; fail; tdd _(id: [rec-4ba11094-3b99-4c8c-b417-c795b942e238](.artifacts/records/project__check-run/rec-4ba11094-3b99-4c8c-b417-c795b942e238.md))_
- **estimate-skill-rollup**: rec-8ea82af0-405d-4dbb-bb7c-a73bdf063adf; dirty; pass; tdd _(id: [rec-ea82231e-3333-4c8a-882f-eb1bddf79085](.artifacts/records/project__check-run/rec-ea82231e-3333-4c8a-882f-eb1bddf79085.md))_

## estimate-skill-sitting

### Acceptance
- **estimate-skill-sitting**: The skill still requires the phase body to record one sitting or more than one, and it says the phase record stores neither size nor estimate_minutes.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_estimate_skill.py -q -k sitting _(id: [rec-bd586f77-929c-45d7-882a-438a63414019](.artifacts/records/project__acceptance/rec-bd586f77-929c-45d7-882a-438a63414019.md))_

### Check
- **estimate-skill-sitting**: rec-bd586f77-929c-45d7-882a-438a63414019; dirty; fail; tdd _(id: [rec-084cd0fd-376d-43d7-8e5d-85c170d463db](.artifacts/records/project__check-run/rec-084cd0fd-376d-43d7-8e5d-85c170d463db.md))_
- **estimate-skill-sitting**: rec-bd586f77-929c-45d7-882a-438a63414019; dirty; pass; tdd _(id: [rec-4b54f00b-37ee-4871-b92a-3cef04ef3f51](.artifacts/records/project__check-run/rec-4b54f00b-37ee-4871-b92a-3cef04ef3f51.md))_

## estimate-table

### Acceptance
- **estimate-table**: test_estimate_view_header_sitting fails before the change and passes after: at 60 columns a phase header shows more than one after the done/total count when the body says Size: more than one sitting, and a phase with no Size line shows no sitting phrase.; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k estimate_view_header_sitting _(id: [rec-0334ff65-b695-433e-97e4-feed4a633233](.artifacts/records/project__acceptance/rec-0334ff65-b695-433e-97e4-feed4a633233.md))_

### Check
- **estimate-table**: rec-0334ff65-b695-433e-97e4-feed4a633233; dirty; pass; tdd _(id: [rec-87bb9a48-ea5a-4252-83c7-a8b9129c983f](.artifacts/records/project__check-run/rec-87bb9a48-ea5a-4252-83c7-a8b9129c983f.md))_
- **estimate-table**: rec-0334ff65-b695-433e-97e4-feed4a633233; dirty; fail; tdd _(id: [rec-d630673d-c238-4e70-9c85-e4f3a86f232e](.artifacts/records/project__check-run/rec-d630673d-c238-4e70-9c85-e4f3a86f232e.md))_

## estimate-table-clip

### Acceptance
- **estimate-table-clip**: test_estimate_view_clip fails before the change and passes after: a long phase title and a long task title are shortened, and the sitting phrase, elapsed minutes, unset count, and task suffix stay whole.; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k estimate_view_clip _(id: [rec-3c8dcd3a-d259-4881-b1d2-d5c39548776a](.artifacts/records/project__acceptance/rec-3c8dcd3a-d259-4881-b1d2-d5c39548776a.md))_

### Check
- **estimate-table-clip**: rec-3c8dcd3a-d259-4881-b1d2-d5c39548776a; dirty; pass; tdd _(id: [rec-c393e5c3-c7a4-4cfe-b716-003a6b61ff73](.artifacts/records/project__check-run/rec-c393e5c3-c7a4-4cfe-b716-003a6b61ff73.md))_
- **estimate-table-clip**: rec-3c8dcd3a-d259-4881-b1d2-d5c39548776a; dirty; fail; tdd _(id: [rec-ffb6dd08-6bf4-49bb-aaca-02acde2f9a22](.artifacts/records/project__check-run/rec-ffb6dd08-6bf4-49bb-aaca-02acde2f9a22.md))_

## estimate-table-elapsed

### Acceptance
- **estimate-table-elapsed**: test_estimate_view_header_elapsed fails before the change and passes after: a subagent wave of 10 and 40 shows 40m on the header, and an inline wave of 10 and 15 shows 25m.; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k estimate_view_header_elapsed _(id: [rec-d4eb4fe3-27e9-44aa-ac89-9138f8666348](.artifacts/records/project__acceptance/rec-d4eb4fe3-27e9-44aa-ac89-9138f8666348.md))_

### Check
- **estimate-table-elapsed**: rec-d4eb4fe3-27e9-44aa-ac89-9138f8666348; dirty; pass; tdd _(id: [rec-37140203-c1a6-4c53-bbbc-908b2f4d0a54](.artifacts/records/project__check-run/rec-37140203-c1a6-4c53-bbbc-908b2f4d0a54.md))_
- **estimate-table-elapsed**: rec-d4eb4fe3-27e9-44aa-ac89-9138f8666348; dirty; fail; tdd _(id: [rec-f36c677b-5264-4da9-93b2-38ae1d433612](.artifacts/records/project__check-run/rec-f36c677b-5264-4da9-93b2-38ae1d433612.md))_

## estimate-table-partial

### Acceptance
- **estimate-table-partial**: test_estimate_view_header_partial fails before the change and passes after: two counted tasks with no estimate show the partial total and 2 unset, and a phase with no estimates shows no minute suffix.; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k estimate_view_header_partial _(id: [rec-f4e5899d-ba88-4a58-ad18-718a28db0e16](.artifacts/records/project__acceptance/rec-f4e5899d-ba88-4a58-ad18-718a28db0e16.md))_

### Check
- **estimate-table-partial**: rec-f4e5899d-ba88-4a58-ad18-718a28db0e16; dirty; pass; tdd _(id: [rec-1fac2cf6-7f41-49d6-a4f0-c465aede6986](.artifacts/records/project__check-run/rec-1fac2cf6-7f41-49d6-a4f0-c465aede6986.md))_
- **estimate-table-partial**: rec-f4e5899d-ba88-4a58-ad18-718a28db0e16; dirty; fail; tdd _(id: [rec-6f35022c-32f0-4c9d-a30b-3b9b5e5abee3](.artifacts/records/project__check-run/rec-6f35022c-32f0-4c9d-a30b-3b9b5e5abee3.md))_

## estimate-table-suffix

### Acceptance
- **estimate-table-suffix**: test_estimate_view_title_suffix fails before the change and passes after: the task title shows size, minutes, and executor before a waits-on note; a missing size is omitted; 0 shows as 0m; a missing executor shows as subagent.; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k estimate_view_title_suffix _(id: [rec-c823c876-890c-4582-b8ac-0b8e804b6de6](.artifacts/records/project__acceptance/rec-c823c876-890c-4582-b8ac-0b8e804b6de6.md))_

### Check
- **estimate-table-suffix**: rec-c823c876-890c-4582-b8ac-0b8e804b6de6; dirty; fail; tdd _(id: [rec-2a34d0dc-66e9-4fa4-9611-8aa1d6f0b953](.artifacts/records/project__check-run/rec-2a34d0dc-66e9-4fa4-9611-8aa1d6f0b953.md))_
- **estimate-table-suffix**: rec-c823c876-890c-4582-b8ac-0b8e804b6de6; dirty; pass; tdd _(id: [rec-59eac60c-c027-49fe-87db-04e923f17fb4](.artifacts/records/project__check-run/rec-59eac60c-c027-49fe-87db-04e923f17fb4.md))_

## evidence-model

### Acceptance
- **evidence-model**: Requirement rows join by phase and id with text, traced task count, status from the latest assessment, and unassessed with the latest check result when no assessment exists; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and requirement' _(id: [rec-d9e2121e-cbda-488a-b93d-f162ca25e09d](.artifacts/records/project__acceptance/rec-d9e2121e-cbda-488a-b93d-f162ca25e09d.md))_

### Check
- **evidence-model**: rec-d9e2121e-cbda-488a-b93d-f162ca25e09d; dirty; pass; tdd _(id: [rec-75cc2533-737d-44ca-8886-1c7d65c86330](.artifacts/records/project__check-run/rec-75cc2533-737d-44ca-8886-1c7d65c86330.md))_

## evidence-model-activity

### Acceptance
- **evidence-model-activity**: Activity lists assessments, integration-reports, and releases, marks upstream routes and level escalation, and flags fail or blocked as failed; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and activity' _(id: [rec-40275e71-0386-466c-9431-b6a06ea32cc4](.artifacts/records/project__acceptance/rec-40275e71-0386-466c-9431-b6a06ea32cc4.md))_

### Check
- **evidence-model-activity**: rec-40275e71-0386-466c-9431-b6a06ea32cc4; dirty; pass; tdd _(id: [rec-ea4330a1-234c-4dcf-9b78-06336c4bfd7c](.artifacts/records/project__check-run/rec-ea4330a1-234c-4dcf-9b78-06336c4bfd7c.md))_

## evidence-model-detail

### Acceptance
- **evidence-model-detail**: load_requirement_detail returns text, decisions, traced tasks, acceptances with latest check and evidence kind, and every assessment oldest first including superseded ones; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and requirement_detail' _(id: [rec-03a4156f-4505-4c4a-84f8-b2dbf28dbc76](.artifacts/records/project__acceptance/rec-03a4156f-4505-4c4a-84f8-b2dbf28dbc76.md))_

### Check
- **evidence-model-detail**: rec-03a4156f-4505-4c4a-84f8-b2dbf28dbc76; dirty; pass; tdd _(id: [rec-58203183-8016-40e0-a8c2-548e817f4ef0](.artifacts/records/project__check-run/rec-58203183-8016-40e0-a8c2-548e817f4ef0.md))_

## evidence-model-legacy

### Acceptance
- **evidence-model-legacy**: A store whose CLI rejects the evidence types loads a snapshot with no error; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and legacy' _(id: [rec-6d2b9680-5f62-4979-8450-8b3f99e1707b](.artifacts/records/project__acceptance/rec-6d2b9680-5f62-4979-8450-8b3f99e1707b.md))_

### Check
- **evidence-model-legacy**: rec-6d2b9680-5f62-4979-8450-8b3f99e1707b; dirty; pass; tdd _(id: [rec-32f00d17-d4df-4b3d-8848-cd9bdc0c2ec5](.artifacts/records/project__check-run/rec-32f00d17-d4df-4b3d-8848-cd9bdc0c2ec5.md))_

## evidence-model-needs

### Acceptance
- **evidence-model-needs**: Needs you gains loop-route items for upstream, blocked, and low-confidence latest assessments and integration items for failed or blocked reports, and none for execute, verify, or insufficient routes; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and needs' _(id: [rec-b629a582-c0ce-42e7-a2c8-006bf618a411](.artifacts/records/project__acceptance/rec-b629a582-c0ce-42e7-a2c8-006bf618a411.md))_

### Check
- **evidence-model-needs**: rec-b629a582-c0ce-42e7-a2c8-006bf618a411; dirty; pass; tdd _(id: [rec-1867057b-8567-406b-bf2d-6b7c385ce15d](.artifacts/records/project__check-run/rec-1867057b-8567-406b-bf2d-6b7c385ce15d.md))_
- **evidence-model-needs**: rec-b629a582-c0ce-42e7-a2c8-006bf618a411; dirty; fail; tdd _(id: [rec-76f589e6-7586-4851-b503-a7807d36329d](.artifacts/records/project__check-run/rec-76f589e6-7586-4851-b503-a7807d36329d.md))_

## evidence-model-release

### Acceptance
- **evidence-model-release**: A ready release sets release_ready on the effort and the phase, and finished is unchanged; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and release' _(id: [rec-0ebb72a4-a992-4c0d-804f-e4b659df3ff1](.artifacts/records/project__acceptance/rec-0ebb72a4-a992-4c0d-804f-e4b659df3ff1.md))_

### Check
- **evidence-model-release**: rec-0ebb72a4-a992-4c0d-804f-e4b659df3ff1; dirty; pass; tdd _(id: [rec-5b187fe6-6249-4331-9bec-26a159d82096](.artifacts/records/project__check-run/rec-5b187fe6-6249-4331-9bec-26a159d82096.md))_

## evidence-model-simple

### Acceptance
- **evidence-model-simple**: A phase with no specification has evidence None and adds no Needs-you or activity item; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and simple' _(id: [rec-5cd3b306-dec8-422d-adcd-d051b9748117](.artifacts/records/project__acceptance/rec-5cd3b306-dec8-422d-adcd-d051b9748117.md))_

### Check
- **evidence-model-simple**: rec-5cd3b306-dec8-422d-adcd-d051b9748117; dirty; pass; tdd _(id: [rec-3998e8e0-527a-419b-a90d-2acf8a4909c6](.artifacts/records/project__check-run/rec-3998e8e0-527a-419b-a90d-2acf8a4909c6.md))_

## evidence-model-stage

### Acceptance
- **evidence-model-stage**: Stage derivation returns each stage for a store built to hit each rule, and release when the latest release is ready; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and stage' _(id: [rec-0efed917-d236-4ffc-893e-994b77883d20](.artifacts/records/project__acceptance/rec-0efed917-d236-4ffc-893e-994b77883d20.md))_

### Check
- **evidence-model-stage**: rec-0efed917-d236-4ffc-893e-994b77883d20; dirty; pass; tdd _(id: [rec-f9558ef2-206d-4a6a-804f-81110e945c61](.artifacts/records/project__check-run/rec-f9558ef2-206d-4a6a-804f-81110e945c61.md))_

## evidence-surfaces

### Acceptance
- **evidence-surfaces**: A structured phase header row shows R n/m verified at 60 and 120 columns; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and tally' _(id: [rec-af8be786-2f56-46ed-95a4-4b0e2f42cfcc](.artifacts/records/project__acceptance/rec-af8be786-2f56-46ed-95a4-4b0e2f42cfcc.md))_

### Check
- **evidence-surfaces**: rec-af8be786-2f56-46ed-95a4-4b0e2f42cfcc; dirty; pass; tdd _(id: [rec-5cfeca21-9bd0-4256-8cca-420a1417d46f](.artifacts/records/project__check-run/rec-5cfeca21-9bd0-4256-8cca-420a1417d46f.md))_

## evidence-surfaces-activity

### Acceptance
- **evidence-surfaces-activity**: Activity shows assessment, integration, and release lines, with failed or blocked ones in the error colour; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and activity' _(id: [rec-f0de4074-6f9b-4db2-96b2-64768ae46a3f](.artifacts/records/project__acceptance/rec-f0de4074-6f9b-4db2-96b2-64768ae46a3f.md))_

### Check
- **evidence-surfaces-activity**: rec-f0de4074-6f9b-4db2-96b2-64768ae46a3f; dirty; pass; tdd _(id: [rec-3be37906-a791-4b99-aad5-e25122eac65d](.artifacts/records/project__check-run/rec-3be37906-a791-4b99-aad5-e25122eac65d.md))_

## evidence-surfaces-needs

### Acceptance
- **evidence-surfaces-needs**: Needs you shows readable loop-route and integration lines at 60 columns; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and needs' _(id: [rec-af74e732-3147-46e6-959b-9de2d204d9f8](.artifacts/records/project__acceptance/rec-af74e732-3147-46e6-959b-9de2d204d9f8.md))_

### Check
- **evidence-surfaces-needs**: rec-af74e732-3147-46e6-959b-9de2d204d9f8; dirty; pass; tdd _(id: [rec-08fc31bf-bd1a-40ad-9f21-ae408dc048a4](.artifacts/records/project__check-run/rec-08fc31bf-bd1a-40ad-9f21-ae408dc048a4.md))_

## evidence-surfaces-phase

### Acceptance
- **evidence-surfaces-phase**: Phase detail shows the stage strip with the current stage marked, the specification weight and non-goals, the design decisions, and the integration result with conflicts, with no line wider than the pane at 60 columns; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and strip' _(id: [rec-11264441-69a2-49e7-bc6f-61337f037af7](.artifacts/records/project__acceptance/rec-11264441-69a2-49e7-bc6f-61337f037af7.md))_

### Check
- **evidence-surfaces-phase**: rec-11264441-69a2-49e7-bc6f-61337f037af7; dirty; pass; tdd _(id: [rec-90e826c4-484d-4d10-9fd5-8a6f87bf92ad](.artifacts/records/project__check-run/rec-90e826c4-484d-4d10-9fd5-8a6f87bf92ad.md))_

## evidence-surfaces-release

### Acceptance
- **evidence-surfaces-release**: A ready release shows Release ready on the effort tab and the phase row; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and release' _(id: [rec-1e0e0e59-dc14-4393-96b8-8b865ab34368](.artifacts/records/project__acceptance/rec-1e0e0e59-dc14-4393-96b8-8b865ab34368.md))_

### Check
- **evidence-surfaces-release**: rec-1e0e0e59-dc14-4393-96b8-8b865ab34368; dirty; pass; tdd _(id: [rec-e03ccf51-fd4a-4e4a-a1f0-7d5093ac3e67](.artifacts/records/project__check-run/rec-e03ccf51-fd4a-4e4a-a1f0-7d5093ac3e67.md))_

## evidence-surfaces-requirements

### Acceptance
- **evidence-surfaces-requirements**: Phase detail lists each requirement with id, status, next, and task count, and an unassessed row shows the latest check result dimmed; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and requirement_list' _(id: [rec-4e3b28bd-22b8-4af2-8798-0bc134ff47ab](.artifacts/records/project__acceptance/rec-4e3b28bd-22b8-4af2-8798-0bc134ff47ab.md))_

### Check
- **evidence-surfaces-requirements**: rec-4e3b28bd-22b8-4af2-8798-0bc134ff47ab; dirty; pass; tdd _(id: [rec-ef989920-a210-4bd1-986d-f2b418d3ae09](.artifacts/records/project__check-run/rec-ef989920-a210-4bd1-986d-f2b418d3ae09.md))_

## evidence-surfaces-simple

### Acceptance
- **evidence-surfaces-simple**: A store with only simple phases renders the same header, stepper, phase detail, and --once output as before; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and simple' _(id: [rec-6d5d3021-1e7d-4938-9385-d0112fce7aa8](.artifacts/records/project__acceptance/rec-6d5d3021-1e7d-4938-9385-d0112fce7aa8.md))_

### Check
- **evidence-surfaces-simple**: rec-6d5d3021-1e7d-4938-9385-d0112fce7aa8; dirty; pass; tdd _(id: [rec-dea38843-a2f4-4f86-97c7-5e6ced92905e](.artifacts/records/project__check-run/rec-dea38843-a2f4-4f86-97c7-5e6ced92905e.md))_

## evidence-surfaces-stepper

### Acceptance
- **evidence-surfaces-stepper**: The stepper's current phase shows its stage word and stays within 60 columns; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and stepper' _(id: [rec-dea24b5b-9884-4880-a246-013ea423d317](.artifacts/records/project__acceptance/rec-dea24b5b-9884-4880-a246-013ea423d317.md))_

### Check
- **evidence-surfaces-stepper**: rec-dea24b5b-9884-4880-a246-013ea423d317; dirty; pass; tdd _(id: [rec-78421eb1-b798-4c33-9e5f-269a77204ed1](.artifacts/records/project__check-run/rec-78421eb1-b798-4c33-9e5f-269a77204ed1.md))_

## execute-landing

### Acceptance
- **execute-landing**: execute-phase creates the worktree, confines code writes to it, keeps store writes on the primary checkout, commits the branch, merges to main, commits the store, and does not push unless Landing names push as a stop; a phase with no Landing stays in the current checkout; tdd; workflow-loop; python3 -m pytest tests/test_execute_landing.py -q _(id: [rec-b89f9c9f-d9f4-4db9-8375-3f877388c961](.artifacts/records/project__acceptance/rec-b89f9c9f-d9f4-4db9-8375-3f877388c961.md))_

### Check
- **execute-landing**: rec-b89f9c9f-d9f4-4db9-8375-3f877388c961; dirty; pass; tdd _(id: [rec-db1a2d05-c946-4377-9044-a73c9a9dfb5b](.artifacts/records/project__check-run/rec-db1a2d05-c946-4377-9044-a73c9a9dfb5b.md))_

## execute-wave-dispatch

### Acceptance
- **execute-wave-dispatch**: execute-phase runs an inline wave in this session and a subagent wave as one worker per task, treats a missing executor as subagent, and does not ask for a recipe when Approach is present; tdd; workflow-loop; python3 -m pytest tests/test_execute_wave_dispatch.py -q _(id: [rec-c95855b2-e077-44d7-ab61-b8b70ec6f7df](.artifacts/records/project__acceptance/rec-c95855b2-e077-44d7-ab61-b8b70ec6f7df.md))_

### Check
- **execute-wave-dispatch**: rec-c95855b2-e077-44d7-ab61-b8b70ec6f7df; dirty; pass; tdd _(id: [rec-07c3a7ec-2a6e-424c-84a0-b633eb4949bd](.artifacts/records/project__check-run/rec-07c3a7ec-2a6e-424c-84a0-b633eb4949bd.md))_

## finished-effort-view

### Acceptance
- **finished-effort-view**: Model test: finished is true only when every phase and counted task is done. Pilot tests: a finished effort shows All N tasks done under Active, sorts after a live effort, and has a dimmed label; a live effort with an empty filter still shows No tasks match; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_app.py -q -k finished _(id: [rec-cc216932-78bb-4df8-b80d-8da0eb287a9c](.artifacts/records/project__acceptance/rec-cc216932-78bb-4df8-b80d-8da0eb287a9c.md))_

### Check
- **finished-effort-view**: rec-cc216932-78bb-4df8-b80d-8da0eb287a9c; 11fdbbe31fe4a60f1985ccc24fa41788fa83d1d5; pass; tdd _(id: [rec-9e17ccb9-1b70-4843-ade6-cabf22d52de2](.artifacts/records/project__check-run/rec-9e17ccb9-1b70-4843-ade6-cabf22d52de2.md))_

## fix-human-gate-constraint

### Acceptance
- **fix-human-gate-constraint**: Active dashboard-human-gate-writes names Needs-you human gates and preserves backlog promote/dismiss as allowed (or clarifies exclusivity without contradicting Non-goals); old never-writes subjects stay retired; check; workflow-loop; /home/andrewyin/adaptive-artifacts/bin/adaptive-artifacts --store /home/andrewyin/se-workflow/.artifacts list --type project:constraint --state active | python3 -c "import sys,json; d=json.load(sys.stdin); stmts=[(r['subject'], (r.get('payload') or {}).get('statement') or '') for r in d['records']]; hg=[t for s,t in stmts if s=='dashboard-human-gate-writes']; assert hg; t=hg[0].lower(); assert 'needs-you' in t or 'human' in t; assert 'backlog' in t and (('promote' in t) or ('dismiss' in t)); old={'dashboard-read-only','dashboard-read-only-dashboard-bugfix','dashboard-read-only-dashboard-features'}; assert not any('never writes' in x.lower() for s,x in stmts if s in old)" _(id: [rec-7cd14081-b40c-4643-9c77-8ead22c68483](.artifacts/records/project__acceptance/rec-7cd14081-b40c-4643-9c77-8ead22c68483.md))_

### Check
- **fix-human-gate-constraint**: rec-7cd14081-b40c-4643-9c77-8ead22c68483; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; check _(id: [rec-1ed320a3-c828-48d4-8de2-9969706b2fa7](.artifacts/records/project__check-run/rec-1ed320a3-c828-48d4-8de2-9969706b2fa7.md))_

## fix-journal-pager-timeout

### Acceptance
- **fix-journal-pager-timeout**: test_journal_detail_pager_pages_record_with_stub passes with raised pilot timeout; tdd; packaging; uv run --with textual --with pytest python -m pytest tests/test_dashboard_journal.py::test_journal_detail_pager_pages_record_with_stub -q _(id: [rec-83a0060b-ad9d-4ebf-9d9d-50a91677b1ff](.artifacts/records/project__acceptance/rec-83a0060b-ad9d-4ebf-9d9d-50a91677b1ff.md))_

### Check
- **fix-journal-pager-timeout**: rec-83a0060b-ad9d-4ebf-9d9d-50a91677b1ff; dirty; fail; tdd _(id: [rec-2483b603-ab08-40c0-b787-865baebd1002](.artifacts/records/project__check-run/rec-2483b603-ab08-40c0-b787-865baebd1002.md))_
- **fix-journal-pager-timeout**: rec-83a0060b-ad9d-4ebf-9d9d-50a91677b1ff; 3379fcf8a1d882d91330bec6e66a2889c71d3ece; pass; tdd _(id: [rec-67c47e4a-2545-4d89-93a9-c83f34293e09](.artifacts/records/project__check-run/rec-67c47e4a-2545-4d89-93a9-c83f34293e09.md))_

## fix-test_dashboard_app

### Acceptance
- **fix-test_dashboard_app**: Module failures cleared: test_running_row_status_shows_its_running_time[120]; test_footer_has_no_palette_and_every_binding_fits_at_60_columns; test_detail_related_panel_lists_related_records[size1-_open_by_click]; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'running_row_status_shows_its_running_time or footer_has_no_palette or detail_related_panel_lists_related_records' _(id: [rec-d2f35534-584a-4e18-b439-3641ec83969d](.artifacts/records/project__acceptance/rec-d2f35534-584a-4e18-b439-3641ec83969d.md))_

### Check
- **fix-test_dashboard_app**: rec-d2f35534-584a-4e18-b439-3641ec83969d; dirty; pass; tdd _(id: [rec-c01b17e8-2ecb-4d56-a364-324cd98b402e](.artifacts/records/project__check-run/rec-c01b17e8-2ecb-4d56-a364-324cd98b402e.md))_
- **fix-test_dashboard_app**: rec-d2f35534-584a-4e18-b439-3641ec83969d; 2f7404eab494720b703ffd0e2e01078236a876ab; pass; tdd _(id: [rec-c2bb099d-b561-4751-9063-0c3a95a508ec](.artifacts/records/project__check-run/rec-c2bb099d-b561-4751-9063-0c3a95a508ec.md))_

## fix-test_dashboard_journal

### Acceptance
- **fix-test_dashboard_journal**: Module failures cleared: test_journal_panel_shows_for_repair_kind; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_journal.py -q -k journal_panel_shows_for_repair_kind _(id: [rec-3df8eb5b-21db-4624-8831-12b8bdc2a294](.artifacts/records/project__acceptance/rec-3df8eb5b-21db-4624-8831-12b8bdc2a294.md))_

### Check
- **fix-test_dashboard_journal**: rec-3df8eb5b-21db-4624-8831-12b8bdc2a294; dirty; pass; tdd _(id: [rec-0863cd5c-7440-4218-8155-5bf3d3c2ff35](.artifacts/records/project__check-run/rec-0863cd5c-7440-4218-8155-5bf3d3c2ff35.md))_
- **fix-test_dashboard_journal**: rec-3df8eb5b-21db-4624-8831-12b8bdc2a294; 2f7404eab494720b703ffd0e2e01078236a876ab; pass; tdd _(id: [rec-f968b020-0e52-4016-a7e1-432bc354f41b](.artifacts/records/project__check-run/rec-f968b020-0e52-4016-a7e1-432bc354f41b.md))_

## fix-test_discuss_skill

### Acceptance
- **fix-test_discuss_skill**: Module failures cleared: test_plan_phase_opens_a_blocking_plan_review_question; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_discuss_skill.py -q -k plan_phase_opens_a_blocking_plan_review_question _(id: [rec-7a209b57-ff35-4f91-b06b-41f8057aecef](.artifacts/records/project__acceptance/rec-7a209b57-ff35-4f91-b06b-41f8057aecef.md))_

### Check
- **fix-test_discuss_skill**: rec-7a209b57-ff35-4f91-b06b-41f8057aecef; 2f7404eab494720b703ffd0e2e01078236a876ab; pass; tdd _(id: [rec-2db0a42c-4698-4121-bdc9-7daf4749d1d4](.artifacts/records/project__check-run/rec-2db0a42c-4698-4121-bdc9-7daf4749d1d4.md))_
- **fix-test_discuss_skill**: rec-7a209b57-ff35-4f91-b06b-41f8057aecef; dirty; fail; tdd _(id: [rec-5f1fbf64-77e1-4d1b-b3ce-5d52ea252a75](.artifacts/records/project__check-run/rec-5f1fbf64-77e1-4d1b-b3ce-5d52ea252a75.md))_

## fix-test_evidence_loop

### Acceptance
- **fix-test_evidence_loop**: Cleared: test_check_run_result_and_method_are_contract_enums; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_evidence_loop.py -q -k check_run_result_and_method_are_contract_enums _(id: [rec-be712a69-03e1-4ea1-a1e1-b0534ae0b828](.artifacts/records/project__acceptance/rec-be712a69-03e1-4ea1-a1e1-b0534ae0b828.md))_

### Check
- **fix-test_evidence_loop**: rec-be712a69-03e1-4ea1-a1e1-b0534ae0b828; 2f7404eab494720b703ffd0e2e01078236a876ab; pass; tdd _(id: [rec-a10d7f0b-0e2c-4f35-a269-2afd2c76ec1a](.artifacts/records/project__check-run/rec-a10d7f0b-0e2c-4f35-a269-2afd2c76ec1a.md))_
- **fix-test_evidence_loop**: rec-be712a69-03e1-4ea1-a1e1-b0534ae0b828; dirty; pass; tdd _(id: [rec-f36113f3-83c1-4d55-afb0-ae1ab32433d1](.artifacts/records/project__check-run/rec-f36113f3-83c1-4d55-afb0-ae1ab32433d1.md))_

## fix-test_plan_landing

### Acceptance
- **fix-test_plan_landing**: Cleared: test_plan_review_stays_closed_until_landing_is_present; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_plan_landing.py -q -k plan_review_stays_closed_until_landing _(id: [rec-47fbfa19-5038-4851-830d-42a55a72a49e](.artifacts/records/project__acceptance/rec-47fbfa19-5038-4851-830d-42a55a72a49e.md))_

### Check
- **fix-test_plan_landing**: rec-47fbfa19-5038-4851-830d-42a55a72a49e; 2f7404eab494720b703ffd0e2e01078236a876ab; pass; tdd _(id: [rec-3872f5a3-92d9-462a-bbc9-a18e3c83ba7e](.artifacts/records/project__check-run/rec-3872f5a3-92d9-462a-bbc9-a18e3c83ba7e.md))_
- **fix-test_plan_landing**: rec-47fbfa19-5038-4851-830d-42a55a72a49e; dirty; pass; tdd _(id: [rec-b585900a-70ef-43b3-ac03-688d876df257](.artifacts/records/project__check-run/rec-b585900a-70ef-43b3-ac03-688d876df257.md))_

## fix-test_plan_wave_rules

### Acceptance
- **fix-test_plan_wave_rules**: Cleared: test_plan_review_stays_closed_until_recipe_executor_and_run_facts_are_present; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_plan_wave_rules.py -q -k plan_review_stays_closed_until_recipe _(id: [rec-f0ad8c81-df6e-457c-8553-9dd57d03f91e](.artifacts/records/project__acceptance/rec-f0ad8c81-df6e-457c-8553-9dd57d03f91e.md))_

### Check
- **fix-test_plan_wave_rules**: rec-f0ad8c81-df6e-457c-8553-9dd57d03f91e; dirty; pass; tdd _(id: [rec-010f08e6-8773-48a3-95de-c92efae83877](.artifacts/records/project__check-run/rec-010f08e6-8773-48a3-95de-c92efae83877.md))_
- **fix-test_plan_wave_rules**: rec-f0ad8c81-df6e-457c-8553-9dd57d03f91e; 2f7404eab494720b703ffd0e2e01078236a876ab; pass; tdd _(id: [rec-ab7a14d0-d11a-458f-a40e-c14ffe4dc4c0](.artifacts/records/project__check-run/rec-ab7a14d0-d11a-458f-a40e-c14ffe4dc4c0.md))_

## fix-test_verify_authority

### Acceptance
- **fix-test_verify_authority**: Cleared: test_skill_close_request_references_check_run_id_for_runner_methods; test_close_batch_does_not_emit_check_run_create_for_runner_methods; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_authority.py -q -k 'skill_close_request_references_check_run_id or close_batch_does_not_emit_check_run_create' _(id: [rec-e09c9aac-f876-43da-9856-41ed79b75404](.artifacts/records/project__acceptance/rec-e09c9aac-f876-43da-9856-41ed79b75404.md))_

### Check
- **fix-test_verify_authority**: rec-e09c9aac-f876-43da-9856-41ed79b75404; dirty; pass; tdd _(id: [rec-5e5e7943-0cfe-47be-bdc1-7c6c5ca5fe32](.artifacts/records/project__check-run/rec-5e5e7943-0cfe-47be-bdc1-7c6c5ca5fe32.md))_
- **fix-test_verify_authority**: rec-e09c9aac-f876-43da-9856-41ed79b75404; 2f7404eab494720b703ffd0e2e01078236a876ab; pass; tdd _(id: [rec-9dbbcb14-8061-4f28-87e0-56bbddc01a16](.artifacts/records/project__check-run/rec-9dbbcb14-8061-4f28-87e0-56bbddc01a16.md))_

## fix-verify-authority-close-batch-import

### Acceptance
- **fix-verify-authority-close-batch-import**: tests/test_verify_authority.py collects and passes without scripts/close_batch import; tdd; packaging; uv run --with pytest python -m pytest tests/test_verify_authority.py -q _(id: [rec-a33322af-14f2-44fd-a072-5bc4073fa8a2](.artifacts/records/project__acceptance/rec-a33322af-14f2-44fd-a072-5bc4073fa8a2.md))_

### Check
- **fix-verify-authority-close-batch-import**: rec-a33322af-14f2-44fd-a072-5bc4073fa8a2; 8109e9aae50c888bd17a06bfb3b8f9e2f55665ab; pass; tdd _(id: [rec-5e5de649-bc10-4d3b-b158-d8f754e7c6c1](.artifacts/records/project__check-run/rec-5e5de649-bc10-4d3b-b158-d8f754e7c6c1.md))_
- **fix-verify-authority-close-batch-import**: rec-a33322af-14f2-44fd-a072-5bc4073fa8a2; dirty; fail; tdd _(id: [rec-774d2cea-d57a-49c8-93c4-0f7cb73285ac](.artifacts/records/project__check-run/rec-774d2cea-d57a-49c8-93c4-0f7cb73285ac.md))_

## gates-landing

### Acceptance
- **gates-landing**: phase_landing reports branch, exists, ahead, and merged or not merged for a scratch repo with a Landing section; no Landing heading returns None; missing branch shows exists false; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_gates.py -q -k 'landing and not (nogr or readonly)' _(id: [rec-79184477-3098-4868-8374-96e8edb0d92c](.artifacts/records/project__acceptance/rec-79184477-3098-4868-8374-96e8edb0d92c.md))_

### Check
- **gates-landing**: rec-79184477-3098-4868-8374-96e8edb0d92c; dirty; pass; tdd _(id: [rec-ac631f0f-5f7e-4ff1-87c5-eb980c002e01](.artifacts/records/project__check-run/rec-ac631f0f-5f7e-4ff1-87c5-eb980c002e01.md))_

## gates-landing-failsoft

### Acceptance
- **gates-landing-failsoft**: With no git repository, no git binary, or a failing git command, phase_landing returns None and raises nothing; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_gates.py -q -k 'nogr or no_git or fail' _(id: [rec-03da42d3-f54d-49ba-8ca2-afca1260b398](.artifacts/records/project__acceptance/rec-03da42d3-f54d-49ba-8ca2-afca1260b398.md))_

### Check
- **gates-landing-failsoft**: rec-03da42d3-f54d-49ba-8ca2-afca1260b398; dirty; pass; tdd _(id: [rec-77950a7e-4aba-4694-b411-a5cab13fe76d](.artifacts/records/project__check-run/rec-77950a7e-4aba-4694-b411-a5cab13fe76d.md))_

## gates-landing-readonly

### Acceptance
- **gates-landing-readonly**: After phase_landing runs, git status and the store directory are unchanged; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_gates.py -q -k readonly _(id: [rec-3ba5ea87-0663-4f77-9a0e-ef0a6da1fc3e](.artifacts/records/project__acceptance/rec-3ba5ea87-0663-4f77-9a0e-ef0a6da1fc3e.md))_

### Check
- **gates-landing-readonly**: rec-3ba5ea87-0663-4f77-9a0e-ef0a6da1fc3e; dirty; pass; tdd _(id: [rec-30fee293-6832-4850-bdce-e7dc53b760a6](.artifacts/records/project__check-run/rec-30fee293-6832-4850-bdce-e7dc53b760a6.md))_

## gates-model

### Acceptance
- **gates-model**: A done phase with Landing whose branch exists and is not merged into main yields a Merge branch Needs you item after integration items; Enter detail carries branch and ahead count; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_gates.py -q -k "gates and (merge or landing_item)" _(id: [rec-72691ffa-0dcd-45d0-a9dc-4cabce493d6e](.artifacts/records/project__acceptance/rec-72691ffa-0dcd-45d0-a9dc-4cabce493d6e.md))_

### Check
- **gates-model**: rec-72691ffa-0dcd-45d0-a9dc-4cabce493d6e; dirty; pass; tdd _(id: [rec-8953d20c-a86f-4baa-a24c-4e2880aff9bb](.artifacts/records/project__check-run/rec-8953d20c-a86f-4baa-a24c-4e2880aff9bb.md))_

## gates-model-quiet

### Acceptance
- **gates-model-quiet**: A quiet running task shows running <time> · quiet in warning colour and its wave strip glyph uses warning colour; quiet tasks add no Needs you item; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_tasks.py -q -k "gates and quiet" _(id: [rec-bbb94de7-ae26-498b-ae76-2528eb547de3](.artifacts/records/project__acceptance/rec-bbb94de7-ae26-498b-ae76-2528eb547de3.md))_

### Check
- **gates-model-quiet**: rec-bbb94de7-ae26-498b-ae76-2528eb547de3; dirty; pass; tdd _(id: [rec-49e5e75a-5390-4d96-a3ac-a3f19faa538a](.artifacts/records/project__check-run/rec-49e5e75a-5390-4d96-a3ac-a3f19faa538a.md))_

## gates-status

### Acceptance
- **gates-status**: In a real tmux server, status-right shows the needs-you count for the pane repo when @dashboard-status-right is on, and shows nothing when off or the count is zero; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests -q -m tmux -k "status and (gates or needs or segment)" _(id: [rec-bec7c314-2052-4053-9d5a-3f78a5db6663](.artifacts/records/project__acceptance/rec-bec7c314-2052-4053-9d5a-3f78a5db6663.md))_

### Check
- **gates-status**: rec-bec7c314-2052-4053-9d5a-3f78a5db6663; dirty; pass; tdd _(id: [rec-d5bb5ebd-2833-4597-bfc7-ecf8bfee067a](.artifacts/records/project__check-run/rec-d5bb5ebd-2833-4597-bfc7-ecf8bfee067a.md))_

## gates-ui

### Acceptance
- **gates-ui**: c on a Needs you item copies the ready agent prompt; c on a task row still copies the slug; footer and key help say copy prompt when Needs you has focus; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k "gates and (copy or prompt)" _(id: [rec-6a06a80a-ba89-47c8-8d09-ef1c546ddbb6](.artifacts/records/project__acceptance/rec-6a06a80a-ba89-47c8-8d09-ef1c546ddbb6.md))_

### Check
- **gates-ui**: rec-6a06a80a-ba89-47c8-8d09-ef1c546ddbb6; dirty; pass; tdd _(id: [rec-b41e3704-d094-429c-8b4e-c0549f937bf9](.artifacts/records/project__check-run/rec-b41e3704-d094-429c-8b4e-c0549f937bf9.md))_

## gates-ui-alert

### Acceptance
- **gates-ui-alert**: A Needs you item absent from the previous snapshot rings the bell and shows a stubbed tmux message naming effort, action, and subject; items present at startup do not alert; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k "gates and (alert or bell or message)" _(id: [rec-eafbbe7b-d2e4-4c00-8ade-b19308d28efd](.artifacts/records/project__acceptance/rec-eafbbe7b-d2e4-4c00-8ade-b19308d28efd.md))_

### Check
- **gates-ui-alert**: rec-eafbbe7b-d2e4-4c00-8ade-b19308d28efd; dirty; pass; tdd _(id: [rec-11fa611b-b22c-4461-beda-193333d0b769](.artifacts/records/project__check-run/rec-11fa611b-b22c-4461-beda-193333d0b769.md))_

## gates-ui-next

### Acceptance
- **gates-ui-next**: Under the goal, a next-step line shows next: plus the first matching R4 rule, then the position text in muted colour; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k "gates and next" _(id: [rec-f1684acd-c413-4721-bdc5-4b9b28b25793](.artifacts/records/project__acceptance/rec-f1684acd-c413-4721-bdc5-4b9b28b25793.md))_

### Check
- **gates-ui-next**: rec-f1684acd-c413-4721-bdc5-4b9b28b25793; dirty; pass; tdd _(id: [rec-d238e363-b7a8-42bb-8a24-a4a03abf0d89](.artifacts/records/project__check-run/rec-d238e363-b7a8-42bb-8a24-a4a03abf0d89.md))_

## gates-vocab

### Acceptance
- **gates-vocab**: action_label returns the R1 verbs for each Needs you kind, and a plan-review scope shows Review plan plus the phase title not the raw scope; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'gates and (label or plan_review or action)' _(id: [rec-dda923b2-838f-49de-82f7-3d6b9e8e648d](.artifacts/records/project__acceptance/rec-dda923b2-838f-49de-82f7-3d6b9e8e648d.md))_

### Check
- **gates-vocab**: rec-dda923b2-838f-49de-82f7-3d6b9e8e648d; dirty; pass; tdd _(id: [rec-333e89ae-61cf-4b06-a898-ae1f07b3465f](.artifacts/records/project__check-run/rec-333e89ae-61cf-4b06-a898-ae1f07b3465f.md))_
- **gates-vocab**: rec-dda923b2-838f-49de-82f7-3d6b9e8e648d; dirty; pass; tdd _(id: [rec-722bd310-6ac0-48c4-96e1-312514ce34b9](.artifacts/records/project__check-run/rec-722bd310-6ac0-48c4-96e1-312514ce34b9.md))_

## gates-vocab-next

### Acceptance
- **gates-vocab-next**: next_step returns the first matching R4 rule string for seeded effort states including plan-review, merge, unsigned, running, ready, and discuss/plan next phase; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'gates and next_step' _(id: [rec-3724b87a-e342-4a93-ad2e-32b3dbf21060](.artifacts/records/project__acceptance/rec-3724b87a-e342-4a93-ad2e-32b3dbf21060.md))_

### Check
- **gates-vocab-next**: rec-3724b87a-e342-4a93-ad2e-32b3dbf21060; dirty; pass; tdd _(id: [rec-461ab218-714c-4e32-b5ff-b5bd26054b97](.artifacts/records/project__check-run/rec-461ab218-714c-4e32-b5ff-b5bd26054b97.md))_

## gates-vocab-prompt

### Acceptance
- **gates-vocab-prompt**: prompt(item, view) returns a ready agent string naming the effort, subject or phase, and action for each Needs you kind; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'gates and prompt' _(id: [rec-287530b8-fbf2-465a-b92d-5e699772d5de](.artifacts/records/project__acceptance/rec-287530b8-fbf2-465a-b92d-5e699772d5de.md))_

### Check
- **gates-vocab-prompt**: rec-287530b8-fbf2-465a-b92d-5e699772d5de; dirty; pass; tdd _(id: [rec-b32e7854-688c-4f90-8680-870d767ee6ee](.artifacts/records/project__check-run/rec-b32e7854-688c-4f90-8680-870d767ee6ee.md))_

## gates-vocab-quiet

### Acceptance
- **gates-vocab-quiet**: is_quiet is true when a running task's last_record_at is older than twice estimate_minutes, or 60 minutes with no estimate, and false otherwise; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'gates and quiet' _(id: [rec-0292d7ca-96a5-452c-aa18-2b9dd5029589](.artifacts/records/project__acceptance/rec-0292d7ca-96a5-452c-aa18-2b9dd5029589.md))_

### Check
- **gates-vocab-quiet**: rec-0292d7ca-96a5-452c-aa18-2b9dd5029589; dirty; pass; tdd _(id: [rec-f923fa9e-6830-4792-9fb7-223e0d9dbc54](.artifacts/records/project__check-run/rec-f923fa9e-6830-4792-9fb7-223e0d9dbc54.md))_

## goal-status-field

### Acceptance
- **goal-status-field**: A goal and position superseded with status closed are absent from handoff and dashboard views; records without status still render; tdd; workflow-loop; python3 -m pytest tests/test_goal_close.py -q _(id: [rec-1f0b047c-50e6-4c2d-8c91-10a6c7d220e0](.artifacts/records/project__acceptance/rec-1f0b047c-50e6-4c2d-8c91-10a6c7d220e0.md))_

### Check
- **goal-status-field**: rec-1f0b047c-50e6-4c2d-8c91-10a6c7d220e0; 8f1c9bbbb89ef3dc90f3fa36d00c83b924f2a721; pass; tdd _(id: [rec-700a7fec-ed34-4ade-8cb4-1f5c163aad2d](.artifacts/records/project__check-run/rec-700a7fec-ed34-4ade-8cb4-1f5c163aad2d.md))_

## handoff-by-effort

### Acceptance
- **handoff-by-effort**: A work-item and a phase position render under their effort section in handoff, not under their own subject; tdd; workflow-loop; python3 -m pytest tests/test_phase_position.py -q _(id: [rec-ca16958b-e8a5-4605-a0cd-7bf1a556bd31](.artifacts/records/project__acceptance/rec-ca16958b-e8a5-4605-a0cd-7bf1a556bd31.md))_

### Check
- **handoff-by-effort**: rec-ca16958b-e8a5-4605-a0cd-7bf1a556bd31; 8d0b7fd43309d93b0b7f2b3db0a3f8a1022e405b; pass; tdd _(id: [rec-19b91624-50af-404d-b9b4-31576913a4be](.artifacts/records/project__check-run/rec-19b91624-50af-404d-b9b4-31576913a4be.md))_

## header-chrome

### Acceptance
- **header-chrome**: Six status tabs at 120 columns read Active (3) with no leading digit, a highlighted selected word, and a dim tally; keys 1-6 still filter; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k "tab_row or tab_labels or number_keys_filter or status_tabs_are_six" _(id: [rec-82ce4065-bcee-43f2-97b2-dfd7a995d323](.artifacts/records/project__acceptance/rec-82ce4065-bcee-43f2-97b2-dfd7a995d323.md))_

### Check
- **header-chrome**: rec-c87d332c-5c16-49a9-9ebe-8991ae8c0060; dirty; pass; tdd _(id: [rec-59a00c7d-27b5-4e7d-9bba-bd5f7d6dd8aa](.artifacts/records/project__check-run/rec-59a00c7d-27b5-4e7d-9bba-bd5f7d6dd8aa.md))_
- **header-chrome**: rec-f93137e4-8a54-4459-a68a-59963e362cbd; dirty; pass; tdd _(id: [rec-c7a5b9cc-1faa-4956-90c4-3a9f401b9c70](.artifacts/records/project__check-run/rec-c7a5b9cc-1faa-4956-90c4-3a9f401b9c70.md))_
- **header-chrome**: rec-82ce4065-bcee-43f2-97b2-dfd7a995d323; dirty; pass; tdd _(id: [rec-e76b0864-a17a-42d2-a008-193fc0b2c787](.artifacts/records/project__check-run/rec-e76b0864-a17a-42d2-a008-193fc0b2c787.md))_
- **header-chrome**: rec-c5330e71-ef6d-401a-856d-dbdfdeb167d6; dirty; pass; tdd _(id: [rec-f16ee258-cdfc-4735-8a63-31e1da8c699d](.artifacts/records/project__check-run/rec-f16ee258-cdfc-4735-8a63-31e1da8c699d.md))_

## header-chrome-headers

### Acceptance
- **header-chrome-headers**: Done phase header rows show the disclosure marker and no check glyph; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k done_phases_collapse _(id: [rec-c5330e71-ef6d-401a-856d-dbdfdeb167d6](.artifacts/records/project__acceptance/rec-c5330e71-ef6d-401a-856d-dbdfdeb167d6.md))_

## header-chrome-once

### Acceptance
- **header-chrome-once**: dashboard --once prints the parenthetical tab line and the collapsed stepper; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k once_tally _(id: [rec-f93137e4-8a54-4459-a68a-59963e362cbd](.artifacts/records/project__acceptance/rec-f93137e4-8a54-4459-a68a-59963e362cbd.md))_

## header-chrome-stepper

### Acceptance
- **header-chrome-stepper**: A stepper with more than two done phases shows N done, the current phase, and one next phase, with no green check, and click expands the finished titles; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k stepper _(id: [rec-c87d332c-5c16-49a9-9ebe-8991ae8c0060](.artifacts/records/project__acceptance/rec-c87d332c-5c16-49a9-9ebe-8991ae8c0060.md))_

## heading-spacing

### Acceptance
- **heading-spacing**: Pilot test: in phase detail the line above each body heading is not blank (except the first line of the panel); the test fails before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k heading _(id: [rec-e3cb339f-2f12-42bd-9dab-4439494334aa](.artifacts/records/project__acceptance/rec-e3cb339f-2f12-42bd-9dab-4439494334aa.md))_

### Check
- **heading-spacing**: rec-e3cb339f-2f12-42bd-9dab-4439494334aa; d6f518bc2b5c2f8f4ae54c678c9ffaf5c8949b6c; pass; tdd _(id: [rec-fb47b275-bf18-4ae2-8c81-21e6ebe99fce](.artifacts/records/project__check-run/rec-fb47b275-bf18-4ae2-8c81-21e6ebe99fce.md))_

## integrate-execute

### Acceptance
- **integrate-execute**: execute-phase writes an integration-report that does not treat a git merge as pass, and test_integrate_rules.py passes.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_integrate_rules.py -q _(id: [rec-bea1bd88-8f1c-41ef-8afe-fe7f17154d84](.artifacts/records/project__acceptance/rec-bea1bd88-8f1c-41ef-8afe-fe7f17154d84.md))_

### Check
- **integrate-execute**: rec-bea1bd88-8f1c-41ef-8afe-fe7f17154d84; dirty; pass; check _(id: [rec-681e2bb6-166a-4807-b709-6831affb3963](.artifacts/records/project__check-run/rec-681e2bb6-166a-4807-b709-6831affb3963.md))_

## journal-agent

### Acceptance
- **journal-agent**: Task detail Agent work shows latest assignment, amendments, and report collapsed to 8 lines; Enter expands; o pages the focused block; earlier assignments are listed; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_journal.py tests/test_dashboard_app.py -q -k 'agent or collaps' _(id: [rec-9a1b4afe-d1e3-4cb9-949c-3869f5a0cd76](.artifacts/records/project__acceptance/rec-9a1b4afe-d1e3-4cb9-949c-3869f5a0cd76.md))_

### Check
- **journal-agent**: rec-9a1b4afe-d1e3-4cb9-949c-3869f5a0cd76; 91ae11437c0099f16a861f551d7f5811bc9c2475; pass; tdd _(id: [rec-13fd0aa7-5391-4ad3-9cb5-459f3e69b9e8](.artifacts/records/project__check-run/rec-13fd0aa7-5391-4ad3-9cb5-459f3e69b9e8.md))_

## journal-model

### Acceptance
- **journal-model**: load_journal and ordered return correct types, phase scope, open-first ordering, and one-line text for seeded stores; missing types do not error; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_journal.py -q -k 'journal and (load or order or scope or missing)' _(id: [rec-8c8cd3b5-eac9-461a-b480-58bd3af0f8fe](.artifacts/records/project__acceptance/rec-8c8cd3b5-eac9-461a-b480-58bd3af0f8fe.md))_

### Check
- **journal-model**: rec-8c8cd3b5-eac9-461a-b480-58bd3af0f8fe; 848314d1c97ebebc6edbee947927009b70f81aba; pass; tdd _(id: [rec-672d4d2c-be56-4039-be34-25ccce79ee87](.artifacts/records/project__check-run/rec-672d4d2c-be56-4039-be34-25ccce79ee87.md))_

## journal-model-kind

### Acceptance
- **journal-model-kind**: Repair and evaluate snapshots carry journal_open for the selected phase; deliver and incidental do not; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'journal and kind' _(id: [rec-ff941da0-90f7-4e86-8d29-fd9593cff4c9](.artifacts/records/project__acceptance/rec-ff941da0-90f7-4e86-8d29-fd9593cff4c9.md))_

### Check
- **journal-model-kind**: rec-ff941da0-90f7-4e86-8d29-fd9593cff4c9; 848314d1c97ebebc6edbee947927009b70f81aba; pass; tdd _(id: [rec-dde27824-3216-4173-a3b5-1600b1b62d0e](.artifacts/records/project__check-run/rec-dde27824-3216-4173-a3b5-1600b1b62d0e.md))_

## journal-panel

### Acceptance
- **journal-panel**: Repair and evaluate efforts show up to 5 open journal rows above the task table; deliver efforts show none; Enter opens detail; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py tests/test_dashboard_journal.py -q -k "panel or kind" _(id: [rec-772b35fe-ecde-4213-8bc8-f56eb55a3517](.artifacts/records/project__acceptance/rec-772b35fe-ecde-4213-8bc8-f56eb55a3517.md))_

### Check
- **journal-panel**: rec-772b35fe-ecde-4213-8bc8-f56eb55a3517; 1eb4f7a6723b779267bc14d030951640dff5c6a3; pass; tdd _(id: [rec-1dedf93f-bdc1-42af-8c2b-4456392d1757](.artifacts/records/project__check-run/rec-1dedf93f-bdc1-42af-8c2b-4456392d1757.md))_

## journal-screen

### Acceptance
- **journal-screen**: J opens the journal for the selected phase; a toggles effort scope; Esc returns; / filters; Enter opens detail; o pages with stub; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_journal.py -q -k "screen or filter or detail or pager" _(id: [rec-5ac93260-7e5b-4f29-8ea4-54b09833796f](.artifacts/records/project__acceptance/rec-5ac93260-7e5b-4f29-8ea4-54b09833796f.md))_

### Check
- **journal-screen**: rec-5ac93260-7e5b-4f29-8ea4-54b09833796f; 1eb4f7a6723b779267bc14d030951640dff5c6a3; pass; tdd _(id: [rec-7dccd89d-a08b-4e67-a264-efc93e0bc27c](.artifacts/records/project__check-run/rec-7dccd89d-a08b-4e67-a264-efc93e0bc27c.md))_

## keyboard-focus

### Acceptance
- **keyboard-focus**: Keyboard-only pilot tests move the cursor to a task below the first row and open it with enter, keep table focus after tab switch and after esc from detail, scroll to Activity with PgDn, and scroll the detail screen with arrows; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q _(id: [rec-97f2e49d-f874-4969-929c-d6c37a1ec61b](.artifacts/records/project__acceptance/rec-97f2e49d-f874-4969-929c-d6c37a1ec61b.md))_

### Check
- **keyboard-focus**: rec-97f2e49d-f874-4969-929c-d6c37a1ec61b; 2d1a3be; pass; tdd _(id: [rec-45530a2e-0c6f-4115-ad97-6032f7040919](.artifacts/records/project__check-run/rec-45530a2e-0c6f-4115-ad97-6032f7040919.md))_

### Finding
- **keyboard-focus**: Nothing focused the task table; the effort tab strip kept focus, so arrows never moved the cursor and enter always opened row 0; Real-store probe and 7 red keys-only tests before 2d1a3be; all pass after; A keys-only test fails to move or open a task after 2d1a3be; none _(id: [rec-60d1962e-aeb0-4972-8002-f424c61f615a](.artifacts/records/project__finding/rec-60d1962e-aeb0-4972-8002-f424c61f615a.md))_

## label-view-fields

### Acceptance
- **label-view-fields**: A view with label_fields true renders field: value pairs; a view without it renders exactly as before; tdd; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q _(id: [rec-0a970468-5d80-49a0-bf80-d5481a65814b](.artifacts/records/project__acceptance/rec-0a970468-5d80-49a0-bf80-d5481a65814b.md))_

### Check
- **label-view-fields**: rec-0a970468-5d80-49a0-bf80-d5481a65814b; 3ecceba31d1cb6a750fd59320ccc43bee095a686; pass; tdd _(id: [rec-8a416f43-46fb-47fc-aeb5-7d656b99024c](.artifacts/records/project__check-run/rec-8a416f43-46fb-47fc-aeb5-7d656b99024c.md))_

## loop-scenarios

### Acceptance
- **loop-scenarios**: test_evidence_loop.py drives adaptive-artifacts through the happy path to release ready, an implementation route, a no-new-evidence raise to design, a design route, a failed integration-report, insufficient evidence, and a legacy pass check-run.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_evidence_loop.py -q _(id: [rec-17e1c5a7-2e32-40d4-9df1-6d7d4f8bb488](.artifacts/records/project__acceptance/rec-17e1c5a7-2e32-40d4-9df1-6d7d4f8bb488.md))_

### Check
- **loop-scenarios**: rec-17e1c5a7-2e32-40d4-9df1-6d7d4f8bb488; dirty; pass; check _(id: [rec-2d41627d-8465-47a4-8299-fcff74f9f375](.artifacts/records/project__check-run/rec-2d41627d-8465-47a4-8299-fcff74f9f375.md))_

## matrix-model

### Acceptance
- **matrix-model**: Matrix helpers return correct row values, tone classes, release blockers, and strip glyphs for seeded evidence including no-specification phases; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_requirement.py -q -k matrix _(id: [rec-65e37e8b-25f6-4953-a8b2-9a0c0fddb74d](.artifacts/records/project__acceptance/rec-65e37e8b-25f6-4953-a8b2-9a0c0fddb74d.md))_

### Check
- **matrix-model**: rec-65e37e8b-25f6-4953-a8b2-9a0c0fddb74d; dirty; pass; tdd _(id: [rec-266fb4cc-1eed-4022-846a-12125240bfc0](.artifacts/records/project__check-run/rec-266fb4cc-1eed-4022-846a-12125240bfc0.md))_
- **matrix-model**: rec-65e37e8b-25f6-4953-a8b2-9a0c0fddb74d; dirty; pass; tdd _(id: [rec-46b9f311-d4f1-4e06-b938-eadf309eb074](.artifacts/records/project__check-run/rec-46b9f311-d4f1-4e06-b938-eadf309eb074.md))_
- **matrix-model**: rec-65e37e8b-25f6-4953-a8b2-9a0c0fddb74d; dirty; pass; tdd _(id: [rec-66ff9889-48bf-409a-a98c-f306a87278e4](.artifacts/records/project__check-run/rec-66ff9889-48bf-409a-a98c-f306a87278e4.md))_
- **matrix-model**: rec-65e37e8b-25f6-4953-a8b2-9a0c0fddb74d; dirty; pass; tdd _(id: [rec-8ab560a6-a96a-46de-b5c1-a990aaa2c1ad](.artifacts/records/project__check-run/rec-8ab560a6-a96a-46de-b5c1-a990aaa2c1ad.md))_
- **matrix-model**: rec-65e37e8b-25f6-4953-a8b2-9a0c0fddb74d; dirty; pass; tdd _(id: [rec-e4647efd-5712-41c4-9d54-cdc51014a6de](.artifacts/records/project__check-run/rec-e4647efd-5712-41c4-9d54-cdc51014a6de.md))_

## matrix-ui

### Acceptance
- **matrix-ui**: Evidence tab shows the matrix and release line; Enter opens requirement detail and Esc returns to the same row; columns drop at 55 and 40 width; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_phase_screen.py -q -k matrix _(id: [rec-e60394f4-9d3c-494c-9b2c-e69db0de52ee](.artifacts/records/project__acceptance/rec-e60394f4-9d3c-494c-9b2c-e69db0de52ee.md))_

### Check
- **matrix-ui**: rec-e60394f4-9d3c-494c-9b2c-e69db0de52ee; dirty; pass; tdd _(id: [rec-3e25e616-2a2d-4fbc-9340-b95aaa00d53a](.artifacts/records/project__check-run/rec-3e25e616-2a2d-4fbc-9340-b95aaa00d53a.md))_
- **matrix-ui**: rec-e60394f4-9d3c-494c-9b2c-e69db0de52ee; dirty; pass; tdd _(id: [rec-a4e5ad10-f2fd-4494-b365-3e042c8f98e1](.artifacts/records/project__check-run/rec-a4e5ad10-f2fd-4494-b365-3e042c8f98e1.md))_
- **matrix-ui**: rec-e60394f4-9d3c-494c-9b2c-e69db0de52ee; dirty; pass; tdd _(id: [rec-cad7ff06-72a0-4efa-9208-969a2de691f9](.artifacts/records/project__check-run/rec-cad7ff06-72a0-4efa-9208-969a2de691f9.md))_

## matrix-ui-strip

### Acceptance
- **matrix-ui-strip**: Selected structured phase shows coloured requirement glyphs after the R tally; click or e opens Evidence; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_phase_screen.py tests/test_dashboard_app.py -q -k "strip or glyph" _(id: [rec-2803f0e2-8159-46ac-90b0-d9cec7762a4a](.artifacts/records/project__acceptance/rec-2803f0e2-8159-46ac-90b0-d9cec7762a4a.md))_

### Check
- **matrix-ui-strip**: rec-2803f0e2-8159-46ac-90b0-d9cec7762a4a; dirty; pass; tdd _(id: [rec-967f4dc8-c14d-4f0f-b094-fdd4e4ed50d4](.artifacts/records/project__check-run/rec-967f4dc8-c14d-4f0f-b094-fdd4e4ed50d4.md))_

## model-fixture-reuse

### Acceptance
- **model-fixture-reuse**: Every test in tests/test_dashboard_model.py still passes and no test setup takes longer than 0.3s; check; test-suite-speed; python3 -m pytest tests/test_dashboard_model.py -q --durations=5 _(id: [rec-660d84e9-e3f2-421c-8094-db9c8427c8da](.artifacts/records/project__acceptance/rec-660d84e9-e3f2-421c-8094-db9c8427c8da.md))_

## model-fixture-reuse-total

### Acceptance
- **model-fixture-reuse-total**: The full suite wall time is under 50s (baseline 101s) and user+sys CPU time does not exceed the baseline of 58s; check; test-suite-speed; time python3 -m pytest -q _(id: [rec-db700c2c-4b03-4fb5-9aec-9517316abf2b](.artifacts/records/project__acceptance/rec-db700c2c-4b03-4fb5-9aec-9517316abf2b.md))_

## narrow-planned

### Acceptance
- **narrow-planned**: The three planned suite acceptances are phase-scoped and those work-item bodies do not say to run the full suite; check; workflow-loop; python3 -c 'import json, subprocess, sys
aa = ["python3", "/home/andrewyin/adaptive-artifacts/tools/artifacts.py", "--root", "/home/andrewyin/se-workflow"]
bad = "pytest tests -q -n 4"
subjects = ("verify-spec-view-suite", "verify-evidence-matrix-suite", "verify-journal-view-suite")
for s in subjects:
    result = subprocess.run([*aa, "list", "--type", "project:acceptance", "--subject", s, "--state", "active", "--full"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr or result.stdout
    recs = json.loads(result.stdout)["records"]
    assert len(recs) == 1, s
    cmd = recs[0]["payload"]["verify_command"]
    assert bad not in cmd, cmd
    assert " -k " in cmd, cmd
ids = ("rec-79a4e4c1-cfcb-421b-a023-64563ff645f3", "rec-8432d854-983c-4de9-bb0f-f99b94ecae9a", "rec-f04fa83f-a51f-4800-b3be-9b658df17590")
for i in ids:
    result = subprocess.run([*aa, "get", "--type", "project:work-item", "--id", i], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr or result.stdout
    body = json.loads(result.stdout)["body"].lower()
    assert "full suite" not in body, i
print("phase checks only")
' _(id: [rec-6d54e8ac-3496-44e6-beff-60a45f056733](.artifacts/records/project__acceptance/rec-6d54e8ac-3496-44e6-beff-60a45f056733.md))_

### Check
- **narrow-planned**: rec-6d54e8ac-3496-44e6-beff-60a45f056733; dirty; pass; check _(id: [rec-43c12516-0641-4a9c-940e-67524f75cb23](.artifacts/records/project__check-run/rec-43c12516-0641-4a9c-940e-67524f75cb23.md))_

## needs-you-list

### Acceptance
- **needs-you-list**: Pilot tests: n focuses the list, arrows move, enter opens the task detail for a linked item and the Needs-you detail with full text for a question, esc returns, c copies the subject; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k needs_you _(id: [rec-7c8645dc-e818-4d9d-b2d1-807437c46a90](.artifacts/records/project__acceptance/rec-7c8645dc-e818-4d9d-b2d1-807437c46a90.md))_

### Check
- **needs-you-list**: rec-7c8645dc-e818-4d9d-b2d1-807437c46a90; 206678413361ffed9978beeaac5dbc557fc5d774; pass; tdd _(id: [rec-0c7f3233-7865-46a8-abf9-dd6a6f6a6ced](.artifacts/records/project__check-run/rec-0c7f3233-7865-46a8-abf9-dd6a6f6a6ced.md))_

## needs-you-records

### Acceptance
- **needs-you-records**: Model tests show the new item fields, task linking for slug and slug-prefix subjects, and no link for effort-level questions; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k needs _(id: [rec-79256814-feaf-46b4-b5da-3c97ec0838c0](.artifacts/records/project__acceptance/rec-79256814-feaf-46b4-b5da-3c97ec0838c0.md))_

### Check
- **needs-you-records**: rec-79256814-feaf-46b4-b5da-3c97ec0838c0; fa6d87206996583b3d87e54147d655e5bddf32f5; pass; tdd _(id: [rec-a6d17cef-9df4-4b82-b9b7-3379e10d87d0](.artifacts/records/project__check-run/rec-a6d17cef-9df4-4b82-b9b7-3379e10d87d0.md))_

### Observation
- **needs-you-records**: list --full for questions, findings and check-runs keeps dashboard-status at about 0.36 s on the real store with 56 check-runs (parent timing after merge).; dashboard-features _(id: [rec-6a8a8cb5-dd1b-42c3-a8fa-8b3b5baa06f1](.artifacts/records/project__investigation-observation/rec-6a8a8cb5-dd1b-42c3-a8fa-8b3b5baa06f1.md))_

## needs-you-tab-removal

### Acceptance
- **needs-you-tab-removal**: Six status tabs on keys 1-6 with no Needs you tab; the panel title reads Needs you N for N items, including effort-level questions; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py tests/test_dashboard_view.py -q _(id: [rec-e781be72-47b4-4705-8bb4-82f57f1391ef](.artifacts/records/project__acceptance/rec-e781be72-47b4-4705-8bb4-82f57f1391ef.md))_

### Check
- **needs-you-tab-removal**: rec-e781be72-47b4-4705-8bb4-82f57f1391ef; 7fbde9ccd60decd8e171bbdd46d83d598cfd2adf; pass; tdd _(id: [rec-1d2fada7-d72d-4924-97ce-8e7317d3a0fa](.artifacts/records/project__check-run/rec-1d2fada7-d72d-4924-97ce-8e7317d3a0fa.md))_

### Observation
- **needs-you-tab-removal**: The Needs you tab matched needs-you subjects against task slugs, so effort-level questions and non-task subjects never counted and the tab disagreed with the panel.; dashboard-bugfix _(id: [rec-613913b9-0be9-46f8-a9b5-5f59739f368b](.artifacts/records/project__investigation-observation/rec-613913b9-0be9-46f8-a9b5-5f59739f368b.md))_

## package-install

### Acceptance
- **package-install**: A plugin install made with sync-plugin.sh runs bin/dashboard --once and prints a frame.; check; dashboard; d=$(mktemp -d) && bash scripts/sync-plugin.sh "$d/p" && test -d "$d/p/dashboard" && "$d/p/dashboard/bin/dashboard" --once _(id: [rec-0379e3d0-879a-4bc5-982a-7ed054623149](.artifacts/records/project__acceptance/rec-0379e3d0-879a-4bc5-982a-7ed054623149.md))_

### Check
- **package-install**: rec-67e721d5-5b8f-482f-b2d7-f9f25c8ec7e3; dirty; pass; check _(id: [rec-1480d72c-012b-4fd8-a3f6-28eb7ff34e2d](.artifacts/records/project__check-run/rec-1480d72c-012b-4fd8-a3f6-28eb7ff34e2d.md))_
- **package-install**: rec-0379e3d0-879a-4bc5-982a-7ed054623149; dirty; pass; check _(id: [rec-901438c7-6124-42ac-8f32-370c6c494f2d](.artifacts/records/project__check-run/rec-901438c7-6124-42ac-8f32-370c6c494f2d.md))_

## package-install-docs

### Acceptance
- **package-install-docs**: The README and tmux conf name no path under scripts/ for the dashboard.; check; dashboard; ! grep -nE 'scripts/(dashboard|tmux-dashboard)' README.md dashboard/tmux.conf _(id: [rec-67e721d5-5b8f-482f-b2d7-f9f25c8ec7e3](.artifacts/records/project__acceptance/rec-67e721d5-5b8f-482f-b2d7-f9f25c8ec7e3.md))_

## package-move

### Acceptance
- **package-move**: The dashboard files are in dashboard/, none remain in scripts/, and the non-tmux dashboard tests pass at the new paths.; tdd; dashboard; test ! -e scripts/dashboard_app.py && test ! -e scripts/dashboard_model.py && test ! -e scripts/artifact_store.py && uv run --with pytest --with textual pytest tests/test_dashboard_app.py tests/test_dashboard_model.py tests/test_dashboard_launcher.py tests/test_dashboard_status.py tests/test_dashboard_view.py tests/test_dashboard_integration.py _(id: [rec-976f8b89-c8c7-4ced-855d-c8c5b3c6c2fb](.artifacts/records/project__acceptance/rec-976f8b89-c8c7-4ced-855d-c8c5b3c6c2fb.md))_

### Check
- **package-move**: rec-976f8b89-c8c7-4ced-855d-c8c5b3c6c2fb; dirty; pass; tdd _(id: [rec-524596ef-2c2e-488e-acc4-0b850f58362d](.artifacts/records/project__check-run/rec-524596ef-2c2e-488e-acc4-0b850f58362d.md))_
- **package-move**: rec-976f8b89-c8c7-4ced-855d-c8c5b3c6c2fb; dirty; pass; tdd _(id: [rec-938ca635-730a-422b-88a4-cd839b708d92](.artifacts/records/project__check-run/rec-938ca635-730a-422b-88a4-cd839b708d92.md))_
- **package-move**: rec-976f8b89-c8c7-4ced-855d-c8c5b3c6c2fb; dirty; pass; tdd _(id: [rec-cb7c9400-741c-4295-8e88-22fdbc1d748f](.artifacts/records/project__check-run/rec-cb7c9400-741c-4295-8e88-22fdbc1d748f.md))_

## pane-width-stable

### Acceptance
- **pane-width-stable**: The stepper test passes 20 of 20 runs of the full app test file under -n 4, and a new test that toggles the pane scrollbar fails before the fix; tdd; dashboard; for i in $(seq 20); do uv run -q --with textual --with pytest --with pytest-xdist python -m pytest tests/test_dashboard_app.py -q -n 4 -p no:cacheprovider || break; done _(id: [rec-ef569598-f20a-4623-ba96-4f0c32edf9f1](.artifacts/records/project__acceptance/rec-ef569598-f20a-4623-ba96-4f0c32edf9f1.md))_

### Check
- **pane-width-stable**: rec-ef569598-f20a-4623-ba96-4f0c32edf9f1; 8d1ef88f88d964b4fc3a400ca293e63ac5fcf1fc; pass; tdd _(id: [rec-d3f599ae-0312-45ec-a47b-f4bcbb2dddd9](.artifacts/records/project__check-run/rec-d3f599ae-0312-45ec-a47b-f4bcbb2dddd9.md))_

### Observation
- **pane-width-stable**: Parent reran the acceptance loop on 8d1ef88: 20/20 clean, 204 passed each. Textual sends no Resize when a widget's own scrollbar toggles; the pane now refits on show_vertical_scrollbar.; dashboard-features _(id: [rec-9b177ada-79ac-4e14-b264-102f00afbf0c](.artifacts/records/project__investigation-observation/rec-9b177ada-79ac-4e14-b264-102f00afbf0c.md))_

## phase-detail-tasks

### Acceptance
- **phase-detail-tasks**: Pilot tests: in a phase detail, arrows move through tasks, enter opens the task detail, and esc returns to the phase detail; the tests fail before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k phase_task _(id: [rec-2356a60d-0eda-499f-b3ab-ee4746d6aa45](.artifacts/records/project__acceptance/rec-2356a60d-0eda-499f-b3ab-ee4746d6aa45.md))_

### Check
- **phase-detail-tasks**: rec-2356a60d-0eda-499f-b3ab-ee4746d6aa45; 1a9ce2781018b688d55b0d949f3e18a2aca70873; pass; tdd _(id: [rec-f9db072e-5521-4e3a-9f86-d1675f5f4775](.artifacts/records/project__check-run/rec-f9db072e-5521-4e3a-9f86-d1675f5f4775.md))_

### Observation
- **phase-detail-tasks**: Cherry-pick onto task-detail-links conflicted only where both added a list class (LinkList, PhaseTaskList); parent kept both; the combined app tests pass (190).; dashboard-features _(id: [rec-31107cb0-d8f3-457b-acd6-e04ed4f3508f](.artifacts/records/project__investigation-observation/rec-31107cb0-d8f3-457b-acd6-e04ed4f3508f.md))_

## phase-model-selection

### Acceptance
- **phase-model-selection**: Default phase follows most-recent activity and falls back to lowest planned or All phases; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'default or selection' _(id: [rec-02c57648-41cf-4d1c-858e-45109cf1514f](.artifacts/records/project__acceptance/rec-02c57648-41cf-4d1c-858e-45109cf1514f.md))_

### Check
- **phase-model-selection**: rec-adb086d3-8dbf-4818-9b58-2c5838a1e177; dirty; pass; tdd _(id: [rec-492e9a12-7648-4645-9172-c34fa07ecca5](.artifacts/records/project__check-run/rec-492e9a12-7648-4645-9172-c34fa07ecca5.md))_
- **phase-model-selection**: rec-02c57648-41cf-4d1c-858e-45109cf1514f; dirty; pass; tdd _(id: [rec-4e8eb412-6a6c-4406-bf19-d3179cb04cd6](.artifacts/records/project__check-run/rec-4e8eb412-6a6c-4406-bf19-d3179cb04cd6.md))_
- **phase-model-selection**: rec-20aa09a5-4b31-4a35-b9c1-c6c1847d6d81; dirty; pass; tdd _(id: [rec-c5cfe635-9a9b-4497-8f2b-5c5bfb4588e3](.artifacts/records/project__check-run/rec-c5cfe635-9a9b-4497-8f2b-5c5bfb4588e3.md))_
- **phase-model-selection**: rec-345b233d-d1c8-4b73-9dd3-8ac45c2fd412; dirty; pass; tdd _(id: [rec-d7076287-a59e-4b85-96ba-303818121b0a](.artifacts/records/project__check-run/rec-d7076287-a59e-4b85-96ba-303818121b0a.md))_

## phase-model-selection-activity

### Acceptance
- **phase-model-selection-activity**: Consecutive same-kind activity items merge into one line naming their subjects; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'activity' _(id: [rec-adb086d3-8dbf-4818-9b58-2c5838a1e177](.artifacts/records/project__acceptance/rec-adb086d3-8dbf-4818-9b58-2c5838a1e177.md))_

## phase-model-selection-follow

### Acceptance
- **phase-model-selection-follow**: Selection follows the current phase until pinned and resumes following when the current default is re-selected; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'follow or pin' _(id: [rec-20aa09a5-4b31-4a35-b9c1-c6c1847d6d81](.artifacts/records/project__acceptance/rec-20aa09a5-4b31-4a35-b9c1-c6c1847d6d81.md))_

## phase-model-selection-nophase

### Acceptance
- **phase-model-selection-nophase**: Effort with no phase records shows no selector state; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'nophase or no_phase' _(id: [rec-345b233d-d1c8-4b73-9dd3-8ac45c2fd412](.artifacts/records/project__acceptance/rec-345b233d-d1c8-4b73-9dd3-8ac45c2fd412.md))_

## phase-once-render

### Acceptance
- **phase-once-render**: dashboard/bin/dashboard --once prints selector line and wave strip for the default selection; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_integration.py -q -k 'once' _(id: [rec-65f00d59-aaa4-48e0-8f70-271787545434](.artifacts/records/project__acceptance/rec-65f00d59-aaa4-48e0-8f70-271787545434.md))_

### Check
- **phase-once-render**: rec-65f00d59-aaa4-48e0-8f70-271787545434; dirty; pass; check _(id: [rec-9dda60c8-bb7d-47e0-992b-245575ec5f5a](.artifacts/records/project__check-run/rec-9dda60c8-bb7d-47e0-992b-245575ec5f5a.md))_

## phase-position-skills

### Acceptance
- **phase-position-skills**: Skills document the per-phase position with payloads the contract accepts; skill/contract consistency tests pass; tdd; workflow-loop; python3 -m pytest tests/test_skill_contract_consistency.py tests/test_phase_position.py -q _(id: [rec-9f326a41-7f0f-4d28-89c6-069154ad5a65](.artifacts/records/project__acceptance/rec-9f326a41-7f0f-4d28-89c6-069154ad5a65.md))_

### Check
- **phase-position-skills**: rec-9f326a41-7f0f-4d28-89c6-069154ad5a65; 8d0b7fd43309d93b0b7f2b3db0a3f8a1022e405b; pass; tdd _(id: [rec-77842b73-9ccb-479a-b84e-5cfd5dab3508](.artifacts/records/project__check-run/rec-77842b73-9ccb-479a-b84e-5cfd5dab3508.md))_

## phase-reviewer-review

### Check
- **phase-reviewer-review**: rec-a5b4ff28-4664-45b7-9b25-489d4f58af19; 11a147e75daa100a2fbca2202399205b480b42e9; pass; review _(id: [rec-2b4e526d-ddb7-401f-910a-d4d5516c94f7](.artifacts/records/project__check-run/rec-2b4e526d-ddb7-401f-910a-d4d5516c94f7.md))_

## phase-sections

### Acceptance
- **phase-sections**: Model and pilot tests group tasks by phase, collapse done and planned phases, fold older done phases, toggle headers by key and click, open a phase detail with body and decisions, show awaiting sign-off, and show effort-wide progress; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py tests/test_dashboard_model.py -q _(id: [rec-611e26b5-b891-4e71-8951-3ebf07ecc715](.artifacts/records/project__acceptance/rec-611e26b5-b891-4e71-8951-3ebf07ecc715.md))_

### Check
- **phase-sections**: rec-611e26b5-b891-4e71-8951-3ebf07ecc715; 78548daa0ea66a4347d31d675b3f6fbd8c3b86f1; pass; tdd _(id: [rec-d0d98c8c-7d91-4cde-ac81-547b807803e4](.artifacts/records/project__check-run/rec-d0d98c8c-7d91-4cde-ac81-547b807803e4.md))_

## phase-selector-ui

### Acceptance
- **phase-selector-ui**: Selector line shows done count, selected phase, in-progress phases, next phase, and All phases; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'selector or stepper' _(id: [rec-39f567da-de81-428f-91b0-131cded1ec16](.artifacts/records/project__acceptance/rec-39f567da-de81-428f-91b0-131cded1ec16.md))_

### Check
- **phase-selector-ui**: rec-bc7d46e2-0d5a-4792-882a-c2afecb5d2aa; dirty; pass; tdd _(id: [rec-6967f540-a927-465b-9c37-ac1e4332e470](.artifacts/records/project__check-run/rec-6967f540-a927-465b-9c37-ac1e4332e470.md))_
- **phase-selector-ui**: rec-c0a861da-d41b-4855-b6f9-44219c1f8343; dirty; pass; tdd _(id: [rec-80c77c92-de0b-4a05-881a-2aa137bfc366](.artifacts/records/project__check-run/rec-80c77c92-de0b-4a05-881a-2aa137bfc366.md))_
- **phase-selector-ui**: rec-39f567da-de81-428f-91b0-131cded1ec16; dirty; pass; tdd _(id: [rec-a7c8ebae-b28a-4560-8fc9-8e5d5b8c338a](.artifacts/records/project__check-run/rec-a7c8ebae-b28a-4560-8fc9-8e5d5b8c338a.md))_
- **phase-selector-ui**: rec-42fa4dd1-20c6-46e2-9809-1554757d18aa; dirty; pass; tdd _(id: [rec-b5fff2fe-47da-4626-9f2b-a673f58b4d89](.artifacts/records/project__check-run/rec-b5fff2fe-47da-4626-9f2b-a673f58b4d89.md))_
- **phase-selector-ui**: rec-1c86657d-12b9-4d8f-a50b-0f751e9410ad; dirty; pass; tdd _(id: [rec-e0dcb23a-fdc2-4672-a0a1-6fb3fed9201c](.artifacts/records/project__check-run/rec-e0dcb23a-fdc2-4672-a0a1-6fb3fed9201c.md))_
- **phase-selector-ui**: rec-eb4361b5-7a63-4383-980b-e9c14c7ea07a; dirty; pass; tdd _(id: [rec-ebd4715c-321c-4a4a-9fff-473b17f03734](.artifacts/records/project__check-run/rec-ebd4715c-321c-4a4a-9fff-473b17f03734.md))_
- **phase-selector-ui**: rec-551d6d24-2144-40d6-9686-91c183e78094; dirty; pass; tdd _(id: [rec-f2398b8d-43c8-4dc8-a030-e80949839060](.artifacts/records/project__check-run/rec-f2398b8d-43c8-4dc8-a030-e80949839060.md))_

## phase-selector-ui-finished

### Acceptance
- **phase-selector-ui-finished**: f toggles finished efforts and +N finished appears; finished efforts with Needs you stay visible; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'finished or toggle' _(id: [rec-551d6d24-2144-40d6-9686-91c183e78094](.artifacts/records/project__acceptance/rec-551d6d24-2144-40d6-9686-91c183e78094.md))_

## phase-selector-ui-help

### Acceptance
- **phase-selector-ui-help**: ? shows the keys available on the current screen and focused widget; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'help or question' _(id: [rec-bc7d46e2-0d5a-4792-882a-c2afecb5d2aa](.artifacts/records/project__acceptance/rec-bc7d46e2-0d5a-4792-882a-c2afecb5d2aa.md))_

## phase-selector-ui-nav

### Acceptance
- **phase-selector-ui-nav**: [ ], ], P, and clicks select phases; picker filters and closes with Esc; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'picker or navigate or step' _(id: [rec-42fa4dd1-20c6-46e2-9809-1554757d18aa](.artifacts/records/project__acceptance/rec-42fa4dd1-20c6-46e2-9809-1554757d18aa.md))_

## phase-selector-ui-phase

### Acceptance
- **phase-selector-ui-phase**: p opens the selected phase detail, and in All phases it opens the cursor row's phase; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'phase_detail or open_phase' _(id: [rec-eb4361b5-7a63-4383-980b-e9c14c7ea07a](.artifacts/records/project__acceptance/rec-eb4361b5-7a63-4383-980b-e9c14c7ea07a.md))_

## phase-selector-ui-scope

### Acceptance
- **phase-selector-ui-scope**: Needs you and Activity stay effort-wide whatever phase is selected; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'needs or activity' _(id: [rec-c0a861da-d41b-4855-b6f9-44219c1f8343](.artifacts/records/project__acceptance/rec-c0a861da-d41b-4855-b6f9-44219c1f8343.md))_

## phase-selector-ui-wave

### Acceptance
- **phase-selector-ui-wave**: Selected phase renders a wave strip with one glyph per task per wave; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'wave_strip or wave' _(id: [rec-1c86657d-12b9-4d8f-a50b-0f751e9410ad](.artifacts/records/project__acceptance/rec-1c86657d-12b9-4d8f-a50b-0f751e9410ad.md))_

## phase-table-scope

### Acceptance
- **phase-table-scope**: Selected phase scopes task table, status counts, and progress; All phases keeps grouped sections; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_tasks.py -q -k 'scope or selected or all_phases' _(id: [rec-a6cc79a2-1384-4e47-92ba-975717a38e99](.artifacts/records/project__acceptance/rec-a6cc79a2-1384-4e47-92ba-975717a38e99.md))_

### Check
- **phase-table-scope**: rec-36bb77d4-81a1-4fcd-b04a-e0b22bf49f14; dirty; pass; tdd _(id: [rec-04c64e66-0d38-4b90-a7d5-df898eaa5c5f](.artifacts/records/project__check-run/rec-04c64e66-0d38-4b90-a7d5-df898eaa5c5f.md))_
- **phase-table-scope**: rec-a6cc79a2-1384-4e47-92ba-975717a38e99; dirty; pass; tdd _(id: [rec-846ca2ef-d789-4ccb-aad7-a5fafe8f821b](.artifacts/records/project__check-run/rec-846ca2ef-d789-4ccb-aad7-a5fafe8f821b.md))_

## phase-table-scope-sections

### Acceptance
- **phase-table-scope-sections**: All phases still folds older done phases and expands in-progress ones by default; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_tasks.py -q -k 'section' _(id: [rec-36bb77d4-81a1-4fcd-b04a-e0b22bf49f14](.artifacts/records/project__acceptance/rec-36bb77d4-81a1-4fcd-b04a-e0b22bf49f14.md))_

## plan-landing-rules

### Acceptance
- **plan-landing-rules**: plan-phase requires a Landing section with branch, worktree, base, close, and push only as a named stop before plan review, and incidental work skips it; tdd; workflow-loop; python3 -m pytest tests/test_plan_landing.py -q _(id: [rec-9f4b54cc-334e-4b5c-92fa-df0b713d662e](.artifacts/records/project__acceptance/rec-9f4b54cc-334e-4b5c-92fa-df0b713d662e.md))_

### Check
- **plan-landing-rules**: rec-9f4b54cc-334e-4b5c-92fa-df0b713d662e; dirty; pass; tdd _(id: [rec-6388f2a2-d1b0-4ff8-bdd6-202699546b5e](.artifacts/records/project__check-run/rec-6388f2a2-d1b0-4ff8-bdd6-202699546b5e.md))_

## plan-wave-rules

### Acceptance
- **plan-wave-rules**: plan-phase requires a recipe, one shared executor of inline or subagent per wave, and phase size, stops, and collision notes, and it does not open plan review until those are present; tdd; workflow-loop; python3 -m pytest tests/test_plan_wave_rules.py -q _(id: [rec-b1c39c5f-6758-426d-bdcf-0ff6c57bcbc5](.artifacts/records/project__acceptance/rec-b1c39c5f-6758-426d-bdcf-0ff6c57bcbc5.md))_

### Check
- **plan-wave-rules**: rec-b1c39c5f-6758-426d-bdcf-0ff6c57bcbc5; dirty; pass; tdd _(id: [rec-89b14150-1845-47bc-aff7-14a220d85c8d](.artifacts/records/project__check-run/rec-89b14150-1845-47bc-aff7-14a220d85c8d.md))_

## plugin-root-and-cli-review

### Check
- **plugin-root-and-cli-review**: plugin-root-and-cli-review; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; review _(id: [rec-3c873e15-1bea-4d72-a177-9f32a90677b6](.artifacts/records/project__check-run/rec-3c873e15-1bea-4d72-a177-9f32a90677b6.md))_
- **plugin-root-and-cli-review**: plugin-root-and-cli-review; 3379fcf8a1d882d91330bec6e66a2889c71d3ece; pass; review _(id: [rec-3d55b74a-4806-47bc-8350-6063559d96a2](.artifacts/records/project__check-run/rec-3d55b74a-4806-47bc-8350-6063559d96a2.md))_
- **plugin-root-and-cli-review**: plugin-root-and-cli-review; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; review _(id: [rec-7051e337-86c9-4da4-b95b-b54d42acc8d3](.artifacts/records/project__check-run/rec-7051e337-86c9-4da4-b95b-b54d42acc8d3.md))_

## plugin-root-and-cli-tier2

### Check
- **plugin-root-and-cli-tier2**: plugin-root-and-cli-tier2; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; fail; check _(id: [rec-03c48fcc-54d8-468e-a2bd-31ecdfcd48b8](.artifacts/records/project__check-run/rec-03c48fcc-54d8-468e-a2bd-31ecdfcd48b8.md))_
- **plugin-root-and-cli-tier2**: plugin-root-and-cli-tier2; 8109e9aae50c888bd17a06bfb3b8f9e2f55665ab; fail; check _(id: [rec-04c9b0b0-d9f6-46a2-ad1e-8c1ad0db624e](.artifacts/records/project__check-run/rec-04c9b0b0-d9f6-46a2-ad1e-8c1ad0db624e.md))_
- **plugin-root-and-cli-tier2**: plugin-root-and-cli-tier2; 3379fcf8a1d882d91330bec6e66a2889c71d3ece; pass; manual; user _(id: [rec-af24fcc0-9a26-4be6-9737-fa78976f6316](.artifacts/records/project__check-run/rec-af24fcc0-9a26-4be6-9737-fa78976f6316.md))_
- **plugin-root-and-cli-tier2**: plugin-root-and-cli-tier2; 3379fcf8a1d882d91330bec6e66a2889c71d3ece; fail; check _(id: [rec-cc94529d-5679-4111-8618-30f3392e2f08](.artifacts/records/project__check-run/rec-cc94529d-5679-4111-8618-30f3392e2f08.md))_

## readme-lifecycle

### Acceptance
- **readme-lifecycle**: The README states the two modes, the verify/assess split, the evidence escalation ladder, and that release ready is not deployed, and test_readme_lifecycle.py passes.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_readme_lifecycle.py -q _(id: [rec-61e95277-ed36-4e3f-9307-df5f8e946151](.artifacts/records/project__acceptance/rec-61e95277-ed36-4e3f-9307-df5f8e946151.md))_

### Check
- **readme-lifecycle**: rec-61e95277-ed36-4e3f-9307-df5f8e946151; dirty; pass; check _(id: [rec-522c9649-86e2-408e-b3e4-3effae133ab9](.artifacts/records/project__check-run/rec-522c9649-86e2-408e-b3e4-3effae133ab9.md))_

## readme-quickstart

### Acceptance
- **readme-quickstart**: The README has a Quick start section that shows the TPM plugin line and a run-shell line, and names no dashboard/tmux.conf or SE_WORKFLOW_DASHBOARD.; check; dashboard; grep -q '^## Quick start' README.md && grep -q "@plugin 'andrewy1n/se-workflow'" README.md && grep -q 'run-shell' README.md && ! grep -nE 'dashboard/tmux\.conf|SE_WORKFLOW_DASHBOARD|source-file' README.md _(id: [rec-757d4417-3c33-4df0-a29e-03c1c09bb8ad](.artifacts/records/project__acceptance/rec-757d4417-3c33-4df0-a29e-03c1c09bb8ad.md))_

### Check
- **readme-quickstart**: rec-757d4417-3c33-4df0-a29e-03c1c09bb8ad; dirty; pass; check _(id: [rec-af317ad2-59e8-4779-8b24-0e1b736e93da](.artifacts/records/project__check-run/rec-af317ad2-59e8-4779-8b24-0e1b736e93da.md))_

## recency-selection

### Acceptance
- **recency-selection**: A role with a 24h recorded_at window selects a record recorded 1h ago and skips one recorded 48h ago; a malformed window fails contract resolution; tdd; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q _(id: [rec-d854ca7d-767b-4729-92e1-18ef8853d92c](.artifacts/records/project__acceptance/rec-d854ca7d-767b-4729-92e1-18ef8853d92c.md))_

### Check
- **recency-selection**: rec-d854ca7d-767b-4729-92e1-18ef8853d92c; 6de1ff4; pass; tdd _(id: [rec-a9d8a1d2-3bb1-478b-9164-bad3436d3a9a](.artifacts/records/project__check-run/rec-a9d8a1d2-3bb1-478b-9164-bad3436d3a9a.md))_

### Observation
- **recency-selection**: View state digests hash store contents only; a recorded_at within-window role changes membership with time alone, so a digest-driven watch will not redraw when a done item ages out; watch-dashboard _(id: [rec-5b58d86c-922d-4747-8533-4f3b685d1c0d](.artifacts/records/project__investigation-observation/rec-5b58d86c-922d-4747-8533-4f3b685d1c0d.md))_

## requirement-links

### Acceptance
- **requirement-links**: Task detail lists the task's requirements and decisions, and enter on a requirement opens its requirement detail; esc returns; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and link and task' _(id: [rec-ceea1aa8-71eb-4308-925b-d17ce2d31253](.artifacts/records/project__acceptance/rec-ceea1aa8-71eb-4308-925b-d17ce2d31253.md))_

### Check
- **requirement-links**: rec-ceea1aa8-71eb-4308-925b-d17ce2d31253; dirty; pass; tdd _(id: [rec-10077915-9992-4211-8523-f34bdd4e5da7](.artifacts/records/project__check-run/rec-10077915-9992-4211-8523-f34bdd4e5da7.md))_
- **requirement-links**: rec-ceea1aa8-71eb-4308-925b-d17ce2d31253; dirty; fail; tdd _(id: [rec-555020ec-bbcd-475c-9760-afbf9ec6256d](.artifacts/records/project__check-run/rec-555020ec-bbcd-475c-9760-afbf9ec6256d.md))_

## requirement-links-needs

### Acceptance
- **requirement-links-needs**: Enter on a loop-route Needs-you item opens the requirement detail; enter on an integration item opens the Needs-you detail; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and link and needs' _(id: [rec-b6a074dd-62de-4eea-85d1-100bd193b1bc](.artifacts/records/project__acceptance/rec-b6a074dd-62de-4eea-85d1-100bd193b1bc.md))_

### Check
- **requirement-links-needs**: rec-b6a074dd-62de-4eea-85d1-100bd193b1bc; dirty; pass; tdd _(id: [rec-41a4c06e-45dd-4b42-9f74-16996cf71a7c](.artifacts/records/project__check-run/rec-41a4c06e-45dd-4b42-9f74-16996cf71a7c.md))_
- **requirement-links-needs**: rec-b6a074dd-62de-4eea-85d1-100bd193b1bc; dirty; fail; tdd _(id: [rec-4787b2de-efbe-4c32-ab5d-e4da41c61579](.artifacts/records/project__check-run/rec-4787b2de-efbe-4c32-ab5d-e4da41c61579.md))_

## requirement-links-phase

### Acceptance
- **requirement-links-phase**: Enter on a requirement in phase detail opens its requirement detail, and esc returns to the phase detail; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'evidence and link and phase' _(id: [rec-61730bf8-c287-4b79-a619-f974d0bef93d](.artifacts/records/project__acceptance/rec-61730bf8-c287-4b79-a619-f974d0bef93d.md))_

### Check
- **requirement-links-phase**: rec-61730bf8-c287-4b79-a619-f974d0bef93d; dirty; fail; tdd _(id: [rec-9c341d7e-065b-4c14-90b2-9e39a347a8f0](.artifacts/records/project__check-run/rec-9c341d7e-065b-4c14-90b2-9e39a347a8f0.md))_
- **requirement-links-phase**: rec-61730bf8-c287-4b79-a619-f974d0bef93d; dirty; pass; tdd _(id: [rec-cb97a248-814a-4806-9f3f-9896f03bb59f](.artifacts/records/project__check-run/rec-cb97a248-814a-4806-9f3f-9896f03bb59f.md))_

## requirement-screen

### Acceptance
- **requirement-screen**: Pilot tests at 60 and 120 columns show the text, status, decisions, traced tasks, acceptances with latest check and evidence kind, and history oldest first; enter on a task opens its detail and esc returns; the screen redraws after a store change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_requirement.py -q _(id: [rec-fe7cbd3d-6b76-4bf1-b258-e4fa9361b6d8](.artifacts/records/project__acceptance/rec-fe7cbd3d-6b76-4bf1-b258-e4fa9361b6d8.md))_

### Check
- **requirement-screen**: rec-fe7cbd3d-6b76-4bf1-b258-e4fa9361b6d8; dirty; pass; tdd _(id: [rec-35e6d3ed-e3ba-41c5-96b9-e142d13d297a](.artifacts/records/project__check-run/rec-35e6d3ed-e3ba-41c5-96b9-e142d13d297a.md))_

## retry-dashboard

### Acceptance
- **retry-dashboard**: Retried task rows show attempt n/budget; model/app tests with attempt_* -k filter pass; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_app.py -q -k "attempt_row or attempt_budget or attempt_snapshot or attempt_title" _(id: [rec-7bd7b9f7-ab98-40b6-9831-a074659941f7](.artifacts/records/project__acceptance/rec-7bd7b9f7-ab98-40b6-9831-a074659941f7.md))_

### Check
- **retry-dashboard**: rec-7bd7b9f7-ab98-40b6-9831-a074659941f7; 0077727e7e8d3b25e53d5aa1722b5c8f9ca58577; pass; tdd _(id: [rec-48ee479b-442e-4ce5-9c7c-d4dcdb02e4af](.artifacts/records/project__check-run/rec-48ee479b-442e-4ce5-9c7c-d4dcdb02e4af.md))_
- **retry-dashboard**: rec-7bd7b9f7-ab98-40b6-9831-a074659941f7; ee1a41be208bfdae700e1b78f9340296d82dae91; fail; tdd _(id: [rec-67c90e91-3195-4f2f-8740-ee38eb5249da](.artifacts/records/project__check-run/rec-67c90e91-3195-4f2f-8740-ee38eb5249da.md))_
- **retry-dashboard**: rec-17744c6d-ef91-4cf9-8072-298566ec8d16; 8ed3d5858b974a2fad5c321a09eb71edbd38bfb1; pass; tdd _(id: [rec-7bd4690f-7209-4c85-827e-68fd5125a8e8](.artifacts/records/project__check-run/rec-7bd4690f-7209-4c85-827e-68fd5125a8e8.md))_
- **retry-dashboard**: rec-17744c6d-ef91-4cf9-8072-298566ec8d16; ee1a41be208bfdae700e1b78f9340296d82dae91; pass; tdd _(id: [rec-867fca21-ef5a-4247-a438-bc49b8d485d5](.artifacts/records/project__check-run/rec-867fca21-ef5a-4247-a438-bc49b8d485d5.md))_
- **retry-dashboard**: rec-17744c6d-ef91-4cf9-8072-298566ec8d16; 0077727e7e8d3b25e53d5aa1722b5c8f9ca58577; pass; tdd _(id: [rec-a4506ee7-e01f-4925-8c0c-0de65f059c69](.artifacts/records/project__check-run/rec-a4506ee7-e01f-4925-8c0c-0de65f059c69.md))_

## retry-engine

### Acceptance
- **retry-engine**: test_retry_loop covers redispatch, amendment, attempts, fix_task/depends_on/no_reopen, budget exhaustion, and next_plan; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_retry_loop.py -q _(id: [rec-09626673-9f46-4904-8541-2d2d5ecaf514](.artifacts/records/project__acceptance/rec-09626673-9f46-4904-8541-2d2d5ecaf514.md))_

### Check
- **retry-engine**: rec-09626673-9f46-4904-8541-2d2d5ecaf514; ee1a41be208bfdae700e1b78f9340296d82dae91; fail; tdd _(id: [rec-a518ce34-e098-4ab4-b526-3c2be4689d66](.artifacts/records/project__check-run/rec-a518ce34-e098-4ab4-b526-3c2be4689d66.md))_
- **retry-engine**: rec-09626673-9f46-4904-8541-2d2d5ecaf514; 0077727e7e8d3b25e53d5aa1722b5c8f9ca58577; pass; tdd _(id: [rec-a9ed2230-6a8f-4a1f-9990-c2ca852598d2](.artifacts/records/project__check-run/rec-a9ed2230-6a8f-4a1f-9990-c2ca852598d2.md))_

## retry-engine-contract

### Acceptance
- **retry-engine-contract**: Optional attempts is on work-item; skill invocations stay contract-legal; consistency tests green; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_contract_self_consistency.py -q _(id: [rec-a40b0635-99ac-481f-a4fb-855a830b6fa1](.artifacts/records/project__acceptance/rec-a40b0635-99ac-481f-a4fb-855a830b6fa1.md))_

### Check
- **retry-engine-contract**: rec-a40b0635-99ac-481f-a4fb-855a830b6fa1; 0077727e7e8d3b25e53d5aa1722b5c8f9ca58577; pass; check _(id: [rec-732dbbeb-f099-4d3a-afe6-cd7f04062180](.artifacts/records/project__check-run/rec-732dbbeb-f099-4d3a-afe6-cd7f04062180.md))_

## review-approval-constraints-spec-gap

### Finding
- **review-approval-constraints-spec-gap**: spec-gap on approval-constraints: exclusive human-gate constraint wording conflicts with preserved backlog promote/dismiss writes; dashboard-human-gate-writes says only Needs-you clears; backlog.py still supersedes with @current; constraint statement names backlog promote/dismiss as allowed or exclusivity is clarified without contradicting Non-goals, and reviewer re-run passes; none _(id: [rec-d3047fa6-a5cf-4f79-8d70-3a32f5590f8f](.artifacts/records/project__finding/rec-d3047fa6-a5cf-4f79-8d70-3a32f5590f8f.md))_

## reviewer-brief

### Acceptance
- **reviewer-brief**: A test asserts the reviewer brief excludes execution-report, check-run, and assessment content; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py -q -k brief _(id: [rec-880e5caf-3938-480b-ae11-a180c0b1ed38](.artifacts/records/project__acceptance/rec-880e5caf-3938-480b-ae11-a180c0b1ed38.md))_

### Check
- **reviewer-brief**: rec-880e5caf-3938-480b-ae11-a180c0b1ed38; dirty; fail; tdd _(id: [rec-a499089a-467b-44c5-842e-b71c171071f4](.artifacts/records/project__check-run/rec-a499089a-467b-44c5-842e-b71c171071f4.md))_
- **reviewer-brief**: rec-880e5caf-3938-480b-ae11-a180c0b1ed38; f063d7aa3b3a2311a9bcfdc6973e90c5065bd145; pass; tdd _(id: [rec-df5cf3a1-37b5-49ae-bdf7-aa9daf4ce6bb](.artifacts/records/project__check-run/rec-df5cf3a1-37b5-49ae-bdf7-aa9daf4ce6bb.md))_

## reviewer-execute

### Acceptance
- **reviewer-execute**: execute-phase invokes the reviewer after closing verification and before merge; parent records method:review / evidence_kind:review check-run at head and findings for NEEDS_WORK; reviewer writes no store records; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py -q -k "execute or parent_write or review_check" _(id: [rec-10c147f9-1f69-4746-8444-72e2fe310165](.artifacts/records/project__acceptance/rec-10c147f9-1f69-4746-8444-72e2fe310165.md))_

### Check
- **reviewer-execute**: rec-10c147f9-1f69-4746-8444-72e2fe310165; dirty; fail; tdd _(id: [rec-28c1dffc-6ced-43ed-838d-1ce61d9f2acc](.artifacts/records/project__check-run/rec-28c1dffc-6ced-43ed-838d-1ce61d9f2acc.md))_
- **reviewer-execute**: rec-10c147f9-1f69-4746-8444-72e2fe310165; 2eaa40ff59e34104c88b041622de2b51b24f18e0; pass; tdd _(id: [rec-77136380-2e02-4e65-9a92-f5d3b61847f8](.artifacts/records/project__check-run/rec-77136380-2e02-4e65-9a92-f5d3b61847f8.md))_

## reviewer-execute-fix

### Acceptance
- **reviewer-execute-fix**: Fixable NEEDS_WORK creates fix work-items under the retry budget; reviewer re-runs once after fixes; exhausted budget escalates without reopening done tasks; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py -q -k "fix_task or rerun or budget" _(id: [rec-7d0c4862-c22a-4fd3-bcae-3679c065e527](.artifacts/records/project__acceptance/rec-7d0c4862-c22a-4fd3-bcae-3679c065e527.md))_

### Check
- **reviewer-execute-fix**: rec-7d0c4862-c22a-4fd3-bcae-3679c065e527; dirty; fail; tdd _(id: [rec-2cc1e133-c736-4d61-865a-bd41be2b3493](.artifacts/records/project__check-run/rec-2cc1e133-c736-4d61-865a-bd41be2b3493.md))_
- **reviewer-execute-fix**: rec-7d0c4862-c22a-4fd3-bcae-3679c065e527; 2eaa40ff59e34104c88b041622de2b51b24f18e0; pass; tdd _(id: [rec-e1b9e60d-af01-48e4-a5a2-d02e91765703](.artifacts/records/project__check-run/rec-e1b9e60d-af01-48e4-a5a2-d02e91765703.md))_

## reviewer-execute-gate

### Acceptance
- **reviewer-execute-gate**: Phase gate requires a passing review check-run at the phase head SHA before merge; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py -q -k gate _(id: [rec-4fe99528-e397-4b36-b07f-f93d2b1291f9](.artifacts/records/project__acceptance/rec-4fe99528-e397-4b36-b07f-f93d2b1291f9.md))_

### Check
- **reviewer-execute-gate**: rec-4fe99528-e397-4b36-b07f-f93d2b1291f9; dirty; fail; tdd _(id: [rec-0f807325-5bee-4853-a175-e0d84bc3f006](.artifacts/records/project__check-run/rec-0f807325-5bee-4853-a175-e0d84bc3f006.md))_
- **reviewer-execute-gate**: rec-4fe99528-e397-4b36-b07f-f93d2b1291f9; 2eaa40ff59e34104c88b041622de2b51b24f18e0; pass; tdd _(id: [rec-6042c68a-2624-42a7-8996-f9ebd5ee5766](.artifacts/records/project__check-run/rec-6042c68a-2624-42a7-8996-f9ebd5ee5766.md))_

## reviewer-execute-integration

### Acceptance
- **reviewer-execute-integration**: Integration-report body is filled from the reviewer integration section; skill/contract consistency stays green; check; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py tests/test_skill_contract_consistency.py -q -k "integration or test_skill_contract" _(id: [rec-87416dee-0be6-4e6a-bf05-d567fac451bf](.artifacts/records/project__acceptance/rec-87416dee-0be6-4e6a-bf05-d567fac451bf.md))_

### Check
- **reviewer-execute-integration**: rec-87416dee-0be6-4e6a-bf05-d567fac451bf; 2eaa40ff59e34104c88b041622de2b51b24f18e0; pass; check _(id: [rec-b69d1c07-b6e6-45d0-a8fe-29fe94c45625](.artifacts/records/project__check-run/rec-b69d1c07-b6e6-45d0-a8fe-29fe94c45625.md))_

## rj-join

### Acceptance
- **rj-join**: A fixture with two sessions and five records attaches each record correctly, marks the overlap record ambiguous on both sessions, and leaves the outside and other-project records unattached.; tdd; session-analysis; python3 -m pytest -q tests/test_record_join.py _(id: [rec-fa22cc2f-06e1-491e-a277-9c9ab01fa21e](.artifacts/records/project__acceptance/rec-fa22cc2f-06e1-491e-a277-9c9ab01fa21e.md))_

### Check
- **rj-join**: rec-fa22cc2f-06e1-491e-a277-9c9ab01fa21e; dirty; pass; tdd _(id: [rec-c6653684-ddd4-40ea-b5bf-2f494fe9e3bd](.artifacts/records/project__check-run/rec-c6653684-ddd4-40ea-b5bf-2f494fe9e3bd.md))_

## rj-record-reader

### Acceptance
- **rj-record-reader**: Stub CLI output yields metadata rows with parsed UTC times and no body text.; tdd; session-analysis; python3 -m pytest -q tests/test_record_reader.py _(id: [rec-f89ab522-1803-4881-b257-f9a885c2d0de](.artifacts/records/project__acceptance/rec-f89ab522-1803-4881-b257-f9a885c2d0de.md))_

### Check
- **rj-record-reader**: rec-f89ab522-1803-4881-b257-f9a885c2d0de; dirty; pass; tdd _(id: [rec-d0f1920c-4142-43ce-a7e2-a539e6d1ff02](.artifacts/records/project__check-run/rec-d0f1920c-4142-43ce-a7e2-a539e6d1ff02.md))_

## rj-report-records

### Acceptance
- **rj-report-records**: With --records the report adds record counts per session on a fixture, and without the flag the output is byte-identical to before.; tdd; session-analysis; python3 -m pytest -q tests/test_session_report.py _(id: [rec-193dfd71-f09c-43b5-95db-e685a4a80e4f](.artifacts/records/project__acceptance/rec-193dfd71-f09c-43b5-95db-e685a4a80e4f.md))_

### Check
- **rj-report-records**: rec-193dfd71-f09c-43b5-95db-e685a4a80e4f; dirty; pass; tdd _(id: [rec-4ba0fea6-e2d0-4a40-a875-158c1643e93b](.artifacts/records/project__check-run/rec-4ba0fea6-e2d0-4a40-a875-158c1643e93b.md))_

### Finding
- **rj-report-records**: The project-plus-time-window join leaves 70% of attached records ambiguous (386 of 553), so per-session record counts are unreliable for overlapping sessions.; Real run of session_report.py --records over 247 sessions: 8 sessions have records, 553 records attach, 386 attach to two or more sessions.; Records carry a session id, or sessions get narrower activity windows that remove the overlap.; none _(id: [rec-b8213c07-3cf9-4b56-a2a5-e9f56bd93f78](.artifacts/records/project__finding/rec-b8213c07-3cf9-4b56-a2a5-e9f56bd93f78.md))_

## route-through-discuss

### Acceptance
- **route-through-discuss**: engage, plan-phase, execute-phase and README route through discuss and the review gate; consistency tests pass; tdd; workflow-loop; python3 -m pytest tests/test_skill_contract_consistency.py tests/test_discuss_skill.py -q _(id: [rec-aac400ee-30c6-4fd2-a3ba-9fbd756f740a](.artifacts/records/project__acceptance/rec-aac400ee-30c6-4fd2-a3ba-9fbd756f740a.md))_

### Check
- **route-through-discuss**: rec-aac400ee-30c6-4fd2-a3ba-9fbd756f740a; 8c697bc88db7147f17a058311b0323cd4a191fee; pass; tdd _(id: [rec-4faad849-e58b-43c3-971c-0273f995955c](.artifacts/records/project__check-run/rec-4faad849-e58b-43c3-971c-0273f995955c.md))_

## se-reviewer-agent

### Acceptance
- **se-reviewer-agent**: agents/se-reviewer.md exists without Write/Edit tools and forbids store writes; sync-plugin.sh installs the agents/ directory; check; workflow-loop; test -f agents/se-reviewer.md && grep -qiE "no Write|without Write" agents/se-reviewer.md && grep -q agents/ scripts/sync-plugin.sh && d=$(mktemp -d) && bash scripts/sync-plugin.sh "$d/p" && test -f "$d/p/agents/se-reviewer.md" _(id: [rec-b06d589a-93d4-47e0-b2a4-5e1bf1fd8f21](.artifacts/records/project__acceptance/rec-b06d589a-93d4-47e0-b2a4-5e1bf1fd8f21.md))_

### Check
- **se-reviewer-agent**: rec-b06d589a-93d4-47e0-b2a4-5e1bf1fd8f21; f063d7aa3b3a2311a9bcfdc6973e90c5065bd145; pass; check _(id: [rec-03654543-d5c3-4c12-9c95-d11fecb0ce53](.artifacts/records/project__check-run/rec-03654543-d5c3-4c12-9c95-d11fecb0ce53.md))_
- **se-reviewer-agent**: rec-b06d589a-93d4-47e0-b2a4-5e1bf1fd8f21; f063d7aa3b3a2311a9bcfdc6973e90c5065bd145; pass; check _(id: [rec-79c540d0-ba3c-4c3f-b914-523a542dc06e](.artifacts/records/project__check-run/rec-79c540d0-ba3c-4c3f-b914-523a542dc06e.md))_

## se-workflow-check

### Acceptance
- **se-workflow-check**: se-workflow check on a throwaway store produces pass and fail check-runs with revision and runner fields through the CLI entry point; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_se_workflow_check.py -q -k "pass or fail or integration or cli" _(id: [rec-b5d23174-3de0-41c1-8cfd-028492fc5d87](.artifacts/records/project__acceptance/rec-b5d23174-3de0-41c1-8cfd-028492fc5d87.md))_

### Check
- **se-workflow-check**: rec-b5d23174-3de0-41c1-8cfd-028492fc5d87; c600c3ec9c7a7a01736618697ca4b3d5aebb9beb; pass; tdd _(id: [rec-5ece32a4-c85c-4570-a10d-bba1c2548df9](.artifacts/records/project__check-run/rec-5ece32a4-c85c-4570-a10d-bba1c2548df9.md))_

## se-workflow-check-dirty

### Acceptance
- **se-workflow-check-dirty**: Dirty pass is refused without --allow-dirty; with override the check-run has revision dirty and diff_sha256; fail may be dirty; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_se_workflow_check.py -q -k dirty _(id: [rec-6b1e869a-6b06-49a6-9d3f-33e8326e05c1](.artifacts/records/project__acceptance/rec-6b1e869a-6b06-49a6-9d3f-33e8326e05c1.md))_

### Check
- **se-workflow-check-dirty**: rec-6b1e869a-6b06-49a6-9d3f-33e8326e05c1; c600c3ec9c7a7a01736618697ca4b3d5aebb9beb; pass; tdd _(id: [rec-69f95f94-1349-4bd6-997f-edb71cbe9ad3](.artifacts/records/project__check-run/rec-69f95f94-1349-4bd6-997f-edb71cbe9ad3.md))_

## se-workflow-check-entry

### Acceptance
- **se-workflow-check-entry**: bin/se-workflow exists, sync-plugin copies bin and se_workflow, and README documents the entry point; check; workflow-loop; uv run --with pytest python -m pytest tests/test_se_workflow_check.py -q -k "entry or sync or install or bin" _(id: [rec-28b0ca39-45c6-4c7c-ac2d-bf41ba33cdf4](.artifacts/records/project__acceptance/rec-28b0ca39-45c6-4c7c-ac2d-bf41ba33cdf4.md))_

### Check
- **se-workflow-check-entry**: rec-28b0ca39-45c6-4c7c-ac2d-bf41ba33cdf4; c600c3ec9c7a7a01736618697ca4b3d5aebb9beb; pass; check _(id: [rec-8101f194-ab18-4e13-ae54-60e3565ab681](.artifacts/records/project__check-run/rec-8101f194-ab18-4e13-ae54-60e3565ab681.md))_

## se-workflow-check-manual

### Acceptance
- **se-workflow-check-manual**: se-workflow check refuses method=manual and does not write a binary check-run for it; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_se_workflow_check.py -q -k manual _(id: [rec-8eee9825-6a0d-4e05-9a8e-0d7558c7ed45](.artifacts/records/project__acceptance/rec-8eee9825-6a0d-4e05-9a8e-0d7558c7ed45.md))_

### Check
- **se-workflow-check-manual**: rec-8eee9825-6a0d-4e05-9a8e-0d7558c7ed45; c600c3ec9c7a7a01736618697ca4b3d5aebb9beb; pass; tdd _(id: [rec-20a0c965-e869-4427-949a-3f333d850bca](.artifacts/records/project__check-run/rec-20a0c965-e869-4427-949a-3f333d850bca.md))_

## se-workflow-check-runner-fields

### Acceptance
- **se-workflow-check-runner-fields**: A tdd/check check-run written by se-workflow check has result derived from the process outcome and populated revision, exit_code, duration_s, output_sha256, and runner (plus requirement/evidence_kind when present on the acceptance); tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_se_workflow_check.py -q -k "runner or fields or metadata or exit_code" _(id: [rec-7715368f-94c3-4b3d-9692-5061c4cabafe](.artifacts/records/project__acceptance/rec-7715368f-94c3-4b3d-9692-5061c4cabafe.md))_

### Check
- **se-workflow-check-runner-fields**: rec-7715368f-94c3-4b3d-9692-5061c4cabafe; c600c3ec9c7a7a01736618697ca4b3d5aebb9beb; pass; tdd _(id: [rec-e3bd1a4b-1d3a-41c2-99b0-a675670cbccd](.artifacts/records/project__check-run/rec-e3bd1a4b-1d3a-41c2-99b0-a675670cbccd.md))_

## shared-aa-resolver

### Acceptance
- **shared-aa-resolver**: Shared resolver follows env → plugin-root/sibling → PATH; home checkout is not a quiet primary fallback; both aa.py and dashboard.artifact_store use it; tdd; packaging; uv run --with pytest python -m pytest tests/test_aa_resolve.py -q _(id: [rec-15f765d5-4785-4b60-8e28-1e0c176acff4](.artifacts/records/project__acceptance/rec-15f765d5-4785-4b60-8e28-1e0c176acff4.md))_

### Check
- **shared-aa-resolver**: rec-15f765d5-4785-4b60-8e28-1e0c176acff4; dirty; fail; tdd _(id: [rec-570c80b2-13ad-4e0c-ad09-ddb8e3f82bb7](.artifacts/records/project__check-run/rec-570c80b2-13ad-4e0c-ad09-ddb8e3f82bb7.md))_
- **shared-aa-resolver**: rec-15f765d5-4785-4b60-8e28-1e0c176acff4; 23c6f922d2a051135dc323f67924f2364b3788db; pass; tdd _(id: [rec-5a71810f-915b-4628-b05b-538d32faa74b](.artifacts/records/project__check-run/rec-5a71810f-915b-4628-b05b-538d32faa74b.md))_
- **shared-aa-resolver**: rec-15f765d5-4785-4b60-8e28-1e0c176acff4; dirty; fail; tdd _(id: [rec-a9a1ceb3-58a7-4c54-bbf5-c3e778574d60](.artifacts/records/project__check-run/rec-a9a1ceb3-58a7-4c54-bbf5-c3e778574d60.md))_

## skill-needs-clear

### Acceptance
- **skill-needs-clear**: kinds-and-focus and engage document human-dismissible clears and remind-without-gate; skills that open those gates document the matching clear; contract consistency and skill doc tests pass; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_discuss_skill.py -q _(id: [rec-0e2c47f2-f119-466d-8e46-fe961b604d3b](.artifacts/records/project__acceptance/rec-0e2c47f2-f119-466d-8e46-fe961b604d3b.md))_

### Check
- **skill-needs-clear**: rec-0e2c47f2-f119-466d-8e46-fe961b604d3b; 8799ca930443a9a3144434eaf3b9e30e497adbce; pass; tdd _(id: [rec-dfedfe05-c9f6-436d-a9cb-10752f198063](.artifacts/records/project__check-run/rec-dfedfe05-c9f6-436d-a9cb-10752f198063.md))_

### Observation
- **skill-needs-clear**: kinds-and-focus and engage lacked Needs-you clear/remind; gate-opening skills lacked clear CLIs; supersede for findings is illegal at runtime; workflow-loop _(id: [rec-3e2848ab-45e5-46ae-8087-757079a4cb07](.artifacts/records/project__investigation-observation/rec-3e2848ab-45e5-46ae-8087-757079a4cb07.md))_

### Finding
- **skill-needs-clear**: Skills opened human Needs-you gates without documenting clear-at-event CLI and engage remind; finding clear must be update needs none not supersede; pre-fix skill text and failing doc assertions; runtime rejects finding supersede; kinds-and-focus/engage and gate skills document clears including update needs none and tests stay green; none _(id: [rec-2d62de79-b64c-433f-b4ba-55c9612ba420](.artifacts/records/project__finding/rec-2d62de79-b64c-433f-b4ba-55c9612ba420.md))_

## skill-needs-clear-engage

### Acceptance
- **skill-needs-clear-engage**: engage skill text lists open human-dismissible Needs-you for the focus and does not block routing on them; check; workflow-loop; uv run --with pytest python -m pytest tests/test_discuss_skill.py -q -k engage _(id: [rec-152ce4a8-e20f-4b8c-87b9-aaf30fb53703](.artifacts/records/project__acceptance/rec-152ce4a8-e20f-4b8c-87b9-aaf30fb53703.md))_

### Check
- **skill-needs-clear-engage**: rec-152ce4a8-e20f-4b8c-87b9-aaf30fb53703; 8799ca930443a9a3144434eaf3b9e30e497adbce; pass; check _(id: [rec-8a447353-10e5-4b7f-bc4c-76b7c2f1ea8f](.artifacts/records/project__check-run/rec-8a447353-10e5-4b7f-bc4c-76b7c2f1ea8f.md))_

## skill-needs-clear-opens

### Acceptance
- **skill-needs-clear-opens**: discuss, plan-phase, verify-work, and execute-phase document the clear command next to each human-gate they open; check; workflow-loop; uv run --with pytest python -m pytest tests/test_discuss_skill.py tests/test_skill_contract_consistency.py -q _(id: [rec-e154ee7d-d057-4d26-bd3e-9962592157f0](.artifacts/records/project__acceptance/rec-e154ee7d-d057-4d26-bd3e-9962592157f0.md))_

### Check
- **skill-needs-clear-opens**: rec-e154ee7d-d057-4d26-bd3e-9962592157f0; 8799ca930443a9a3144434eaf3b9e30e497adbce; pass; check _(id: [rec-91b822ea-acd7-4c65-81d6-fa35a64f4129](.artifacts/records/project__check-run/rec-91b822ea-acd7-4c65-81d6-fa35a64f4129.md))_

## skill-plugin-paths

### Acceptance
- **skill-plugin-paths**: ensure-store documents CLAUDE_PLUGIN_ROOT and CURSOR_PLUGIN_ROOT; Plugin root section does not hardcode ~/.cursor/plugins/local/se-workflow as a numbered step; check; packaging; grep -q CLAUDE_PLUGIN_ROOT skills/ensure-store.md && grep -q CURSOR_PLUGIN_ROOT skills/ensure-store.md && ! grep -E '^[0-9]+\. .*\.cursor/plugins/local/se-workflow' skills/ensure-store.md _(id: [rec-1dc4bf40-0968-4e85-845f-c345a81a9768](.artifacts/records/project__acceptance/rec-1dc4bf40-0968-4e85-845f-c345a81a9768.md))_

### Check
- **skill-plugin-paths**: rec-1dc4bf40-0968-4e85-845f-c345a81a9768; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; check _(id: [rec-3d166850-209a-42d1-85c0-d13eebf7102a](.artifacts/records/project__check-run/rec-3d166850-209a-42d1-85c0-d13eebf7102a.md))_

## skill-plugin-paths-close

### Acceptance
- **skill-plugin-paths-close**: verify-work documents se-workflow close-batch and does not call scripts/close_batch.py; check; packaging; grep -qE "se-workflow close-batch|bin/se-workflow close-batch" skills/verify-work/SKILL.md && ! grep -q scripts/close_batch.py skills/verify-work/SKILL.md _(id: [rec-05718b54-2ff0-42df-9d90-5563f4509289](.artifacts/records/project__acceptance/rec-05718b54-2ff0-42df-9d90-5563f4509289.md))_

### Check
- **skill-plugin-paths-close**: rec-05718b54-2ff0-42df-9d90-5563f4509289; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; check _(id: [rec-2fd379a5-8ec6-415d-b321-f9aa2fd3e4e5](.artifacts/records/project__check-run/rec-2fd379a5-8ec6-415d-b321-f9aa2fd3e4e5.md))_

## skill-plugin-paths-contract

### Acceptance
- **skill-plugin-paths-contract**: skill/contract consistency passes after skill edits; check; packaging; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py -q _(id: [rec-3b720bda-fcdb-4cab-9cb2-e965636a73b0](.artifacts/records/project__acceptance/rec-3b720bda-fcdb-4cab-9cb2-e965636a73b0.md))_

### Check
- **skill-plugin-paths-contract**: rec-3b720bda-fcdb-4cab-9cb2-e965636a73b0; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; check _(id: [rec-3ca9c3cb-a02a-47bf-9ac9-79d2bf5d2a00](.artifacts/records/project__check-run/rec-3ca9c3cb-a02a-47bf-9ac9-79d2bf5d2a00.md))_

## skills-backlog

### Acceptance
- **skills-backlog**: engage and README still say do not collect or create feedback, and document backlog-item list/create/promote; skill/contract consistency passes for every adaptive-artifacts invocation added; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_assess_routing.py -q _(id: [rec-95459f66-4633-441b-a73b-d1aa7b68957a](.artifacts/records/project__acceptance/rec-95459f66-4633-441b-a73b-d1aa7b68957a.md))_

### Check
- **skills-backlog**: rec-95459f66-4633-441b-a73b-d1aa7b68957a; cdb10d65ed56a425a426d5c291c0f5c1a8e69b71; pass; check _(id: [rec-e8570fcb-09a4-4c71-92bd-8d44ce81ac88](.artifacts/records/project__check-run/rec-e8570fcb-09a4-4c71-92bd-8d44ce81ac88.md))_

## skills-backlog-promote

### Acceptance
- **skills-backlog-promote**: engage documents promote as supersede to promoted then discuss/new phase or incidental, and dismiss as supersede to dismissed, with no GitHub scrape; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_assess_routing.py -q _(id: [rec-9dcc1726-0246-424d-a8f7-edd8b8c98ea6](.artifacts/records/project__acceptance/rec-9dcc1726-0246-424d-a8f7-edd8b8c98ea6.md))_

### Check
- **skills-backlog-promote**: rec-9dcc1726-0246-424d-a8f7-edd8b8c98ea6; cdb10d65ed56a425a426d5c291c0f5c1a8e69b71; pass; check _(id: [rec-0821a163-8752-41df-a60a-9421a9b67f50](.artifacts/records/project__check-run/rec-0821a163-8752-41df-a60a-9421a9b67f50.md))_

## skills-red-first

### Acceptance
- **skills-red-first**: verify-work documents enforced red-first close fields and refusal; skill/contract consistency stays green; wording no longer says the engine does not enforce red-first; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_assess_routing.py -q _(id: [rec-4106666c-c561-474e-a8fd-4291869e42db](.artifacts/records/project__acceptance/rec-4106666c-c561-474e-a8fd-4291869e42db.md))_

### Check
- **skills-red-first**: rec-4106666c-c561-474e-a8fd-4291869e42db; c14dedbd9ec027e7e79b8eb1508b24d0d65063fc; pass; check _(id: [rec-5b667532-d22d-4457-9115-c3258f78d31b](.artifacts/records/project__check-run/rec-5b667532-d22d-4457-9115-c3258f78d31b.md))_

## spec-model

### Acceptance
- **spec-model**: tabs_for returns full tabs for a structured phase and Overview/Spec/Decisions/Tasks for a simple phase or missing specification type; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'phase_screen and tabs' _(id: [rec-7d44b243-444f-4d8f-a42d-2d8bce0f9b6d](.artifacts/records/project__acceptance/rec-7d44b243-444f-4d8f-a42d-2d8bce0f9b6d.md))_

### Check
- **spec-model**: rec-7d44b243-444f-4d8f-a42d-2d8bce0f9b6d; dirty; pass; tdd _(id: [rec-854cf41f-e189-49ae-8b52-af9acd8b9163](.artifacts/records/project__check-run/rec-854cf41f-e189-49ae-8b52-af9acd8b9163.md))_

## spec-model-decisions

### Acceptance
- **spec-model-decisions**: load_decision_log returns phase-scoped active decisions, effort groups in ordinal order when phase is None, and superseded entries under successors when history is true; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'phase_screen and decision' _(id: [rec-403cd5dd-db5b-4e68-b04b-311599c18032](.artifacts/records/project__acceptance/rec-403cd5dd-db5b-4e68-b04b-311599c18032.md))_

### Check
- **spec-model-decisions**: rec-403cd5dd-db5b-4e68-b04b-311599c18032; dirty; pass; tdd _(id: [rec-f53066b4-a3ab-453b-a694-a647380fda14](.artifacts/records/project__check-run/rec-f53066b4-a3ab-453b-a694-a647380fda14.md))_

## spec-model-simple

### Acceptance
- **spec-model-simple**: A simple phase's detail carries phase body and constraints for the Spec tab and empty design body; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'phase_screen and simple' _(id: [rec-0227d202-cb23-4c79-97e0-d7d58c3bb952](.artifacts/records/project__acceptance/rec-0227d202-cb23-4c79-97e0-d7d58c3bb952.md))_

### Check
- **spec-model-simple**: rec-0227d202-cb23-4c79-97e0-d7d58c3bb952; dirty; pass; tdd _(id: [rec-08a91db0-b1de-4066-bcd3-3190cd6967b2](.artifacts/records/project__check-run/rec-08a91db0-b1de-4066-bcd3-3190cd6967b2.md))_

## spec-pager

### Acceptance
- **spec-pager**: With glow absent and $PAGER set to a stub, the helper writes the tab text outside the store, the stub receives it, and the file is deleted afterwards; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_phase_screen.py tests/test_dashboard_pager.py -q -k pager _(id: [rec-05a167b0-042f-4057-b1a0-82dd15d96cbf](.artifacts/records/project__acceptance/rec-05a167b0-042f-4057-b1a0-82dd15d96cbf.md))_

### Check
- **spec-pager**: rec-05a167b0-042f-4057-b1a0-82dd15d96cbf; dirty; pass; tdd _(id: [rec-084043c2-20ee-4927-9e82-c4bf81e31a57](.artifacts/records/project__check-run/rec-084043c2-20ee-4927-9e82-c4bf81e31a57.md))_

## spec-screen

### Acceptance
- **spec-screen**: Phase screen shows the correct tab set; p/s/e open Overview/Spec/Evidence from the main screen; left/right and letter keys switch tabs; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_phase_screen.py -q -k "tab or open or key" _(id: [rec-b864e9ae-db02-462b-ae3a-227f4fdf5f0b](.artifacts/records/project__acceptance/rec-b864e9ae-db02-462b-ae3a-227f4fdf5f0b.md))_

### Check
- **spec-screen**: rec-b864e9ae-db02-462b-ae3a-227f4fdf5f0b; dirty; pass; tdd _(id: [rec-001af826-6491-4f9e-b224-e9be808fe140](.artifacts/records/project__check-run/rec-001af826-6491-4f9e-b224-e9be808fe140.md))_

## spec-screen-content

### Acceptance
- **spec-screen-content**: Spec and Design render full Markdown; requirement rows open detail; Decisions expand with a/h toggles; Evidence and Tasks match today; Esc returns to the same tab and row; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_phase_screen.py -q -k "spec or design or decision or evidence or task or esc" _(id: [rec-fb12c32d-c03a-47d3-8f10-bff1fa09e822](.artifacts/records/project__acceptance/rec-fb12c32d-c03a-47d3-8f10-bff1fa09e822.md))_

### Check
- **spec-screen-content**: rec-fb12c32d-c03a-47d3-8f10-bff1fa09e822; dirty; pass; tdd _(id: [rec-579a1572-3f30-4d70-b1c2-ddf4a1826b5e](.artifacts/records/project__check-run/rec-579a1572-3f30-4d70-b1c2-ddf4a1826b5e.md))_

## spec-screen-pager

### Acceptance
- **spec-screen-pager**: o on the phase screen pages the current tab through the stubbed pager and removes the temp file; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_phase_screen.py -q -k pager _(id: [rec-2c20fcfa-8ea0-4f55-b8ba-0fadcb3fe9b0](.artifacts/records/project__acceptance/rec-2c20fcfa-8ea0-4f55-b8ba-0fadcb3fe9b0.md))_

### Check
- **spec-screen-pager**: rec-2c20fcfa-8ea0-4f55-b8ba-0fadcb3fe9b0; dirty; pass; tdd _(id: [rec-5e7aff7f-586e-4bca-8339-b35891a0eb27](.artifacts/records/project__check-run/rec-5e7aff7f-586e-4bca-8339-b35891a0eb27.md))_

## specify-design

### Acceptance
- **specify-design**: discuss creates a specification and a design with the contract's required fields, and test_discuss_skill.py passes.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_discuss_skill.py -q _(id: [rec-7683d746-1d29-4de5-bc76-3bdcc678f158](.artifacts/records/project__acceptance/rec-7683d746-1d29-4de5-bc76-3bdcc678f158.md))_

### Check
- **specify-design**: rec-7683d746-1d29-4de5-bc76-3bdcc678f158; dirty; pass; check _(id: [rec-871a92d2-51c9-4d46-babe-ea58c9695e02](.artifacts/records/project__check-run/rec-871a92d2-51c9-4d46-babe-ea58c9695e02.md))_

## status-line-from-snapshot

### Acceptance
- **status-line-from-snapshot**: For a seeded store, every status line names an effort in the app snapshot with matching counts, and an effort with no goal prints nothing; the test fails before the fix; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_status.py -q _(id: [rec-fb5c210c-4e78-42c4-8fb9-f8f585e3f5f8](.artifacts/records/project__acceptance/rec-fb5c210c-4e78-42c4-8fb9-f8f585e3f5f8.md))_

### Check
- **status-line-from-snapshot**: rec-fb5c210c-4e78-42c4-8fb9-f8f585e3f5f8; afd60845e9ffcfcd44d028603b46bdcffadc313a; pass; tdd _(id: [rec-dc270731-1127-4bab-9491-3793856d02ff](.artifacts/records/project__check-run/rec-dc270731-1127-4bab-9491-3793856d02ff.md))_

### Observation
- **status-line-from-snapshot**: dashboard-status listed efforts from the contract dashboard view (grouped by work-item effort) while the app lists efforts with an active goal, so goal-less efforts appeared only in the status line.; dashboard-bugfix _(id: [rec-34b1b626-5692-42e3-87e5-d7c8562d6cf5](.artifacts/records/project__investigation-observation/rec-34b1b626-5692-42e3-87e5-d7c8562d6cf5.md))_

## status-tab-row

### Acceptance
- **status-tab-row**: Pilot tests: six tabs on one row at 120 columns, wrapped at 60, each label starts with its number key; the tests fail before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k tab_row _(id: [rec-ba223a32-d09b-4dd0-9256-101bd04d0ea1](.artifacts/records/project__acceptance/rec-ba223a32-d09b-4dd0-9256-101bd04d0ea1.md))_

### Check
- **status-tab-row**: rec-ba223a32-d09b-4dd0-9256-101bd04d0ea1; ee6469389256ef6d9cf8f8e9c80cd93ef5fcb5aa; pass; tdd _(id: [rec-146b610c-0238-4e4b-9049-a5bb6d569c98](.artifacts/records/project__check-run/rec-146b610c-0238-4e4b-9049-a5bb6d569c98.md))_

## status-tabs

### Acceptance
- **status-tabs**: Pilot tests at 60 and 120 columns show counts on every tab, default to Active, filter the table by each tab via keys and click, show Needs you tasks from open items, combine with the / filter, and have no d binding; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q _(id: [rec-5a31e5b1-1af0-4738-bf89-20d16bf3dcaa](.artifacts/records/project__acceptance/rec-5a31e5b1-1af0-4738-bf89-20d16bf3dcaa.md))_

### Check
- **status-tabs**: rec-5a31e5b1-1af0-4738-bf89-20d16bf3dcaa; 75e530c1e06c4584efe45adfad12d926e8843849; pass; check _(id: [rec-0734553d-7a25-4dd7-af9b-6ef24e128a1d](.artifacts/records/project__check-run/rec-0734553d-7a25-4dd7-af9b-6ef24e128a1d.md))_
- **status-tabs**: rec-5a31e5b1-1af0-4738-bf89-20d16bf3dcaa; f6153cee88400795bfb23fb4d0d97e48e69438c9; pass; check _(id: [rec-4bb08f27-39d2-46a7-9b11-69a848dc6b79](.artifacts/records/project__check-run/rec-4bb08f27-39d2-46a7-9b11-69a848dc6b79.md))_

### Finding
- **status-tabs**: status-tabs gap closed: 7 tabs, keys 1-7, left/right and README landed at 75e530c; Execution report rec-10a142d4 and a parent re-run of 116 passing tests at 75e530c; A tab, key or README row from the description is missing; none _(id: [rec-94362ae8-0f01-4ad1-bfcd-cffa426566b8](.artifacts/records/project__finding/rec-94362ae8-0f01-4ad1-bfcd-cffa426566b8.md))_

## status-tabs-fixture

### Acceptance
- **status-tabs-fixture**: status-tabs fixture yields NEEDS_WORK with a spec-gap finding; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py -q -k status_tabs _(id: [rec-a6aabc11-4cb5-47dd-84da-5c01fd225ab5](.artifacts/records/project__acceptance/rec-a6aabc11-4cb5-47dd-84da-5c01fd225ab5.md))_

### Check
- **status-tabs-fixture**: rec-a6aabc11-4cb5-47dd-84da-5c01fd225ab5; dirty; fail; tdd _(id: [rec-08bd8014-2867-4ca6-931c-09db1591de04](.artifacts/records/project__check-run/rec-08bd8014-2867-4ca6-931c-09db1591de04.md))_
- **status-tabs-fixture**: rec-a6aabc11-4cb5-47dd-84da-5c01fd225ab5; 11a147e75daa100a2fbca2202399205b480b42e9; pass; tdd _(id: [rec-925cc63c-17c3-4ab7-8b23-b9c66e8e0c93](.artifacts/records/project__check-run/rec-925cc63c-17c3-4ab7-8b23-b9c66e8e0c93.md))_

## stepper-wrap

### Acceptance
- **stepper-wrap**: Pilot test at 60 columns: every stepper line starts with a phase glyph and no line ends with a bare glyph, and no line is wider than the pane; the test fails before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k stepper _(id: [rec-c2df3f61-8b0b-44d8-89b3-f3033ebcf9d0](.artifacts/records/project__acceptance/rec-c2df3f61-8b0b-44d8-89b3-f3033ebcf9d0.md))_

### Check
- **stepper-wrap**: rec-c2df3f61-8b0b-44d8-89b3-f3033ebcf9d0; 0ec0a8bb801ff9f528cfd6366bd5c08208282ff4; pass; tdd _(id: [rec-6a6b6040-193a-42e4-b5fc-4bab45d162e8](.artifacts/records/project__check-run/rec-6a6b6040-193a-42e4-b5fc-4bab45d162e8.md))_

### Observation
- **stepper-wrap**: test_stepper_wraps_by_pane_width_and_keeps_glyph_with_label failed 3/10: stepper lines were wider than pane.scrollable_content_region.width. Hypothesis: the status-tab grid wraps, the pane overflows 20 rows, a vertical scrollbar appears after the stepper rendered, narrowing the content region without a pane resize, so EffortPane.on_resize never re-shows.; dashboard-features _(id: [rec-b3951803-56a0-4f76-aefb-68962a329e8a](.artifacts/records/project__investigation-observation/rec-b3951803-56a0-4f76-aefb-68962a329e8a.md))_

## table-focus

### Acceptance
- **table-focus**: Pick an empty tab, pick Active, press down: the cursor is on row 1 and enter opens that row; the test fails before the fix; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k focus _(id: [rec-2536ed50-f949-40fe-a914-f283c9633975](.artifacts/records/project__acceptance/rec-2536ed50-f949-40fe-a914-f283c9633975.md))_

### Check
- **table-focus**: rec-2536ed50-f949-40fe-a914-f283c9633975; 1aeb3058d93fa9ac486dd0d6de690d7c0d681388; pass; tdd _(id: [rec-d9988bf2-7166-422b-beb2-94ee365a1a0b](.artifacts/records/project__check-run/rec-d9988bf2-7166-422b-beb2-94ee365a1a0b.md))_

### Observation
- **table-focus**: After an empty status tab hides #tasks, a tab that shows it again leaves app.focused None; arrows do nothing and enter opens row 0. Root cause: select_status_tab never refocuses the table after fill_tasks hides it.; dashboard-bugfix _(id: [rec-2c0c2c80-ff18-40fe-801a-e3f95f11e0e0](.artifacts/records/project__investigation-observation/rec-2c0c2c80-ff18-40fe-801a-e3f95f11e0e0.md))_

## task-commit

### Acceptance
- **task-commit**: execute-phase documents a commit per task on the phase branch before verify, and the dedicated tests for that rule pass; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_task_commit.py tests/test_execute_landing.py tests/test_skill_contract_consistency.py -q -k 'commit or landing or task_commit' _(id: [rec-34f5bd84-dee8-4fa6-bf3a-1f646de23f5e](.artifacts/records/project__acceptance/rec-34f5bd84-dee8-4fa6-bf3a-1f646de23f5e.md))_

### Check
- **task-commit**: rec-34f5bd84-dee8-4fa6-bf3a-1f646de23f5e; 4ba5a390c79e1a6841c74467844b029055941985; pass; tdd _(id: [rec-116c845e-beb1-492c-bd63-156a5ccba707](.artifacts/records/project__check-run/rec-116c845e-beb1-492c-bd63-156a5ccba707.md))_

## task-detail-links

### Acceptance
- **task-detail-links**: Pilot tests: in a task detail, enter on a dependency opens that task, enter on a blocked task opens it, enter on the phase opens the phase detail, and esc walks back one screen at a time; the tests fail before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k link _(id: [rec-79b9e2f6-49a8-4d48-8788-0da94d698726](.artifacts/records/project__acceptance/rec-79b9e2f6-49a8-4d48-8788-0da94d698726.md))_

### Check
- **task-detail-links**: rec-79b9e2f6-49a8-4d48-8788-0da94d698726; f1d91299f3812c61327da0d352b1541bebdc0d38; pass; tdd _(id: [rec-3c74b663-3b9f-4872-b3ef-a3e4e8acec7a](.artifacts/records/project__check-run/rec-3c74b663-3b9f-4872-b3ef-a3e4e8acec7a.md))_

## task-detail-model

### Acceptance
- **task-detail-model**: Tests against a temp store show the loader returns the work-item, dependency links, acceptances with their latest check-run, the ordered timeline with report bodies, and related findings, and ignores another task whose slug shares a prefix; tdd; dashboard; python3 -m pytest tests/test_dashboard_model.py -q _(id: [rec-8f020a2f-f7de-43e3-b46f-423d52e44fe4](.artifacts/records/project__acceptance/rec-8f020a2f-f7de-43e3-b46f-423d52e44fe4.md))_

### Check
- **task-detail-model**: rec-8f020a2f-f7de-43e3-b46f-423d52e44fe4; 38c2399; pass; tdd _(id: [rec-93b50136-8ef3-4e78-a5fd-29d38ee008b8](.artifacts/records/project__check-run/rec-93b50136-8ef3-4e78-a5fd-29d38ee008b8.md))_

## task-detail-module

### Acceptance
- **task-detail-module**: TaskDetailScreen is defined in dashboard/task_detail.py, not app.py, and the dashboard app tests pass.; tdd; dashboard; ! grep -n '^class TaskDetailScreen' dashboard/app.py && grep -c '^class TaskDetailScreen' dashboard/task_detail.py && uv run --with pytest --with textual pytest tests/test_dashboard_app.py _(id: [rec-7f83addf-fb83-4129-9116-b02371346c5d](.artifacts/records/project__acceptance/rec-7f83addf-fb83-4129-9116-b02371346c5d.md))_

### Check
- **task-detail-module**: rec-7f83addf-fb83-4129-9116-b02371346c5d; dirty; pass; tdd _(id: [rec-cc977b6d-5388-4c49-b3e7-edb62496015a](.artifacts/records/project__check-run/rec-cc977b6d-5388-4c49-b3e7-edb62496015a.md))_

## task-detail-screen

### Acceptance
- **task-detail-screen**: Textual pilot tests at 60 and 160 columns open the detail screen by Enter and by click, find every section's content for a seeded task, see a redraw after a store change, and return to the same row on Esc; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q _(id: [rec-421586f5-5f49-4a47-b715-eeb09ad69b90](.artifacts/records/project__acceptance/rec-421586f5-5f49-4a47-b715-eeb09ad69b90.md))_

### Check
- **task-detail-screen**: rec-421586f5-5f49-4a47-b715-eeb09ad69b90; e6cf774; pass; tdd _(id: [rec-d4342ee2-0473-4fa8-b8b8-4abc42c914ec](.artifacts/records/project__check-run/rec-d4342ee2-0473-4fa8-b8b8-4abc42c914ec.md))_

## task-list-filters

### Acceptance
- **task-list-filters**: Pilot tests at 60 and 120 columns narrow the table by typed text, clear it with Esc, hide and show done tasks with d, keep both across a store refresh, and show them in the panel title; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q _(id: [rec-982fcf31-6ef8-41aa-97a6-03ec860bfccb](.artifacts/records/project__acceptance/rec-982fcf31-6ef8-41aa-97a6-03ec860bfccb.md))_

### Check
- **task-list-filters**: rec-982fcf31-6ef8-41aa-97a6-03ec860bfccb; e3b7751; pass; tdd _(id: [rec-faa84f50-9fb4-422a-b887-7877e889ac3b](.artifacts/records/project__check-run/rec-faa84f50-9fb4-422a-b887-7877e889ac3b.md))_

## task-row-cells

### Acceptance
- **task-row-cells**: Pilot tests: a waiting row shows waits on with its unfinished dependencies, a running row shows its running time, the task detail shows it, and the grouped table has no phase column at 60 and 120 columns; the tests fail before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'waits or running or phase_column' _(id: [rec-daa1a988-73f2-45f9-8cde-f795662613c1](.artifacts/records/project__acceptance/rec-daa1a988-73f2-45f9-8cde-f795662613c1.md))_

### Check
- **task-row-cells**: rec-daa1a988-73f2-45f9-8cde-f795662613c1; ef6325fb4ef1128ad071f79e64d709bd1d28781d; pass; tdd _(id: [rec-79370462-4380-4f9b-94d2-a90ed8569ee7](.artifacts/records/project__check-run/rec-79370462-4380-4f9b-94d2-a90ed8569ee7.md))_

## task-row-model

### Acceptance
- **task-row-model**: Model tests: waits_on lists only unfinished dependency slugs, running_since is the latest assignment time for an in-progress task and None otherwise; the tests fail before the change; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'waits or running' _(id: [rec-60e78986-208c-43d5-8207-9803afeab4df](.artifacts/records/project__acceptance/rec-60e78986-208c-43d5-8207-9803afeab4df.md))_

### Check
- **task-row-model**: rec-60e78986-208c-43d5-8207-9803afeab4df; 865fc75f021559acf6184b145f73f5b8ca57c313; pass; tdd _(id: [rec-f112e2ec-e4d3-46b7-9e18-40531b7f5da2](.artifacts/records/project__check-run/rec-f112e2ec-e4d3-46b7-9e18-40531b7f5da2.md))_

### Observation
- **task-row-model**: Withdrawn dependencies stay in waits_on, matching the engine: derived.ready only treats done as satisfied, so the task really is still waiting.; dashboard-features _(id: [rec-a6aba57e-2094-4cc5-9145-31dccbf7f288](.artifacts/records/project__investigation-observation/rec-a6aba57e-2094-4cc5-9145-31dccbf7f288.md))_

## task-table-module

### Acceptance
- **task-table-module**: The task table, filter, section and cell code is defined in dashboard/tasks.py, not app.py, and the dashboard app tests pass.; tdd; dashboard; ! grep -nE '^(class TaskFilter|class SectionRow|def section_rows|def visible_tasks|class TaskTable)' dashboard/app.py && grep -c 'class TaskFilter' dashboard/tasks.py && uv run --with pytest --with textual pytest tests/test_dashboard_app.py tests/test_dashboard_tasks.py _(id: [rec-9a70606f-50c9-40b0-9b8c-107ff6573a06](.artifacts/records/project__acceptance/rec-9a70606f-50c9-40b0-9b8c-107ff6573a06.md))_

### Check
- **task-table-module**: rec-9a70606f-50c9-40b0-9b8c-107ff6573a06; dirty; pass; tdd _(id: [rec-4acae157-ca43-4995-93fc-cbfbf4e8ce80](.artifacts/records/project__check-run/rec-4acae157-ca43-4995-93fc-cbfbf4e8ce80.md))_

## terminal-view-format

### Acceptance
- **terminal-view-format**: Given a rendered dashboard, the formatter output has no id suffixes or banner, headings are bold only with colour on, no line exceeds the width, and an empty view gives the empty-state line; tdd; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q _(id: [rec-afb68d05-d961-45dd-813e-948c8e137722](.artifacts/records/project__acceptance/rec-afb68d05-d961-45dd-813e-948c8e137722.md))_

### Check
- **terminal-view-format**: rec-afb68d05-d961-45dd-813e-948c8e137722; 0f8791a808f1a5d81eb5beb6e03a7b56905f1644; pass; tdd _(id: [rec-0a4f74c4-1ca9-485b-ad92-c50608f178e5](.artifacts/records/project__check-run/rec-0a4f74c4-1ca9-485b-ad92-c50608f178e5.md))_

## test-suite-speed

### Acceptance
- **test-suite-speed**: All 262 tests pass, full suite wall time is at most 158s (half of the 317s clean-HEAD baseline), CPU time stays under 250s, and no timeout or deadline value is larger than before the change; check; test-suite-speed; time uv run --with textual --with pytest python -m pytest tests -q _(id: [rec-6e6e5c69-9ab0-44f3-9016-49c3512fcd99](.artifacts/records/project__acceptance/rec-6e6e5c69-9ab0-44f3-9016-49c3512fcd99.md))_

### Check
- **test-suite-speed**: rec-6e6e5c69-9ab0-44f3-9016-49c3512fcd99; 6cb58b4; pass; check _(id: [rec-e81acb74-ed4a-4e0f-bb5c-9ea42abfa56e](.artifacts/records/project__check-run/rec-e81acb74-ed4a-4e0f-bb5c-9ea42abfa56e.md))_

## tier2-dashboard

### Acceptance
- **tier2-dashboard**: At 60 and 120 columns, a phase header shows tier-2 running / passed@SHA / failed@SHA from seeded store state; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py tests/test_dashboard_model.py -q -k tier2 _(id: [rec-b5eb3ea3-6ec1-4431-ab56-fcb60d7b1574](.artifacts/records/project__acceptance/rec-b5eb3ea3-6ec1-4431-ab56-fcb60d7b1574.md))_

### Check
- **tier2-dashboard**: rec-b5eb3ea3-6ec1-4431-ab56-fcb60d7b1574; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; tdd _(id: [rec-557c638d-ef97-48d0-8892-54706a5542b2](.artifacts/records/project__check-run/rec-557c638d-ef97-48d0-8892-54706a5542b2.md))_
- **tier2-dashboard**: rec-b5eb3ea3-6ec1-4431-ab56-fcb60d7b1574; dirty; fail; tdd _(id: [rec-c7a6acac-a090-445c-9efa-ff2f72cf3516](.artifacts/records/project__check-run/rec-c7a6acac-a090-445c-9efa-ff2f72cf3516.md))_

## tier2-engine

### Acceptance
- **tier2-engine**: Parent starts a background tmux full-suite run in the phase worktree after reviewer pass without blocking the agent session, and records one tier-2 check-run at the phase head SHA with exit code, duration, output digest, and failing node IDs when failed; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_tiered_verification.py -q -k "runner or background or check_run or tmux" _(id: [rec-66d14411-07cd-479e-bb45-abfd3ee105f3](.artifacts/records/project__acceptance/rec-66d14411-07cd-479e-bb45-abfd3ee105f3.md))_

### Check
- **tier2-engine**: rec-66d14411-07cd-479e-bb45-abfd3ee105f3; dirty; fail; tdd _(id: [rec-48587139-b25f-4095-84d6-f09a5fad4399](.artifacts/records/project__check-run/rec-48587139-b25f-4095-84d6-f09a5fad4399.md))_
- **tier2-engine**: rec-66d14411-07cd-479e-bb45-abfd3ee105f3; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; tdd _(id: [rec-5a5855fb-5dd7-499b-9c69-2b323dde9ee0](.artifacts/records/project__check-run/rec-5a5855fb-5dd7-499b-9c69-2b323dde9ee0.md))_

## tier2-engine-fix

### Acceptance
- **tier2-engine-fix**: A tier-2 failure creates fix work-item(s) under the retry-loop budget clustered by failing test file/module, with no inline fix-and-rerun inside the verification step; after fixes tier-2 is expected to rerun at the new head; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_tiered_verification.py -q -k "fix or cluster or budget" _(id: [rec-e54af7a4-185c-4adc-93b9-6ca9417d5f0f](.artifacts/records/project__acceptance/rec-e54af7a4-185c-4adc-93b9-6ca9417d5f0f.md))_

### Check
- **tier2-engine-fix**: rec-e54af7a4-185c-4adc-93b9-6ca9417d5f0f; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; tdd _(id: [rec-2ab5c73a-c1a5-4393-9cc7-1d2334a71432](.artifacts/records/project__check-run/rec-2ab5c73a-c1a5-4393-9cc7-1d2334a71432.md))_
- **tier2-engine-fix**: rec-e54af7a4-185c-4adc-93b9-6ca9417d5f0f; dirty; fail; tdd _(id: [rec-51ae3745-10a9-4740-ba5d-2965a47905b6](.artifacts/records/project__check-run/rec-51ae3745-10a9-4740-ba5d-2965a47905b6.md))_

## tier2-engine-gate

### Acceptance
- **tier2-engine-gate**: Phase gate requires every active phase acceptance to have a passing runner check-run at the phase head SHA and a passing tier-2 check-run at that same SHA before merge; missing or failing tier-2 blocks merge; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_tiered_verification.py -q -k gate _(id: [rec-5ad44d4e-6fd3-4829-be3e-95e48379990b](.artifacts/records/project__acceptance/rec-5ad44d4e-6fd3-4829-be3e-95e48379990b.md))_

### Check
- **tier2-engine-gate**: rec-5ad44d4e-6fd3-4829-be3e-95e48379990b; dirty; fail; tdd _(id: [rec-504fe546-d509-44bb-af08-7830343269b8](.artifacts/records/project__check-run/rec-504fe546-d509-44bb-af08-7830343269b8.md))_
- **tier2-engine-gate**: rec-5ad44d4e-6fd3-4829-be3e-95e48379990b; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; tdd _(id: [rec-deacd1a7-dd90-434b-b6de-bf7e06e1f237](.artifacts/records/project__check-run/rec-deacd1a7-dd90-434b-b6de-bf7e06e1f237.md))_

## tier2-engine-meta

### Acceptance
- **tier2-engine-meta**: The tier-2 check-run carries runner metadata: revision = phase head SHA, exit_code, duration_s, output_sha256, and failing node IDs when failed, with evidence_kind integration; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_tiered_verification.py -q -k "meta or fields or evidence_kind or digest" _(id: [rec-f434ce3c-77ee-4e17-80d6-ad308eadb1f2](.artifacts/records/project__acceptance/rec-f434ce3c-77ee-4e17-80d6-ad308eadb1f2.md))_

### Check
- **tier2-engine-meta**: rec-f434ce3c-77ee-4e17-80d6-ad308eadb1f2; dirty; fail; tdd _(id: [rec-013637c5-73ac-4c16-b70e-82fc55eaf098](.artifacts/records/project__check-run/rec-013637c5-73ac-4c16-b70e-82fc55eaf098.md))_
- **tier2-engine-meta**: rec-f434ce3c-77ee-4e17-80d6-ad308eadb1f2; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; tdd _(id: [rec-1f7b0d92-ecc5-419d-89a3-42a302d2b53b](.artifacts/records/project__check-run/rec-1f7b0d92-ecc5-419d-89a3-42a302d2b53b.md))_

## tier2-engine-scoped

### Acceptance
- **tier2-engine-scoped**: Skills/README/test_verify_budget keep per-task verification scoped (no whole-suite per-task verify_command) while documenting the required phase-level tier-2 full run; skill↔contract consistency stays green; check; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_budget.py tests/test_skill_contract_consistency.py -q _(id: [rec-97b46204-7027-47b9-bf84-e4b585da8849](.artifacts/records/project__acceptance/rec-97b46204-7027-47b9-bf84-e4b585da8849.md))_

### Check
- **tier2-engine-scoped**: rec-97b46204-7027-47b9-bf84-e4b585da8849; dirty; pass; check _(id: [rec-31522e93-58ea-4e24-83d5-28c4df9fbc85](.artifacts/records/project__check-run/rec-31522e93-58ea-4e24-83d5-28c4df9fbc85.md))_
- **tier2-engine-scoped**: rec-97b46204-7027-47b9-bf84-e4b585da8849; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; check _(id: [rec-6a37cb49-2c89-4c26-9228-8047de254e26](.artifacts/records/project__check-run/rec-6a37cb49-2c89-4c26-9228-8047de254e26.md))_

## tier2-journal-pager-flake

### Finding
- **tier2-journal-pager-flake**: test_journal_detail_pager_pages_record_with_stub timed out under tier-2 parallel load; tier-2 at 3379fcf still fails same test after 40s timeout; screen never loads under xdist; test passes stably under same suite or human accepts waiver; none _(id: [rec-c174fd42-e8c9-41ea-bb43-8aee75770421](.artifacts/records/project__finding/rec-c174fd42-e8c9-41ea-bb43-8aee75770421.md))_

## tier2-plugin-root-and-cli

### Finding
- **tier2-plugin-root-and-cli**: tier-2 failed at phase head: verify_authority import of scripts/close_batch + journal pager flake; exit 1; nodes ['tests/test_dashboard_journal.py::test_journal_detail_pager_pages_record_with_stub', 'tests/test_verify_authority.py']; tier-2 passes at new phase head; none _(id: [rec-c8de37ab-a66a-4589-ab5a-2299788a4be9](.artifacts/records/project__finding/rec-c8de37ab-a66a-4589-ab5a-2299788a4be9.md))_

## tiered-verification-review

### Check
- **tiered-verification-review**: tiered-verification-review; 2f7404eab494720b703ffd0e2e01078236a876ab; pass; review _(id: [rec-05620909-2f20-41d8-9e42-a7aa6720812a](.artifacts/records/project__check-run/rec-05620909-2f20-41d8-9e42-a7aa6720812a.md))_
- **tiered-verification-review**: tiered-verification-review; 6d43454d3673e4e693fce13d5d4ea328f36943a3; pass; review _(id: [rec-216b86b7-5b0a-42ef-a2b4-cf0d3fbfbea0](.artifacts/records/project__check-run/rec-216b86b7-5b0a-42ef-a2b4-cf0d3fbfbea0.md))_
- **tiered-verification-review**: tiered-verification-review; a19db351754f233dec442631abd4d94f28575f1c; pass; review _(id: [rec-24715006-cbd1-4a2f-9bf3-1ef1ac73a981](.artifacts/records/project__check-run/rec-24715006-cbd1-4a2f-9bf3-1ef1ac73a981.md))_
- **tiered-verification-review**: tiered-verification-review; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; review _(id: [rec-af99ba51-538e-40fb-84b3-ce8525aa5cd6](.artifacts/records/project__check-run/rec-af99ba51-538e-40fb-84b3-ce8525aa5cd6.md))_
- **tiered-verification-review**: tiered-verification-review; 5e07f9a48bc4b935d6a3a90f7fc7ef4edcfc0246; pass; review _(id: [rec-b0010871-e548-46b2-88e7-4dfc9b2d16b5](.artifacts/records/project__check-run/rec-b0010871-e548-46b2-88e7-4dfc9b2d16b5.md))_
- **tiered-verification-review**: tiered-verification-review; 8ea0179b2e0b93b47df97d43ba7973e0875fe449; pass; review _(id: [rec-d3d21029-e99b-463c-8359-a7cc03e11f7a](.artifacts/records/project__check-run/rec-d3d21029-e99b-463c-8359-a7cc03e11f7a.md))_

## tiered-verification-tier2

### Check
- **tiered-verification-tier2**: tiered-verification-tier2; dirty; fail; check _(id: [rec-22e4965f-ca79-4bb0-9cc7-f479ff1b8ed1](.artifacts/records/project__check-run/rec-22e4965f-ca79-4bb0-9cc7-f479ff1b8ed1.md))_
- **tiered-verification-tier2**: tiered-verification-tier2; 8ea0179b2e0b93b47df97d43ba7973e0875fe449; pass; check _(id: [rec-7d0ee8e0-42cb-4a53-bc2e-aab7573071e2](.artifacts/records/project__check-run/rec-7d0ee8e0-42cb-4a53-bc2e-aab7573071e2.md))_
- **tiered-verification-tier2**: tiered-verification-tier2; dirty; fail; check _(id: [rec-a24a9ec0-30f8-41e7-a2dc-c8552984c3ae](.artifacts/records/project__check-run/rec-a24a9ec0-30f8-41e7-a2dc-c8552984c3ae.md))_
- **tiered-verification-tier2**: tiered-verification-tier2; 5e07f9a48bc4b935d6a3a90f7fc7ef4edcfc0246; fail; check _(id: [rec-b029a228-d2e6-4916-a21c-0ee8d8d8e59d](.artifacts/records/project__check-run/rec-b029a228-d2e6-4916-a21c-0ee8d8d8e59d.md))_
- **tiered-verification-tier2**: tiered-verification-tier2; 2f7404eab494720b703ffd0e2e01078236a876ab; fail; check _(id: [rec-db63b61e-ff54-44f5-8f57-39dbb9737ba5](.artifacts/records/project__check-run/rec-db63b61e-ff54-44f5-8f57-39dbb9737ba5.md))_
- **tiered-verification-tier2**: tiered-verification-tier2; 6d43454d3673e4e693fce13d5d4ea328f36943a3; fail; check _(id: [rec-fd72157e-80df-43c2-aac6-744fbac2d367](.artifacts/records/project__check-run/rec-fd72157e-80df-43c2-aac6-744fbac2d367.md))_

## tiered-verification-tier2-budget

### Finding
- **tiered-verification-tier2-budget**: Tier-2 fix-task budget exhausted with remaining failing modules; tier-2 check-run rec-a24a9ec0-30f8-41e7-a2dc-c8552984c3ae failed with 10 node ids across 7 modules; created 3 fix tasks (dashboard_app, dashboard_journal, discuss_skill); remaining: evidence_loop, plan_landing, plan_wave_rules, verify_authority; remaining modules fixed and tier-2 passes at phase head, or human accepts scoped waiver; none _(id: [rec-b8101acf-ff6c-4dbc-8042-6499702bd5e5](.artifacts/records/project__finding/rec-b8101acf-ff6c-4dbc-8042-6499702bd5e5.md))_

## tm-cli

### Acceptance
- **tm-cli**: The command over a fixture projects directory prints valid JSON with one summary per session and no message text.; tdd; session-analysis; python3 -m pytest -q tests/test_session_report.py _(id: [rec-be629630-2798-4a55-92ca-322aba930e94](.artifacts/records/project__acceptance/rec-be629630-2798-4a55-92ca-322aba930e94.md))_

### Check
- **tm-cli**: rec-be629630-2798-4a55-92ca-322aba930e94; dirty; pass; tdd _(id: [rec-4f4277b5-896a-4a11-a64f-5db71bc729fb](.artifacts/records/project__check-run/rec-4f4277b5-896a-4a11-a64f-5db71bc729fb.md))_

## tm-parse-events

### Acceptance
- **tm-parse-events**: A fixture with a malformed line and an unknown event type yields all valid events and a bad-line count of 1.; tdd; session-analysis; python3 -m pytest -q tests/test_session_metrics.py -k parse _(id: [rec-2df7a704-c3ba-43a0-966d-42474d3c2318](.artifacts/records/project__acceptance/rec-2df7a704-c3ba-43a0-966d-42474d3c2318.md))_

### Check
- **tm-parse-events**: rec-2df7a704-c3ba-43a0-966d-42474d3c2318; dirty; pass; tdd _(id: [rec-95a8ff7f-ad6e-4e72-8d4f-10f08cc8e68b](.artifacts/records/project__check-run/rec-95a8ff7f-ad6e-4e72-8d4f-10f08cc8e68b.md))_

## tm-session-fields

### Acceptance
- **tm-session-fields**: A fixture yields the expected session id, branch, duration, turn count, cost and skill names.; tdd; session-analysis; python3 -m pytest -q tests/test_session_fields.py _(id: [rec-5f8ebfcf-f591-4f07-932d-65fabc8871fb](.artifacts/records/project__acceptance/rec-5f8ebfcf-f591-4f07-932d-65fabc8871fb.md))_

### Check
- **tm-session-fields**: rec-5f8ebfcf-f591-4f07-932d-65fabc8871fb; dirty; pass; tdd _(id: [rec-da978d42-a6a0-4ac2-986b-6cc1e1121e13](.artifacts/records/project__check-run/rec-da978d42-a6a0-4ac2-986b-6cc1e1121e13.md))_

## tm-tool-metrics

### Acceptance
- **tm-tool-metrics**: A fixture with 5 tool calls, 2 errors and 1 retry yields exactly those counts per tool name.; tdd; session-analysis; python3 -m pytest -q tests/test_session_tools.py _(id: [rec-eb5399be-74fd-4403-bf2d-69fb1cb5bce9](.artifacts/records/project__acceptance/rec-eb5399be-74fd-4403-bf2d-69fb1cb5bce9.md))_

### Check
- **tm-tool-metrics**: rec-eb5399be-74fd-4403-bf2d-69fb1cb5bce9; dirty; pass; tdd _(id: [rec-61c34384-57d2-4cb4-9033-6a25173c9e45](.artifacts/records/project__check-run/rec-61c34384-57d2-4cb4-9033-6a25173c9e45.md))_

## tmux-conf-removal

### Acceptance
- **tmux-conf-removal**: No code, test or script refers to dashboard/tmux.conf or SE_WORKFLOW_DASHBOARD, and the file is gone.; check; dashboard; test ! -e dashboard/tmux.conf && ! grep -rnE 'dashboard/tmux\.conf|SE_WORKFLOW_DASHBOARD' dashboard scripts tests _(id: [rec-3aa70906-2826-4ae6-86f0-1b6d7a206306](.artifacts/records/project__acceptance/rec-3aa70906-2826-4ae6-86f0-1b6d7a206306.md))_

### Check
- **tmux-conf-removal**: rec-202b31bb-dba8-4bb0-ab9b-cae95af2386e; dirty; pass; check _(id: [rec-66c30d25-49c5-4f57-9f48-88678f80e597](.artifacts/records/project__check-run/rec-66c30d25-49c5-4f57-9f48-88678f80e597.md))_
- **tmux-conf-removal**: rec-3aa70906-2826-4ae6-86f0-1b6d7a206306; dirty; pass; check _(id: [rec-7a78f485-6ff0-4ac6-9af7-64e3e3e284d7](.artifacts/records/project__check-run/rec-7a78f485-6ff0-4ac6-9af7-64e3e3e284d7.md))_

## tmux-conf-removal-install

### Acceptance
- **tmux-conf-removal-install**: A plugin install made with sync-plugin.sh contains an executable se-workflow.tmux.; check; dashboard; d=$(mktemp -d) && bash scripts/sync-plugin.sh "$d/p" && test -x "$d/p/se-workflow.tmux" _(id: [rec-202b31bb-dba8-4bb0-ab9b-cae95af2386e](.artifacts/records/project__acceptance/rec-202b31bb-dba8-4bb0-ab9b-cae95af2386e.md))_

## tmux-entry-script

### Acceptance
- **tmux-entry-script**: With no options set, prefix A is a popup and prefix S a side pane of the launcher, both in the pane directory, using the path of the script's own directory.; tdd; dashboard; uv run --with pytest --with textual pytest -m tmux tests/test_tmux_entry.py -k default _(id: [rec-f6564330-b301-4302-a1d2-6e9c206c489b](.artifacts/records/project__acceptance/rec-f6564330-b301-4302-a1d2-6e9c206c489b.md))_

### Check
- **tmux-entry-script**: rec-f6564330-b301-4302-a1d2-6e9c206c489b; dirty; pass; tdd _(id: [rec-35197428-1805-468f-9d8d-36f62eb9a436](.artifacts/records/project__check-run/rec-35197428-1805-468f-9d8d-36f62eb9a436.md))_
- **tmux-entry-script**: rec-a19b9fe0-d373-4e93-a176-b941fa8236f0; dirty; pass; tdd _(id: [rec-efc1c7dd-67d6-4626-b64b-7289b0292719](.artifacts/records/project__check-run/rec-efc1c7dd-67d6-4626-b64b-7289b0292719.md))_

## tmux-entry-script-options

### Acceptance
- **tmux-entry-script-options**: Setting @dashboard-popup-key and @dashboard-pane-key before the script runs rebinds the keys and leaves A and S unbound.; tdd; dashboard; uv run --with pytest --with textual pytest -m tmux tests/test_tmux_entry.py -k custom_keys _(id: [rec-a19b9fe0-d373-4e93-a176-b941fa8236f0](.artifacts/records/project__acceptance/rec-a19b9fe0-d373-4e93-a176-b941fa8236f0.md))_

## tmux-suite-flake

### Finding
- **tmux-suite-flake**: One tmux integration test fails rarely: 1 of 19 serial tmux runs on e4484c4, test name not captured; Parent reruns on fix/dashboard-bugfix: 1 failed of 10 right after the xdist run, then 18 clean runs (15 full tmux runs, 3 full sequences); the extended popup test passed 12/12 alone; A tmux failure is captured with -rf and fixed, or 50 consecutive clean runs _(id: [rec-68330501-7b9a-446c-b24a-bf84af04e8e8](.artifacts/records/project__finding/rec-68330501-7b9a-446c-b24a-bf84af04e8e8.md))_

## tmux-test-waits

### Acceptance
- **tmux-test-waits**: The six failing tmux and e2e tests pass, and each tmux popup test takes under 4s; check; test-suite-speed; python3 -m pytest tests/test_tmux_integration.py tests/test_e2e_dashboard.py -q --durations=6 _(id: [rec-572fa450-b4a2-45bb-b52e-b5198f0e9b91](.artifacts/records/project__acceptance/rec-572fa450-b4a2-45bb-b52e-b5198f0e9b91.md))_

## trace-plan

### Acceptance
- **trace-plan**: plan-phase stamps requirements and decisions on work-items and requirement on acceptances when a specification exists, and test_plan_trace.py passes.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_plan_trace.py -q _(id: [rec-6aa2fdc3-4b8f-4d53-a585-a4405107bef5](.artifacts/records/project__acceptance/rec-6aa2fdc3-4b8f-4d53-a585-a4405107bef5.md))_

### Check
- **trace-plan**: rec-6aa2fdc3-4b8f-4d53-a585-a4405107bef5; dirty; pass; check _(id: [rec-6288d5e3-7aed-4c8a-ad22-2e2fa716b9fc](.artifacts/records/project__check-run/rec-6288d5e3-7aed-4c8a-ad22-2e2fa716b9fc.md))_

## unsigned-check-label

### Acceptance
- **unsigned-check-label**: An unsigned check reads as its acceptance criterion and task slug, never a rec- id, with a fallback when the acceptance is missing; the test fails before the fix; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k unsigned _(id: [rec-403febb3-cbe5-474d-8413-5687934c29d2](.artifacts/records/project__acceptance/rec-403febb3-cbe5-474d-8413-5687934c29d2.md))_

### Check
- **unsigned-check-label**: rec-403febb3-cbe5-474d-8413-5687934c29d2; 3ca5175c7dc8e6e60b0f501bf3c0e30309e9403d; pass; tdd _(id: [rec-7d02868c-4d2e-4265-8548-c3b0ab4de18c](.artifacts/records/project__check-run/rec-7d02868c-4d2e-4265-8548-c3b0ab4de18c.md))_

### Observation
- **unsigned-check-label**: _needs_you built unsigned-check text from the raw criterion_id and used the check-run subject, so the panel showed a rec- id instead of the criterion and task.; dashboard-bugfix _(id: [rec-45a1d50b-0dae-47ec-88c3-19cab12238ba](.artifacts/records/project__investigation-observation/rec-45a1d50b-0dae-47ec-88c3-19cab12238ba.md))_

## verify-authority

### Acceptance
- **verify-authority**: verify-work and close_batch use runner-produced check-runs for tdd/check and do not invent binary results; skill-contract consistency tests pass; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_authority.py tests/test_skill_contract_consistency.py -q _(id: [rec-88c394e4-ca2e-45c8-a222-073b4b621bdd](.artifacts/records/project__acceptance/rec-88c394e4-ca2e-45c8-a222-073b4b621bdd.md))_

### Check
- **verify-authority**: rec-88c394e4-ca2e-45c8-a222-073b4b621bdd; 4bd42b96e925562686c726d6da61a27b99481255; pass; tdd _(id: [rec-36df2410-3b45-4803-bf95-3fca393989fe](.artifacts/records/project__check-run/rec-36df2410-3b45-4803-bf95-3fca393989fe.md))_

## verify-backlog-capture

### Acceptance
- **verify-backlog-capture**: Through the adaptive-artifacts CLI on a seeded store, create/list/promote/dismiss backlog-item works and is distinct from feedback; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_backlog_item.py -q _(id: [rec-91696e19-7aa5-4cf8-8215-8d8cf9f668df](.artifacts/records/project__acceptance/rec-91696e19-7aa5-4cf8-8215-8d8cf9f668df.md))_

### Check
- **verify-backlog-capture**: rec-91696e19-7aa5-4cf8-8215-8d8cf9f668df; 2ba3f658a6c7a374ef157640f4dd4a3024588e90; pass; tdd _(id: [rec-47c792b2-2a4c-4abb-90cb-10c624a2c9fd](.artifacts/records/project__check-run/rec-47c792b2-2a4c-4abb-90cb-10c624a2c9fd.md))_

## verify-backlog-capture-contract

### Acceptance
- **verify-backlog-capture-contract**: Bundled contract resolves project:backlog-item and project:feedback; contract self-consistency suite passes; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_contract_self_consistency.py -q _(id: [rec-2648b75d-644b-4eee-ba8d-4d1ff62f7f48](.artifacts/records/project__acceptance/rec-2648b75d-644b-4eee-ba8d-4d1ff62f7f48.md))_

### Check
- **verify-backlog-capture-contract**: rec-2648b75d-644b-4eee-ba8d-4d1ff62f7f48; 2ba3f658a6c7a374ef157640f4dd4a3024588e90; pass; check _(id: [rec-97baaa14-fc25-4b83-a734-e53b49728765](.artifacts/records/project__check-run/rec-97baaa14-fc25-4b83-a734-e53b49728765.md))_

## verify-backlog-capture-dashboard

### Acceptance
- **verify-backlog-capture-dashboard**: Dashboard Backlog panel shows open items for an effort and promote/dismiss work via CLI; Needs you does not list backlog; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_app.py -q -k backlog _(id: [rec-5607f8c7-adf7-44e7-89c3-fa6d5588b4ec](.artifacts/records/project__acceptance/rec-5607f8c7-adf7-44e7-89c3-fa6d5588b4ec.md))_

### Check
- **verify-backlog-capture-dashboard**: rec-5607f8c7-adf7-44e7-89c3-fa6d5588b4ec; 2ba3f658a6c7a374ef157640f4dd4a3024588e90; pass; tdd _(id: [rec-3ef4a9ef-2227-41b5-be04-18243536b5cc](.artifacts/records/project__check-run/rec-3ef4a9ef-2227-41b5-be04-18243536b5cc.md))_

## verify-backlog-capture-skills

### Acceptance
- **verify-backlog-capture-skills**: Skill/contract consistency and engage feedback-vs-backlog documentation checks pass; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_assess_routing.py -q _(id: [rec-f9cf16cd-69d0-4a84-86aa-b134b078c167](.artifacts/records/project__acceptance/rec-f9cf16cd-69d0-4a84-86aa-b134b078c167.md))_

### Check
- **verify-backlog-capture-skills**: rec-f9cf16cd-69d0-4a84-86aa-b134b078c167; 2ba3f658a6c7a374ef157640f4dd4a3024588e90; pass; check _(id: [rec-077b461e-5d00-4c30-8e8d-b8fab0b2e996](.artifacts/records/project__check-run/rec-077b461e-5d00-4c30-8e8d-b8fab0b2e996.md))_

## verify-check-runner

### Acceptance
- **verify-check-runner**: se-workflow check produces pass/fail/blocked check-runs with revision and runner fields for a throwaway store, observed through the CLI entry point; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_se_workflow_check.py -q -k "pass or fail or blocked or integration or cli" _(id: [rec-89a78033-b672-4f71-9f59-10deea6ef8bf](.artifacts/records/project__acceptance/rec-89a78033-b672-4f71-9f59-10deea6ef8bf.md))_

### Check
- **verify-check-runner**: rec-89a78033-b672-4f71-9f59-10deea6ef8bf; 4bd42b96e925562686c726d6da61a27b99481255; pass; tdd _(id: [rec-1cf0921c-d6f8-4b07-91c0-982887547c2b](.artifacts/records/project__check-run/rec-1cf0921c-d6f8-4b07-91c0-982887547c2b.md))_

## verify-check-runner-commit

### Acceptance
- **verify-check-runner-commit**: execute-phase requires per-task commit; its tests cover that rule; check; workflow-loop; uv run --with pytest python -m pytest tests/test_task_commit.py tests/test_execute_landing.py tests/test_skill_contract_consistency.py -q -k "commit or landing or task_commit" _(id: [rec-efdf2173-e187-41a1-a65f-9539da56742e](.artifacts/records/project__acceptance/rec-efdf2173-e187-41a1-a65f-9539da56742e.md))_

### Check
- **verify-check-runner-commit**: rec-efdf2173-e187-41a1-a65f-9539da56742e; 4bd42b96e925562686c726d6da61a27b99481255; pass; check _(id: [rec-3317616f-d1b1-4f1e-b6dd-28d4e910cbef](.artifacts/records/project__check-run/rec-3317616f-d1b1-4f1e-b6dd-28d4e910cbef.md))_

## verify-check-runner-contract

### Acceptance
- **verify-check-runner-contract**: Contract rejects illegal result/method; self-consistency and enum tests pass; check; workflow-loop; uv run --with pytest python -m pytest tests/test_contract_self_consistency.py tests/test_evidence_loop.py tests/test_assess_routing.py -q -k "enum or result or method or contract" _(id: [rec-d00ce191-345a-46ed-9dc8-4c0242f31984](.artifacts/records/project__acceptance/rec-d00ce191-345a-46ed-9dc8-4c0242f31984.md))_

### Check
- **verify-check-runner-contract**: rec-d00ce191-345a-46ed-9dc8-4c0242f31984; 4bd42b96e925562686c726d6da61a27b99481255; pass; check _(id: [rec-cd7664df-a8ea-42c5-8d6c-bd73a246680d](.artifacts/records/project__check-run/rec-cd7664df-a8ea-42c5-8d6c-bd73a246680d.md))_

## verify-check-runner-dirty

### Acceptance
- **verify-check-runner-dirty**: Dirty pass refused without override; override records dirty plus diff_sha256; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_se_workflow_check.py -q -k dirty _(id: [rec-5c18090c-ca0b-43a3-aa61-78ebd2383d7e](.artifacts/records/project__acceptance/rec-5c18090c-ca0b-43a3-aa61-78ebd2383d7e.md))_

### Check
- **verify-check-runner-dirty**: rec-5c18090c-ca0b-43a3-aa61-78ebd2383d7e; 4bd42b96e925562686c726d6da61a27b99481255; pass; tdd _(id: [rec-a82aad47-82a2-4024-9f31-14314ea0c2ab](.artifacts/records/project__check-run/rec-a82aad47-82a2-4024-9f31-14314ea0c2ab.md))_

## verify-check-runner-skills

### Acceptance
- **verify-check-runner-skills**: verify-work and close_batch use CLI-produced check-runs for tdd/check; skill-contract tests pass; check; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_authority.py tests/test_skill_contract_consistency.py -q _(id: [rec-a831be0f-059e-414e-90bb-36c485017676](.artifacts/records/project__acceptance/rec-a831be0f-059e-414e-90bb-36c485017676.md))_

### Check
- **verify-check-runner-skills**: rec-a831be0f-059e-414e-90bb-36c485017676; 4bd42b96e925562686c726d6da61a27b99481255; pass; check _(id: [rec-ce3653a8-b5bd-40e1-a2af-0f37ef5045a8](.artifacts/records/project__check-run/rec-ce3653a8-b5bd-40e1-a2af-0f37ef5045a8.md))_

## verify-dashboard-actions-phase

### Acceptance
- **verify-dashboard-actions-phase**: The full test suite passes, including a tmux test that filters, copies a slug into the tmux buffer, and opens a commit view in the popup; check; dashboard; uv run --with textual --with pytest python -m pytest tests -q _(id: [rec-468f8719-9cf5-4262-aea7-6d372a9cd6a9](.artifacts/records/project__acceptance/rec-468f8719-9cf5-4262-aea7-6d372a9cd6a9.md))_

### Check
- **verify-dashboard-actions-phase**: rec-468f8719-9cf5-4262-aea7-6d372a9cd6a9; 03d561c; pass; check _(id: [rec-5d987a65-62e1-4cdf-b91a-3ecf881ab599](.artifacts/records/project__check-run/rec-5d987a65-62e1-4cdf-b91a-3ecf881ab599.md))_

## verify-dashboard-actions-phase-signoff

### Acceptance
- **verify-dashboard-actions-phase-signoff**: The user tries filter, hide-done, copy, and commit view in the popup and the side pane and signs off; manual; dashboard _(id: [rec-aa7012e9-f5d9-427c-a0d5-74e173544519](.artifacts/records/project__acceptance/rec-aa7012e9-f5d9-427c-a0d5-74e173544519.md))_

### Check
- **verify-dashboard-actions-phase-signoff**: rec-aa7012e9-f5d9-427c-a0d5-74e173544519; 03d561c; pass; manual; ayin _(id: [rec-78f4574a-6127-4ae1-96c4-73dc987b5fb5](.artifacts/records/project__check-run/rec-78f4574a-6127-4ae1-96c4-73dc987b5fb5.md))_

## verify-dashboard-approvals

### Acceptance
- **verify-dashboard-approvals**: Through the Textual dashboard app entry point: list d opens detail with no write; confirm/cancel and Approve/Reject/Sign/Accept-risk behave as specified with notes; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k approval _(id: [rec-5b8ab6e4-d17d-479a-b038-38d2f8a03d1e](.artifacts/records/project__acceptance/rec-5b8ab6e4-d17d-479a-b038-38d2f8a03d1e.md))_

### Check
- **verify-dashboard-approvals**: rec-5b8ab6e4-d17d-479a-b038-38d2f8a03d1e; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; tdd _(id: [rec-9c48b2f5-2c80-48c2-9307-e09626304985](.artifacts/records/project__check-run/rec-9c48b2f5-2c80-48c2-9307-e09626304985.md))_

## verify-dashboard-approvals-constraints

### Acceptance
- **verify-dashboard-approvals-constraints**: Stale never-writes dashboard constraints superseded; dashboard-human-gate-writes active with human-gate write policy; check; workflow-loop; /home/andrewyin/adaptive-artifacts/bin/adaptive-artifacts --store /home/andrewyin/se-workflow/.artifacts list --type project:constraint --state active | python3 -c "import sys,json; d=json.load(sys.stdin); stmts=[(r['subject'], (r.get('payload') or {}).get('statement') or '') for r in d['records']]; assert any(s=='dashboard-human-gate-writes' for s,_ in stmts); hg=[t for s,t in stmts if s=='dashboard-human-gate-writes']; assert hg and ('human Needs-you' in hg[0] or 'human-gate' in hg[0].lower()); old={'dashboard-read-only','dashboard-read-only-dashboard-bugfix','dashboard-read-only-dashboard-features'}; assert not any('never writes' in t.lower() for s,t in stmts if s in old); assert all('Retired' in t or 'dashboard-human-gate-writes' in t for s,t in stmts if s in old)" _(id: [rec-9c7c3c55-1e86-41fd-bb53-3c6f41567cf4](.artifacts/records/project__acceptance/rec-9c7c3c55-1e86-41fd-bb53-3c6f41567cf4.md))_

### Check
- **verify-dashboard-approvals-constraints**: rec-9c7c3c55-1e86-41fd-bb53-3c6f41567cf4; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; check _(id: [rec-3dedc0b5-6009-4849-95dc-65f6e62f939d](.artifacts/records/project__check-run/rec-3dedc0b5-6009-4849-95dc-65f6e62f939d.md))_
- **verify-dashboard-approvals-constraints**: rec-9c7c3c55-1e86-41fd-bb53-3c6f41567cf4; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; check _(id: [rec-a640fb3c-6ccb-44b0-b00e-2b19a18336a8](.artifacts/records/project__check-run/rec-a640fb3c-6ccb-44b0-b00e-2b19a18336a8.md))_

## verify-dashboard-approvals-docs

### Acceptance
- **verify-dashboard-approvals-docs**: README keys updated; skill↔contract consistency green when skills mention the new optional note fields; check; workflow-loop; grep -E 'Approve|Reject|Accept risk' README.md && uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py -q _(id: [rec-a764fa17-a012-4fec-8c30-4b0eb791b434](.artifacts/records/project__acceptance/rec-a764fa17-a012-4fec-8c30-4b0eb791b434.md))_

### Check
- **verify-dashboard-approvals-docs**: rec-a764fa17-a012-4fec-8c30-4b0eb791b434; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; check _(id: [rec-2217d59f-1402-4be9-933a-989549a02264](.artifacts/records/project__check-run/rec-2217d59f-1402-4be9-933a-989549a02264.md))_

## verify-dashboard-approvals-revision

### Acceptance
- **verify-dashboard-approvals-revision**: Stale displayed revision shows a visible message and skips the write; no @current retry; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'approval and stale' _(id: [rec-84aa203e-910a-40ea-a99b-1e0c3efdda28](.artifacts/records/project__acceptance/rec-84aa203e-910a-40ea-a99b-1e0c3efdda28.md))_

### Check
- **verify-dashboard-approvals-revision**: rec-84aa203e-910a-40ea-a99b-1e0c3efdda28; a27e7b9c4852347de20f4ce2ca3b6fae8ff58d3d; pass; tdd _(id: [rec-dbe073f3-68cf-48fe-95cc-be9663767655](.artifacts/records/project__check-run/rec-dbe073f3-68cf-48fe-95cc-be9663767655.md))_

## verify-dashboard-package

### Acceptance
- **verify-dashboard-package**: The dashboard launcher in the new package prints a frame for a seeded store (real entry point).; tdd; dashboard; uv run --with pytest --with textual pytest tests/test_dashboard_launcher.py tests/test_dashboard_integration.py _(id: [rec-f6216dac-0349-43a1-86a4-f5dd48eb2f51](.artifacts/records/project__acceptance/rec-f6216dac-0349-43a1-86a4-f5dd48eb2f51.md))_

### Check
- **verify-dashboard-package**: rec-f6216dac-0349-43a1-86a4-f5dd48eb2f51; dirty; pass; tdd _(id: [rec-15e73fc5-ec3f-4de8-8efe-703fdbb29ff3](.artifacts/records/project__check-run/rec-15e73fc5-ec3f-4de8-8efe-703fdbb29ff3.md))_
- **verify-dashboard-package**: rec-92205670-6c11-4582-8a88-f1b38046ccb8; dirty; pass; check _(id: [rec-5d354ac3-5272-44ce-9569-01bca5b201da](.artifacts/records/project__check-run/rec-5d354ac3-5272-44ce-9569-01bca5b201da.md))_
- **verify-dashboard-package**: rec-1d30f9a6-5236-45c6-8ba7-265bc6a9ca53; dirty; pass; check _(id: [rec-8b1dab0f-4baf-4743-9d66-bce1fc4aab1b](.artifacts/records/project__check-run/rec-8b1dab0f-4baf-4743-9d66-bce1fc4aab1b.md))_
- **verify-dashboard-package**: rec-02b72b32-48e0-46c4-a910-8b9d64ded6a5; dirty; pass; check _(id: [rec-c37483d8-fe5d-4ce7-ab6b-56f94388ee51](.artifacts/records/project__check-run/rec-c37483d8-fe5d-4ce7-ab6b-56f94388ee51.md))_
- **verify-dashboard-package**: rec-78759ece-bf5a-4584-9ce1-17650f1217c6; dirty; pass; check _(id: [rec-d9db7e39-b1a3-49bc-adb2-44bba4167033](.artifacts/records/project__check-run/rec-d9db7e39-b1a3-49bc-adb2-44bba4167033.md))_

## verify-dashboard-package-entry-points

### Acceptance
- **verify-dashboard-package-entry-points**: The tmux conf and a plugin install start the dashboard through the tmux tests.; check; dashboard; uv run --with pytest --with textual pytest -m tmux tests/test_tmux_integration.py tests/test_e2e_dashboard.py _(id: [rec-92205670-6c11-4582-8a88-f1b38046ccb8](.artifacts/records/project__acceptance/rec-92205670-6c11-4582-8a88-f1b38046ccb8.md))_

## verify-dashboard-package-full-suite

### Acceptance
- **verify-dashboard-package-full-suite**: The full suite passes.; check; dashboard; uv run --with pytest --with textual pytest _(id: [rec-02b72b32-48e0-46c4-a910-8b9d64ded6a5](.artifacts/records/project__acceptance/rec-02b72b32-48e0-46c4-a910-8b9d64ded6a5.md))_

## verify-dashboard-package-outside-scripts

### Acceptance
- **verify-dashboard-package-outside-scripts**: The dashboard code lives in dashboard/ and no dashboard file remains in scripts/.; check; dashboard; test -f dashboard/app.py && test -f dashboard/model.py && ! ls scripts | grep -i dashboard _(id: [rec-78759ece-bf5a-4584-9ce1-17650f1217c6](.artifacts/records/project__acceptance/rec-78759ece-bf5a-4584-9ce1-17650f1217c6.md))_

## verify-dashboard-package-task-modules

### Acceptance
- **verify-dashboard-package-task-modules**: The task code is in dashboard/tasks.py and dashboard/task_detail.py, not app.py.; check; dashboard; test -f dashboard/tasks.py && test -f dashboard/task_detail.py && ! grep -nE '^class (TaskFilter|TaskTable|TaskDetailScreen)' dashboard/app.py _(id: [rec-1d30f9a6-5236-45c6-8ba7-265bc6a9ca53](.artifacts/records/project__acceptance/rec-1d30f9a6-5236-45c6-8ba7-265bc6a9ca53.md))_

## verify-dashboard-view-phase

### Acceptance
- **verify-dashboard-view-phase**: The CLI integration test passes: after each lifecycle step every record appears in exactly its expected dashboard section; tdd; dashboard; cd ~/se-workflow && python3 -m pytest tests/test_dashboard_integration.py -q _(id: [rec-35c98548-4ccf-4c7c-8286-3a1e7ba21185](.artifacts/records/project__acceptance/rec-35c98548-4ccf-4c7c-8286-3a1e7ba21185.md))_

### Check
- **verify-dashboard-view-phase**: rec-83fc3486-af5f-49af-9000-8d9fd6890f3c; 5ba4e0a; pass; manual; ayin _(id: [rec-2141a70f-c8a2-4b54-ae34-9dc12cbf02f2](.artifacts/records/project__check-run/rec-2141a70f-c8a2-4b54-ae34-9dc12cbf02f2.md))_
- **verify-dashboard-view-phase**: rec-83fc3486-af5f-49af-9000-8d9fd6890f3c; 5ba4e0a; pass; manual _(id: [rec-8a7977e1-dba3-47b2-a074-5f9b6b91fe15](.artifacts/records/project__check-run/rec-8a7977e1-dba3-47b2-a074-5f9b6b91fe15.md))_
- **verify-dashboard-view-phase**: rec-1a3c142c-b9c6-4f57-baf0-b38000b5bb9f; 5ba4e0a; fail; check _(id: [rec-8c16b297-2e38-48b5-8259-b8c2211f2a1f](.artifacts/records/project__check-run/rec-8c16b297-2e38-48b5-8259-b8c2211f2a1f.md))_
- **verify-dashboard-view-phase**: rec-1a3c142c-b9c6-4f57-baf0-b38000b5bb9f; aa:92f1e0d se:5ba4e0a; pass; check _(id: [rec-dd5cd8a1-81be-4583-a6a3-c30f14c9a1e4](.artifacts/records/project__check-run/rec-dd5cd8a1-81be-4583-a6a3-c30f14c9a1e4.md))_
- **verify-dashboard-view-phase**: rec-35c98548-4ccf-4c7c-8286-3a1e7ba21185; 5ba4e0a; pass; tdd _(id: [rec-e8e1a102-2225-493f-9dfb-f1fa5c21e3f1](.artifacts/records/project__check-run/rec-e8e1a102-2225-493f-9dfb-f1fa5c21e3f1.md))_

## verify-dashboard-view-phase-live

### Acceptance
- **verify-dashboard-view-phase-live**: The dashboard rendered from ~/.artifacts/se-workflow shows the watch-dashboard goal, phase dashboard-view, the open plugin question under needs-you, and each phase-1 task in the section its lifecycle implies; manual; dashboard; ~/adaptive-artifacts/bin/adaptive-artifacts --store ~/.artifacts/se-workflow view --id project:dashboard _(id: [rec-83fc3486-af5f-49af-9000-8d9fd6890f3c](.artifacts/records/project__acceptance/rec-83fc3486-af5f-49af-9000-8d9fd6890f3c.md))_

## verify-dashboard-view-phase-suites

### Acceptance
- **verify-dashboard-view-phase-suites**: Full test suites of both repos pass on the phase-1 changes; check; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q && cd ~/se-workflow && python3 -m pytest tests -q _(id: [rec-1a3c142c-b9c6-4f57-baf0-b38000b5bb9f](.artifacts/records/project__acceptance/rec-1a3c142c-b9c6-4f57-baf0-b38000b5bb9f.md))_

## verify-end-to-end-phase

### Acceptance
- **verify-end-to-end-phase**: Scripted end-to-end test and both full suites pass; check; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q && cd ~/se-workflow && python3 -m pytest tests -q _(id: [rec-a5e71d14-1f25-4868-a42e-3a2b17e16616](.artifacts/records/project__acceptance/rec-a5e71d14-1f25-4868-a42e-3a2b17e16616.md))_

### Check
- **verify-end-to-end-phase**: rec-a5e71d14-1f25-4868-a42e-3a2b17e16616; aa:227523b se:a3b4ee2; pass; check _(id: [rec-01016663-beda-482a-810a-0d16bd2c46b8](.artifacts/records/project__check-run/rec-01016663-beda-482a-810a-0d16bd2c46b8.md))_
- **verify-end-to-end-phase**: rec-a5e71d14-1f25-4868-a42e-3a2b17e16616; dirty; pass; check _(id: [rec-2e3f5376-89d0-4d9f-8029-3bb418ae2ef8](.artifacts/records/project__check-run/rec-2e3f5376-89d0-4d9f-8029-3bb418ae2ef8.md))_
- **verify-end-to-end-phase**: rec-9dce7bb8-9cc7-4a4d-9ebd-48a749f7cc85; se:a3b4ee2; fail; check _(id: [rec-a746fedb-faa4-4de5-b32c-ba6466e9fad6](.artifacts/records/project__check-run/rec-a746fedb-faa4-4de5-b32c-ba6466e9fad6.md))_
- **verify-end-to-end-phase**: rec-9dce7bb8-9cc7-4a4d-9ebd-48a749f7cc85; dirty; pass; check _(id: [rec-ae0525f6-a5fc-45bc-ba9e-b3798959856f](.artifacts/records/project__check-run/rec-ae0525f6-a5fc-45bc-ba9e-b3798959856f.md))_

## verify-end-to-end-phase-clear

### Acceptance
- **verify-end-to-end-phase-clear**: The watch-dashboard dashboard shows no Open Question, Needs Human, or Unsigned Manual Check; check; dashboard; ~/se-workflow/scripts/dashboard-status ~/se-workflow _(id: [rec-9dce7bb8-9cc7-4a4d-9ebd-48a749f7cc85](.artifacts/records/project__acceptance/rec-9dce7bb8-9cc7-4a4d-9ebd-48a749f7cc85.md))_

## verify-estimate-view

### Acceptance
- **verify-estimate-view**: A 60-column pilot shows one sitting or more than one and the derived elapsed minutes on the phase header, and the full suite passes.; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k estimate_view_header_sitting && uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m "not tmux" && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-9b9d3ec2-b413-4471-8991-8546a7f1c82b](.artifacts/records/project__acceptance/rec-9b9d3ec2-b413-4471-8991-8546a7f1c82b.md))_

### Check
- **verify-estimate-view**: rec-9b9d3ec2-b413-4471-8991-8546a7f1c82b; dirty; pass; check _(id: [rec-efe08a21-419f-4d83-807f-611eb22ffb33](.artifacts/records/project__check-run/rec-efe08a21-419f-4d83-807f-611eb22ffb33.md))_
- **verify-estimate-view**: rec-9b9d3ec2-b413-4471-8991-8546a7f1c82b; dirty; fail; check _(id: [rec-fa5a5160-58ea-4624-a2ea-a639be11ad07](.artifacts/records/project__check-run/rec-fa5a5160-58ea-4624-a2ea-a639be11ad07.md))_

## verify-estimate-view-chips

### Acceptance
- **verify-estimate-view-chips**: Task detail at 60 columns shows chips for size, minutes, and executor.; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_estimate.py -q -k estimate_view_chips _(id: [rec-eae79ebb-8d5c-4378-b484-8ce816861f28](.artifacts/records/project__acceptance/rec-eae79ebb-8d5c-4378-b484-8ce816861f28.md))_

### Check
- **verify-estimate-view-chips**: rec-eae79ebb-8d5c-4378-b484-8ce816861f28; dirty; pass; check _(id: [rec-97cd4f75-7ba9-4354-afd0-d489e7b0e7ec](.artifacts/records/project__check-run/rec-97cd4f75-7ba9-4354-afd0-d489e7b0e7ec.md))_

## verify-estimate-view-clip

### Acceptance
- **verify-estimate-view-clip**: Clipping shortens the title and keeps the sitting phrase, the elapsed minutes, the unset count, and the task suffix.; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k estimate_view_clip _(id: [rec-e58b5f93-f9e3-4650-9853-ddcd0d0a0470](.artifacts/records/project__acceptance/rec-e58b5f93-f9e3-4650-9853-ddcd0d0a0470.md))_

### Check
- **verify-estimate-view-clip**: rec-e58b5f93-f9e3-4650-9853-ddcd0d0a0470; dirty; pass; check _(id: [rec-82298d56-6212-428e-bd49-994cd0f3af76](.artifacts/records/project__check-run/rec-82298d56-6212-428e-bd49-994cd0f3af76.md))_

## verify-estimate-view-contract

### Acceptance
- **verify-estimate-view-contract**: The phase diff does not change contract/project-design.json, and a task with neither field still shows executor subagent.; check; dashboard; uv run --with pytest python -m pytest tests/test_dashboard_model.py -q -k estimate_view_blank_executor && test -z "$(git diff --name-only main -- contract/project-design.json)" _(id: [rec-7303a69d-1a5e-4661-b5c4-228c5b3dc28d](.artifacts/records/project__acceptance/rec-7303a69d-1a5e-4661-b5c4-228c5b3dc28d.md))_

### Check
- **verify-estimate-view-contract**: rec-7303a69d-1a5e-4661-b5c4-228c5b3dc28d; dirty; pass; check _(id: [rec-29e6fa05-2c7e-46bc-9313-aa2159a8812e](.artifacts/records/project__check-run/rec-29e6fa05-2c7e-46bc-9313-aa2159a8812e.md))_

## verify-estimate-view-suffix

### Acceptance
- **verify-estimate-view-suffix**: Each task title shows its size, minutes, and executor. A missing size is omitted, 0 shows as 0m, and a missing executor shows as subagent.; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k estimate_view_title_suffix _(id: [rec-f812f0d8-f363-4ec3-b7c8-32463a0d9d0b](.artifacts/records/project__acceptance/rec-f812f0d8-f363-4ec3-b7c8-32463a0d9d0b.md))_

### Check
- **verify-estimate-view-suffix**: rec-f812f0d8-f363-4ec3-b7c8-32463a0d9d0b; dirty; pass; check _(id: [rec-a4023a51-d70b-4eb6-97fc-ac9e6a44ad3c](.artifacts/records/project__check-run/rec-a4023a51-d70b-4eb6-97fc-ac9e6a44ad3c.md))_

## verify-estimate-view-unset

### Acceptance
- **verify-estimate-view-unset**: A phase where some counted tasks have no estimate_minutes shows the partial total and the unset count. A phase where none have an estimate shows no minute suffix.; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_app.py -q -k 'estimate_view_unset_count or estimate_view_header_partial' _(id: [rec-8b8345bb-5686-47dc-869d-39897b52c173](.artifacts/records/project__acceptance/rec-8b8345bb-5686-47dc-869d-39897b52c173.md))_

### Check
- **verify-estimate-view-unset**: rec-8b8345bb-5686-47dc-869d-39897b52c173; dirty; pass; check _(id: [rec-49ba2a0e-e84e-4124-9686-0f46a64882d8](.artifacts/records/project__check-run/rec-49ba2a0e-e84e-4124-9686-0f46a64882d8.md))_

## verify-estimate-view-wave

### Acceptance
- **verify-estimate-view-wave**: The header minute figure matches the wave rule, including a parallel subagent wave that contributes its longest task.; check; dashboard; uv run --with pytest python -m pytest tests/test_dashboard_model.py -q -k estimate_view_wave_rule _(id: [rec-29ba3627-46df-4308-bae9-8939ff93b2f1](.artifacts/records/project__acceptance/rec-29ba3627-46df-4308-bae9-8939ff93b2f1.md))_

### Check
- **verify-estimate-view-wave**: rec-29ba3627-46df-4308-bae9-8939ff93b2f1; dirty; pass; check _(id: [rec-94e4eecc-6d14-489c-b911-6aed5d9bec61](.artifacts/records/project__check-run/rec-94e4eecc-6d14-489c-b911-6aed5d9bec61.md))_

## verify-evidence-loop

### Acceptance
- **verify-evidence-loop**: tests/test_evidence_loop.py drives adaptive-artifacts on a fresh store through release ready, a check-run with no level or next, a repeated implementation failure that routes to design, a design route, integration failure, insufficient evidence, and a legacy pass check-run.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_evidence_loop.py -q _(id: [rec-c6f57f2f-cef8-4daf-b8f1-7899cd1a7e27](.artifacts/records/project__acceptance/rec-c6f57f2f-cef8-4daf-b8f1-7899cd1a7e27.md))_

### Check
- **verify-evidence-loop**: rec-a072e603-a6d5-4e9c-9f0d-2b55f6543af8; dirty; pass; check _(id: [rec-77720c61-994f-4b64-a26e-e8bfd14c8d46](.artifacts/records/project__check-run/rec-77720c61-994f-4b64-a26e-e8bfd14c8d46.md))_
- **verify-evidence-loop**: rec-a7ead56b-fe80-4a0d-a5ae-9b34a976c46f; dirty; pass; check _(id: [rec-b7fea9c3-cbe2-4442-976f-5714774f6bdd](.artifacts/records/project__check-run/rec-b7fea9c3-cbe2-4442-976f-5714774f6bdd.md))_
- **verify-evidence-loop**: rec-c6f57f2f-cef8-4daf-b8f1-7899cd1a7e27; dirty; pass; check _(id: [rec-cfe8b022-b5b2-4c6a-91bd-8dfecf1b156e](.artifacts/records/project__check-run/rec-cfe8b022-b5b2-4c6a-91bd-8dfecf1b156e.md))_
- **verify-evidence-loop**: rec-19a87492-4386-45cb-9b12-53cf66c22e09; dirty; pass; check _(id: [rec-dfb1b6e8-b07f-42b2-a6cc-671f86b19583](.artifacts/records/project__check-run/rec-dfb1b6e8-b07f-42b2-a6cc-671f86b19583.md))_

## verify-evidence-loop-contract

### Acceptance
- **verify-evidence-loop-contract**: The bundled contract resolves specification, design, integration-report, assessment, release, and feedback, and check-run accepts pass, fail, blocked, and insufficient.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_contract_self_consistency.py -q _(id: [rec-19a87492-4386-45cb-9b12-53cf66c22e09](.artifacts/records/project__acceptance/rec-19a87492-4386-45cb-9b12-53cf66c22e09.md))_

## verify-evidence-loop-readme

### Acceptance
- **verify-evidence-loop-readme**: The README states the two modes, the verify/assess split, the evidence escalation ladder, and that release ready is not deployed.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_readme_lifecycle.py -q _(id: [rec-a072e603-a6d5-4e9c-9f0d-2b55f6543af8](.artifacts/records/project__acceptance/rec-a072e603-a6d5-4e9c-9f0d-2b55f6543af8.md))_

## verify-evidence-loop-skills

### Acceptance
- **verify-evidence-loop-skills**: The six skills document only contract-legal writes for specification, design, trace fields, integration-report, and assessment routing.; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_discuss_skill.py tests/test_plan_trace.py tests/test_integrate_rules.py tests/test_assess_routing.py -q _(id: [rec-a7ead56b-fe80-4a0d-a5ae-9b34a976c46f](.artifacts/records/project__acceptance/rec-a7ead56b-fe80-4a0d-a5ae-9b34a976c46f.md))_

## verify-evidence-matrix

### Acceptance
- **verify-evidence-matrix**: Matrix row values, tones, blockers, and strip glyphs hold in model tests; pilots cover Enter, width dropping, and strip click; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_requirement.py tests/test_dashboard_phase_screen.py -q -k matrix _(id: [rec-44755f3e-cfe0-44bf-8751-6f8850f4700a](.artifacts/records/project__acceptance/rec-44755f3e-cfe0-44bf-8751-6f8850f4700a.md))_

### Check
- **verify-evidence-matrix**: rec-44755f3e-cfe0-44bf-8751-6f8850f4700a; dirty; pass; check _(id: [rec-701861ae-0cbf-431d-b38f-8500d7ba6486](.artifacts/records/project__check-run/rec-701861ae-0cbf-431d-b38f-8500d7ba6486.md))_

## verify-evidence-matrix-suite

### Acceptance
- **verify-evidence-matrix-suite**: the evidence-matrix checks pass; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_requirement.py tests/test_dashboard_phase_screen.py -q -k matrix _(id: [rec-90a86f40-7f74-4dc3-875a-9d1043564b55](.artifacts/records/project__acceptance/rec-90a86f40-7f74-4dc3-875a-9d1043564b55.md))_

### Check
- **verify-evidence-matrix-suite**: rec-90a86f40-7f74-4dc3-875a-9d1043564b55; dirty; pass; check _(id: [rec-af62d62f-5d5b-4918-85b1-f1d681f7a05e](.artifacts/records/project__check-run/rec-af62d62f-5d5b-4918-85b1-f1d681f7a05e.md))_
- **verify-evidence-matrix-suite**: rec-242ca52f-0229-46fb-8334-e9d041b5c06d; dirty; pass; check _(id: [rec-db8ec3ec-aca0-46a3-b3ac-d073165f0ad7](.artifacts/records/project__check-run/rec-db8ec3ec-aca0-46a3-b3ac-d073165f0ad7.md))_

## verify-evidence-view

### Acceptance
- **verify-evidence-view**: Through the real tmux entry point a structured phase shows unassessed, an upstream route under Needs you, then R n/m verified, the stage word, Release ready, and a requirement detail opened by keys; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_e2e_dashboard.py -q -m tmux -k evidence _(id: [rec-7ed13ebd-7b0a-436b-9c12-dfd4ef8cefcd](.artifacts/records/project__acceptance/rec-7ed13ebd-7b0a-436b-9c12-dfd4ef8cefcd.md))_

### Check
- **verify-evidence-view**: rec-7ed13ebd-7b0a-436b-9c12-dfd4ef8cefcd; dirty; pass; tdd _(id: [rec-e9556130-ae13-4c2f-9877-8be6e9aed7b5](.artifacts/records/project__check-run/rec-e9556130-ae13-4c2f-9877-8be6e9aed7b5.md))_

## verify-evidence-view-app

### Acceptance
- **verify-evidence-view-app**: Exit criterion 2: the app and requirement screen pilot tests pass; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py tests/test_dashboard_requirement.py -q _(id: [rec-08b630d4-2e32-4b18-a674-8d21a0733158](.artifacts/records/project__acceptance/rec-08b630d4-2e32-4b18-a674-8d21a0733158.md))_

### Check
- **verify-evidence-view-app**: rec-08b630d4-2e32-4b18-a674-8d21a0733158; dirty; pass; check _(id: [rec-c3d8c774-9eba-446a-851a-c14513e7f9f7](.artifacts/records/project__check-run/rec-c3d8c774-9eba-446a-851a-c14513e7f9f7.md))_

## verify-evidence-view-legacy

### Acceptance
- **verify-evidence-view-legacy**: Exit criterion 3: a store whose contract lacks the evidence types loads with no error; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k 'evidence and legacy' _(id: [rec-04bc526a-2703-4f22-8c56-9b068bc7869b](.artifacts/records/project__acceptance/rec-04bc526a-2703-4f22-8c56-9b068bc7869b.md))_

### Check
- **verify-evidence-view-legacy**: rec-04bc526a-2703-4f22-8c56-9b068bc7869b; dirty; pass; check _(id: [rec-16ef55d5-c4c5-42dd-9dc3-f12f8ed4711c](.artifacts/records/project__check-run/rec-16ef55d5-c4c5-42dd-9dc3-f12f8ed4711c.md))_

## verify-evidence-view-model

### Acceptance
- **verify-evidence-view-model**: Exit criterion 1: the evidence model tests pass; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k evidence _(id: [rec-ab6549b4-827c-4cb8-9fd1-4adcc54de77d](.artifacts/records/project__acceptance/rec-ab6549b4-827c-4cb8-9fd1-4adcc54de77d.md))_

### Check
- **verify-evidence-view-model**: rec-ab6549b4-827c-4cb8-9fd1-4adcc54de77d; dirty; pass; check _(id: [rec-571ad7b4-d991-4250-8066-99335077a868](.artifacts/records/project__check-run/rec-571ad7b4-d991-4250-8066-99335077a868.md))_

## verify-evidence-view-readme

### Acceptance
- **verify-evidence-view-readme**: Exit criterion 4: the README documents the requirement detail, the tally, the stage strip and word, Release ready, and the new Needs-you items; check; dashboard; grep -qi 'requirement detail' README.md && grep -q 'verified' README.md && grep -qi 'release ready' README.md && grep -qi 'stage' README.md _(id: [rec-338cf500-251e-4741-8168-ea67b1147ccc](.artifacts/records/project__acceptance/rec-338cf500-251e-4741-8168-ea67b1147ccc.md))_

### Check
- **verify-evidence-view-readme**: rec-338cf500-251e-4741-8168-ea67b1147ccc; dirty; pass; check _(id: [rec-869ea489-1127-4ac8-b27d-f003336f11d3](.artifacts/records/project__check-run/rec-869ea489-1127-4ac8-b27d-f003336f11d3.md))_

## verify-evidence-view-suite

### Acceptance
- **verify-evidence-view-suite**: Exit criterion 4: the full suite passes, including the tmux tests; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m 'not tmux' && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-ffb67717-3553-4bc6-9497-fb877731866f](.artifacts/records/project__acceptance/rec-ffb67717-3553-4bc6-9497-fb877731866f.md))_

### Check
- **verify-evidence-view-suite**: rec-ffb67717-3553-4bc6-9497-fb877731866f; dirty; pass; check _(id: [rec-546ad19a-e086-4be8-ad6d-39ff6135a78f](.artifacts/records/project__check-run/rec-546ad19a-e086-4be8-ad6d-39ff6135a78f.md))_

## verify-human-gates

### Acceptance
- **verify-human-gates**: dashboard/bin/dashboard --once against a seeded store with plan-review, Landing, and a quiet task prints action verbs, a next-step line, and landing branch/ahead/merged on the selector; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_integration.py -q -k "gates or once" _(id: [rec-c61f4280-d622-4017-83d1-4a8222faed84](.artifacts/records/project__acceptance/rec-c61f4280-d622-4017-83d1-4a8222faed84.md))_

### Check
- **verify-human-gates**: rec-c61f4280-d622-4017-83d1-4a8222faed84; dirty; pass; check _(id: [rec-65fe5f9e-0653-44de-a8a1-b48a7afa10d3](.artifacts/records/project__check-run/rec-65fe5f9e-0653-44de-a8a1-b48a7afa10d3.md))_

## verify-human-gates-app

### Acceptance
- **verify-human-gates-app**: c copies the prompt and new items trigger the message and bell in a Textual pilot with tmux stubbed; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k gates _(id: [rec-d63e9f38-6953-44e4-a67f-8793531de963](.artifacts/records/project__acceptance/rec-d63e9f38-6953-44e4-a67f-8793531de963.md))_

### Check
- **verify-human-gates-app**: rec-d63e9f38-6953-44e4-a67f-8793531de963; dirty; pass; check _(id: [rec-92a4682a-8b32-4f73-bfcb-6d3c812c1af4](.artifacts/records/project__check-run/rec-92a4682a-8b32-4f73-bfcb-6d3c812c1af4.md))_

## verify-human-gates-model

### Acceptance
- **verify-human-gates-model**: Verbs, plan-review recognition, prompt text, next-step rules, landing state, Merge branch item, and quiet rule hold in model and gates tests; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_gates.py -q -k gates _(id: [rec-8ca825cb-80c2-47cc-9b12-ebfeb449dca9](.artifacts/records/project__acceptance/rec-8ca825cb-80c2-47cc-9b12-ebfeb449dca9.md))_

### Check
- **verify-human-gates-model**: rec-8ca825cb-80c2-47cc-9b12-ebfeb449dca9; dirty; pass; check _(id: [rec-882ec15d-d5e0-4cf1-b2cf-34855cb81c4a](.artifacts/records/project__check-run/rec-882ec15d-d5e0-4cf1-b2cf-34855cb81c4a.md))_

## verify-human-gates-suite

### Acceptance
- **verify-human-gates-suite**: The full non-tmux and tmux test suites pass; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m "not tmux" && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-84b6b2c0-f0cc-49a6-93fd-ebd2e5390f9a](.artifacts/records/project__acceptance/rec-84b6b2c0-f0cc-49a6-93fd-ebd2e5390f9a.md))_

### Check
- **verify-human-gates-suite**: rec-84b6b2c0-f0cc-49a6-93fd-ebd2e5390f9a; dirty; pass; check _(id: [rec-4d33d4c5-08df-486b-99d0-ce5aab20392e](.artifacts/records/project__check-run/rec-4d33d4c5-08df-486b-99d0-ce5aab20392e.md))_

## verify-human-gates-tmux

### Acceptance
- **verify-human-gates-tmux**: The status-right needs-you segment appears in a real tmux server when enabled; check; dashboard; uv run --with textual --with pytest python -m pytest tests -q -m tmux -k "status and (gates or needs or segment)" _(id: [rec-fa10fcaa-3669-4d69-a554-844faf4d41b6](.artifacts/records/project__acceptance/rec-fa10fcaa-3669-4d69-a554-844faf4d41b6.md))_

### Check
- **verify-human-gates-tmux**: rec-fa10fcaa-3669-4d69-a554-844faf4d41b6; dirty; pass; check _(id: [rec-281456a3-47c1-4258-b732-c664aa99a58b](.artifacts/records/project__check-run/rec-281456a3-47c1-4258-b732-c664aa99a58b.md))_

## verify-journal-view

### Acceptance
- **verify-journal-view**: Journal scoping, open-first order, kind panel, and agent-work blocks hold in model and pilot tests; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_journal.py tests/test_dashboard_app.py -q -k journal _(id: [rec-23b9ae39-56ef-401b-b2df-9b05b78d4967](.artifacts/records/project__acceptance/rec-23b9ae39-56ef-401b-b2df-9b05b78d4967.md))_

### Check
- **verify-journal-view**: rec-23b9ae39-56ef-401b-b2df-9b05b78d4967; 1eb4f7a6723b779267bc14d030951640dff5c6a3; pass; check _(id: [rec-64cc1377-67d4-40d8-9e29-eed31077423b](.artifacts/records/project__check-run/rec-64cc1377-67d4-40d8-9e29-eed31077423b.md))_

## verify-journal-view-suite

### Acceptance
- **verify-journal-view-suite**: the journal-view checks pass; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_journal.py tests/test_dashboard_app.py -q -k journal _(id: [rec-628b0b42-c0af-421a-a077-8f9238c5eb0b](.artifacts/records/project__acceptance/rec-628b0b42-c0af-421a-a077-8f9238c5eb0b.md))_

### Check
- **verify-journal-view-suite**: rec-628b0b42-c0af-421a-a077-8f9238c5eb0b; 1eb4f7a6723b779267bc14d030951640dff5c6a3; pass; check _(id: [rec-fd830ba3-b57a-46b3-807f-15d1ebd1197f](.artifacts/records/project__check-run/rec-fd830ba3-b57a-46b3-807f-15d1ebd1197f.md))_

## verify-layout-phase

### Acceptance
- **verify-layout-phase**: The tmux popup layout test passes, README shows the tab row with number keys, and the full suite passes; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m 'not tmux' && uv run --with textual --with pytest python -m pytest tests -q -m tmux -rf _(id: [rec-5d64f143-cdea-49dc-8cb4-7ca9fb9f2517](.artifacts/records/project__acceptance/rec-5d64f143-cdea-49dc-8cb4-7ca9fb9f2517.md))_

### Check
- **verify-layout-phase**: rec-5d64f143-cdea-49dc-8cb4-7ca9fb9f2517; d9e3eebae5096d3bfd0852e9a910fe4e8df9a725; pass; check _(id: [rec-b2b9ebb8-5411-4a63-93c3-1028295a1ce7](.artifacts/records/project__check-run/rec-b2b9ebb8-5411-4a63-93c3-1028295a1ce7.md))_

## verify-navigation-phase

### Acceptance
- **verify-navigation-phase**: The tmux popup navigation test passes, README documents detail links, and the full suite passes; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m 'not tmux' && uv run --with textual --with pytest python -m pytest tests -q -m tmux -rf _(id: [rec-d1da938c-12b5-4cb9-9f02-e4a6731c1222](.artifacts/records/project__acceptance/rec-d1da938c-12b5-4cb9-9f02-e4a6731c1222.md))_

### Check
- **verify-navigation-phase**: rec-d1da938c-12b5-4cb9-9f02-e4a6731c1222; b892587e80bbd40f785d3e104581a5587c250406; pass; check _(id: [rec-f864bb3e-40ce-4a6d-b048-471044f223c5](.artifacts/records/project__check-run/rec-f864bb3e-40ce-4a6d-b048-471044f223c5.md))_

## verify-needs-you-close

### Acceptance
- **verify-needs-you-close**: Dashboard dismiss pilots pass through the Textual app entry point for human-dismissible kinds and refuse non-human kinds; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k dismiss _(id: [rec-acabf3ed-70af-4c45-bbc2-55df0b063fec](.artifacts/records/project__acceptance/rec-acabf3ed-70af-4c45-bbc2-55df0b063fec.md))_

### Check
- **verify-needs-you-close**: rec-acabf3ed-70af-4c45-bbc2-55df0b063fec; 8799ca930443a9a3144434eaf3b9e30e497adbce; pass; tdd _(id: [rec-5c64fd33-a70b-495b-966f-eda2ef698239](.artifacts/records/project__check-run/rec-5c64fd33-a70b-495b-966f-eda2ef698239.md))_

### Observation
- **verify-needs-you-close**: All three phase verify_commands passed: dismiss 4, refuse/fail 2, skills 18; workflow-loop _(id: [rec-ca617edc-862b-403f-b7f0-193fd05ff8bb](.artifacts/records/project__investigation-observation/rec-ca617edc-862b-403f-b7f0-193fd05ff8bb.md))_

## verify-needs-you-close-refuse

### Acceptance
- **verify-needs-you-close-refuse**: Dismiss refuse and CLI-failure pilots keep non-human and failed items open with an error through the app; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'dismiss and (refuse or fail or error)' _(id: [rec-519937ac-4467-4bbd-8f45-7786679a7d4f](.artifacts/records/project__acceptance/rec-519937ac-4467-4bbd-8f45-7786679a7d4f.md))_

### Check
- **verify-needs-you-close-refuse**: rec-519937ac-4467-4bbd-8f45-7786679a7d4f; 8799ca930443a9a3144434eaf3b9e30e497adbce; pass; tdd _(id: [rec-0971c5bf-012b-47c8-846d-25a165e3d9b1](.artifacts/records/project__check-run/rec-0971c5bf-012b-47c8-846d-25a165e3d9b1.md))_

## verify-needs-you-close-skills

### Acceptance
- **verify-needs-you-close-skills**: Skill contract consistency and engage/clear documentation tests pass; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_discuss_skill.py -q _(id: [rec-53401a27-dd75-4ef2-adbb-a699505dc9fc](.artifacts/records/project__acceptance/rec-53401a27-dd75-4ef2-adbb-a699505dc9fc.md))_

### Check
- **verify-needs-you-close-skills**: rec-53401a27-dd75-4ef2-adbb-a699505dc9fc; 8799ca930443a9a3144434eaf3b9e30e497adbce; pass; check _(id: [rec-2bc38933-9600-44a1-af0c-4a16f8c7f191](.artifacts/records/project__check-run/rec-2bc38933-9600-44a1-af0c-4a16f8c7f191.md))_

## verify-needs-you-data-phase

### Acceptance
- **verify-needs-you-data-phase**: The tmux popup tests pass with six tabs, a counted Needs you title and a readable unsigned line, and the full suite passes; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m 'not tmux' && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-fe83e6fe-5005-4c88-97e8-3c15e744047a](.artifacts/records/project__acceptance/rec-fe83e6fe-5005-4c88-97e8-3c15e744047a.md))_

### Check
- **verify-needs-you-data-phase**: rec-fe83e6fe-5005-4c88-97e8-3c15e744047a; e4484c4c6ed29016f301e3e963957a2aa7bfdcac; pass; check _(id: [rec-0d607cff-8414-4a07-886b-115e54b99dbe](.artifacts/records/project__check-run/rec-0d607cff-8414-4a07-886b-115e54b99dbe.md))_

## verify-needs-you-phase

### Acceptance
- **verify-needs-you-phase**: The tmux popup test for Needs you and finished efforts passes, README documents n and the Needs-you detail, and the full suite passes; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m 'not tmux' && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-d5958a14-e6a7-4c20-b110-5ae0c0ee54a3](.artifacts/records/project__acceptance/rec-d5958a14-e6a7-4c20-b110-5ae0c0ee54a3.md))_

### Check
- **verify-needs-you-phase**: rec-d5958a14-e6a7-4c20-b110-5ae0c0ee54a3; 94e39818ef6151434de8ef1617c69e0c9dcbda6b; pass; check _(id: [rec-e5ff5760-6474-4fc5-8f68-9d1e0a3d4453](.artifacts/records/project__check-run/rec-e5ff5760-6474-4fc5-8f68-9d1e0a3d4453.md))_

### Observation
- **verify-needs-you-phase**: tab from a live effort with Needs you items to a pane whose task table is hidden bounces back: Screen._reset_focus moves focus from the hidden TaskTable to the sibling NeedsList, and TabbedContent re-activates the pane holding focus. Reproduces every run; absent without Needs you items.; dashboard-features _(id: [rec-63c67821-d6d9-4012-8437-37c5beda8310](.artifacts/records/project__investigation-observation/rec-63c67821-d6d9-4012-8437-37c5beda8310.md))_

## verify-phase-landing

### Acceptance
- **verify-phase-landing**: plan-phase and execute-phase name the same landing: branch phase/<phase-slug>, the sibling worktree, base main, merge into main, store commit on the primary checkout, and push only as a human stop; tdd; workflow-loop; python3 -m pytest tests/test_phase_landing.py tests/test_plan_landing.py tests/test_execute_landing.py -q _(id: [rec-5f277ff6-f5de-48ae-a3fa-43825f135561](.artifacts/records/project__acceptance/rec-5f277ff6-f5de-48ae-a3fa-43825f135561.md))_

### Check
- **verify-phase-landing**: rec-c376fad0-9993-4448-9e97-21adc7a1ec8d; dirty; pass; tdd _(id: [rec-1795aff9-df1b-49c3-97ae-46cc6beb5a7b](.artifacts/records/project__check-run/rec-1795aff9-df1b-49c3-97ae-46cc6beb5a7b.md))_
- **verify-phase-landing**: rec-5f277ff6-f5de-48ae-a3fa-43825f135561; dirty; pass; tdd _(id: [rec-55600d6d-b7b7-4816-8df3-1680e8abfb98](.artifacts/records/project__check-run/rec-55600d6d-b7b7-4816-8df3-1680e8abfb98.md))_
- **verify-phase-landing**: rec-58522d3a-4f28-4cd8-bcf8-4f8ab951dd54; dirty; pass; tdd _(id: [rec-99acf357-0cc7-4cce-8a8b-d102945d8956](.artifacts/records/project__check-run/rec-99acf357-0cc7-4cce-8a8b-d102945d8956.md))_

## verify-phase-landing-execute

### Acceptance
- **verify-phase-landing-execute**: execute-phase creates the worktree, keeps the store on the primary checkout, merges the phase branch into main, and does not push unless Landing names push as a stop; tdd; workflow-loop; python3 -m pytest tests/test_execute_landing.py -q _(id: [rec-c376fad0-9993-4448-9e97-21adc7a1ec8d](.artifacts/records/project__acceptance/rec-c376fad0-9993-4448-9e97-21adc7a1ec8d.md))_

## verify-phase-landing-plan

### Acceptance
- **verify-phase-landing-plan**: plan-phase requires a Landing section before plan review, and incidental work skips it; tdd; workflow-loop; python3 -m pytest tests/test_plan_landing.py -q _(id: [rec-58522d3a-4f28-4cd8-bcf8-4f8ab951dd54](.artifacts/records/project__acceptance/rec-58522d3a-4f28-4cd8-bcf8-4f8ab951dd54.md))_

## verify-phase-reviewer

### Acceptance
- **verify-phase-reviewer**: Through pytest entry point, phase-reviewer tests prove brief limits, parent review check-run/findings, fix routing, one re-run, gate, and integration-report from reviewer output; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py -q _(id: [rec-a5b4ff28-4664-45b7-9b25-489d4f58af19](.artifacts/records/project__acceptance/rec-a5b4ff28-4664-45b7-9b25-489d4f58af19.md))_

### Check
- **verify-phase-reviewer**: rec-a5b4ff28-4664-45b7-9b25-489d4f58af19; e5b769d5e7bf6a24f52d7ec7abc6b77190aad96a; fail; tdd _(id: [rec-1f4f33ef-460a-44cc-8c60-c7beee639790](.artifacts/records/project__check-run/rec-1f4f33ef-460a-44cc-8c60-c7beee639790.md))_
- **verify-phase-reviewer**: rec-a5b4ff28-4664-45b7-9b25-489d4f58af19; 11a147e75daa100a2fbca2202399205b480b42e9; pass; tdd _(id: [rec-ffac3710-847f-458c-a367-9a5061c23261](.artifacts/records/project__check-run/rec-ffac3710-847f-458c-a367-9a5061c23261.md))_

## verify-phase-reviewer-agent

### Acceptance
- **verify-phase-reviewer-agent**: Reviewer agent exists with restricted tools and sync-plugin installs it; execute-phase documents phase-end invocation after verification; check; workflow-loop; test -f agents/se-reviewer.md && grep -qiE "no Write|without Write" agents/se-reviewer.md && grep -q agents/ scripts/sync-plugin.sh && grep -qiE "reviewer|se-reviewer" skills/execute-phase/SKILL.md _(id: [rec-1c47f604-3a3d-43ce-b488-7f0dc461180e](.artifacts/records/project__acceptance/rec-1c47f604-3a3d-43ce-b488-7f0dc461180e.md))_

### Check
- **verify-phase-reviewer-agent**: rec-1c47f604-3a3d-43ce-b488-7f0dc461180e; 11a147e75daa100a2fbca2202399205b480b42e9; pass; check _(id: [rec-5078fe00-d85e-49a7-b9ea-e9793ef902eb](.artifacts/records/project__check-run/rec-5078fe00-d85e-49a7-b9ea-e9793ef902eb.md))_

## verify-phase-reviewer-contract

### Acceptance
- **verify-phase-reviewer-contract**: Skill and contract consistency stay green with review check-run and phase-end reviewer writes; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_contract_self_consistency.py -q _(id: [rec-5fe7f197-7081-4e2e-a8dd-bd9014170eaf](.artifacts/records/project__acceptance/rec-5fe7f197-7081-4e2e-a8dd-bd9014170eaf.md))_

### Check
- **verify-phase-reviewer-contract**: rec-5fe7f197-7081-4e2e-a8dd-bd9014170eaf; 11a147e75daa100a2fbca2202399205b480b42e9; pass; check _(id: [rec-3012d3ea-a62d-4087-8c33-d3422223f820](.artifacts/records/project__check-run/rec-3012d3ea-a62d-4087-8c33-d3422223f820.md))_

## verify-phase-reviewer-fixture

### Acceptance
- **verify-phase-reviewer-fixture**: status-tabs fixture returns NEEDS_WORK / spec-gap; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py -q -k status_tabs _(id: [rec-14227c0e-f22a-4354-92b7-eb89f4eba878](.artifacts/records/project__acceptance/rec-14227c0e-f22a-4354-92b7-eb89f4eba878.md))_

### Check
- **verify-phase-reviewer-fixture**: rec-14227c0e-f22a-4354-92b7-eb89f4eba878; 11a147e75daa100a2fbca2202399205b480b42e9; pass; tdd _(id: [rec-5b936122-cc58-4c04-871d-68359835b5da](.artifacts/records/project__check-run/rec-5b936122-cc58-4c04-871d-68359835b5da.md))_
- **verify-phase-reviewer-fixture**: rec-14227c0e-f22a-4354-92b7-eb89f4eba878; e5b769d5e7bf6a24f52d7ec7abc6b77190aad96a; fail; tdd _(id: [rec-cc0d0a68-bc39-41f2-aefa-ab1e8a01c42f](.artifacts/records/project__check-run/rec-cc0d0a68-bc39-41f2-aefa-ab1e8a01c42f.md))_

## verify-phase-reviewer-gate

### Acceptance
- **verify-phase-reviewer-gate**: Phase gate requires passing review at head before merge; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_phase_reviewer.py -q -k gate _(id: [rec-47250685-0161-4993-80af-7bd73bdce32b](.artifacts/records/project__acceptance/rec-47250685-0161-4993-80af-7bd73bdce32b.md))_

### Check
- **verify-phase-reviewer-gate**: rec-47250685-0161-4993-80af-7bd73bdce32b; e5b769d5e7bf6a24f52d7ec7abc6b77190aad96a; fail; tdd _(id: [rec-59db4225-ccae-4eb8-b66a-5ae39fc0f6df](.artifacts/records/project__check-run/rec-59db4225-ccae-4eb8-b66a-5ae39fc0f6df.md))_
- **verify-phase-reviewer-gate**: rec-47250685-0161-4993-80af-7bd73bdce32b; 11a147e75daa100a2fbca2202399205b480b42e9; pass; tdd _(id: [rec-e4302069-0e0a-4871-bc13-0bda3c12a807](.artifacts/records/project__check-run/rec-e4302069-0e0a-4871-bc13-0bda3c12a807.md))_

## verify-phase-selector

### Acceptance
- **verify-phase-selector**: dashboard/bin/dashboard --once prints the selector line and wave strip at the default selection; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_integration.py -q -k once _(id: [rec-a14d5cc4-9daf-4279-9625-b803a75d93cb](.artifacts/records/project__acceptance/rec-a14d5cc4-9daf-4279-9625-b803a75d93cb.md))_

### Check
- **verify-phase-selector**: rec-c559dd9b-03f5-4cb5-8d62-8dff85a9ad2e; dirty; pass; check _(id: [rec-0ed70697-b26d-4565-ac2b-aa9667183cb7](.artifacts/records/project__check-run/rec-0ed70697-b26d-4565-ac2b-aa9667183cb7.md))_
- **verify-phase-selector**: rec-a11805b7-bc3c-4f57-bcb4-db7d8ffa9ed9; dirty; fail; check _(id: [rec-2e3ddfae-c775-4b2e-8497-05064b8042fa](.artifacts/records/project__check-run/rec-2e3ddfae-c775-4b2e-8497-05064b8042fa.md))_
- **verify-phase-selector**: rec-2924db08-5149-4136-bbd9-b6deb59a93b8; dirty; pass; check _(id: [rec-9b7a3ab5-4d12-4e39-ae0a-c64d2dc14669](.artifacts/records/project__check-run/rec-9b7a3ab5-4d12-4e39-ae0a-c64d2dc14669.md))_
- **verify-phase-selector**: rec-a14d5cc4-9daf-4279-9625-b803a75d93cb; dirty; pass; check _(id: [rec-f836b11f-ee98-4e95-a264-3ea7f5f761bb](.artifacts/records/project__check-run/rec-f836b11f-ee98-4e95-a264-3ea7f5f761bb.md))_
- **verify-phase-selector**: rec-a11805b7-bc3c-4f57-bcb4-db7d8ffa9ed9; dirty; pass; check _(id: [rec-fe8dbe67-529a-4306-a1d4-9fcf5698bd41](.artifacts/records/project__check-run/rec-fe8dbe67-529a-4306-a1d4-9fcf5698bd41.md))_

## verify-phase-selector-app

### Acceptance
- **verify-phase-selector-app**: Textual pilot tests for selector, picker, keys, wave strip, finished toggle, and key help pass; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q _(id: [rec-2924db08-5149-4136-bbd9-b6deb59a93b8](.artifacts/records/project__acceptance/rec-2924db08-5149-4136-bbd9-b6deb59a93b8.md))_

## verify-phase-selector-model

### Acceptance
- **verify-phase-selector-model**: Model and task tests for default selection, follow/pin, merged activity, scoped counts, and All-phases grouping pass; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_tasks.py -q _(id: [rec-c559dd9b-03f5-4cb5-8d62-8dff85a9ad2e](.artifacts/records/project__acceptance/rec-c559dd9b-03f5-4cb5-8d62-8dff85a9ad2e.md))_

## verify-phase-selector-suite

### Acceptance
- **verify-phase-selector-suite**: Full non-tmux and tmux test suites pass; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m not tmux && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-a11805b7-bc3c-4f57-bcb4-db7d8ffa9ed9](.artifacts/records/project__acceptance/rec-a11805b7-bc3c-4f57-bcb4-db7d8ffa9ed9.md))_

## verify-plugin-dep-marketplace

### Acceptance
- **verify-plugin-dep-marketplace**: claude plugin validate . succeeds with both plugins listed and adaptive-artifacts dependency declared (exit criterion 1, real entry point); check; packaging; claude plugin validate . && python3 -c "import json;p=json.load(open('.claude-plugin/plugin.json'));d=p.get('dependencies',[]);assert 'adaptive-artifacts' in d or any(isinstance(x,dict) and x.get('name')=='adaptive-artifacts' for x in d);m=json.load(open('.claude-plugin/marketplace.json'));assert {x.get('name') for x in m['plugins']}>= {'se-workflow','adaptive-artifacts'}" _(id: [rec-463ee27b-5093-4184-bbf6-7b80770d43ac](.artifacts/records/project__acceptance/rec-463ee27b-5093-4184-bbf6-7b80770d43ac.md))_

### Check
- **verify-plugin-dep-marketplace**: rec-463ee27b-5093-4184-bbf6-7b80770d43ac; 40db2970236ac7ff04afd9eaf08292f072a912a2; pass; check _(id: [rec-b1f44839-d82d-48a0-86c5-662ab8a5aa40](.artifacts/records/project__check-run/rec-b1f44839-d82d-48a0-86c5-662ab8a5aa40.md))_

## verify-plugin-dep-marketplace-readme

### Acceptance
- **verify-plugin-dep-marketplace-readme**: README Install matches manifests: single Claude marketplace add; Cursor does not claim dependency auto-install (exit criteria 2-3); check; packaging; grep -q 'claude plugin marketplace add andrewy1n/se-workflow' README.md && grep -qi Cursor README.md && ! grep -qiE 'Cursor.*(auto-?install|plugin dependenc).*adaptive-artifacts' README.md _(id: [rec-c30aaca7-94df-4c02-a6f3-fcce0c8d6b00](.artifacts/records/project__acceptance/rec-c30aaca7-94df-4c02-a6f3-fcce0c8d6b00.md))_

### Check
- **verify-plugin-dep-marketplace-readme**: rec-c30aaca7-94df-4c02-a6f3-fcce0c8d6b00; 40db2970236ac7ff04afd9eaf08292f072a912a2; pass; check _(id: [rec-78e62280-8d1d-4f1d-95ba-eabd70e4efeb](.artifacts/records/project__check-run/rec-78e62280-8d1d-4f1d-95ba-eabd70e4efeb.md))_

## verify-plugin-root-and-cli

### Acceptance
- **verify-plugin-root-and-cli**: Exit 1: shared AA resolve order and plugin-root docs hold (unit + grep gates); tdd; packaging; uv run --with pytest python -m pytest tests/test_aa_resolve.py -q && grep -q CLAUDE_PLUGIN_ROOT skills/ensure-store.md && grep -q CURSOR_PLUGIN_ROOT skills/ensure-store.md && ! grep -E '^[0-9]+\. .*\.cursor/plugins/local/se-workflow' skills/ensure-store.md && ! grep -n "Path.home() / \"adaptive-artifacts\"" se_workflow/aa.py dashboard/artifact_store.py _(id: [rec-d1532551-f82b-44a4-94c5-de313a93d078](.artifacts/records/project__acceptance/rec-d1532551-f82b-44a4-94c5-de313a93d078.md))_

### Check
- **verify-plugin-root-and-cli**: rec-d1532551-f82b-44a4-94c5-de313a93d078; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; tdd _(id: [rec-2c5ab419-57ca-454c-bb77-b31fa827c8f9](.artifacts/records/project__check-run/rec-2c5ab419-57ca-454c-bb77-b31fa827c8f9.md))_
- **verify-plugin-root-and-cli**: rec-d1532551-f82b-44a4-94c5-de313a93d078; dirty; fail; tdd _(id: [rec-48b7e94c-45cb-4821-a3ed-6419005cf989](.artifacts/records/project__check-run/rec-48b7e94c-45cb-4821-a3ed-6419005cf989.md))_
- **verify-plugin-root-and-cli**: rec-d1532551-f82b-44a4-94c5-de313a93d078; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; tdd _(id: [rec-63797327-51f1-4c0f-82ef-e872e3955d6e](.artifacts/records/project__check-run/rec-63797327-51f1-4c0f-82ef-e872e3955d6e.md))_
- **verify-plugin-root-and-cli**: rec-e2174663-bdbf-4250-aa23-5075f95e0c8d; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; manual; inline _(id: [rec-f6cba71a-4b1d-46dc-bf7d-aa1ca14e1b26](.artifacts/records/project__check-run/rec-f6cba71a-4b1d-46dc-bf7d-aa1ca14e1b26.md))_

## verify-plugin-root-and-cli-close

### Acceptance
- **verify-plugin-root-and-cli-close**: Exit 2: bin/se-workflow close-batch works through CLI; skills do not call scripts/close_batch.py; tdd; packaging; uv run --with pytest python -m pytest tests/test_close_batch.py -q && grep -qE 'se-workflow close-batch|bin/se-workflow close-batch' skills/verify-work/SKILL.md && ! grep -q scripts/close_batch.py skills/verify-work/SKILL.md && uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py -q _(id: [rec-db3cca7b-c7b5-482b-be36-b59f59c5621b](.artifacts/records/project__acceptance/rec-db3cca7b-c7b5-482b-be36-b59f59c5621b.md))_

### Check
- **verify-plugin-root-and-cli-close**: rec-db3cca7b-c7b5-482b-be36-b59f59c5621b; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; tdd _(id: [rec-03d83276-1c06-4e72-8435-27ec1f7d47dd](.artifacts/records/project__check-run/rec-03d83276-1c06-4e72-8435-27ec1f7d47dd.md))_
- **verify-plugin-root-and-cli-close**: rec-db3cca7b-c7b5-482b-be36-b59f59c5621b; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; tdd _(id: [rec-a6dede01-8956-457b-8b51-e0c8892a835b](.artifacts/records/project__check-run/rec-a6dede01-8956-457b-8b51-e0c8892a835b.md))_
- **verify-plugin-root-and-cli-close**: rec-db3cca7b-c7b5-482b-be36-b59f59c5621b; dirty; fail; tdd _(id: [rec-be6d0d5a-d576-41c7-9466-22e2c25a6304](.artifacts/records/project__check-run/rec-be6d0d5a-d576-41c7-9466-22e2c25a6304.md))_

## verify-plugin-root-and-cli-landing

### Acceptance
- **verify-plugin-root-and-cli-landing**: Exit 3: phase branch merged to main and store committed on primary checkout (Landing); manual; packaging _(id: [rec-e2174663-bdbf-4250-aa23-5075f95e0c8d](.artifacts/records/project__acceptance/rec-e2174663-bdbf-4250-aa23-5075f95e0c8d.md))_

### Check
- **verify-plugin-root-and-cli-landing**: rec-e2174663-bdbf-4250-aa23-5075f95e0c8d; 269ab7bde409ee04e1d7fa5de38363d9acb46c1e; pass; manual; inline _(id: [rec-50bafa17-3590-4c1e-8b34-946abf764d36](.artifacts/records/project__check-run/rec-50bafa17-3590-4c1e-8b34-946abf764d36.md))_

## verify-quiet-header

### Acceptance
- **verify-quiet-header**: dashboard --once prints the parenthetical tab line and the collapsed stepper; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k once_tally _(id: [rec-bc634371-b551-458a-a1c6-a010d02af538](.artifacts/records/project__acceptance/rec-bc634371-b551-458a-a1c6-a010d02af538.md))_

### Check
- **verify-quiet-header**: rec-bc634371-b551-458a-a1c6-a010d02af538; dirty; pass; check _(id: [rec-41d5454e-4c98-49ed-be3a-95a1619ced7d](.artifacts/records/project__check-run/rec-41d5454e-4c98-49ed-be3a-95a1619ced7d.md))_
- **verify-quiet-header**: rec-47663207-ae0c-4fd9-a2f8-e127cd7a753c; dirty; pass; check _(id: [rec-51df4b07-20c8-45d4-89b3-c227730a94d2](.artifacts/records/project__check-run/rec-51df4b07-20c8-45d4-89b3-c227730a94d2.md))_
- **verify-quiet-header**: rec-6fe96e57-e909-4bac-8895-59df57721d8d; dirty; pass; check _(id: [rec-6bc349cc-7f8f-4b98-9664-501e66f4361e](.artifacts/records/project__check-run/rec-6bc349cc-7f8f-4b98-9664-501e66f4361e.md))_
- **verify-quiet-header**: rec-b888f503-6a00-4777-899c-1887b314935d; dirty; pass; check _(id: [rec-9ca5e7d0-234a-40fa-b3d6-b1c664a9923b](.artifacts/records/project__check-run/rec-9ca5e7d0-234a-40fa-b3d6-b1c664a9923b.md))_
- **verify-quiet-header**: rec-ed5ce2ba-5329-44cc-9895-c8dc5586000b; dirty; pass; check _(id: [rec-9e451d65-8e48-4164-a466-b937fdb49495](.artifacts/records/project__check-run/rec-9e451d65-8e48-4164-a466-b937fdb49495.md))_
- **verify-quiet-header**: rec-40732634-5a9c-4595-bc25-89fe2a6a00cc; dirty; pass; check _(id: [rec-e485556f-ed51-46d1-a61f-2fb4d396d904](.artifacts/records/project__check-run/rec-e485556f-ed51-46d1-a61f-2fb4d396d904.md))_

## verify-quiet-header-headers

### Acceptance
- **verify-quiet-header-headers**: Done phase header rows have no check glyph; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k done_phases_collapse _(id: [rec-47663207-ae0c-4fd9-a2f8-e127cd7a753c](.artifacts/records/project__acceptance/rec-47663207-ae0c-4fd9-a2f8-e127cd7a753c.md))_

## verify-quiet-header-keys

### Acceptance
- **verify-quiet-header-keys**: Keys 1-6, left/right, and click still filter the table, and the footer still shows 1-6; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k "number_keys_filter or status_tabs_are_six" _(id: [rec-6fe96e57-e909-4bac-8895-59df57721d8d](.artifacts/records/project__acceptance/rec-6fe96e57-e909-4bac-8895-59df57721d8d.md))_

## verify-quiet-header-stepper

### Acceptance
- **verify-quiet-header-stepper**: An effort with more than two done phases shows N done, the current phase, and one next phase, with no green check, and activating the stepper expands the finished titles; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k stepper _(id: [rec-ed5ce2ba-5329-44cc-9895-c8dc5586000b](.artifacts/records/project__acceptance/rec-ed5ce2ba-5329-44cc-9895-c8dc5586000b.md))_

## verify-quiet-header-suite

### Acceptance
- **verify-quiet-header-suite**: The full suite passes, including the tmux tests; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m "not tmux" && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-40732634-5a9c-4595-bc25-89fe2a6a00cc](.artifacts/records/project__acceptance/rec-40732634-5a9c-4595-bc25-89fe2a6a00cc.md))_

## verify-quiet-header-tabs

### Acceptance
- **verify-quiet-header-tabs**: Six status tabs at 120 columns read Active (3) with no leading digit, a highlighted selected word, and a dim tally; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k "tab_row or tab_labels" _(id: [rec-b888f503-6a00-4777-899c-1887b314935d](.artifacts/records/project__acceptance/rec-b888f503-6a00-4777-899c-1887b314935d.md))_

## verify-readable-layout-phase

### Acceptance
- **verify-readable-layout-phase**: The full test suite passes with the new dashboard in the isolated tmux server; check; dashboard; uv run --with textual --with pytest python -m pytest tests -q _(id: [rec-b9c2eff5-a486-4b57-89bc-cc4a3aa95314](.artifacts/records/project__acceptance/rec-b9c2eff5-a486-4b57-89bc-cc4a3aa95314.md))_

### Check
- **verify-readable-layout-phase**: rec-b9c2eff5-a486-4b57-89bc-cc4a3aa95314; 360ebcc; pass; check _(id: [rec-0efdae3e-e624-4a9e-9b04-d42daa11fd0f](.artifacts/records/project__check-run/rec-0efdae3e-e624-4a9e-9b04-d42daa11fd0f.md))_

## verify-readable-layout-phase-signoff

### Acceptance
- **verify-readable-layout-phase-signoff**: The user views the dashboard in the popup and the side pane and signs off that it is readable and clean; manual; dashboard _(id: [rec-83820e9f-6ff5-407c-aa8f-deb4e441d5a5](.artifacts/records/project__acceptance/rec-83820e9f-6ff5-407c-aa8f-deb4e441d5a5.md))_

### Check
- **verify-readable-layout-phase-signoff**: rec-83820e9f-6ff5-407c-aa8f-deb4e441d5a5; 360ebcc; pass; manual; ayin _(id: [rec-ca53b246-7587-4e4e-9c59-75ca4deed553](.artifacts/records/project__check-run/rec-ca53b246-7587-4e4e-9c59-75ca4deed553.md))_

## verify-red-first

### Acceptance
- **verify-red-first**: Through close_batch.py CLI/entry, pass-only tdd done without finding exits 2 and names the criterion; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k red_first_pass_only _(id: [rec-c954223e-18ce-4392-ba4a-051f35046275](.artifacts/records/project__acceptance/rec-c954223e-18ce-4392-ba4a-051f35046275.md))_

### Check
- **verify-red-first**: rec-c954223e-18ce-4392-ba4a-051f35046275; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-28189b12-afcd-4c2b-a2c5-9800c98bf66b](.artifacts/records/project__check-run/rec-28189b12-afcd-4c2b-a2c5-9800c98bf66b.md))_
- **verify-red-first**: rec-c954223e-18ce-4392-ba4a-051f35046275; c14dedbd9ec027e7e79b8eb1508b24d0d65063fc; pass; tdd _(id: [rec-7ee60230-c110-4f33-b770-23ed56cf32bb](.artifacts/records/project__check-run/rec-7ee60230-c110-4f33-b770-23ed56cf32bb.md))_

## verify-red-first-escape

### Acceptance
- **verify-red-first-escape**: Finding escape permits close without red and forces needs human; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k red_first_escape _(id: [rec-964973af-b0ff-4bdc-b880-c49820487c8a](.artifacts/records/project__acceptance/rec-964973af-b0ff-4bdc-b880-c49820487c8a.md))_

### Check
- **verify-red-first-escape**: rec-964973af-b0ff-4bdc-b880-c49820487c8a; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-1cff2ee9-9d3b-4ca1-b202-6ad73892bc91](.artifacts/records/project__check-run/rec-1cff2ee9-9d3b-4ca1-b202-6ad73892bc91.md))_
- **verify-red-first-escape**: rec-964973af-b0ff-4bdc-b880-c49820487c8a; c14dedbd9ec027e7e79b8eb1508b24d0d65063fc; pass; tdd _(id: [rec-acd4ed29-d9f3-456b-bec8-9d7269cb547a](.artifacts/records/project__check-run/rec-acd4ed29-d9f3-456b-bec8-9d7269cb547a.md))_

## verify-red-first-methods

### Acceptance
- **verify-red-first-methods**: check and manual closes remain valid without red_check_run_id; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k red_first_other_methods _(id: [rec-9167287b-ab92-4409-89bd-e19a6db7f820](.artifacts/records/project__acceptance/rec-9167287b-ab92-4409-89bd-e19a6db7f820.md))_

### Check
- **verify-red-first-methods**: rec-9167287b-ab92-4409-89bd-e19a6db7f820; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-98211ba1-fc74-4a39-80ce-91eab05e1526](.artifacts/records/project__check-run/rec-98211ba1-fc74-4a39-80ce-91eab05e1526.md))_
- **verify-red-first-methods**: rec-9167287b-ab92-4409-89bd-e19a6db7f820; c14dedbd9ec027e7e79b8eb1508b24d0d65063fc; pass; tdd _(id: [rec-be32d9b7-5a1f-47e1-8095-3353c79104fa](.artifacts/records/project__check-run/rec-be32d9b7-5a1f-47e1-8095-3353c79104fa.md))_

## verify-red-first-order

### Acceptance
- **verify-red-first-order**: Fail→pass with valid ancestry or dirty red+diff_sha256 accepted; wrong order/non-ancestor refused; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_close_batch.py -q -k red_first_order _(id: [rec-cb28d166-0f0f-49ed-8751-925ad1e8d708](.artifacts/records/project__acceptance/rec-cb28d166-0f0f-49ed-8751-925ad1e8d708.md))_

### Check
- **verify-red-first-order**: rec-cb28d166-0f0f-49ed-8751-925ad1e8d708; c14dedbd9ec027e7e79b8eb1508b24d0d65063fc; pass; tdd _(id: [rec-449bcc1e-5bc3-4938-86e4-9db40d324a2f](.artifacts/records/project__check-run/rec-449bcc1e-5bc3-4938-86e4-9db40d324a2f.md))_
- **verify-red-first-order**: rec-cb28d166-0f0f-49ed-8751-925ad1e8d708; b3159b685f2992638a84ad36d56a81f9ed8e8151; fail; tdd _(id: [rec-bb86ff24-33c3-4950-b075-453cfc1ceaff](.artifacts/records/project__check-run/rec-bb86ff24-33c3-4950-b075-453cfc1ceaff.md))_

## verify-red-first-skills

### Acceptance
- **verify-red-first-skills**: verify-work matches enforced red-first; skill/contract consistency green; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_assess_routing.py -q _(id: [rec-5990039c-6afc-47d7-9a08-43aafa3d1a8e](.artifacts/records/project__acceptance/rec-5990039c-6afc-47d7-9a08-43aafa3d1a8e.md))_

### Check
- **verify-red-first-skills**: rec-5990039c-6afc-47d7-9a08-43aafa3d1a8e; c14dedbd9ec027e7e79b8eb1508b24d0d65063fc; pass; check _(id: [rec-423e77e6-9e33-4dd6-b9be-7823d6b85ac6](.artifacts/records/project__check-run/rec-423e77e6-9e33-4dd6-b9be-7823d6b85ac6.md))_

## verify-retry-loop

### Acceptance
- **verify-retry-loop**: Through pytest entry point, retry-loop tests prove redispatch, amendment, attempts, fix_task, budget, and next_plan; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_retry_loop.py -q _(id: [rec-882f6075-f91a-479c-b426-a0eee0ffba59](.artifacts/records/project__acceptance/rec-882f6075-f91a-479c-b426-a0eee0ffba59.md))_

### Check
- **verify-retry-loop**: rec-882f6075-f91a-479c-b426-a0eee0ffba59; ee1a41be208bfdae700e1b78f9340296d82dae91; fail; tdd _(id: [rec-06ceed68-9985-49ab-8afe-cb6f5ae46934](.artifacts/records/project__check-run/rec-06ceed68-9985-49ab-8afe-cb6f5ae46934.md))_
- **verify-retry-loop**: rec-882f6075-f91a-479c-b426-a0eee0ffba59; 0077727e7e8d3b25e53d5aa1722b5c8f9ca58577; pass; tdd _(id: [rec-1f8ce933-3053-4082-acc2-205434fa5917](.artifacts/records/project__check-run/rec-1f8ce933-3053-4082-acc2-205434fa5917.md))_

## verify-retry-loop-contract

### Acceptance
- **verify-retry-loop-contract**: Skill and contract consistency stay green with optional attempts declared; check; workflow-loop; uv run --with pytest python -m pytest tests/test_skill_contract_consistency.py tests/test_contract_self_consistency.py -q _(id: [rec-0b667469-29df-4007-a46b-05a8b860091a](.artifacts/records/project__acceptance/rec-0b667469-29df-4007-a46b-05a8b860091a.md))_

### Check
- **verify-retry-loop-contract**: rec-0b667469-29df-4007-a46b-05a8b860091a; 0077727e7e8d3b25e53d5aa1722b5c8f9ca58577; pass; check _(id: [rec-88071789-8032-4b6c-b4cf-208f9d56ad30](.artifacts/records/project__check-run/rec-88071789-8032-4b6c-b4cf-208f9d56ad30.md))_

## verify-retry-loop-dashboard

### Acceptance
- **verify-retry-loop-dashboard**: Dashboard shows attempt n/budget on retried rows; tdd; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py tests/test_dashboard_app.py -q -k "attempt_row or attempt_budget or attempt_snapshot or attempt_title" _(id: [rec-7d873780-5fa8-4f70-af41-851701195ec5](.artifacts/records/project__acceptance/rec-7d873780-5fa8-4f70-af41-851701195ec5.md))_

### Check
- **verify-retry-loop-dashboard**: rec-7d873780-5fa8-4f70-af41-851701195ec5; ee1a41be208bfdae700e1b78f9340296d82dae91; fail; tdd _(id: [rec-64f16e57-2fb5-429d-a774-fbe5113cef83](.artifacts/records/project__check-run/rec-64f16e57-2fb5-429d-a774-fbe5113cef83.md))_
- **verify-retry-loop-dashboard**: rec-7d873780-5fa8-4f70-af41-851701195ec5; 0077727e7e8d3b25e53d5aa1722b5c8f9ca58577; pass; tdd _(id: [rec-8ff6e514-0880-4828-8e5b-ca7a6c8dca7b](.artifacts/records/project__check-run/rec-8ff6e514-0880-4828-8e5b-ca7a6c8dca7b.md))_

## verify-run-facts

### Acceptance
- **verify-run-facts**: Through the adaptive-artifacts CLI, a fresh store accepts a work-item with size L and estimate_minutes 25, accepts estimate_minutes 0, accepts a work-item that omits both, and rejects size XXL.; tdd; dashboard; uv run --with pytest python -m pytest tests/test_estimate_cli.py -q _(id: [rec-421c70cd-39cf-4be7-8247-8e651bd0617d](.artifacts/records/project__acceptance/rec-421c70cd-39cf-4be7-8247-8e651bd0617d.md))_

### Check
- **verify-run-facts**: rec-421c70cd-39cf-4be7-8247-8e651bd0617d; dirty; pass; tdd _(id: [rec-34c7b8d2-ea71-440b-9a57-ebcee0786044](.artifacts/records/project__check-run/rec-34c7b8d2-ea71-440b-9a57-ebcee0786044.md))_

## verify-run-facts-contract

### Acceptance
- **verify-run-facts-contract**: contract/project-design.json allows optional size (XS, S, M, L, XL) and optional estimate_minutes on project:work-item, and the phase record does not gain either field.; check; dashboard; uv run --with pytest python -m pytest tests/test_estimate_contract.py -q _(id: [rec-559ae6f2-7bcd-483a-b04a-47312542235e](.artifacts/records/project__acceptance/rec-559ae6f2-7bcd-483a-b04a-47312542235e.md))_

### Check
- **verify-run-facts-contract**: rec-559ae6f2-7bcd-483a-b04a-47312542235e; dirty; pass; check _(id: [rec-47b6c395-57d0-4db2-9d8c-b67bba203107](.artifacts/records/project__check-run/rec-47b6c395-57d0-4db2-9d8c-b67bba203107.md))_

## verify-run-facts-dashboard

### Acceptance
- **verify-run-facts-dashboard**: The phase diff does not change dashboard/.; check; dashboard; test -z "$(git diff --name-only main -- dashboard/)" _(id: [rec-3a8cb50a-c1bf-4698-8b25-1a91d9ad70a2](.artifacts/records/project__acceptance/rec-3a8cb50a-c1bf-4698-8b25-1a91d9ad70a2.md))_

### Check
- **verify-run-facts-dashboard**: rec-3a8cb50a-c1bf-4698-8b25-1a91d9ad70a2; dirty; pass; check _(id: [rec-c79fee1b-527c-4ba9-bb42-803676decc50](.artifacts/records/project__check-run/rec-c79fee1b-527c-4ba9-bb42-803676decc50.md))_

## verify-run-facts-skill

### Acceptance
- **verify-run-facts-skill**: plan-phase requires size and estimate_minutes on each new work-item, and states the five size meanings, the inline sum, the subagent-wave maximum, the phase elapsed time, and the sitting line.; check; dashboard; uv run --with pytest python -m pytest tests/test_estimate_skill.py tests/test_skill_contract_consistency.py tests/test_plan_wave_rules.py tests/test_plan_trace.py -q _(id: [rec-a7ce611e-022e-44b3-a49b-512336cf04a6](.artifacts/records/project__acceptance/rec-a7ce611e-022e-44b3-a49b-512336cf04a6.md))_

### Check
- **verify-run-facts-skill**: rec-a7ce611e-022e-44b3-a49b-512336cf04a6; dirty; pass; check _(id: [rec-1061f910-3272-419b-a5a1-6284f7ed3d6f](.artifacts/records/project__check-run/rec-1061f910-3272-419b-a5a1-6284f7ed3d6f.md))_

## verify-run-facts-suite

### Acceptance
- **verify-run-facts-suite**: The full suite passes, including the tmux tests.; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m "not tmux" && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-b43db00d-52de-4ffe-ba39-07011280cbbb](.artifacts/records/project__acceptance/rec-b43db00d-52de-4ffe-ba39-07011280cbbb.md))_

### Check
- **verify-run-facts-suite**: rec-b43db00d-52de-4ffe-ba39-07011280cbbb; dirty; fail; check _(id: [rec-389edfb5-bb7e-4fff-9659-263ef95dcf07](.artifacts/records/project__check-run/rec-389edfb5-bb7e-4fff-9659-263ef95dcf07.md))_
- **verify-run-facts-suite**: rec-b43db00d-52de-4ffe-ba39-07011280cbbb; dirty; pass; check _(id: [rec-39c113c6-6e92-4900-bc66-5b3abb6be177](.artifacts/records/project__check-run/rec-39c113c6-6e92-4900-bc66-5b3abb6be177.md))_

## verify-spec-view

### Acceptance
- **verify-spec-view**: Opening the phase screen from the dashboard entry shows tabs and Spec Markdown for a seeded structured phase; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_phase_screen.py tests/test_dashboard_integration.py -q -k "phase_screen or once" _(id: [rec-323fc48e-f2ba-4fcf-bea1-344c61a9f338](.artifacts/records/project__acceptance/rec-323fc48e-f2ba-4fcf-bea1-344c61a9f338.md))_

### Check
- **verify-spec-view**: rec-323fc48e-f2ba-4fcf-bea1-344c61a9f338; dirty; pass; check _(id: [rec-145ad5aa-3475-4107-a9d7-d1a124b58d38](.artifacts/records/project__check-run/rec-145ad5aa-3475-4107-a9d7-d1a124b58d38.md))_

## verify-spec-view-model

### Acceptance
- **verify-spec-view-model**: Tab sets, decision log scopes, and superseded links hold in model tests; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_model.py -q -k phase_screen _(id: [rec-b45738a2-3a4d-4384-8296-2710d92c7f41](.artifacts/records/project__acceptance/rec-b45738a2-3a4d-4384-8296-2710d92c7f41.md))_

### Check
- **verify-spec-view-model**: rec-b45738a2-3a4d-4384-8296-2710d92c7f41; dirty; pass; check _(id: [rec-0251f9f1-1d20-4445-8112-ebd2b8119d44](.artifacts/records/project__check-run/rec-0251f9f1-1d20-4445-8112-ebd2b8119d44.md))_

## verify-spec-view-suite

### Acceptance
- **verify-spec-view-suite**: the spec-view phase checks pass through the phase screen and the dashboard entry; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_phase_screen.py tests/test_dashboard_integration.py -q -k "phase_screen or once" _(id: [rec-09c72984-b31a-4157-a36c-f922a4700458](.artifacts/records/project__acceptance/rec-09c72984-b31a-4157-a36c-f922a4700458.md))_

### Check
- **verify-spec-view-suite**: rec-09c72984-b31a-4157-a36c-f922a4700458; dirty; pass; check _(id: [rec-8402b94b-7bc4-4593-b0e7-26789e290d82](.artifacts/records/project__check-run/rec-8402b94b-7bc4-4593-b0e7-26789e290d82.md))_

## verify-status-line-phase

### Acceptance
- **verify-status-line-phase**: The tmux status segment and e2e tests pass with the rebuilt status line, and the full suite passes; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m 'not tmux' && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-2e2b15a3-c245-48ab-874a-9efbfd69ff60](.artifacts/records/project__acceptance/rec-2e2b15a3-c245-48ab-874a-9efbfd69ff60.md))_

### Check
- **verify-status-line-phase**: rec-2e2b15a3-c245-48ab-874a-9efbfd69ff60; afd60845e9ffcfcd44d028603b46bdcffadc313a; pass; check _(id: [rec-43db24a6-a3a6-4320-b00e-64c22fd00fa5](.artifacts/records/project__check-run/rec-43db24a6-a3a6-4320-b00e-64c22fd00fa5.md))_

## verify-table-state-phase

### Acceptance
- **verify-table-state-phase**: The tmux popup test for focus and resize passes, and the full suite passes; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m 'not tmux' && uv run --with textual --with pytest python -m pytest tests -q -m tmux _(id: [rec-c31c7b82-4a88-43bf-877c-1ffabb4f08e3](.artifacts/records/project__acceptance/rec-c31c7b82-4a88-43bf-877c-1ffabb4f08e3.md))_

### Check
- **verify-table-state-phase**: rec-c31c7b82-4a88-43bf-877c-1ffabb4f08e3; 3d740d2b7c02175520ca2f03e713c70c450c6603; pass; check _(id: [rec-cdcf77bc-e4da-4c06-8707-0180febff2ce](.artifacts/records/project__check-run/rec-cdcf77bc-e4da-4c06-8707-0180febff2ce.md))_

### Observation
- **verify-table-state-phase**: Without b104980 the stale-width resize race fails the tmux test in about 4 of 5 runs; the pilot test from b104980 is the deterministic guard.; dashboard-bugfix _(id: [rec-9feddfcd-4869-456a-9597-16da85a789cc](.artifacts/records/project__investigation-observation/rec-9feddfcd-4869-456a-9597-16da85a789cc.md))_

## verify-task-details-phase

### Acceptance
- **verify-task-details-phase**: The full test suite passes, including a tmux test that opens a task's detail screen in the popup and sees it update through a lifecycle; check; dashboard; uv run --with textual --with pytest python -m pytest tests -q _(id: [rec-98ab04e9-ab1a-488f-8712-716c9a11b7ba](.artifacts/records/project__acceptance/rec-98ab04e9-ab1a-488f-8712-716c9a11b7ba.md))_

### Check
- **verify-task-details-phase**: rec-98ab04e9-ab1a-488f-8712-716c9a11b7ba; 70b0501; pass; check _(id: [rec-d63e8d3d-8054-4434-9f6a-908518f99237](.artifacts/records/project__check-run/rec-d63e8d3d-8054-4434-9f6a-908518f99237.md))_

## verify-task-details-phase-signoff

### Acceptance
- **verify-task-details-phase-signoff**: The user opens task details in the popup and the side pane and signs off that they show what the task needs and what happened on it; manual; dashboard _(id: [rec-11643a9d-4693-4761-b94a-ba3a6be27ad6](.artifacts/records/project__acceptance/rec-11643a9d-4693-4761-b94a-ba3a6be27ad6.md))_

### Check
- **verify-task-details-phase-signoff**: rec-11643a9d-4693-4761-b94a-ba3a6be27ad6; 03d561c; pass; manual; ayin _(id: [rec-3049cecc-9049-4792-b1d6-8d607534885f](.artifacts/records/project__check-run/rec-3049cecc-9049-4792-b1d6-8d607534885f.md))_

## verify-task-navigation-phase

### Acceptance
- **verify-task-navigation-phase**: The full test suite passes, including a keys-only tmux test through status tabs, phase sections, and a task detail; check; dashboard; uv run --with textual --with pytest python -m pytest tests -q _(id: [rec-b9307639-88bf-43f4-8ad7-d0e4a77db060](.artifacts/records/project__acceptance/rec-b9307639-88bf-43f4-8ad7-d0e4a77db060.md))_

### Check
- **verify-task-navigation-phase**: rec-892a40a7-5d4e-4027-a096-a484d58b9787; 671220afbe8e7adb39f8e250bfafed07823d11c4; pass; manual; Andrew Yin _(id: [rec-553ce6d1-ba21-49fc-9c32-cbab20dab9ca](.artifacts/records/project__check-run/rec-553ce6d1-ba21-49fc-9c32-cbab20dab9ca.md))_
- **verify-task-navigation-phase**: rec-b9307639-88bf-43f4-8ad7-d0e4a77db060; 671220afbe8e7adb39f8e250bfafed07823d11c4; pass; check _(id: [rec-ac579a85-7728-4f68-9674-bdc27b578da9](.artifacts/records/project__check-run/rec-ac579a85-7728-4f68-9674-bdc27b578da9.md))_
- **verify-task-navigation-phase**: rec-b9307639-88bf-43f4-8ad7-d0e4a77db060; 671220afbe8e7adb39f8e250bfafed07823d11c4; pass; check _(id: [rec-f5162a90-c6e6-48fe-b3ae-2aaffcf1ddae](.artifacts/records/project__check-run/rec-f5162a90-c6e6-48fe-b3ae-2aaffcf1ddae.md))_

## verify-task-navigation-phase-signoff

### Acceptance
- **verify-task-navigation-phase-signoff**: The user navigates with the keyboard, status tabs, and phase sections in the popup and the side pane and signs off; manual; dashboard _(id: [rec-892a40a7-5d4e-4027-a096-a484d58b9787](.artifacts/records/project__acceptance/rec-892a40a7-5d4e-4027-a096-a484d58b9787.md))_

## verify-task-rows-phase

### Acceptance
- **verify-task-rows-phase**: The tmux popup test for task rows and activity passes, README describes waits-on, running time and failed activity, and the full suite passes; check; dashboard; uv run --with textual --with pytest --with pytest-xdist python -m pytest tests -q -n 4 -m 'not tmux' && uv run --with textual --with pytest python -m pytest tests -q -m tmux -rf _(id: [rec-92df6b15-9068-4342-b3fa-899bc28247b3](.artifacts/records/project__acceptance/rec-92df6b15-9068-4342-b3fa-899bc28247b3.md))_

### Check
- **verify-task-rows-phase**: rec-92df6b15-9068-4342-b3fa-899bc28247b3; e6591ab8dd58b85e63d1bed9702b6edaf0b236a1; pass; check _(id: [rec-07e2fbea-ed1f-4ea9-95b1-0b6416449996](.artifacts/records/project__check-run/rec-07e2fbea-ed1f-4ea9-95b1-0b6416449996.md))_

## verify-tiered-verification

### Acceptance
- **verify-tiered-verification**: Through the pytest entry point, background tier-2 run records a check-run at phase head without blocking the agent session for the suite duration; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_tiered_verification.py -q -k "runner or background or check_run" _(id: [rec-e094b9fe-4161-4ebd-81ad-00b66dce7444](.artifacts/records/project__acceptance/rec-e094b9fe-4161-4ebd-81ad-00b66dce7444.md))_

### Check
- **verify-tiered-verification**: rec-e094b9fe-4161-4ebd-81ad-00b66dce7444; dirty; fail; tdd _(id: [rec-3e568900-d5ec-445c-9d0c-ba14ccaeae3f](.artifacts/records/project__check-run/rec-3e568900-d5ec-445c-9d0c-ba14ccaeae3f.md))_
- **verify-tiered-verification**: rec-e094b9fe-4161-4ebd-81ad-00b66dce7444; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; tdd _(id: [rec-a20e2413-ec98-4a31-ab42-c74cd5d6c8bd](.artifacts/records/project__check-run/rec-a20e2413-ec98-4a31-ab42-c74cd5d6c8bd.md))_

## verify-tiered-verification-fix

### Acceptance
- **verify-tiered-verification-fix**: Tier-2 failure creates fix work-item(s) under retry budget with no inline verifier fix loop; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_tiered_verification.py -q -k "fix or cluster or budget" _(id: [rec-3441488d-4728-4c7e-855a-ef05fc967f31](.artifacts/records/project__acceptance/rec-3441488d-4728-4c7e-855a-ef05fc967f31.md))_

### Check
- **verify-tiered-verification-fix**: rec-3441488d-4728-4c7e-855a-ef05fc967f31; dirty; fail; tdd _(id: [rec-60a08648-2453-4612-b2a3-9cc4610430ef](.artifacts/records/project__check-run/rec-60a08648-2453-4612-b2a3-9cc4610430ef.md))_
- **verify-tiered-verification-fix**: rec-3441488d-4728-4c7e-855a-ef05fc967f31; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; tdd _(id: [rec-b050a616-916d-499f-8922-b9a2917b1a95](.artifacts/records/project__check-run/rec-b050a616-916d-499f-8922-b9a2917b1a95.md))_

## verify-tiered-verification-gate

### Acceptance
- **verify-tiered-verification-gate**: Phase gate requires head-SHA acceptance passes and a passing tier-2 check-run before merge; tdd; workflow-loop; uv run --with pytest python -m pytest tests/test_tiered_verification.py -q -k gate _(id: [rec-6c629730-fc3a-4ca1-9d42-88c84c5b8b34](.artifacts/records/project__acceptance/rec-6c629730-fc3a-4ca1-9d42-88c84c5b8b34.md))_

### Check
- **verify-tiered-verification-gate**: rec-6c629730-fc3a-4ca1-9d42-88c84c5b8b34; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; tdd _(id: [rec-2774e5e4-c77b-434e-b925-10be104a10cc](.artifacts/records/project__check-run/rec-2774e5e4-c77b-434e-b925-10be104a10cc.md))_
- **verify-tiered-verification-gate**: rec-6c629730-fc3a-4ca1-9d42-88c84c5b8b34; dirty; fail; tdd _(id: [rec-de87e2d2-4a36-4ff8-9e04-33e7452816a3](.artifacts/records/project__check-run/rec-de87e2d2-4a36-4ff8-9e04-33e7452816a3.md))_

## verify-tiered-verification-surfaces

### Acceptance
- **verify-tiered-verification-surfaces**: Dashboard shows tier-2 status on the phase header; skills/README/verify-budget stay scoped for per-task checks; skill↔contract consistency green; CI-owned tier-2 remains future/non-goal; check; workflow-loop; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py tests/test_dashboard_model.py -q -k tier2 && uv run --with pytest python -m pytest tests/test_verify_budget.py tests/test_skill_contract_consistency.py -q _(id: [rec-07249524-c6b9-49bf-8823-074594abbd01](.artifacts/records/project__acceptance/rec-07249524-c6b9-49bf-8823-074594abbd01.md))_

### Check
- **verify-tiered-verification-surfaces**: rec-07249524-c6b9-49bf-8823-074594abbd01; dirty; fail; check _(id: [rec-2b894e41-e3ec-4ceb-b87d-ff1946dd257f](.artifacts/records/project__check-run/rec-2b894e41-e3ec-4ceb-b87d-ff1946dd257f.md))_
- **verify-tiered-verification-surfaces**: rec-07249524-c6b9-49bf-8823-074594abbd01; 87fb88a22889fc016d21b6dbece2e02836fca56a; pass; check _(id: [rec-c8aff61d-c10a-4960-9f58-9e583315e4d1](.artifacts/records/project__check-run/rec-c8aff61d-c10a-4960-9f58-9e583315e4d1.md))_

## verify-tmux-integration-phase

### Acceptance
- **verify-tmux-integration-phase**: The isolated tmux test passes: the side pane shows the repo's dashboard, the popup binding runs the launcher in the pane directory and renders, and the status segment counts match; tdd; dashboard; cd ~/se-workflow && python3 -m pytest tests/test_tmux_integration.py -q _(id: [rec-66a8f44a-bfea-4ee2-aea0-cbe426d17d69](.artifacts/records/project__acceptance/rec-66a8f44a-bfea-4ee2-aea0-cbe426d17d69.md))_

### Check
- **verify-tmux-integration-phase**: rec-66a8f44a-bfea-4ee2-aea0-cbe426d17d69; ea5a5c9; pass; tdd _(id: [rec-08b2c386-6b30-4edb-ae03-1e4897affc66](.artifacts/records/project__check-run/rec-08b2c386-6b30-4edb-ae03-1e4897affc66.md))_
- **verify-tmux-integration-phase**: rec-4a323bc2-c820-4133-8409-d9be1a13b97a; aa:227523b se:ea5a5c9; pass; check _(id: [rec-9298f363-45b4-4925-a9fa-c1d4ab529196](.artifacts/records/project__check-run/rec-9298f363-45b4-4925-a9fa-c1d4ab529196.md))_

## verify-tmux-integration-phase-suites

### Acceptance
- **verify-tmux-integration-phase-suites**: Full test suites of both repos pass on the phase-3 changes; check; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q && cd ~/se-workflow && python3 -m pytest tests -q _(id: [rec-4a323bc2-c820-4133-8409-d9be1a13b97a](.artifacts/records/project__acceptance/rec-4a323bc2-c820-4133-8409-d9be1a13b97a.md))_

## verify-tmux-plugin-entry

### Acceptance
- **verify-tmux-plugin-entry**: In a real tmux server loaded through se-workflow.tmux, prefix A and prefix S open the dashboard (real entry point).; tdd; dashboard; uv run --with pytest --with textual pytest -m tmux tests/test_tmux_integration.py tests/test_e2e_dashboard.py tests/test_tmux_entry.py _(id: [rec-307dcaee-56c1-444b-8e02-b54d47eb903a](.artifacts/records/project__acceptance/rec-307dcaee-56c1-444b-8e02-b54d47eb903a.md))_

### Check
- **verify-tmux-plugin-entry**: rec-81b6561f-39c6-4892-91e4-e2a043e7dd9b; dirty; pass; check _(id: [rec-08bdaf65-fa59-4c53-a5c6-33301962123b](.artifacts/records/project__check-run/rec-08bdaf65-fa59-4c53-a5c6-33301962123b.md))_
- **verify-tmux-plugin-entry**: rec-22a2f699-9b2e-4971-8f8f-72f726491c0f; dirty; pass; check _(id: [rec-332dbaf0-4782-47d9-8e6d-e17b37b70058](.artifacts/records/project__check-run/rec-332dbaf0-4782-47d9-8e6d-e17b37b70058.md))_
- **verify-tmux-plugin-entry**: rec-307dcaee-56c1-444b-8e02-b54d47eb903a; dirty; pass; tdd _(id: [rec-9895eccc-a929-4aab-9958-a100220972af](.artifacts/records/project__check-run/rec-9895eccc-a929-4aab-9958-a100220972af.md))_
- **verify-tmux-plugin-entry**: rec-bc65d5e2-9428-4c8c-966d-4ebaa8e3cc34; dirty; pass; check _(id: [rec-c4d7e14c-d49a-48ce-808d-e768c5fa4c15](.artifacts/records/project__check-run/rec-c4d7e14c-d49a-48ce-808d-e768c5fa4c15.md))_
- **verify-tmux-plugin-entry**: rec-c78b573b-fc0f-4ab7-8f1a-52f73766dc61; dirty; pass; check _(id: [rec-f6d58704-063a-4a24-b4d0-0bdab29d2da6](.artifacts/records/project__check-run/rec-f6d58704-063a-4a24-b4d0-0bdab29d2da6.md))_

## verify-tmux-plugin-entry-conf-gone

### Acceptance
- **verify-tmux-plugin-entry-conf-gone**: dashboard/tmux.conf is gone and nothing refers to it.; check; dashboard; test ! -e dashboard/tmux.conf && ! grep -rnE 'dashboard/tmux\.conf|SE_WORKFLOW_DASHBOARD' dashboard scripts tests README.md _(id: [rec-bc65d5e2-9428-4c8c-966d-4ebaa8e3cc34](.artifacts/records/project__acceptance/rec-bc65d5e2-9428-4c8c-966d-4ebaa8e3cc34.md))_

## verify-tmux-plugin-entry-full-suite

### Acceptance
- **verify-tmux-plugin-entry-full-suite**: The full suite passes, including the tmux tests.; check; dashboard; uv run --with pytest --with textual pytest && uv run --with pytest --with textual pytest -m tmux _(id: [rec-c78b573b-fc0f-4ab7-8f1a-52f73766dc61](.artifacts/records/project__acceptance/rec-c78b573b-fc0f-4ab7-8f1a-52f73766dc61.md))_

## verify-tmux-plugin-entry-key-options

### Acceptance
- **verify-tmux-plugin-entry-key-options**: The key options rebind the keys and the defaults are A and S.; check; dashboard; uv run --with pytest --with textual pytest -m tmux tests/test_tmux_entry.py -k 'default or custom_keys' _(id: [rec-22a2f699-9b2e-4971-8f8f-72f726491c0f](.artifacts/records/project__acceptance/rec-22a2f699-9b2e-4971-8f8f-72f726491c0f.md))_

## verify-tmux-plugin-entry-readme

### Acceptance
- **verify-tmux-plugin-entry-readme**: The README has a numbered Quick start that covers TPM and run-shell.; check; dashboard; grep -q '^## Quick start' README.md && grep -q "@plugin 'andrewy1n/se-workflow'" README.md && grep -q 'run-shell' README.md _(id: [rec-81b6561f-39c6-4892-91e4-e2a043e7dd9b](.artifacts/records/project__acceptance/rec-81b6561f-39c6-4892-91e4-e2a043e7dd9b.md))_

## verify-verify-budget

### Acceptance
- **verify-verify-budget**: Through adaptive-artifacts list and get, the planned spec-view, evidence-matrix, and journal-view verification tasks no longer name the full suite; check; workflow-loop; python3 -c 'import json, subprocess, sys
aa = ["python3", "/home/andrewyin/adaptive-artifacts/tools/artifacts.py", "--root", "/home/andrewyin/se-workflow"]
bad = "pytest tests -q -n 4"
subjects = ("verify-spec-view-suite", "verify-evidence-matrix-suite", "verify-journal-view-suite")
for s in subjects:
    result = subprocess.run([*aa, "list", "--type", "project:acceptance", "--subject", s, "--state", "active", "--full"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr or result.stdout
    recs = json.loads(result.stdout)["records"]
    assert len(recs) == 1, s
    cmd = recs[0]["payload"]["verify_command"]
    assert bad not in cmd, cmd
    assert " -k " in cmd, cmd
ids = ("rec-79a4e4c1-cfcb-421b-a023-64563ff645f3", "rec-8432d854-983c-4de9-bb0f-f99b94ecae9a", "rec-f04fa83f-a51f-4800-b3be-9b658df17590")
for i in ids:
    result = subprocess.run([*aa, "get", "--type", "project:work-item", "--id", i], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr or result.stdout
    body = json.loads(result.stdout)["body"].lower()
    assert "full suite" not in body, i
print("phase checks only")
' _(id: [rec-0ebd4258-1ee3-4bc5-86e9-617467468a47](.artifacts/records/project__acceptance/rec-0ebd4258-1ee3-4bc5-86e9-617467468a47.md))_

### Check
- **verify-verify-budget**: rec-0ebd4258-1ee3-4bc5-86e9-617467468a47; dirty; pass; check _(id: [rec-d3a7ce5d-d6b6-43d7-a373-e9d9460885e0](.artifacts/records/project__check-run/rec-d3a7ce5d-d6b6-43d7-a373-e9d9460885e0.md))_

## verify-verify-budget-skills

### Acceptance
- **verify-verify-budget-skills**: The instruction tests and the skill contract consistency test pass; check; workflow-loop; uv run --with pytest python -m pytest tests/test_verify_budget.py tests/test_skill_contract_consistency.py -q _(id: [rec-fe773a87-15bf-4633-9fc3-54fe95587755](.artifacts/records/project__acceptance/rec-fe773a87-15bf-4633-9fc3-54fe95587755.md))_

### Check
- **verify-verify-budget-skills**: rec-fe773a87-15bf-4633-9fc3-54fe95587755; dirty; pass; check _(id: [rec-aed285c3-4165-45a9-9d64-aa9c9526a564](.artifacts/records/project__check-run/rec-aed285c3-4165-45a9-9d64-aa9c9526a564.md))_

## verify-waits-on-compact

### Acceptance
- **verify-waits-on-compact**: Through the dashboard app entry point, a waiting row with several unfinished deps shows no waits on in the title cell and stays one line at typical widths; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'waiting_row or waits' _(id: [rec-2229ea3a-838b-401d-a6cf-cfe1a00067db](.artifacts/records/project__acceptance/rec-2229ea3a-838b-401d-a6cf-cfe1a00067db.md))_

### Check
- **verify-waits-on-compact**: rec-2229ea3a-838b-401d-a6cf-cfe1a00067db; 98bcbd8 dirty; pass; tdd _(id: [rec-d500da71-250f-4225-885b-d760f0cd9bea](.artifacts/records/project__check-run/rec-d500da71-250f-4225-885b-d760f0cd9bea.md))_

## verify-waits-on-compact-detail

### Acceptance
- **verify-waits-on-compact-detail**: Through the dashboard app, task detail for that waiting task still lists Depends on links for its dependencies; tdd; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_app.py -q -k 'detail and (Depends or blocked)' _(id: [rec-adf5aef7-5c16-4f3a-bd91-f3b8a49d2e84](.artifacts/records/project__acceptance/rec-adf5aef7-5c16-4f3a-bd91-f3b8a49d2e84.md))_

### Check
- **verify-waits-on-compact-detail**: rec-adf5aef7-5c16-4f3a-bd91-f3b8a49d2e84; 98bcbd8 dirty; pass; tdd _(id: [rec-9800fc0a-7581-41ce-a0c4-5eff49d7be82](.artifacts/records/project__check-run/rec-9800fc0a-7581-41ce-a0c4-5eff49d7be82.md))_

## verify-waits-on-compact-suite

### Acceptance
- **verify-waits-on-compact-suite**: Focused dashboard tasks/app tests that formerly expected row waits on pass against the dropped form; check; dashboard; uv run --with textual --with pytest python -m pytest tests/test_dashboard_tasks.py tests/test_dashboard_app.py -q -k 'waits or title_cell or waiting_row' _(id: [rec-2ad10a07-f300-4aee-b79c-4cabb9cb3e3f](.artifacts/records/project__acceptance/rec-2ad10a07-f300-4aee-b79c-4cabb9cb3e3f.md))_

### Check
- **verify-waits-on-compact-suite**: rec-2ad10a07-f300-4aee-b79c-4cabb9cb3e3f; 98bcbd8 dirty; pass; check _(id: [rec-6e68d8cc-6b7f-42c7-ad57-e5ceaa1451f4](.artifacts/records/project__check-run/rec-6e68d8cc-6b7f-42c7-ad57-e5ceaa1451f4.md))_

## verify-watch-renderer-phase

### Acceptance
- **verify-watch-renderer-phase**: The pty integration test passes: first frame shown, redraw within 3 s of a record write, zero redraws over an idle second, SIGINT exits 0; tdd; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q -k watch_integration _(id: [rec-cadda757-0424-444f-8ae1-31d415d18e6d](.artifacts/records/project__acceptance/rec-cadda757-0424-444f-8ae1-31d415d18e6d.md))_

### Check
- **verify-watch-renderer-phase**: rec-02bac654-25f6-4bc0-b6ec-5efa03a4941e; 227523b; pass; check _(id: [rec-5e3ceb64-1808-4d83-b107-c53695f20ae2](.artifacts/records/project__check-run/rec-5e3ceb64-1808-4d83-b107-c53695f20ae2.md))_
- **verify-watch-renderer-phase**: rec-cadda757-0424-444f-8ae1-31d415d18e6d; 227523b; pass; tdd _(id: [rec-61d5c15f-2e8c-444c-a58b-aa9eeccae777](.artifacts/records/project__check-run/rec-61d5c15f-2e8c-444c-a58b-aa9eeccae777.md))_
- **verify-watch-renderer-phase**: rec-02bac654-25f6-4bc0-b6ec-5efa03a4941e; 227523b; tdd; check rec-cadda757-0424-444f-8ae1-31d415d18e6d _(id: [rec-c5dbe94f-0573-4d20-b91b-25ada50fd363](.artifacts/records/project__check-run/rec-c5dbe94f-0573-4d20-b91b-25ada50fd363.md))_
- **verify-watch-renderer-phase**: rec-02bac654-25f6-4bc0-b6ec-5efa03a4941e; 227523b; pass; check _(id: [rec-c8eab97a-7fef-4703-b22a-527699417339](.artifacts/records/project__check-run/rec-c8eab97a-7fef-4703-b22a-527699417339.md))_

## verify-watch-renderer-phase-suites

### Acceptance
- **verify-watch-renderer-phase-suites**: Full test suites of both repos pass on the phase-2 changes; check; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q && cd ~/se-workflow && python3 -m pytest tests -q _(id: [rec-02bac654-25f6-4bc0-b6ec-5efa03a4941e](.artifacts/records/project__acceptance/rec-02bac654-25f6-4bc0-b6ec-5efa03a4941e.md))_

## verify-wave-executor

### Acceptance
- **verify-wave-executor**: plan-phase and execute-phase name the same executors, inline and subagent, and a missing executor means subagent; tdd; workflow-loop; python3 -m pytest tests/test_wave_executor_phase.py -q _(id: [rec-5fe7bba7-cd21-447d-a698-ed9bb1379f58](.artifacts/records/project__acceptance/rec-5fe7bba7-cd21-447d-a698-ed9bb1379f58.md))_

### Check
- **verify-wave-executor**: rec-5fe7bba7-cd21-447d-a698-ed9bb1379f58; dirty; pass; tdd _(id: [rec-040c3fe0-5e55-4cc6-9299-f428da66edf9](.artifacts/records/project__check-run/rec-040c3fe0-5e55-4cc6-9299-f428da66edf9.md))_
- **verify-wave-executor**: rec-d8b61721-30cb-41fd-885d-85e673c7d6d7; dirty; pass; tdd _(id: [rec-68993ac9-1572-4d48-85b6-daf3d3211fb8](.artifacts/records/project__check-run/rec-68993ac9-1572-4d48-85b6-daf3d3211fb8.md))_
- **verify-wave-executor**: rec-61bdf854-1a06-491f-8af6-aeda309ec357; dirty; pass; tdd _(id: [rec-cde58bbe-0260-4526-b43a-d37ef52a05ca](.artifacts/records/project__check-run/rec-cde58bbe-0260-4526-b43a-d37ef52a05ca.md))_

## verify-wave-executor-execute

### Acceptance
- **verify-wave-executor-execute**: execute-phase runs an inline wave in this session and a subagent wave as one worker per task, and does not ask for a recipe when Approach is present; tdd; workflow-loop; python3 -m pytest tests/test_execute_wave_dispatch.py -q _(id: [rec-d8b61721-30cb-41fd-885d-85e673c7d6d7](.artifacts/records/project__acceptance/rec-d8b61721-30cb-41fd-885d-85e673c7d6d7.md))_

## verify-wave-executor-plan

### Acceptance
- **verify-wave-executor-plan**: plan-phase requires a recipe, one shared executor per wave, and phase size, stops, and collision notes before plan review; tdd; workflow-loop; python3 -m pytest tests/test_plan_wave_rules.py -q _(id: [rec-61bdf854-1a06-491f-8af6-aeda309ec357](.artifacts/records/project__acceptance/rec-61bdf854-1a06-491f-8af6-aeda309ec357.md))_

## watch-command

### Acceptance
- **watch-command**: With an injected clock, sleep and output stream: a changed render gives one redraw, an unchanged render gives none, a render error shows and the loop continues, KeyboardInterrupt returns exit 0, and --once prints one frame; tdd; dashboard; cd ~/adaptive-artifacts && python3 -m pytest tools/runtime/tests -q _(id: [rec-ec792cef-650b-492a-ac2d-eed325546c19](.artifacts/records/project__acceptance/rec-ec792cef-650b-492a-ac2d-eed325546c19.md))_

### Check
- **watch-command**: rec-ec792cef-650b-492a-ac2d-eed325546c19; 846188f; pass; tdd _(id: [rec-f370db55-4f74-4981-bfae-1d39e925d6ff](.artifacts/records/project__check-run/rec-f370db55-4f74-4981-bfae-1d39e925d6ff.md))_
