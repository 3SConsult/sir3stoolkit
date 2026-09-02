# -*- coding: utf-8 -*-
"""
Shared helper for sir3stoolkit's optional ("mantle") third-party dependencies.

Each sir3stoolkit.mantle module calls require_packages() with its own actual requirements as the
first thing it does (before any of the third-party imports it's checking for), so a missing package
surfaces as one clear, actionable message naming exactly what's missing and how to install it -
instead of a raw ModuleNotFoundError/ImportError traceback from wherever inside that package's own
import machinery it happened to fail.

@author: Jablonski
"""
import importlib.util


def require_packages(module_name: str, *package_names: str) -> None:
    """
    Verify each of ``package_names`` is importable, and raise one combined ImportError naming every
    missing one if any are missing.

    Uses importlib.util.find_spec() rather than actually importing each package - cheap (no module
    code executes) and side-effect-free, so calling this before the real imports below it doesn't
    do any of that work twice.

    :param module_name: The calling module's ``__name__``, used in the error message so the user
                    knows which part of sir3stoolkit needs the missing package(s).
    :type module_name: str
    :param package_names: Top-level import names to check (e.g. "pandas", "geopandas"). Assumed to
                    match their PyPI/pip distribution name - true for every package sir3stoolkit's
                    "mantle" extra currently uses.
    :type package_names: str
    :raises ImportError: If any of package_names is not importable.
    """
    missing = [name for name in package_names if importlib.util.find_spec(name) is None]
    if missing:
        raise ImportError(
            f"{module_name} requires the following package(s), which are not installed: "
            f"{', '.join(missing)}. Install them via `pip install \"sir3stoolkit[mantle]\"` "
            f"(recommended - installs everything the mantle subpackage needs), or individually via "
            f"`pip install {' '.join(missing)}`."
        )
