"""
Prepares the tutorial archives that are attached to each GitHub release (v<version>) by
.github/workflows/release.yml - users download them with ``python -m sir3stoolkit tutorials``.

1. Network 3 (docs/source/networks/Network3.py), the shared demo model of the mantle tutorials, is
   copied as Network3.db3 into the asset folder of every tutorial that uses it. If
   docs/source/networks/Network3.db3 does not exist, it is built first (needs a local SIR 3S
   installation) - unless --no-build is given (release workflow): then that is an error.
2. One zip per tutorial (TutorialNNN_Assets.zip) and one per tutorial group (Tutorials000-049_Assets.zip:
   SIR3S_Model/, Tutorials050-099_Assets.zip: SIR3S_Model_Mantle/). A zip holds only the notebook and the
   files listed for the tutorial in FILES - the asset folders may hold more (results, backups, and in
   the mantle folders confidential models of real networks, which must never be published), so nothing
   else is packed. Plus the (empty) working directory folder of every packed model, see working_directory().
   A tutorial whose notebook opens a file that is neither listed nor in CREATED is not packed and the
   script ends with exit code 1.

The model files listed in FILES are committed to git as exceptions to the *.db3 rule in .gitignore
(listed one by one there as well; test/unit/test_prepare_tutorials.py checks both lists match).
They are the state the tutorials start from. Running a tutorial changes its model file (SIR 3S writes
housekeeping data to a model already when opening it; tutorial 010 saves its calculation settings, 008
migrates its model) - restore the committed models (git checkout -- <file>) before committing.

Usage: python prepare_tutorials.py [--no-build] [--rebuild] [--zip-dir DIR]
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

TUTORIALS_DIR = Path(__file__).resolve().parent
NETWORKS_DIR = TUTORIALS_DIR.parent / "networks"
NETWORK3_BUILDER = NETWORKS_DIR / "Network3.py"
NETWORK3_DB = NETWORKS_DIR / "Network3.db3"

GROUPS = {  # group folder: name of the archive with all its tutorials
    "SIR3S_Model": "Tutorials000-049_Assets.zip",
    "SIR3S_Model_Mantle": "Tutorials050-099_Assets.zip",
}

# Mantle tutorials using Network 3; it is copied into their asset folders (not committed there).
NETWORK3_TUTORIALS = ["051", "052", "053", "056", "057", "061", "071", "072", "073"]

# Files packed per tutorial besides the notebook ToolkitTutorialNNN.ipynb: the files it opens.
# An entry is the file name, or (name in the zip, file in the asset folder).
FILES = {
    "000": [],
    "001": ["Toolkit_Tutorial1_OpenModel.db3", "Toolkit_Tutorial1_OpenModel_XML.xml"],
    "002": ["Toolkit_Tutorial2_Model.db3"],
    "003": ["Toolkit_Tutorial3_Model.db3"],
    "004": ["Toolkit_Tutorial4_Model.db3"],
    "005": [],
    "006": ["Toolkit_Tutorial6_Model.db3"],
    "007": ["Toolkit_Tutorial7_Model.db3"],
    # the model from SIR 3S 90-14 that the tutorial migrates; the asset folder's copy of that name is
    # migrated as soon as the tutorial has run once, SirGraf's backup keeps the original
    "008": ["Toolkit_Tutorial8_Model.db3",
            ("Toolkit_Tutorial8_PotsdamVersionModel.db3",
             "Toolkit_Tutorial8_PotsdamVersionModel_Backup_Ver9014_20261014_141345.db3")],
    "009": ["Toolkit_Tutorial9_Model.db3"],
    "010": ["Toolkit_Tutorial10_Model.db3"],
    "011": ["Toolkit_Tutorial11_Model.db3"],
    "050": [],
    "054": ["Toolkit_Tutorial54_Model.db3"],
    "055": ["Toolkit_Tutorial55_Model.db3"],
    "062": ["Toolkit_Tutorial62_Model.db3"],
    "081": ["Toolkit_Tutorial81_Model.db3"],
    **{nr: ["Network3.db3"] for nr in NETWORK3_TUTORIALS},
}

# Files a tutorial's notebook refers to but creates itself - not packed.
CREATED = {
    "001": ["Toolkit_Tutorial1_NewModel.db3"],  # NewModel()
    "005": ["Toolkit_Tutorial5_Model.db3"],  # NewModel()
    "008": ["Tutorial8.log"],  # SetLogFilePath()
}

ASSET_FOLDER = re.compile(r"^Tutorial(\d{3})_Assets$")
FILE_IN_NOTEBOOK = re.compile(r"""["']([^"'\\/]+\.(?:db3|xml|log|csv))["']""", re.IGNORECASE)


def build_network3(rebuild, no_build):
    if NETWORK3_DB.exists() and not rebuild:
        print(f"Network 3: using {NETWORK3_DB}")
        return
    if no_build:
        sys.exit(f"Network 3: {NETWORK3_DB} is missing (--no-build). Build it with {NETWORK3_BUILDER.name} and commit it.")
    if NETWORK3_DB.exists():
        NETWORK3_DB.unlink()
    for wd in NETWORKS_DIR.glob("WDNetwork3"):  # case-insensitive on Windows
        shutil.rmtree(wd)
    print(f"Network 3: building with {NETWORK3_BUILDER.name} (needs SIR 3S) ...")
    subprocess.run([sys.executable, str(NETWORK3_BUILDER), str(NETWORK3_DB)], check=True)


def working_directory(model_file):
    """
    The working directory of a model (results) is the folder WD<file name> next to the .db3.
    The tutorials open their model by file name only (relative dbName): then SirDB finds the working
    directory only if this folder already exists - otherwise the working directory is empty and
    SirCalc writes its results to \\B1\\... on the current drive. So the folder is created next to
    every copy of Network 3 and packed (empty) into the zips.
    """
    return model_file.parent / f"WD{model_file.stem}"


def copy_network3():
    for nr in NETWORK3_TUTORIALS:
        folder = TUTORIALS_DIR / "SIR3S_Model_Mantle" / f"Tutorial{nr}_Assets"
        for wd in folder.glob("WDNetwork3"):  # results of the previous copy
            shutil.rmtree(wd)
        shutil.copy2(NETWORK3_DB, folder / "Network3.db3")
        working_directory(folder / "Network3.db3").mkdir()
    print(f"Network 3: copied into Tutorial{{{','.join(NETWORK3_TUTORIALS)}}}_Assets")


def notebook_files(notebook):
    """Files (name without directory) the notebook's code cells refer to."""
    cells = json.loads(notebook.read_text(encoding="utf-8"))["cells"]
    code = "\n".join("".join(c["source"]) for c in cells if c["cell_type"] == "code")
    return set(FILE_IN_NOTEBOOK.findall(code))


