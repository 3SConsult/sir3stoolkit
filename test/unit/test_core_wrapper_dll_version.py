import logging
import shutil
from pathlib import Path

from sir3stoolkit.core import wrapper

LIB = Path(wrapper.__file__).resolve().parents[1] / "lib"


def test_file_version_of_versioned_and_unversioned_dll():
    assert wrapper.Get_Toolkit_Dll_File_Version(str(LIB / "90-15-26" / "Sir3S_Toolkit.dll")) == "90.15.10.0"
    assert wrapper.Get_Toolkit_Dll_File_Version(str(LIB / "90-15-25")) == "1.0.0.0"  # directory, DLL before 90.15.26


def test_file_version_missing_dll_returns_none(tmp_path):
    assert wrapper.Get_Toolkit_Dll_File_Version(str(tmp_path)) is None


def test_file_version_defaults_to_sirgraf_dir(monkeypatch):
    monkeypatch.setattr(wrapper, "SIR3S_SIRGRAF_DIR", str(LIB / "90-15-26"))
    assert wrapper.Get_Toolkit_Dll_File_Version() == "90.15.10.0"


def test_bundled_dll_is_newest_lib_folder():
    folders = sorted((p.parent.name for p in LIB.glob("*/Sir3S_Toolkit.dll")),
                     key=lambda name: tuple(int(x) for x in name.split("-")))
    assert Path(wrapper._bundled_toolkit_dll_path()).parent.name == folders[-1]


def _sirgraf_dir(tmp_path, lib_folder):
    sirgraf = tmp_path / "sirgraf"
    sirgraf.mkdir()
    shutil.copy2(LIB / lib_folder / "Sir3S_Toolkit.dll", sirgraf / "Sir3S_Toolkit.dll")
    return str(sirgraf)


def test_check_warns_for_older_dll(monkeypatch, tmp_path, caplog):
    monkeypatch.setattr(wrapper, "_bundled_toolkit_dll_path", lambda: str(LIB / "90-15-26" / "Sir3S_Toolkit.dll"))
    with caplog.at_level(logging.INFO):
        wrapper._check_toolkit_dll_version(_sirgraf_dir(tmp_path, "90-15-25"))
    warnings = [r.getMessage() for r in caplog.records if r.levelno == logging.WARNING]
    assert len(warnings) == 1 and "1.0.0.0" in warnings[0] and "needs 90.15.10.0" in warnings[0]


def test_check_warns_for_newer_dll(monkeypatch, tmp_path, caplog):
    monkeypatch.setattr(wrapper, "_bundled_toolkit_dll_path", lambda: str(LIB / "90-15-25" / "Sir3S_Toolkit.dll"))
    with caplog.at_level(logging.INFO):
        wrapper._check_toolkit_dll_version(_sirgraf_dir(tmp_path, "90-15-26"))
    assert "newer than 1.0.0.0" in caplog.text


def test_check_logs_match_and_skips_missing_dll(monkeypatch, tmp_path, caplog):
    monkeypatch.setattr(wrapper, "_bundled_toolkit_dll_path", lambda: str(LIB / "90-15-26" / "Sir3S_Toolkit.dll"))
    with caplog.at_level(logging.INFO):
        wrapper._check_toolkit_dll_version(_sirgraf_dir(tmp_path, "90-15-26"))
        wrapper._check_toolkit_dll_version(str(tmp_path / "no_sirgraf"))  # no DLL: nothing logged, no error
    assert [r.levelno for r in caplog.records] == [logging.INFO]
    assert "90.15.10.0 (matches" in caplog.text
