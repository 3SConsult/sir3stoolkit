import io
import json
import urllib.error
import zipfile

import pytest

from sir3stoolkit import sirgraf_config, tutorials
from sir3stoolkit.__main__ import main as cli_main


def make_zip(entries):
    """entries: {name: content (str) or None for a directory entry}"""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        for name, content in entries.items():
            zf.writestr(name, "" if content is None else content)
    return buffer.getvalue()


ARCHIVES = {
    "Tutorials000-049_Assets.zip": make_zip({"Tutorial002_Assets/ToolkitTutorial002.ipynb": "nb2",
                                             "Tutorial002_Assets/Toolkit_Tutorial2_Model.db3": "model2",
                                             "Tutorial002_Assets/WDToolkit_Tutorial2_Model/": None}),
    "Tutorials050-099_Assets.zip": make_zip({"Tutorial051_Assets/ToolkitTutorial051.ipynb": "nb51",
                                             "Tutorial051_Assets/Network3.db3": "network3",
                                             "Tutorial051_Assets/WDNetwork3/": None}),
}


@pytest.fixture(autouse=True)
def no_sirgraf_config(monkeypatch, tmp_path_factory):
    """Isolates the tests from the SirGraf folder stored on the machine running them."""
    monkeypatch.setattr(sirgraf_config, "PACKAGE_DIR", tmp_path_factory.mktemp("package"))
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path_factory.mktemp("LocalAppData")))


@pytest.fixture
def downloads(monkeypatch):
    """Replaces the download by the archives above; returns the list of requested URLs."""
    urls = []

    def fake_download(url):
        urls.append(url)
        return ARCHIVES[url.rsplit("/", 1)[1]]
    monkeypatch.setattr(tutorials, "_download", fake_download)
    return urls


def test_url_points_at_the_release_of_the_version():
    assert tutorials.get_tutorials_url("mantle", "90.15.27") == \
        "https://github.com/3SConsult/sir3stoolkit/releases/download/v90.15.27/Tutorials050-099_Assets.zip"


def test_url_defaults_to_the_installed_version(monkeypatch):
    monkeypatch.setattr(tutorials, "_installed_version", lambda: "90.15.28")
    assert "/v90.15.28/Tutorials000-049_Assets.zip" in tutorials.get_tutorials_url("core")


def test_url_of_a_test_release():
    # test releases (.github/workflows/test-release.yml) have the version of pyproject.toml plus .devN
    assert tutorials.get_tutorials_url("core", "90.15.27.dev3").endswith("/v90.15.27.dev3/Tutorials000-049_Assets.zip")


@pytest.mark.parametrize("version", ["90.15.27+local", None])
def test_unreleased_version_is_rejected(monkeypatch, version):
    monkeypatch.setattr(tutorials, "_installed_version", lambda: version)
    with pytest.raises(ValueError, match="no published tutorials"):
        tutorials.get_tutorials_url("core")


def test_unknown_group_is_rejected():
    with pytest.raises(ValueError, match="Unknown tutorial group"):
        tutorials.get_tutorials_url("both", "90.15.27")


def test_download_unpacks_with_the_repository_layout(downloads, tmp_path):
    result = tutorials.download_tutorials(tmp_path, version="90.15.27")
    assert (tmp_path / "SIR3S_Model" / "Tutorial002_Assets" / "Toolkit_Tutorial2_Model.db3").read_text() == "model2"
    assert (tmp_path / "SIR3S_Model_Mantle" / "Tutorial051_Assets" / "Network3.db3").read_text() == "network3"
    assert (tmp_path / "SIR3S_Model_Mantle" / "Tutorial051_Assets" / "WDNetwork3").is_dir()  # empty working directory
    assert len(result["written"]) == 4 and result["kept"] == []
    assert [u.rsplit("/", 2)[1] for u in downloads] == ["v90.15.27", "v90.15.27"]


def test_only_one_group(downloads, tmp_path):
    tutorials.download_tutorials(tmp_path, groups=["mantle"], version="90.15.27")
    assert len(downloads) == 1 and not (tmp_path / "SIR3S_Model").exists()


