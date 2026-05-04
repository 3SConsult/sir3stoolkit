from __future__ import annotations

import os
from pathlib import Path

import pytest

nbformat = pytest.importorskip("nbformat")
nbclient = pytest.importorskip("nbclient")
from nbclient.exceptions import CellExecutionError


ROOT = Path(__file__).resolve().parents[2]
TUTORIAL_CANDIDATES = [
    ROOT / "docs" / "source" / "tutorials",
    ROOT / "docs" / "tutorials",
]

TUTORIALS_DIR = next((path for path in TUTORIAL_CANDIDATES if path.is_dir()), None)

RUN_LOCAL_NOTEBOOKS = os.getenv("SIR3S_RUN_NOTEBOOKS", "0").lower() in {
    "1",
    "true",
    "yes",
    "on",
}


def _collect_notebooks() -> list[Path]:
    if TUTORIALS_DIR is None:
        return []
    return sorted(
        notebook
        for notebook in TUTORIALS_DIR.rglob("*.ipynb")
        if notebook.name != "Test.ipynb" and ".ipynb_checkpoints" not in notebook.parts
    )


NOTEBOOKS = _collect_notebooks()


@pytest.mark.skipif(
    not RUN_LOCAL_NOTEBOOKS,
    reason="Set SIR3S_RUN_NOTEBOOKS=1 to run notebook execution locally.",
)
@pytest.mark.parametrize("notebook_path", NOTEBOOKS, ids=lambda p: str(p.relative_to(ROOT)))
def test_tutorial_notebook_executes_end_to_end(notebook_path: Path):
    """Execute all cells in tutorial notebooks to ensure full run completion."""
    with notebook_path.open("r", encoding="utf-8") as fp:
        notebook = nbformat.read(fp, as_version=4)

    client = nbclient.NotebookClient(
        notebook,
        timeout=900,
        resources={"metadata": {"path": str(notebook_path.parent)}},
        allow_errors=False,
    )

    try:
        client.execute()
    except CellExecutionError as exc:
        pytest.fail(f"Notebook execution failed for {notebook_path}: {exc}")
