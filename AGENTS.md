# AGENTS.md

This repo is the evidence layer. Plugin **0.2.0** keeps the `aff`
command `verdict`. `aff` is verdict-only. It is not a template you copy
into other projects.

The orchestration plugin is **orchestra** at `~/orchestra`. That repo
holds the skills, the dashboard, the session scripts, and `agents/`.
Skill slugs stay `engage`, `init`, `discuss`, `plan-phase`,
`execute-phase`, `verify-work`, and `analyze-sessions`.

Requires the **adaptive-artifacts** plugin (`adaptive-artifacts` on
PATH). That runtime is unpublished experimental **0.1.0**. Its agent
protocol is `~/adaptive-artifacts/AGENTS.md`.

## Two trees

| You are in… | Store | What you edit |
|---|---|---|
| This repo, building the evidence layer | this repo's `.artifacts/` | `affidavit/`, `bin/aff`, `tests/`, `contract/` |
| `~/orchestra`, building the plugin | that repo's `.artifacts/` | skills, dashboard, scripts, agents |
| Some other repo, using the skills | that repo's `.artifacts/` | that repo's code, through the orchestra skills |

Do not copy this tree into a work project. Do not look for the skills
or the dashboard here. The bundled plugin contract is
`~/orchestra/contract/project-design.json`. Orchestra's `init` copies
it into a work repo on first use. When that file's `"project"` is
`affidavit`, ensure-store rewrites it to `orchestra`. When the field
is any other value, ensure-store stops and does not replace the design.

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

An incidental change that fits this chat gets no records. Kinds, focus,
and phase positions live with the orchestra skills.

## What stays here

`bin/aff verdict`. This package does not import orchestra. `aff verdict`
does not read a record store.

check, close-batch, and the store client live in orchestra. Orchestra
skills call `aff verdict` on `PATH`. `~/affidavit` is the checkout that
provides the `aff` binary.

## Contract and the runtime

`contract/project-design.json` in this repo is the design this store
resolves. Record types are expected to grow. Tests must not hardcode
today's type list as if it were frozen.

Later contract edits belong in the orchestra repo, then get copied
here so this store still resolves.

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
| Skills, dashboard, session scripts | `~/orchestra` |
| Bundled plugin contract | `~/orchestra/contract/project-design.json` |
| Evidence CLI | `README.md` |
| Runtime change gate | `~/adaptive-artifacts/AGENTS.md` |
