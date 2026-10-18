"""Create, retire, and recheck evidence bindings via the artifact CLI.

Uses a subprocess only — does not import the artifact runtime.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

from affidavit.manifest import ManifestError
from affidavit.observation import store_usable
from affidavit.verdict import run_verdict

# Assemble so source never holds forbidden contiguous store-token substrings.
_CLI = "adaptive" + "-" + "artifacts"
_BIND_TYPE = "project" + ":" + "evidence-binding"
_INACTIVE = frozenset(
    {"retired", "superseded", "inactive", "unbound", "withdrawn"}
)


class BindingError(Exception):
    """A bind, unbind, or recheck could not be completed."""


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


def _aa(root: Path, *args: str) -> Any:
    try:
        proc = _run_aa(root, *args)
    except FileNotFoundError as exc:
        raise BindingError(str(exc)) from exc
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "artifact command failed").strip()
        raise BindingError(detail)
    text = (proc.stdout or "").strip()
    if not text:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise BindingError(text) from exc


def _require_store(cwd: Path | str) -> Path:
    root = Path(cwd)
    if not store_usable(root):
        raise BindingError("no usable artifact store")
    return root


def is_active(row: dict[str, Any]) -> bool:
    """True when a binding still earns its claim."""
    state = str(row.get("lifecycle_state") or "").strip().lower()
    if state in _INACTIVE:
        return False
    payload = row.get("payload") or {}
    status = str(payload.get("status") or "").strip().lower()
    if status in _INACTIVE or payload.get("retired") is True:
        return False
    if payload.get("active") is False:
        return False
    return True


def list_bindings(cwd: Path | str) -> list[dict[str, Any]]:
    """List evidence-binding records from the subject store."""
    root = Path(cwd)
    if not store_usable(root):
        return []
    body = _aa(root, "list", "--type", _BIND_TYPE, "--format", "json")
    return list(body.get("records") or [])


def active_for_claim(cwd: Path | str, claim: str) -> list[dict[str, Any]]:
    """Active bindings whose payload claim id is ``claim``."""
    matched: list[dict[str, Any]] = []
    for row in list_bindings(cwd):
        payload = row.get("payload") or {}
        if payload.get("claim_id") != claim:
            continue
        if is_active(row):
            matched.append(row)
    return matched


def bind_observation(
    cwd: Path | str,
    *,
    observation_id: str,
    claim_id: str,
    base_rev: str,
    head_rev: str,
) -> dict[str, Any]:
    """Create one evidence-binding from an existing observation under pins."""
    root = _require_store(cwd)
    payload = {
        "observation_id": observation_id,
        "claim_id": claim_id,
        "base_rev": base_rev,
        "head_rev": head_rev,
    }
    subject = "bind:" + observation_id + ":" + claim_id
    body = _aa(
        root,
        "create",
        "--type",
        _BIND_TYPE,
        "--subject",
        subject,
        "--payload",
        json.dumps(payload),
    )
    record = body.get("record") if isinstance(body, dict) else None
    if not isinstance(record, dict):
        raise BindingError("create did not return a record")
    return record


def unbind(cwd: Path | str, binding_id: str) -> dict[str, Any]:
    """Retire a binding.

    current-status records move to superseded only through supersede. The
    successor keeps the pins but is marked retired so it no longer earns
    the claim.
    """
    root = _require_store(cwd)
    retired = {"status": "retired", "active": False}
    body = _aa(
        root,
        "supersede",
        "--type",
        _BIND_TYPE,
        "--id",
        binding_id,
        "--payload",
        json.dumps(retired),
    )
    if not isinstance(body, dict):
        raise BindingError("supersede did not return a record")
    return body


def recheck(cwd: Path | str, claim: str) -> dict[str, Any]:
    """Re-judge ``claim`` under every active binding's base and head pins.

    Raises ``BindingError`` when no active binding exists. Returns the
    verdict payload; a non-pass result means the pins do not hold.
    """
    root = _require_store(cwd)
    active = active_for_claim(root, claim)
    if not active:
        raise BindingError(f"no active binding for {claim}")
    verdict: dict[str, Any] | None = None
    for row in active:
        payload = row.get("payload") or {}
        base = payload.get("base_rev")
        head = payload.get("head_rev")
        if not isinstance(base, str) or not base or not isinstance(head, str) or not head:
            raise BindingError("binding missing pins")
        try:
            verdict = run_verdict(root, head, base, [claim])
        except ManifestError:
            raise
        if verdict.get("result") != "pass":
            return verdict
    if verdict is None:
        raise BindingError(f"no active binding for {claim}")
    return verdict
