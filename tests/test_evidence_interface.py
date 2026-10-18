"""Evidence-interface oracles: store-backed observations and aff trail (R1–R4)."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from conftest import CONTRACT_PATH, REPO_ROOT, load_current_contract, run_cli
from test_verdict import (
    AFF,
    APP_GREEN,
    APP_RED,
    CLAIM,
    ORACLE,
    _commit,
    _manifest,
    _payload,
    _write_tree,
    ALLOW,
)

RECORD_TYPE = "project:evidence-observation"
REQUIRED_PAYLOAD = ("technique", "base_rev", "head_rev", "result", "claim_ids")


def _env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    return env


def _aff(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(AFF), *args],
        cwd=str(cwd) if cwd else None,
        env=_env(),
        capture_output=True,
        text=True,
    )


def _seed_verdict_subject(root: Path) -> tuple[str, str]:
    """Overlay a red→green claim-widget subject onto an existing git+store root."""
    _write_tree(
        root,
        oracle=ORACLE,
        app=APP_RED,
        allowlist=ALLOW,
        manifest=_manifest(ORACLE),
    )
    base = _commit(root, "evidence-interface red")
    _write_tree(
        root,
        oracle=ORACLE,
        app=APP_GREEN,
        allowlist=ALLOW,
        manifest=_manifest(ORACLE),
    )
    head = _commit(root, "evidence-interface green")
    return base, head


def _verdict(
    root: Path, base: str, head: str
) -> subprocess.CompletedProcess[str]:
    return _aff(
        "verdict",
        "--cwd",
        str(root),
        "--base",
        base,
        "--at",
        head,
        CLAIM,
    )


def _list_evidence_observations(root: Path) -> list[dict]:
    result = run_cli(
        "list",
        "--type",
        RECORD_TYPE,
        "--format",
        "json",
        root=root,
    )
    if result.returncode != 0:
        return []
    body = json.loads(result.stdout)
    return list(body.get("records") or [])


def _technique(item: dict) -> str | None:
    if "technique" in item:
        return item.get("technique")
    payload = item.get("payload") or {}
    return payload.get("technique")


def _observation_id(item: dict) -> str | None:
    return item.get("id")


def test_r1_contract_defines_evidence_observation(store: Path) -> None:
    """R1 / observation-contract: evidence-observation type + adaptive-artifacts validate."""
    contract = load_current_contract()
    by_name = {rec["name"]: rec for rec in contract["records"]}
    assert "evidence-observation" in by_name, (
        "contract/project-design.json must define records entry "
        "'evidence-observation'"
    )
    rec = by_name["evidence-observation"]
    assert rec.get("pattern") == "observation"
    payload_fields = list(rec.get("payload") or [])
    for field in REQUIRED_PAYLOAD:
        assert field in payload_fields, (
            f"evidence-observation payload must include {field!r}; "
            f"got {payload_fields}"
        )
    optional = set(rec.get("optional_payload") or [])
    carry = set(payload_fields) | optional
    assert "effort" in carry, "payload must be able to carry effort"
    assert "replay" in carry or "outcomes" in carry, (
        "payload must be able to carry structured outcomes and/or replay metadata"
    )

    # Live contract copy under the disposable store must resolve and validate.
    design = store / ".artifacts" / "project-design.json"
    design.write_text(CONTRACT_PATH.read_text())
    resolve = run_cli("resolve", root=store)
    assert resolve.returncode == 0, resolve.stdout + resolve.stderr
    validate = run_cli("validate", root=store)
    assert validate.returncode == 0, validate.stdout + validate.stderr

    create = run_cli(
        "create",
        "--type",
        RECORD_TYPE,
        "--subject",
        "oracle-r1-evidence-observation",
        "--payload",
        json.dumps(
            {
                "technique": "verdict",
                "base_rev": "base",
                "head_rev": "head",
                "result": "pass",
                "claim_ids": CLAIM,
            }
        ),
        root=store,
    )
    assert create.returncode == 0, create.stdout + create.stderr
    created = json.loads(create.stdout)["record"]
    assert created["record_type"] == RECORD_TYPE
    assert created["payload"]["technique"] == "verdict"


def test_r2_verdict_records_one_evidence_observation(store: Path) -> None:
    """R2 / observation-cli: passing aff verdict creates one evidence-observation."""
    for path in sorted((REPO_ROOT / "affidavit").rglob("*.py")):
        text = path.read_text(encoding="utf-8")
        assert "adaptive_artifacts" not in text, (
            f"{path.relative_to(REPO_ROOT)} must not import adaptive-artifacts "
            "Python packages"
        )

    base, head = _seed_verdict_subject(store)
    before = _list_evidence_observations(store)
    proc = _verdict(store, base, head)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert _payload(proc)["result"] == "pass"

    after = _list_evidence_observations(store)
    assert len(after) == len(before) + 1, (
        f"expected one new {RECORD_TYPE} after verdict; "
        f"before={len(before)} after={len(after)}"
    )
    created = [row for row in after if row["id"] not in {r["id"] for r in before}]
    assert len(created) == 1
    row = created[0]
    assert row["record_type"] == RECORD_TYPE
    assert row["payload"]["technique"] == "verdict"
    claim_ids = str(row["payload"].get("claim_ids") or "")
    assert CLAIM in claim_ids


def test_r2_verdict_without_store_matches_prephase_semantics(tmp_path: Path) -> None:
    """R2 constraint: without a usable store, stdout/exit match pre-phase verdict."""
    from test_verdict import _repo

    root = tmp_path / "no-store"
    base, head = _repo(root, base_app=APP_RED, head_app=APP_GREEN)
    assert not (root / ".artifacts" / "resolved-contract.json").is_file()
    proc = _verdict(root, base, head)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert _payload(proc) == {
        "result": "pass",
        "claims": [{"id": CLAIM, "result": "pass"}],
    }
    assert not (root / ".artifacts" / "records" / "project__evidence-observation").exists()


def test_r3_aff_trail_lists_observations_as_json(store: Path) -> None:
    """R3 / observation-cli-trail: aff trail prints JSON; filterable by claim id."""
    proc = _aff("trail", "--cwd", str(store))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    items = json.loads(proc.stdout)
    assert isinstance(items, list), "aff trail must print a JSON list"

    create = run_cli(
        "create",
        "--type",
        RECORD_TYPE,
        "--subject",
        "oracle-r3-trail",
        "--payload",
        json.dumps(
            {
                "technique": "verdict",
                "base_rev": "base",
                "head_rev": "head",
                "result": "pass",
                "claim_ids": CLAIM,
            }
        ),
        root=store,
    )
    assert create.returncode == 0, create.stdout + create.stderr
    seeded = json.loads(create.stdout)["record"]

    listed = _aff("trail", "--cwd", str(store))
    assert listed.returncode == 0, listed.stdout + listed.stderr
    items = json.loads(listed.stdout)
    assert isinstance(items, list)
    assert seeded["id"] in {_observation_id(item) for item in items}
    match = next(item for item in items if _observation_id(item) == seeded["id"])
    assert _technique(match) == "verdict"

    filtered = _aff("trail", "--cwd", str(store), "--claim", CLAIM)
    assert filtered.returncode == 0, filtered.stdout + filtered.stderr
    claimed = json.loads(filtered.stdout)
    assert isinstance(claimed, list)
    assert any(_observation_id(item) == seeded["id"] for item in claimed)

    other = _aff("trail", "--cwd", str(store), "--claim", "claim-does-not-exist")
    assert other.returncode == 0, other.stdout + other.stderr
    assert seeded["id"] not in {
        _observation_id(item) for item in json.loads(other.stdout)
    }


def test_r4_verdict_trail_and_subsequent_verdict_pass(store: Path) -> None:
    """R4 / verify-evidence-interface: verdict → trail → verdict still exits 0."""
    base, head = _seed_verdict_subject(store)
    before = _list_evidence_observations(store)

    first = _verdict(store, base, head)
    assert first.returncode == 0, first.stdout + first.stderr
    assert _payload(first)["result"] == "pass"

    after = _list_evidence_observations(store)
    assert len(after) == len(before) + 1
    created = [row for row in after if row["id"] not in {r["id"] for r in before}]
    assert len(created) == 1
    obs = created[0]
    assert obs["payload"]["technique"] == "verdict"

    trail = _aff("trail", "--cwd", str(store))
    assert trail.returncode == 0, trail.stdout + trail.stderr
    items = json.loads(trail.stdout)
    assert isinstance(items, list)
    assert any(_observation_id(item) == obs["id"] for item in items)
    assert any(
        _observation_id(item) == obs["id"] and _technique(item) == "verdict"
        for item in items
    )

    second = _verdict(store, base, head)
    assert second.returncode == 0, second.stdout + second.stderr
    assert _payload(second)["result"] == "pass"
