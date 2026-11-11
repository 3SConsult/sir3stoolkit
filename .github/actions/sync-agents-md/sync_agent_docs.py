"""
Copies the guide for AI assistants into the package, so it's included in the wheel via package-data:

- AGENTS.md          -> <out>/AGENTS.md
- ai/                -> <out>/ai/
- the cell sources of each tutorial notebook (docs/source/tutorials/*/TutorialNNN_Assets/ToolkitTutorialNNN.ipynb,
  markdown and code cells, outputs left out) -> <out>/ai/tutorials/ToolkitTutorialNNN.md

With --version, the GitHub links of the copied markdown files are pointed from main to the release tag
v<version> - except releases.rst and CONTRIBUTING.md, which must stay on main - and a note saying so is added
below the title of each file. Without --version, the files are copied unchanged.

Run from the repository root (used by action.yml; also runnable locally with --out pointing at a temporary
folder - don't create src/sir3stoolkit/AGENTS.md in a working copy).
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

LINK_PATTERN = re.compile(r"(3SConsult/sir3stoolkit/(?:blob/)?)main/(?!docs/source/releases\.rst|CONTRIBUTING\.md)")
TUTORIAL_GLOB = "docs/source/tutorials/*/Tutorial[0-9][0-9][0-9]_Assets/ToolkitTutorial[0-9][0-9][0-9].ipynb"
NOTE = ("> **This copy ships with the installed sir3stoolkit {version}.** Its GitHub links point at the release tag "
        "`{tag}` - the docs, tutorials and references of exactly this version. Only the links to `releases.rst` and "
        "`CONTRIBUTING.md` point at `main` (newer releases, current development state).")


def _read(path: Path) -> str:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read()


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def point_links_at_tag(text: str, version: str) -> tuple[str, int]:
    """Returns the text with its main links pointed at v<version> and the number of links changed."""
    return LINK_PATTERN.subn(r"\g<1>v" + version + "/", text)


def add_note_below_title(text: str, version: str) -> str:
    nl = "\r\n" if "\r\n" in text else "\n"
    i = text.index(nl) + len(nl)
    return text[:i] + nl + NOTE.format(version=version, tag="v" + version) + nl + text[i:]


def notebook_to_markdown(notebook: Path, root: Path) -> str:
    """Markdown and code cells of a notebook as markdown, outputs left out."""
    nb = json.loads(notebook.read_text(encoding="utf-8"))
    rel = notebook.relative_to(root).as_posix()
    parts = [f"# {notebook.stem} - cell sources",
             f"Source: `{rel}` - markdown and code cells only, outputs left out. The notebook with its outputs "
             "(GitHub, docs site) is linked from `ai/tutorials.md`."]
    for cell in nb.get("cells", []):
        source = "".join(cell.get("source", [])).strip("\n")
        if not source.strip():
            continue
        if cell.get("cell_type") == "code":
            parts.append("```python\n" + source + "\n```")
        elif cell.get("cell_type") == "markdown":
            parts.append(source)
        else:
            parts.append("```text\n" + source + "\n```")
    return "\n\n".join(parts) + "\n"


def sync(root: Path, out: Path, version: str = "") -> dict:
    out_ai = out / "ai"
    if out_ai.exists():
        shutil.rmtree(out_ai)
    shutil.copytree(root / "ai", out_ai)
    shutil.copyfile(root / "AGENTS.md", out / "AGENTS.md")

    tutorials = sorted(root.glob(TUTORIAL_GLOB))
    if not tutorials:
        raise SystemExit(f"No tutorial notebooks found ({TUTORIAL_GLOB}) - did the folder layout change?")
    for nb in tutorials:
        _write(out_ai / "tutorials" / (nb.stem + ".md"), notebook_to_markdown(nb, root))

    changed = {}
    if version:
        guide_files = [out / "AGENTS.md"] + sorted(p for p in out_ai.glob("*.md"))
        for path in guide_files:
            text, count = point_links_at_tag(_read(path), version)
            _write(path, add_note_below_title(text, version))
            changed[path.relative_to(out).as_posix()] = count
        if changed["AGENTS.md"] == 0:
            raise SystemExit("No GitHub links to main found in AGENTS.md - did the link format change? Adjust "
                             "LINK_PATTERN in this script.")
    return {"tutorials": len(tutorials), "links_changed": changed}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", default="", help="release version (e.g. 90.15.27); empty: copy unchanged")
    parser.add_argument("--out", default="src/sir3stoolkit", help="package folder to copy into")
    parser.add_argument("--root", default=".", help="repository root")
    args = parser.parse_args(argv)
    result = sync(Path(args.root), Path(args.out), args.version.strip())
    print(f"Copied AGENTS.md and ai/ into {args.out}, exported {result['tutorials']} tutorials.")
    for name, count in result["links_changed"].items():
        print(f"  {name}: pointed {count} GitHub links from main to v{args.version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
