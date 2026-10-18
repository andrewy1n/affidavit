---
{
  "base_kind": "claim",
  "epistemic_status": "asserted",
  "id": "rec-3769bb20-27ee-400d-ae2c-bbbd1fece475",
  "identity": "unknown",
  "lifecycle_state": "active",
  "payload": {
    "decisions": "record-bind-policy-in-skills",
    "effort": "evidence-layer",
    "phase": "evidence-workflow"
  },
  "record_type": "project:design",
  "recorded_at": "2026-10-18T09:29:16+00:00",
  "relationships": {},
  "revision": "sha256:fb8388112cb27b34479a828dc1b75dec89d9a5a087007fd9a152b2a68f666f79",
  "stewardship": {
    "steward": "agent"
  },
  "subject": "evidence-workflow",
  "time": {
    "as_of": "2026-10-18T09:29:16+00:00"
  }
}
---

## Architecture

Aff exposes verbs: record (via technique commands), `trail`, `bind`, `unbind`, `recheck`. Orchestra skills decide when each is used.

```
verify-work / execute-phase
    |-- aff <technique>     # may record unbound observation
    |-- aff trail           # inspect
    |-- aff bind / recheck  # earn / hold
    \-- orchestra check     # task check-run (unchanged authority)
```

No aff mode flag selects “record mode” vs “bind mode.”

## Interfaces

- Skill text in `~/orchestra/skills/verify-work` and `execute-phase` (discuss cues only if needed for authoring).
- Tests under `~/orchestra/tests` asserting skill wording / no aff mode invention.
- Handoff or verify narrative: claim id → binding id → observation id.

## Decisions

- `record-bind-policy-in-skills`

## Invariants

- Aff gains no work-kind/mode for this policy.
- Manifest claims remain the assertion authority; bindings earn them via observations, they do not replace the manifest.

## Assumptions

- Bind and ingest CLIs exist for the skills to name.
- Existing skill-evidence-boundary tests can grow a no-mode fixture.

## Tradeoffs

- Skill prose vs wrapper CLI: chose skills to keep earn visible and aff mode-free.
- Early skill edits before bind lands: sequence this phase after bind/ingest so verbs in the text are real.

## Risks

- Skills drift from CLI names — mitigate with orchestra tests that grep for `aff bind` / `aff trail`.
- Agents ignore skill policy — same class of risk as today’s verdict gate; binding makes non-compliance visible in the trail.