def test_existing_files_are_kept_unless_overwrite(downloads, tmp_path):
    model = tmp_path / "SIR3S_Model_Mantle" / "Tutorial051_Assets" / "Network3.db3"
    model.parent.mkdir(parents=True)
    model.write_text("changed by the user")
    result = tutorials.download_tutorials(tmp_path, groups=["mantle"], version="90.15.27")
    assert model.read_text() == "changed by the user" and result["kept"] == [model.resolve()]
    tutorials.download_tutorials(tmp_path, groups=["mantle"], version="90.15.27", overwrite=True)
    assert model.read_text() == "network3"


def test_archive_entries_outside_the_target_are_refused(tmp_path):
    archive = make_zip({"Tutorial051_Assets/ok.txt": "ok", "../evil.txt": "evil"})
    with pytest.raises(ValueError, match="Unsafe path"):
        tutorials.extract_tutorials(archive, tmp_path / "target")
    assert not (tmp_path / "evil.txt").exists() and not (tmp_path / "target" / "Tutorial051_Assets" / "ok.txt").exists()


def test_missing_release_gives_a_clear_error(monkeypatch):
    def not_found(url, timeout):
        raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
    monkeypatch.setattr(tutorials.urllib.request, "urlopen", not_found)
    with pytest.raises(ValueError, match="No tutorials found"):
        tutorials._download("https://example.invalid/x.zip")


def test_cli(downloads, tmp_path, capsys):
    assert cli_main(["tutorials", str(tmp_path), "--only", "core", "--version", "90.15.27"]) == 0
    out = capsys.readouterr().out
    assert "1 file(s) written" not in out and "2 file(s) written" in out and "SIR3S_SIRGRAF_DIR" in out
    assert cli_main(["tutorials", str(tmp_path), "--only", "core", "--version", "90.15.27"]) == 0
    assert "existing file(s) kept" in capsys.readouterr().out


def test_cli_prints_the_target_before_downloading(monkeypatch, tmp_path, capsys):
    printed_before = []

    def fake_download(url):
        printed_before.append(capsys.readouterr().out)
        return ARCHIVES[url.rsplit("/", 1)[1]]
    monkeypatch.setattr(tutorials, "_download", fake_download)
    assert cli_main(["tutorials", str(tmp_path / "out"), "--only", "core", "--version", "90.15.27"]) == 0
    assert f"(release v90.15.27) into {(tmp_path / 'out').resolve()}" in printed_before[0]


def test_cli_write_error_gives_a_message_not_a_traceback(monkeypatch, downloads, tmp_path, capsys):
    def no_permission(*args, **kwargs):
        raise PermissionError(13, "Permission denied", str(tmp_path / "out" / "x.db3"))
    monkeypatch.setattr(tutorials, "download_tutorials", no_permission)
    assert cli_main(["tutorials", str(tmp_path / "out"), "--version", "90.15.27"]) == 1
    err = capsys.readouterr().err
    assert "Cannot write to" in err and "Permission denied" in err and "choose another folder" in err


def test_cli_unwritable_target_fails_before_downloading(monkeypatch, downloads, tmp_path, capsys):
    blocker = tmp_path / "file"
    blocker.write_text("not a folder")
    assert cli_main(["tutorials", str(blocker / "sub"), "--version", "90.15.27"]) == 1
    assert downloads == [] and "Cannot write to" in capsys.readouterr().err


