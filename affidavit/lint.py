"""Cheap witness lint: no-assert sources and skips added between revisions."""

from __future__ import annotations

import ast
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Sequence

from affidavit.manifest import load_manifest, resolve_commit
from affidavit.runner import run_tests


def find_no_assert(paths: Sequence[Path | str]) -> list[str]:
    """Return test names (or paths) whose bodies lack assert / pytest.raises."""
    findings: list[str] = []
    for path in paths:
        findings.extend(_no_assert_in_file(Path(path)))
    return findings


def find_new_skips(
    cwd: Path | str,
    base: str,
    head: str,
    *,
    claim_id: str,
) -> list[str]:
    """Return claim witness ids skipped at ``head`` that were not skipped at ``base``."""
    root = Path(cwd)
    base_commit = resolve_commit(root, base)
    head_commit = resolve_commit(root, head)
    head_manifest = load_manifest(root, head_commit)
    claim = next((c for c in head_manifest.claims if c.id == claim_id), None)
    if claim is None:
        return []
    test_ids = list(claim.tests)
    if not test_ids:
        return []

    base_tree = _checkout(root, base_commit)
    head_tree = _checkout(root, head_commit)
    try:
        base_wt = _worktree(base_tree)
        head_wt = _worktree(head_tree)
        base_outcomes = (
            run_tests(base_wt, test_ids, head_manifest.runner)
            if base_wt is not None
            else {tid: "not_run" for tid in test_ids}
        )
        head_outcomes = (
            run_tests(head_wt, test_ids, head_manifest.runner)
            if head_wt is not None
            else {tid: "not_run" for tid in test_ids}
        )
    finally:
        _remove(root, base_tree)
        _remove(root, head_tree)

    return [
        test_id
        for test_id in test_ids
        if head_outcomes.get(test_id) == "not_run"
        and base_outcomes.get(test_id) != "not_run"
    ]


def _no_assert_in_file(path: Path) -> list[str]:
    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError:
        return [str(path)]
    findings: list[str] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("test") and not _has_outcome_signal(node):
                findings.append(node.name)
        elif isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if item.name.startswith("test") and not _has_outcome_signal(item):
                        findings.append(f"{node.name}::{item.name}")
    if not findings and not any(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
        for n in tree.body
    ):
        return [str(path)]
    return findings


def _has_outcome_signal(fn: ast.AST) -> bool:
    for node in ast.walk(fn):
        if isinstance(node, ast.Assert):
            return True
        if isinstance(node, ast.Call) and _is_raises_call(node.func):
            return True
        if isinstance(node, ast.With):
            for item in node.items:
                call = item.context_expr
                if isinstance(call, ast.Call) and _is_raises_call(call.func):
                    return True
    return False


def _is_raises_call(func: ast.AST) -> bool:
    if isinstance(func, ast.Name) and func.id == "raises":
        return True
    if isinstance(func, ast.Attribute) and func.attr == "raises":
        return True
    return False


def _checkout(cwd: Path, commit: str) -> tuple[Path, Path] | None:
    parent = Path(tempfile.mkdtemp(prefix="aff-lint-"))
    worktree = parent / "wt"
    added = subprocess.run(
        ["git", "-C", str(cwd), "worktree", "add", "--detach", str(worktree), commit],
        capture_output=True,
    )
    if added.returncode != 0:
        shutil.rmtree(parent, ignore_errors=True)
        return None
    return parent, worktree


def _worktree(checked: tuple[Path, Path] | None) -> Path | None:
    if checked is None:
        return None
    return checked[1]


def _remove(cwd: Path, checked: tuple[Path, Path] | None) -> None:
    if checked is None:
        return
    parent, worktree = checked
    subprocess.run(
        ["git", "-C", str(cwd), "worktree", "remove", "--force", str(worktree)],
        capture_output=True,
    )
    shutil.rmtree(parent, ignore_errors=True)