def tutorial_entries(folder, nr):
    """[(name in the zip, source file)] of a tutorial, or None (with the reason printed) if it cannot be packed."""
    notebook = folder / f"ToolkitTutorial{nr}.ipynb"
    if nr not in FILES:
        print(f"  NOT PACKED {folder.name}: not listed in FILES")
        return None
    entries = [(e, e) if isinstance(e, str) else e for e in FILES[nr]]
    unlisted = notebook_files(notebook) - {name for name, _ in entries} - set(CREATED.get(nr, []))
    missing = [source for _, source in entries if not (folder / source).is_file()]
    if unlisted:
        print(f"  NOT PACKED {folder.name}: the notebook opens file(s) not listed in FILES: {sorted(unlisted)}")
        return None
    if missing:
        print(f"  NOT PACKED {folder.name}: listed file(s) missing: {missing}")
        return None
    return [(notebook.name, notebook.name)] + entries


def write_tutorial(zf, folder, entries):
    for name, source in entries:
        zf.write(folder / source, f"{folder.name}/{name}")
        if name.lower().endswith(".db3"):  # empty working directory, see working_directory()
            zf.writestr(f"{folder.name}/{working_directory(Path(name)).name}/", "")


def zip_tutorials(zip_dir):
    """Returns the number of tutorials that could not be packed."""
    not_packed = 0
    for group, combined_name in GROUPS.items():
        group_dir = TUTORIALS_DIR / group
        target = zip_dir or group_dir
        target.mkdir(parents=True, exist_ok=True)
        print(f"Zipping {group} -> {target}")
        packed = []
        for folder in sorted(p for p in group_dir.iterdir() if p.is_dir() and ASSET_FOLDER.match(p.name)):
            entries = tutorial_entries(folder, ASSET_FOLDER.match(folder.name).group(1))
            if entries is None:
                not_packed += 1
                continue
            with zipfile.ZipFile(target / f"{folder.name}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
                write_tutorial(zf, folder, entries)
            packed.append((folder, entries))
            print(f"  {folder.name}.zip: {', '.join(name for name, _ in entries)}")
        with zipfile.ZipFile(target / combined_name, "w", zipfile.ZIP_DEFLATED) as zf:
            for folder, entries in packed:
                write_tutorial(zf, folder, entries)
        print(f"  {combined_name}: {len(packed)} tutorial(s)")
    return not_packed


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--no-build", action="store_true",
                        help="fail instead of building a missing Network3.db3 (release workflow)")
    parser.add_argument("--rebuild", action="store_true", help="rebuild Network3.db3 even if it exists (new tks)")
    parser.add_argument("--zip-dir", type=Path, help="folder for all zips (default: next to the asset folders)")
    args = parser.parse_args()

    build_network3(args.rebuild, args.no_build)
    copy_network3()
    not_packed = zip_tutorials(args.zip_dir)
    if not_packed:
        sys.exit(f"{not_packed} tutorial(s) not packed, see above.")


if __name__ == "__main__":
    main()
