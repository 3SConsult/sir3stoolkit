# This file is part of PythonPluginTemplate.

"""
Resources (resolve SirGraf directory).

Author: Michael Fischer
"""

# General modules
import logging
logging.info("Enter resources.")

from pathlib import Path


class SirGrafResolveError(RuntimeError):
    pass


def has_required_dlls(sirgraf_dir):
    """Minimal check for expected dlls in SirGraf directory.

    Parameters
    ----------
    sirgraf_dir : Path
        SirGraf path.

    Returns
    -------
    exist : bool
        Dlls exist.
    """

    required = [
        "Sir3S_Repository.ModelManager.dll",
        "Sir3S_Repository.Utilities.dll",
        "Sir3S_Repository.Interfaces.dll",
    ]

    return all((sirgraf_dir / name).exists() for name in required)


def find_unique_sirgraf_under(root, validate=True):
    """Search for unique dir starting with 'SirGraf', else Exception.

    Parameters
    ----------
    root : Path
        Base path (here: a dir starting with 'SirGraf' is searched for).
    validate : bool
        Validate for SirGraf dlls.

    Returns
    -------
    sirgraf : Path
        SirGraf path.
    """

    if not root.exists():
        raise SirGrafResolveError(f"Base dir not found: {root}")

    cands = (
        p for p in root.iterdir()
        if p.is_dir() and p.name.lower().startswith("sirgraf")
    )
    candidates = sorted(cands)
    if len(candidates) == 0:
        raise SirGrafResolveError(f"No 'SirGraf*'-dir under: {root}")
    if len(candidates) > 1:
        names = ", ".join(p.name for p in candidates)
        raise SirGrafResolveError(f"Multiple 'SirGraf*'-dirs under {root}: {names} (not unique).")

    sirgraf_dir = candidates[0]
    if validate and not has_required_dlls(sirgraf_dir):
        raise SirGrafResolveError(f"Found SirGraf-dir, but appears to be incomplete: {sirgraf_dir}")

    return sirgraf_dir


def resolve_sirgraf_dir(explicit=None, plugin_dir=None, validate=True):
    """Resolve path to SirGraf directory according to rules (hierarchy):

      1) If set 'explicit' (e.g. via config/ENV), then use this path (validation optional).
         If 'explicit' is empty string or None: proceed with (2).
      2) Plugin under '...\\SirGraf-...\\Plugins\\<PluginName>', then two levels up, this is the SirGraf dir.
      3) Plugin under '...\\Common\\Plugins\\<PluginName>', then two levels up to '<root>'and search for
         *exactly one* 'SirGraf*'.
      4) If everything fails: Exception.

    Parameters
    ----------
    explicit : str
        Explicit path.
    plugin_dir : Path
        Plugin path.
    validate : bool
        Validate for SirGraf dlls.

    Returns
    -------
    sirgraf : Path
        SirGraf path.
    """

    # 1) explicit
    if explicit:
        sirgraf_dir = Path(explicit).resolve()
        if not sirgraf_dir.exists():
            raise SirGrafResolveError(f"Explicit path does not exist: {sirgraf_dir}")
        if validate and not has_required_dlls(sirgraf_dir):
            raise SirGrafResolveError(f"Explicit path appears to be no valid SirGraf installation: {sirgraf_dir}")
        return sirgraf_dir

    # 2) Plugin under '...\\SirGraf-...\\Plugins\\<PluginName>'
    parent = plugin_dir.parent
    if parent.name.lower() == "plugins":
        cand = parent.parent.parent
        if cand.name.lower().startswith("sirgraf"):
            if not cand.exists():
                raise SirGrafResolveError(f"Expected SirGraf path does not exist: {cand}")
            if validate and not has_required_dlls(cand):
                raise SirGrafResolveError(f"Found SirGraf path (from Plugins), but invalid: {cand}")
            return cand

    # 3) Plugin under '...\\Common\\Plugins\\<PluginName>'
    if parent.name.lower() == "plugins" and parent.parent.name.lower() == "common":
        root = parent.parent.parent  # ...\SIR3S
        return find_unique_sirgraf_under(root, validate=validate)

    # 4) Everything fails
    raise SirGrafResolveError("SirGraf path could not be resolved. Set 'explicit' or check installation.")
