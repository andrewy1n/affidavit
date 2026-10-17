# affidavit

Evidence layer for a software-engineering loop on adaptive-artifacts.
This repo keeps `aff check`, `aff close-batch`, and `aff verdict`.

The orchestration plugin is orchestra at `~/orchestra`: skills, the
dashboard, session scripts, and agents.
Install that plugin for the skill loop. This repo is the checkout that
provides the `aff` binary (`~/affidavit`).

Requires the **adaptive-artifacts** plugin (`adaptive-artifacts` on PATH).

## CLI

`bin/aff` dispatches the evidence commands. From this checkout, inside
a project that has a store when the command writes one:

```bash
bin/aff check --help
bin/aff close-batch --help
bin/aff verdict --help

bin/aff check --acceptance <acceptance-id>
bin/aff check --acceptance <id> --cwd /path/to/phase-worktree
bin/aff check --acceptance <id> --allow-dirty   # pass on a dirty tree

bin/aff verdict --cwd <repo> --at <sha> <claim-id>
```

`check` runs an acceptance whose method is `tdd` or `check` and writes
a `project:check-run`. It refuses `method=manual`. `close-batch` closes
a work-item from runner-produced check-runs. `verdict` re-executes the
frozen oracle tests for a claim. It does not read the artifact store.

Orchestra skills call these commands on `PATH`.

## What lives where

| Here | `~/orchestra` |
|---|---|
| `affidavit/` and `bin/aff` | skills (same slugs as before) |
| tests for the evidence CLI | dashboard and session scripts |
| this repo's `.artifacts/` (`evidence-layer`) | `agents/` and the reviewer and suite modules |

`affidavit` does not import the dashboard or orchestra. Orchestra may
import affidavit.

## Testing

```bash
python3 -m pip install --user pytest   # if not already available
python3 -m pytest tests -q
```

`pytest.ini` skips tests marked `tmux` unless `-m tmux` is set.

By default the suite looks for the runtime at `~/adaptive-artifacts`.
Point it elsewhere with `ADAPTIVE_ARTIFACTS_ROOT`:

```bash
ADAPTIVE_ARTIFACTS_ROOT=/path/to/adaptive-artifacts python3 -m pytest tests -q
```

Tests drive `adaptive-artifacts`'s public CLI against a fresh,
disposable, git-backed store built from this repo's
`contract/project-design.json`. Nothing here touches a real store.
The contract is expected to keep growing, so tests do not hardcode
today's record types.

Dashboard and skill tests run in `~/orchestra`.