def test_cli_error_exit_code(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(tutorials, "_installed_version", lambda: None)
    assert cli_main(["tutorials", str(tmp_path)]) == 1
    assert "no published tutorials" in capsys.readouterr().err


# --- SirGraf folder in the notebooks ----------------------------------------------------------------

MARKDOWN_LINE = r'SIR3S_SIRGRAF_DIR = r"C:\in\markdown"'


def notebook(*code_cells):
    nb = {"cells": [{"cell_type": "markdown", "metadata": {}, "source": [MARKDOWN_LINE]}]
          + [{"cell_type": "code", "metadata": {}, "outputs": [], "execution_count": None, "source": src}
             for src in code_cells],
          "metadata": {}, "nbformat": 4, "nbformat_minor": 5}
    return json.dumps(nb, indent=1).encode("utf-8")


def code_sources(content):
    return ["".join(c["source"]) if isinstance(c["source"], list) else c["source"]
            for c in json.loads(content)["cells"] if c["cell_type"] == "code"]


def test_sirgraf_dir_line_is_replaced_in_code_cells_only():
    original = notebook([r'SIR3S_SIRGRAF_DIR = r"C:\3S\SIR 3S\SirGraf-90-15-00-24_Quebec-Upd2" #change to local path'],
                        "from sir3stoolkit.core import wrapper\nwrapper.Initialize_Toolkit(SIR3S_SIRGRAF_DIR)")
    content, changed = tutorials.set_sirgraf_dir_in_notebook(original, "D:/SIR 3S/SirGraf-90-15-01")
    assert changed
    assert code_sources(content)[0] == \
        r'SIR3S_SIRGRAF_DIR = r"D:\SIR 3S\SirGraf-90-15-01"  # SirGraf folder from the sir3stoolkit config'
    assert code_sources(content)[1] == "from sir3stoolkit.core import wrapper\nwrapper.Initialize_Toolkit(SIR3S_SIRGRAF_DIR)"
    assert json.loads(content)["cells"][0]["source"] == [MARKDOWN_LINE]  # markdown untouched


def test_notebook_without_the_line_or_no_notebook_is_unchanged():
    original = notebook("print(1)")
    assert tutorials.set_sirgraf_dir_in_notebook(original, "D:/x") == (original, False)
    assert tutorials.set_sirgraf_dir_in_notebook(b"not json", "D:/x") == (b"not json", False)


def test_configured_sirgraf_dir(tmp_path):
    sirgraf, default = tmp_path / "SirGraf", tmp_path / "Default"
    sirgraf.mkdir()
    default.mkdir()
    assert tutorials.get_configured_sirgraf_dir() is None
    sirgraf_config.get_package_config_file().write_text(default.as_posix(), encoding="utf-8")  # shipped default
    assert tutorials.get_configured_sirgraf_dir() == str(default)
    user_file = sirgraf_config.get_user_config_file()
    user_file.parent.mkdir(parents=True)
    user_file.write_text(f"# comment\n\n{sirgraf.as_posix()}\n", encoding="utf-8")
    assert tutorials.get_configured_sirgraf_dir() == str(sirgraf)
    # the developer override takes precedence; a folder that does not exist is not used
    sirgraf_config.get_developer_config_file().write_text(str(tmp_path / "missing"), encoding="utf-8")
    assert tutorials.get_configured_sirgraf_dir() is None


def test_download_sets_the_configured_sirgraf_dir(monkeypatch, downloads, tmp_path):
    sirgraf = tmp_path / "SirGraf"
    sirgraf.mkdir()
    monkeypatch.setattr(tutorials, "get_configured_sirgraf_dir", lambda: str(sirgraf))
    nb = notebook([r'SIR3S_SIRGRAF_DIR = r"C:\x" #change to local path'])
    monkeypatch.setitem(ARCHIVES, "Tutorials050-099_Assets.zip", make_zip({"Tutorial051_Assets/ToolkitTutorial051.ipynb": nb}))
    result = tutorials.download_tutorials(tmp_path / "out", groups=["mantle"], version="90.15.27")
    path = tmp_path / "out" / "SIR3S_Model_Mantle" / "Tutorial051_Assets" / "ToolkitTutorial051.ipynb"
    assert result["sirgraf_dir_set"] == [path.resolve()]
    assert code_sources(path.read_bytes())[0].startswith(f'SIR3S_SIRGRAF_DIR = r"{sirgraf}"')
    tutorials.download_tutorials(tmp_path / "plain", groups=["mantle"], version="90.15.27", sirgraf_dir="")
    assert (tmp_path / "plain" / "SIR3S_Model_Mantle" / "Tutorial051_Assets" / "ToolkitTutorial051.ipynb").read_bytes() == nb


def test_cli_sirgraf_dir(monkeypatch, downloads, tmp_path, capsys):
    nb = notebook([r'SIR3S_SIRGRAF_DIR = r"C:\x"'])
    monkeypatch.setitem(ARCHIVES, "Tutorials050-099_Assets.zip", make_zip({"Tutorial051_Assets/ToolkitTutorial051.ipynb": nb}))
    assert cli_main(["tutorials", str(tmp_path / "out"), "--only", "mantle", "--version", "90.15.27",
                     "--sirgraf-dir", str(tmp_path)]) == 0
    assert f"SIR3S_SIRGRAF_DIR set to {tmp_path} in 1 notebook(s)" in capsys.readouterr().out
    assert cli_main(["tutorials", str(tmp_path / "out"), "--sirgraf-dir", str(tmp_path / "missing")]) == 1
    assert "SirGraf folder not found" in capsys.readouterr().err
