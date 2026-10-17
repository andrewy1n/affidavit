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
