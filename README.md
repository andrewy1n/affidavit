# affidavit

Evidence layer for a software-engineering loop.
This repo ships the `aff` evidence CLI (`~/affidavit`).

## CLI

`bin/aff` is the evidence CLI. Flags and argv live in each subcommand's
`--help`. From this checkout:

```bash
bin/aff --help
bin/aff <command> --help
```

| Command | Role |
|---|---|
| `verdict` | Re-execute frozen oracle tests at two revisions |
| `runner-template` | Print a shipped runner template argv as JSON |
| `attest` | Emit or verify a signed verdict attestation |
| `lint` | Report no-assert witnesses, new skips, or claim wording |
| `claim` | Author manifest claims |
| `freeze` | Record oracle file hashes into the manifest |
| `audit` | Advisory: label diff blocks; optional mutants and probes |
| `trail` | List evidence-observations from the artifact store |
| `bind` | Attach an observation to a claim under pinned revisions |
| `unbind` | Retire a binding |
| `recheck` | Re-judge a claim under its active binding pins |

`verdict` does not read a workflow store for its gate answer.
`trail` / `bind` / `unbind` / `recheck` use the work repo's
`.artifacts/` evidence records when present.

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
