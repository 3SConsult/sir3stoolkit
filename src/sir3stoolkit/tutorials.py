# -*- coding: utf-8 -*-
"""
Downloads the tutorials of sir3stoolkit - the notebooks and the SIR 3S models they use - into a local
folder: ``python -m sir3stoolkit tutorials [folder]`` (see ``python -m sir3stoolkit tutorials -h``).

The tutorials of each version are attached as zip archives to its GitHub release (tag ``v<version>``),
by .github/workflows/release.yml on the same trigger as the upload to PyPI. By default the tutorials of
the installed version are downloaded, so they match its functions.

The archives are unpacked with the folder layout of the repository (``SIR3S_Model/TutorialNNN_Assets``,
``SIR3S_Model_Mantle/TutorialNNN_Assets``): each tutorial folder holds the notebook, the models it opens
and their (empty) working directory folders. The tutorials change their models and write calculation
results next to them, so they are meant to be run from that folder - not from the installed package.

If a SirGraf folder is configured (``wrapper.Write_SirGraf_Config_Path()``, see Tutorial 0), it is
written into the ``SIR3S_SIRGRAF_DIR = r"..."`` line of the unpacked notebooks.
"""

import importlib.metadata
import io
import json
import re
import shutil
import urllib.error
import urllib.request
import zipfile
from pathlib import Path, PureWindowsPath
from typing import Dict, List, Optional, Sequence, Tuple, Union

from sir3stoolkit import sirgraf_config

RELEASE_URL = "https://github.com/3SConsult/sir3stoolkit/releases/download/v{version}/{archive}"
GROUPS = {  # group: (folder, archive)
    "core": ("SIR3S_Model", "Tutorials000-049_Assets.zip"),
    "mantle": ("SIR3S_Model_Mantle", "Tutorials050-099_Assets.zip"),
}
DEFAULT_FOLDER = "sir3stoolkit_tutorials"
_RELEASE_VERSION = re.compile(r"\d+(\.\d+)*(\.dev\d+)?")  # .devN: test releases (.github/workflows/test-release.yml)
# the line of a tutorial notebook that sets the SirGraf folder, e.g. SIR3S_SIRGRAF_DIR = r"C:\3S\..." #change to local path
_SIRGRAF_DIR_LINE = re.compile(r"""^(\s*SIR3S_SIRGRAF_DIR\s*=\s*)r?(["']).*?\2.*$""", re.MULTILINE)


def get_configured_sirgraf_dir() -> Optional[str]:
    """
    Returns the SirGraf folder stored with ``wrapper.Write_SirGraf_Config_Path()``, if it exists - the same
    one ``wrapper.Read_SirGraf_Config_Path()`` returns (see ``sir3stoolkit.sirgraf_config``), read without
    loading the .NET-based wrapper.

    :return: The stored SirGraf folder, or None if none is stored or the folder does not exist.
    :rtype: str, optional
    """
    path, _ = sirgraf_config.read_configured_path()
    return str(PureWindowsPath(path)) if path and Path(path).is_dir() else None


