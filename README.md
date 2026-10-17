# affidavit

Evidence layer for a software-engineering loop.
This repo's `aff` is verdict-only.

The orchestration plugin is orchestra at `~/orchestra`: skills, the
dashboard, session scripts, and agents. check, close-batch, and the
store client live in orchestra.
Install that plugin for the skill loop. This repo is the checkout that
provides the `aff` binary (`~/affidavit`).

## CLI

`bin/aff` dispatches `verdict`. From this checkout:

```bash
bin/aff verdict --help

bin/aff verdict --cwd <repo> --at <sha> <claim-id>
```

`verdict` re-executes the frozen oracle tests for a claim. It does not
read a record store. check, close-batch, and the store client live in
orchestra.

## What lives where

| Here | `~/orchestra` |
|---|---|
| `affidavit/` and `bin/aff` | skills (same slugs as before) |
| tests for `aff verdict` | dashboard, session scripts, and the store client |
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
