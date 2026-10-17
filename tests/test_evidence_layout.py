"""Evidence layer has no orchestration trees or suite shims."""

from __future__ import annotations

import importlib

import pytest

from conftest import REPO_ROOT

_ABSENT_DIRS = ("skills", "dashboard", "scripts", "agents")
_ABSENT_MODULES = ("affidavit.tier2", "affidavit.suite")


@pytest.mark.parametrize("dirname", _ABSENT_DIRS)
def test_orchestration_directory_absent(dirname: str) -> None:
    assert not (REPO_ROOT / dirname).is_dir()


@pytest.mark.parametrize("module", _ABSENT_MODULES)
def test_moved_module_does_not_import(module: str) -> None:
    with pytest.raises(ImportError):
        importlib.import_module(module)


def test_aa_py_does_not_mention_dashboard() -> None:
    source = (REPO_ROOT / "affidavit" / "aa.py").read_text(encoding="utf-8")
    assert "dashboard" not in source


_PROTOCOL_DOCS = ("AGENTS.md", "README.md", "CLAUDE.md")
_REMOVED_INSTALL_PATHS = (
    "skills/init",
    "dashboard/bin",
    "skills/kinds-and-focus.md",
)


def test_protocol_docs_describe_the_evidence_layer() -> None:
    for name in _PROTOCOL_DOCS:
        text = (REPO_ROOT / name).read_text(encoding="utf-8")
        assert "orchestra" in text, name
        lowered = text.lower()
        assert "evidence layer" in lowered or "evidence-layer" in lowered, name
        for needle in _REMOVED_INSTALL_PATHS:
            assert needle not in text, f"{name} still cites {needle}"


_STORE_TOKENS = (
    "project:",
    "SE_WORKFLOW_STORE",
    "store-binding.json",
    "adaptive-artifacts",
)


def test_no_store_tokens() -> None:
    hits: list[str] = []
    for path in sorted((REPO_ROOT / "affidavit").rglob("*.py")):
        text = path.read_text(encoding="utf-8")
        for token in _STORE_TOKENS:
            if token in text:
                hits.append(f"{path.relative_to(REPO_ROOT)} contains {token}")
    assert hits == []
