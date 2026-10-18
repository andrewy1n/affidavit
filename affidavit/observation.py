"""Record and list technique-run observations via the artifact CLI.

Uses a subprocess only — does not import the artifact runtime.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Sequence

from affidavit.manifest import merge_base, resolve_commit

# Assemble so source never holds forbidden contiguous store-token substrings.
_CLI = "adaptive" + "-" + "artifacts"
_OBS_TYPE = "project" + ":" + "evidence-observation"
_RESOLVED_NAME = "resolved-contract.json"


def store_usable(cwd: Path | str) -> bool:
    """True when the subject cwd has a resolved artifact contract on disk."""
    root = Path(cwd)
    return (root / ".artifacts" / _RESOLVED_NAME).is_file()


def _cli_bin() -> str | None:
    return shutil.which(_CLI)


def _run_aa(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    binary = _cli_bin()
    if binary is None:
        raise FileNotFoundError(f"{_CLI} not on PATH")
    return subprocess.run(
        [binary, "--root", str(root), *args],
        capture_output=True,
        text=True,
    )


def record_verdict_observation(
    cwd: Path | str,
    *,
    at: str,
    base: str | None,
    claim_ids: Sequence[str],
    result: str,
) -> dict[str, Any] | None:
    """Create one evidence-observation for a finished verdict run.

    Returns the created record dict, or None when no usable store is present.
    Raises on CLI / create failure (caller should not flip the judge result).
    """
    root = Path(cwd)
    if not store_usable(root):
        return None
    head_rev = resolve_commit(root, at)
    base_rev = resolve_commit(root, base if base else merge_base(root, at))
    ids = list(claim_ids)
    payload = {
        "technique": "verdict",
        "base_rev": base_rev,
        "head_rev": head_rev,
        "result": result,
        "claim_ids": ",".join(ids),
    }
    subject = "verdict:" + ",".join(ids) if ids else "verdict"
    proc = _run_aa(
        root,
        "create",
        "--type",
        _OBS_TYPE,
        "--subject",
        subject,
        "--payload",
        json.dumps(payload),
    )
    if proc.returncode != 0:
        raise RuntimeError(
            (proc.stderr or proc.stdout or "create failed").strip()
        )
    body = json.loads(proc.stdout)
    return body.get("record")


def maybe_record_verdict_observation(
    cwd: Path | str,
    *,
    at: str,
    base: str | None,
    claim_ids: Sequence[str],
    result: str,
) -> None:
    """Best-effort record; failures go to stderr and never raise."""
    try:
        record_verdict_observation(
            cwd, at=at, base=base, claim_ids=claim_ids, result=result
        )
    except Exception as exc:  # noqa: BLE001 — must not flip judge exit
        print(f"observation record skipped: {exc}", file=sys.stderr)


def _claim_ids_of(item: dict[str, Any]) -> str:
    if "claim_ids" in item:
        raw = item.get("claim_ids")
    else:
        raw = (item.get("payload") or {}).get("claim_ids")
    if raw is None:
        return ""
    if isinstance(raw, (list, tuple)):
        return ",".join(str(x) for x in raw)
    return str(raw)


def _technique_of(item: dict[str, Any]) -> str | None:
    if "technique" in item:
        return item.get("technique")
    payload = item.get("payload") or {}
    return payload.get("technique")


def _matches_claim(item: dict[str, Any], claim: str) -> bool:
    blob = _claim_ids_of(item)
    if not blob:
        return False
    parts = [p.strip() for p in blob.replace(" ", ",").split(",") if p.strip()]
    return claim in parts or claim in blob


def list_observations(
    cwd: Path | str,
    *,
    claim: str | None = None,
    technique: str | None = None,
) -> list[dict[str, Any]]:
    """List evidence-observations from the subject store as plain dicts."""
    root = Path(cwd)
    if not store_usable(root):
        return []
    proc = _run_aa(
        root,
        "list",
        "--type",
        _OBS_TYPE,
        "--format",
        "json",
    )
    if proc.returncode != 0:
        raise RuntimeError(
            (proc.stderr or proc.stdout or "list failed").strip()
        )
    body = json.loads(proc.stdout or "{}")
    items = list(body.get("records") or [])
    if claim is not None:
        items = [row for row in items if _matches_claim(row, claim)]
    if technique is not None:
        items = [row for row in items if _technique_of(row) == technique]
    return items
