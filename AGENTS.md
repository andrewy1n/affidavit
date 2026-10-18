# AGENTS.md

This repo is the evidence layer. It ships the `aff` evidence CLI
(`verdict`, `claim`, `freeze`, `audit`, `trail`, `bind`, `unbind`,
`recheck`, and related verbs). It is not a template you copy into
other projects.

Requires the **adaptive-artifacts** plugin (`adaptive-artifacts` on
PATH). That runtime is unpublished experimental **0.1.0**. Its agent
protocol is `~/adaptive-artifacts/AGENTS.md`.

## What you edit here

`affidavit/`, `bin/aff`, `tests/`, `contract/`, and this repo's
`.artifacts/` store for the `evidence-layer` effort. Command map:
`README.md`.

## Live protocol

This repo's own memory is `.artifacts/`. At session start, if views
were not injected, run `adaptive-artifacts hook-start` and read the
derived views. Capture at the event with the `adaptive-artifacts` CLI.
Views under `.artifacts/views/` are derived — regenerate them; do not
edit them. At session end, if facts changed, write records, regenerate
views, and run `adaptive-artifacts hook-stop`. Fix validation errors
before finishing.

Only the parent session writes the store. Subagents return evidence in
their response. They do not call `adaptive-artifacts`.

A hand-edited record fails validation (`record revision tamper
detected`). Redo the edit through the CLI.

An incidental change that fits this chat gets no records.

## Evidence CLI

`bin/aff` is the evidence CLI. `aff verdict` does not read a workflow
store for its gate answer. `trail` / `bind` / `unbind` / `recheck`
talk to evidence records in a work repo's `.artifacts/` when present.

## Contract and the runtime

`contract/project-design.json` in this repo is the design this store
resolves. Record types are expected to grow. Tests must not hardcode
today's type list as if it were frozen.

Tests drive the public CLI as a subprocess
(`~/adaptive-artifacts/tools/artifacts.py`, or
`ADAPTIVE_ARTIFACTS_ROOT`). They do not import the runtime's Python
modules. The suite builds a fresh git-backed store from this contract.
It does not touch a real store.

## Adaptive-artifacts changes

A change to the runtime, catalog, hooks, or adaptive-artifacts skills
is an extension change. Follow `~/adaptive-artifacts/AGENTS.md`, section
"Changing the extension": capture it in **that** repo's store and apply
it only with human approval. Do not patch `~/adaptive-artifacts` mid-task
from an affidavit session. `reassess-artifacts` redesigns a project's
own contract. It does not edit the extension.

If this repo's `contract/project-design.json` can express the need,
change that file here.

## Testing

`pytest.ini` skips tests marked `tmux` unless `-m tmux` is set. While
editing, run the affected files. Before closing the task, run that
task's `verify_command`.

Commands and the `ADAPTIVE_ARTIFACTS_ROOT` override are in the README,
section "Testing".

## What to read

| Need | Where |
|---|---|
| Live goal, position, next | `.artifacts/views/handoff.md` (derived) |
| This protocol | this file |
| Evidence CLI | `README.md` |
| Runtime change gate | `~/adaptive-artifacts/AGENTS.md` |