def set_sirgraf_dir_in_notebook(notebook: bytes, sirgraf_dir: str) -> Tuple[bytes, bool]:
    """
    Sets the SirGraf folder in the ``SIR3S_SIRGRAF_DIR = r"..."`` line of a tutorial notebook.

    :param notebook: The notebook file content (.ipynb).
    :type notebook: bytes
    :param sirgraf_dir: The SirGraf folder.
    :type sirgraf_dir: str
    :return: (notebook content, whether a line was changed) - unchanged if it is no valid notebook
    :rtype: tuple[bytes, bool]
    """
    try:
        nb = json.loads(notebook.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return notebook, False
    value = f'r"{PureWindowsPath(sirgraf_dir)}"  # SirGraf folder from the sir3stoolkit config'
    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        new_source, n = _SIRGRAF_DIR_LINE.subn(lambda m: m.group(1) + value, source)
        if n:
            cell["source"] = new_source.splitlines(keepends=True) if isinstance(cell["source"], list) else new_source
            changed = True
    if not changed:
        return notebook, False
    return (json.dumps(nb, indent=1, ensure_ascii=False) + "\n").encode("utf-8"), True


def _installed_version() -> Optional[str]:
    try:
        return importlib.metadata.version("sir3stoolkit")
    except importlib.metadata.PackageNotFoundError:
        return None


def get_tutorials_url(group: str, version: Optional[str] = None) -> str:
    """
    Returns the download URL of the tutorial archive of a group and version.

    :param group: "core" (tutorials 0-49, SIR3S_Model) or "mantle" (tutorials 50-99, SIR3S_Model_Mantle).
    :type group: str
    :param version: sir3stoolkit version, e.g. "90.15.27". Default: the installed version.
    :type version: str, optional
    :return: URL of the zip archive attached to the GitHub release ``v<version>``.
    :rtype: str
    :raises ValueError: if group is unknown, or the version is not a released one (e.g. a development
        version of a repository checkout) - pass the version of a release then.
    """
    if group not in GROUPS:
        raise ValueError(f"Unknown tutorial group {group!r} - use one of {sorted(GROUPS)}.")
    version = version or _installed_version()
    if not version or not _RELEASE_VERSION.fullmatch(version):
        raise ValueError(f"sir3stoolkit version {version!r} has no published tutorials (not a released version) - "
                         f"pass the version of a release, e.g. --version 90.15.27.")
    return RELEASE_URL.format(version=version, archive=GROUPS[group][1])


def _download(url: str) -> bytes:
    try:
        with urllib.request.urlopen(url, timeout=120) as response:  # uses the proxy of HTTPS_PROXY if set
            return response.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(f"No tutorials found at {url} - this version has no tutorial archives on GitHub "
                             f"(they are published with each release from 90.15.27 on).") from e
        raise ConnectionError(f"Download of {url} failed: HTTP {e.code} {e.reason}") from e
    except urllib.error.URLError as e:
        raise ConnectionError(f"Download of {url} failed: {e.reason} - check the internet connection "
                              f"(behind a proxy: set HTTPS_PROXY).") from e


def extract_tutorials(archive: Union[bytes, str, Path], target_dir: Union[str, Path],
                      overwrite: bool = False, sirgraf_dir: Optional[str] = None) -> Dict[str, List[Path]]:
    """
    Unpacks a tutorial archive into target_dir.

    :param archive: The zip archive: its content (bytes) or its path.
    :type archive: bytes | str | Path
    :param target_dir: Folder to unpack into (created if missing).
    :type target_dir: str | Path
    :param overwrite: Replace files that already exist. Default False: keep them - the tutorials change
        their models, and you may have changed the notebooks.
    :type overwrite: bool
    :param sirgraf_dir: SirGraf folder to set in the ``SIR3S_SIRGRAF_DIR`` line of the unpacked notebooks.
        Default None: leave the notebooks unchanged.
    :type sirgraf_dir: str, optional
    :return: {"written": [paths], "kept": [existing paths not replaced], "sirgraf_dir_set": [notebooks
        whose SIR3S_SIRGRAF_DIR was set]}
    :rtype: dict
    :raises ValueError: if an entry of the archive points outside target_dir (nothing is written then).
    """
    target = Path(target_dir).resolve()
    result: Dict[str, List[Path]] = {"written": [], "kept": [], "sirgraf_dir_set": []}
    source = io.BytesIO(archive) if isinstance(archive, bytes) else archive
    with zipfile.ZipFile(source) as zf:
        infos = zf.infolist()
        for info in infos:
            dest = (target / info.filename).resolve()
            if dest != target and target not in dest.parents:
                raise ValueError(f"Unsafe path in the tutorial archive: {info.filename!r} - nothing unpacked.")
        for info in infos:
            dest = (target / info.filename).resolve()
            if info.is_dir():
                dest.mkdir(parents=True, exist_ok=True)
                continue
            if dest.exists() and not overwrite:
                result["kept"].append(dest)
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            if sirgraf_dir and dest.suffix.lower() == ".ipynb":
                content, changed = set_sirgraf_dir_in_notebook(zf.read(info), sirgraf_dir)
                dest.write_bytes(content)
                if changed:
                    result["sirgraf_dir_set"].append(dest)
            else:
                with zf.open(info) as src, open(dest, "wb") as dst:
                    shutil.copyfileobj(src, dst)
            result["written"].append(dest)
    return result


def download_tutorials(target_dir: Union[str, Path] = DEFAULT_FOLDER, groups: Sequence[str] = ("core", "mantle"),
                       version: Optional[str] = None, overwrite: bool = False,
                       sirgraf_dir: Optional[str] = None) -> Dict[str, List[Path]]:
    """
    Downloads the tutorials (notebooks and the models they use) of a sir3stoolkit version from its
    GitHub release and unpacks them into target_dir: ``<target_dir>/SIR3S_Model/TutorialNNN_Assets``
    (core, tutorials 0-49) and ``<target_dir>/SIR3S_Model_Mantle/TutorialNNN_Assets`` (mantle, 50-99).
    Command line: ``python -m sir3stoolkit tutorials``.

    :param target_dir: Folder to unpack into (created if missing). Default: "sir3stoolkit_tutorials".
    :type target_dir: str | Path
    :param groups: Tutorial groups to download: "core" and/or "mantle". Default: both.
    :type groups: sequence of str
    :param version: sir3stoolkit version whose tutorials to download, e.g. "90.15.27". Default: the installed
        version - the tutorials then match its functions.
    :type version: str, optional
    :param overwrite: Replace files that already exist. Default False: keep them.
    :type overwrite: bool
    :param sirgraf_dir: SirGraf folder to set in the ``SIR3S_SIRGRAF_DIR`` line of the unpacked notebooks.
        Default None: the configured one (get_configured_sirgraf_dir()), if any; "" leaves the notebooks unchanged.
    :type sirgraf_dir: str, optional
    :return: {"written": [paths], "kept": [existing paths not replaced], "sirgraf_dir_set": [notebooks
        whose SIR3S_SIRGRAF_DIR was set]}
    :rtype: dict
    :raises ValueError: unknown group, unreleased version, or no tutorials published for the version.
    :raises ConnectionError: if the download fails.
    """
    if sirgraf_dir is None:
        sirgraf_dir = get_configured_sirgraf_dir()
    urls = []
    for group in groups:  # validates all groups and the version before anything is downloaded
        url = get_tutorials_url(group, version)
        urls.append((GROUPS[group][0], url))
    result: Dict[str, List[Path]] = {"written": [], "kept": [], "sirgraf_dir_set": []}
    for folder, url in urls:
        unpacked = extract_tutorials(_download(url), Path(target_dir) / folder, overwrite=overwrite,
                                     sirgraf_dir=sirgraf_dir)
        for key in result:
            result[key] += unpacked[key]
    return result
