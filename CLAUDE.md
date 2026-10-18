# CLAUDE.md

Follow [AGENTS.md](AGENTS.md). This repo is the evidence layer and
ships the `aff` evidence CLI.

## Testing

While editing, run only the affected test files. Before closing the
task, run that task's `verify_command`. `pytest.ini` already skips
`tmux`.

The suite needs a checkout of adaptive-artifacts at
`~/adaptive-artifacts` (override with `ADAPTIVE_ARTIFACTS_ROOT`). It
calls that repo's `tools/artifacts.py`. It does not import the runtime.
More detail is in the README, section "Testing".

## Store

Records are the authority. `.artifacts/views/` are derived — regenerate
with `adaptive-artifacts`, do not edit view files. Write records with
the `adaptive-artifacts` CLI. A hand-edited record fails validation.

Only this session writes the store. Subagents return evidence in their
response and do not call `adaptive-artifacts`.

An incidental edit that fits this chat gets no records.

## Adaptive-artifacts

Leave `~/adaptive-artifacts` alone unless the user has approved an
extension change. That approval is the gate in
`~/adaptive-artifacts/AGENTS.md` ("Changing the extension"): capture the
amendment in that repo's store first. `reassess-artifacts` is for a
project's own contract, not for the runtime.

If this repo's `contract/project-design.json` can express the need,
change that file here.
