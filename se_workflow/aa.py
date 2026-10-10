"""Resolve and invoke the adaptive-artifacts CLI as a subprocess."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def resolve_aa_command() -> list[str]:
    override = os.environ.get("ADAPTIVE_ARTIFACTS_BIN")
    if override:
        path = Path(override)
        if path.name.endswith(".py"):
            return [sys.executable, str(path)]
        return [str(path)]
    root = os.environ.get("ADAPTIVE_ARTIFACTS_ROOT")
    if root:
        tools = Path(root).expanduser() / "tools" / "artifacts.py"
        if tools.is_file():
            return [sys.executable, str(tools)]
    checkout = Path.home() / "adaptive-artifacts" / "bin" / "adaptive-artifacts"
    if os.access(checkout, os.X_OK):
        return [str(checkout)]
    which = shutil.which("adaptive-artifacts")
    if which:
        return [which]
    tools = Path.home() / "adaptive-artifacts" / "tools" / "artifacts.py"
    if tools.is_file():
        return [sys.executable, str(tools)]
    raise FileNotFoundError(
        "adaptive-artifacts not found. Install it on PATH, set "
        "ADAPTIVE_ARTIFACTS_BIN, or set ADAPTIVE_ARTIFACTS_ROOT."
    )


def find_store_root(start: Path) -> Path:
    """Walk up from start for a directory that has .artifacts/meta.json."""
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".artifacts" / "meta.json").is_file():
            return candidate
    return start.resolve()


def run_aa(
    *args: str,
    root: Path,
    check: bool = False,
) -> subprocess.CompletedProcess[str]:
    cmd = [*resolve_aa_command(), "--root", str(root), *args]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(
            f"adaptive-artifacts {' '.join(args)} failed "
            f"(exit {result.returncode}): {result.stdout}{result.stderr}"
        )
    return result


def get_record(root: Path, record_id: str, record_type: str | None = None) -> dict[str, Any]:
    args = ["get", "--id", record_id]
    if record_type:
        args.extend(["--type", record_type])
    result = run_aa(*args, root=root)
    if result.returncode != 0:
        raise LookupError(
            f"record {record_id!r} not found: {result.stdout}{result.stderr}".strip()
        )
    payload = json.loads(result.stdout)
    if "record" in payload and isinstance(payload["record"], dict):
        return payload["record"]
    return payload


def create_record(
    root: Path,
    *,
    record_type: str,
    subject: str,
    payload: dict[str, Any],
    rels: list[str] | None = None,
    body: str | None = None,
) -> dict[str, Any]:
    args = [
        "create",
        "--type",
        record_type,
        "--subject",
        subject,
        "--payload",
        json.dumps(payload),
    ]
    for rel in rels or []:
        args.extend(["--rel", rel])
    if body is not None:
        args.extend(["--body", body])
    result = run_aa(*args, root=root)
    if result.returncode != 0:
        raise RuntimeError(
            f"create {record_type} failed (exit {result.returncode}): "
            f"{result.stdout}{result.stderr}"
        )
    return json.loads(result.stdout)["record"]
