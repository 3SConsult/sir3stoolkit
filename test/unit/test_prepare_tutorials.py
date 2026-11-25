"""Checks docs/source/tutorials/prepare_tutorials.py, which packs the tutorial archives of each release."""
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "docs" / "source" / "tutorials" / "prepare_tutorials.py"


@pytest.fixture(scope="module")
def prep():
    spec = importlib.util.spec_from_file_location("prepare_tutorials", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def committed_model_files(prep):
    """Repository paths of the model files FILES packs (Network 3 itself instead of its copies)."""
    paths = {prep.NETWORK3_DB.relative_to(ROOT).as_posix()}
    for nr, entries in prep.FILES.items():
        group = "SIR3S_Model" if int(nr) < 50 else "SIR3S_Model_Mantle"
        for entry in entries:
            source = entry if isinstance(entry, str) else entry[1]
            if source.lower().endswith(".db3") and source != "Network3.db3":
                paths.add(f"docs/source/tutorials/{group}/Tutorial{nr}_Assets/{source}")
    return paths


def test_gitignore_exceptions_match_the_packed_models(prep):
    # the models are committed as exceptions to *.db3, listed one by one - never more than FILES packs
    lines = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    exceptions = {line[1:] for line in lines if line.startswith("!") and line.lower().endswith(".db3")}
    assert exceptions == committed_model_files(prep)


def test_every_tutorial_is_listed(prep):
    for group in prep.GROUPS:
        for folder in (prep.TUTORIALS_DIR / group).iterdir():
            match = prep.ASSET_FOLDER.match(folder.name)
            if match:
                assert match.group(1) in prep.FILES, f"{folder.name} missing in FILES of prepare_tutorials.py"


def test_notebooks_open_only_packed_or_created_files(prep):
    # a notebook opening a file that is not packed would not run from the downloaded archive
    for nr in prep.FILES:
        group = "SIR3S_Model" if int(nr) < 50 else "SIR3S_Model_Mantle"
        notebook = prep.TUTORIALS_DIR / group / f"Tutorial{nr}_Assets" / f"ToolkitTutorial{nr}.ipynb"
        packed = {e if isinstance(e, str) else e[0] for e in prep.FILES[nr]}
        unpacked = prep.notebook_files(notebook) - packed - set(prep.CREATED.get(nr, []))
        assert not unpacked, f"Tutorial {nr} opens {sorted(unpacked)}, which is neither packed nor created by it"
