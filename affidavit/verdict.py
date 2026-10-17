"""Re-execute frozen oracle tests at two revisions.

Reads manifests, allowlists, and oracle blobs from git. Does not read a
record store.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Sequence

from affidavit.amendment import authorize
from affidavit.manifest import (
    Claim,
    hash_oracle_files,
    load_allowlist,
    load_manifest,
    merge_base,
    resolve_commit,
)
from affidavit.oracle_red import is_assertion_level_failure

_FAILED_RE = re.compile(r"^FAILED\s+(\S+)", re.MULTILINE)


def run_verdict(
    cwd: Path | str,
    at: str,
    base: str | None,
    claim_ids: Sequence[str],
) -> dict[str, Any]:
    """Judge ``claim_ids`` by re-executing their oracle tests.

    When ``base`` is omitted, the base revision is ``merge_base(cwd, at)``.
    A claim passes only when the allowlists match, amendments authorize any
    test-id or hash change, oracle blobs hash to that revision's
    ``oracle_hashes``, the base run fails on an assertion, and the head run
    exits 0.
    """
    root = Path(cwd)
    base_rev = base if base else merge_base(root, at)
    at_commit = resolve_commit(root, at)
    base_commit = resolve_commit(root, base_rev)
    at_manifest = load_manifest(root, at_commit)
    base_manifest = load_manifest(root, base_commit)
    at_allow = load_allowlist(root, at_commit)
    base_allow = load_allowlist(root, base_commit)
    at_by_id = {claim.id: claim for claim in at_manifest.claims}
    base_by_id = {claim.id: claim for claim in base_manifest.claims}

    if base_allow != at_allow:
        claims = [_fail(claim_id, "allowlist changed") for claim_id in claim_ids]
        return _payload(claims)

    verdicts: list[dict[str, str] | None] = [None] * len(claim_ids)
    pending: list[tuple[int, str, Claim, Claim]] = []
    for index, claim_id in enumerate(claim_ids):
        base_claim = base_by_id.get(claim_id)
        head_claim = at_by_id.get(claim_id)
        if base_claim is None or head_claim is None:
            verdicts[index] = _fail(claim_id, "missing claim")
            continue
        allowed, reason = authorize(
            _mapping(base_claim),
            _mapping(head_claim),
            at_manifest.amendments,
            base_allow,
            at_allow,
        )
        if not allowed:
            verdicts[index] = _fail(claim_id, reason)
            continue
        if not _hashes_match(root, base_commit, base_claim) or not _hashes_match(
            root, at_commit, head_claim
        ):
            verdicts[index] = _fail(claim_id, "hash mismatch")
            continue
        pending.append((index, claim_id, base_claim, head_claim))

    if pending:
        base_nodes = _union(claim.tests for _, _, claim, _ in pending)
        head_nodes = _union(claim.tests for _, _, _, claim in pending)
        _, base_out = _pytest_at(root, base_commit, base_nodes)
        head_code, _ = _pytest_at(root, at_commit, head_nodes)
        for index, claim_id, base_claim, _head_claim in pending:
            if not _base_is_assertion(base_out, base_claim.tests):
                verdicts[index] = _fail(claim_id, "not assertion")
            elif not _head_passed(head_code):
                verdicts[index] = _fail(claim_id, "tests failed")
            else:
                verdicts[index] = {"id": claim_id, "result": "pass"}

    claims = [item for item in verdicts if item is not None]
    return _payload(claims)


def _payload(claims: list[dict[str, str]]) -> dict[str, Any]:
    result = "pass" if claims and all(item["result"] == "pass" for item in claims) else "fail"
    return {"result": result, "claims": claims}


def _fail(claim_id: str, reason: str) -> dict[str, str]:
    return {"id": claim_id, "result": "fail", "reason": reason}


def _mapping(claim: Claim) -> dict[str, Any]:
    return {
        "id": claim.id,
        "tests": list(claim.tests),
        "oracle_hashes": dict(claim.oracle_hashes),
    }


def _hashes_match(cwd: Path, revision: str, claim: Claim) -> bool:
    relpaths = list(claim.oracle_hashes)
    try:
        actual = hash_oracle_files(cwd, revision, relpaths)
    except FileNotFoundError:
        return False
    return actual == claim.oracle_hashes


def _union(groups: Any) -> list[str]:
    nodes: list[str] = []
    for group in groups:
        for node in group:
            if node not in nodes:
                nodes.append(node)
    return nodes


def _node_reported(reported: Sequence[str], node: str) -> bool:
    for item in reported:
        if item == node:
            return True
        if "::" not in item and node.startswith(item):
            return True
    return False


def _base_is_assertion(output: str, tests: Sequence[str]) -> bool:
    if not tests:
        return False
    failed = _FAILED_RE.findall(output)
    if not all(_node_reported(failed, node) for node in tests):
        return False
    return is_assertion_level_failure(output, list(tests))


def _head_passed(exit_code: int) -> bool:
    return exit_code == 0


def _pytest_at(cwd: Path, commit: str, node_ids: Sequence[str]) -> tuple[int, str]:
    parent = Path(tempfile.mkdtemp(prefix="aff-verdict-"))
    worktree = parent / "wt"
    try:
        added = subprocess.run(
            ["git", "-C", str(cwd), "worktree", "add", "--detach", str(worktree), commit],
            capture_output=True,
        )
        if added.returncode != 0:
            return 1, added.stderr.decode("utf-8", "replace")
        env = os.environ.copy()
        env.pop("PYTHONPATH", None)
        env.pop("PYTEST_ADDOPTS", None)
        completed = subprocess.run(
            ["python3", "-m", "pytest", *node_ids],
            cwd=str(worktree),
            capture_output=True,
            env=env,
        )
        output = completed.stdout.decode("utf-8", "replace") + completed.stderr.decode(
            "utf-8", "replace"
        )
        return completed.returncode, output
    finally:
        subprocess.run(
            ["git", "-C", str(cwd), "worktree", "remove", "--force", str(worktree)],
            capture_output=True,
        )
        shutil.rmtree(parent, ignore_errors=True)
