"""Signed amendment chains for claim test-id and hash changes."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path
from typing import Any, Mapping, Sequence


def canonical_payload(amendment: Mapping[str, Any]) -> bytes:
    """UTF-8 bytes signed for one amendment. The signature field is omitted."""
    lines = [
        "affidavit-amendment v1",
        f"claim: {amendment['claim']}",
        "old_tests: " + ",".join(amendment["old_tests"]),
        "new_tests: " + ",".join(amendment["new_tests"]),
        "old_hashes:",
    ]
    for relpath in sorted(amendment["old_hashes"]):
        lines.append(f"{relpath} {amendment['old_hashes'][relpath]}")
    lines.append("new_hashes:")
    for relpath in sorted(amendment["new_hashes"]):
        lines.append(f"{relpath} {amendment['new_hashes'][relpath]}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _principals(allowlist_bytes: bytes) -> list[str]:
    try:
        text = allowlist_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return []
    principals: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        principals.append(stripped.split()[0])
    return principals


def verify_signature(
    payload: bytes,
    signature: str | bytes,
    allowlist_bytes: bytes,
) -> bool:
    """True when any allowlist principal verifies the payload."""
    principals = _principals(allowlist_bytes)
    if not principals:
        return False
    sig_bytes = signature.encode("utf-8") if isinstance(signature, str) else bytes(signature)
    if not sig_bytes:
        return False
    with tempfile.TemporaryDirectory() as tmp:
        directory = Path(tmp)
        allowlist_path = directory / "allowed_signers"
        sig_path = directory / "amendment.sig"
        allowlist_path.write_bytes(allowlist_bytes)
        sig_path.write_bytes(sig_bytes)
        for principal in principals:
            completed = subprocess.run(
                [
                    "ssh-keygen",
                    "-Y",
                    "verify",
                    "-f",
                    str(allowlist_path),
                    "-I",
                    principal,
                    "-n",
                    "affidavit-amendment",
                    "-s",
                    str(sig_path),
                ],
                input=payload,
                capture_output=True,
                check=False,
            )
            if completed.returncode == 0:
                return True
    return False


def _as_tests(value: Sequence[str]) -> list[str]:
    return list(value)


def _as_hashes(value: Mapping[str, str]) -> dict[str, str]:
    return dict(value)


def authorize(
    base_claim: Mapping[str, Any],
    head_claim: Mapping[str, Any],
    amendments: Sequence[Mapping[str, Any]],
    base_allowlist: bytes,
    head_allowlist: bytes,
) -> tuple[bool, str]:
    """Whether amendments connect base to head under the base allowlist."""
    if base_allowlist != head_allowlist:
        return False, "allowlist changed"
    current_tests = _as_tests(base_claim["tests"])
    current_hashes = _as_hashes(base_claim["oracle_hashes"])
    head_tests = _as_tests(head_claim["tests"])
    head_hashes = _as_hashes(head_claim["oracle_hashes"])
    if current_tests == head_tests and current_hashes == head_hashes:
        return True, ""
    claim_id = base_claim["id"]
    for amendment in amendments:
        if amendment.get("claim") != claim_id:
            continue
        old_tests = _as_tests(amendment["old_tests"])
        old_hashes = _as_hashes(amendment["old_hashes"])
        if old_tests != current_tests or old_hashes != current_hashes:
            return False, "missing step"
        signature = amendment.get("signature", b"")
        if not verify_signature(canonical_payload(amendment), signature, base_allowlist):
            return False, "bad signature"
        current_tests = _as_tests(amendment["new_tests"])
        current_hashes = _as_hashes(amendment["new_hashes"])
    if current_tests != head_tests or current_hashes != head_hashes:
        return False, "missing step"
    return True, ""
