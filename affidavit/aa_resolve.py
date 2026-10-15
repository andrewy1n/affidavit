"""Resolve the adaptive-artifacts CLI argv (no store binding imports)."""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


def _as_argv(path: Path) -> list[str]:
    if path.name.endswith(".py"):
        return [sys.executable, str(path)]
    return [str(path)]


def _usable(path: Path) -> list[str] | None:
    if path.name.endswith(".py") and path.is_file():
        return _as_argv(path)
    if os.access(path, os.X_OK):
        return _as_argv(path)
    return None


def _plugin_roots() -> list[Path]:
    roots: list[Path] = []
    for key in ("CLAUDE_PLUGIN_ROOT", "CURSOR_PLUGIN_ROOT"):
        raw = os.environ.get(key)
        if not raw:
            continue
        path = Path(raw).expanduser()
        if path.is_dir():
            roots.append(path.resolve())
    return roots


def _search_roots(roots: list[Path]) -> list[str] | None:
    seen: set[Path] = set()
    candidates: list[Path] = []
    for root in roots:
        candidates.extend(
            [
                root / "bin" / "adaptive-artifacts",
                root / "tools" / "artifacts.py",
                root.parent / "adaptive-artifacts" / "bin" / "adaptive-artifacts",
                root.parent / "adaptive-artifacts" / "tools" / "artifacts.py",
            ]
        )
    for candidate in candidates:
        key = candidate.resolve() if candidate.exists() else candidate
        if key in seen:
            continue
        seen.add(key)
        found = _usable(candidate)
        if found is not None:
            return found
    return None


def resolve_aa_command() -> list[str]:
    """Return argv for adaptive-artifacts.

    Order: ADAPTIVE_ARTIFACTS_BIN, ADAPTIVE_ARTIFACTS_ROOT, plugin-root /
    sibling discovery, then PATH. Does not quietly prefer ~/adaptive-artifacts.
    """
    override = os.environ.get("ADAPTIVE_ARTIFACTS_BIN")
    if override:
        return _as_argv(Path(override).expanduser())

    root = os.environ.get("ADAPTIVE_ARTIFACTS_ROOT")
    if root:
        tools = Path(root).expanduser() / "tools" / "artifacts.py"
        if tools.is_file():
            return _as_argv(tools)

    from_plugins = _search_roots(_plugin_roots())
    if from_plugins is not None:
        return from_plugins

    which = shutil.which("adaptive-artifacts")
    if which:
        return [which]

    raise FileNotFoundError(
        "adaptive-artifacts not found. Install it on PATH, set "
        "ADAPTIVE_ARTIFACTS_BIN or ADAPTIVE_ARTIFACTS_ROOT, or run under a "
        "host that sets CLAUDE_PLUGIN_ROOT / CURSOR_PLUGIN_ROOT with a "
        "co-installed adaptive-artifacts plugin."
    )
