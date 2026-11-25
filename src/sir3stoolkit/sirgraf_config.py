# -*- coding: utf-8 -*-
"""
Where sir3stoolkit stores the SirGraf folder, so that ``wrapper.Initialize_Toolkit()`` works without a path.

``wrapper.Write_SirGraf_Config_Path()`` stores it in a per-user file outside the package,
``%LOCALAPPDATA%\\sir3stoolkit\\config.txt`` - it is kept when sir3stoolkit is updated or reinstalled
and applies to every Python environment of the Windows user on this computer. Only if that file cannot be
written, the path is written to ``config.txt`` in the package folder, which every update replaces. (Up to
version 90.15.26 the path was always written there.)

Files read, first usable one wins (first non-empty line that is no ``#`` comment):

1. ``config.local.txt`` in the package folder - developer override for editable installs (git-ignored).
2. ``%LOCALAPPDATA%\\sir3stoolkit\\config.txt`` - the per-user file.
3. ``config.txt`` in the package folder - shipped with the package, preset to the default SirGraf
   installation folder.

Plain Python, no .NET: also used where the .NET-based wrapper is not loaded (``python -m sir3stoolkit tutorials``).
"""

import os
from pathlib import Path
from typing import List, Optional, Tuple

PACKAGE_DIR = Path(__file__).resolve().parent


def get_developer_config_file() -> Path:
    """
    :return: ``config.local.txt`` in the package folder (developer override, read first).
    :rtype: Path
    """
    return PACKAGE_DIR / "config.local.txt"


def get_user_config_file() -> Path:
    """
    :return: The per-user config file: ``%LOCALAPPDATA%\\sir3stoolkit\\config.txt`` (machine-specific, like
        the SirGraf installation; without LOCALAPPDATA: ``~/AppData/Local/sir3stoolkit/config.txt``).
    :rtype: Path
    """
    local_app_data = os.environ.get("LOCALAPPDATA")
    base = Path(local_app_data) if local_app_data else Path.home() / "AppData" / "Local"
    return base / "sir3stoolkit" / "config.txt"


def get_package_config_file() -> Path:
    """
    :return: ``config.txt`` in the package folder (shipped with the package, read last; replaced by every update).
    :rtype: Path
    """
    return PACKAGE_DIR / "config.txt"


def get_config_files() -> List[Path]:
    """
    :return: The config files in the order they are read: developer override, per-user file, package file.
    :rtype: list[Path]
    """
    return [get_developer_config_file(), get_user_config_file(), get_package_config_file()]


def read_path_from_file(config_file: Path) -> Optional[str]:
    """
    :param config_file: A config file.
    :type config_file: Path
    :return: Its first non-empty line that is no ``#`` comment, or None (also if the file cannot be read).
    :rtype: str, optional
    """
    try:
        lines = Path(config_file).read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            return line
    return None


def read_configured_path() -> Tuple[Optional[str], Optional[Path]]:
    """
    Reads the stored SirGraf folder (not checked for existence).

    :return: (path, config file it was read from), or (None, None) if none is stored.
    :rtype: tuple
    """
    for config_file in get_config_files():
        path = read_path_from_file(config_file)
        if path is not None:
            return path, config_file
    return None, None


def write_configured_path(path: str) -> Path:
    """
    Stores the SirGraf folder (normalized to forward slashes): in ``config.local.txt`` if that developer
    override exists, otherwise in the per-user file (its folder is created if missing) - and only if that
    cannot be written, in ``config.txt`` in the package folder.

    :param path: The SirGraf folder.
    :type path: str
    :return: The config file written.
    :rtype: Path
    :raises OSError: if no config file can be written.
    """
    content = Path(path).as_posix() + "\n"
    developer_file = get_developer_config_file()
    if developer_file.exists():
        developer_file.write_text(content, encoding="utf-8")
        return developer_file
    user_file = get_user_config_file()
    try:
        user_file.parent.mkdir(parents=True, exist_ok=True)
        user_file.write_text(content, encoding="utf-8")
        return user_file
    except OSError:
        package_file = get_package_config_file()
        package_file.write_text(content, encoding="utf-8")
        return package_file
