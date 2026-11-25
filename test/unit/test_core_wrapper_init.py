from pathlib import Path

import pytest

from sir3stoolkit import sirgraf_config
from sir3stoolkit.core import wrapper

def test_read_base_path_from_config_returns_first_usable_line(tmp_path):
	config_file = tmp_path / "config.txt"
	config_file.write_text("\n# comment\n  C:\\3S\\SirGraf\n", encoding="utf-8")

	result = wrapper._read_base_path_from_config(config_file)

	assert result == r"C:\3S\SirGraf"


def test_resolve_base_path_uses_explicit_input(tmp_path):
	explicit_dir = tmp_path / "sirgraf"
	explicit_dir.mkdir()

	result = wrapper._resolve_base_path(str(explicit_dir))

	assert result == str(explicit_dir)


def test_resolve_base_path_uses_host_app_when_no_explicit(monkeypatch, tmp_path):
	host_dir = tmp_path / "host_sirgraf"
	host_dir.mkdir()

	monkeypatch.setattr(wrapper, "_read_base_path_from_host_app", lambda: str(host_dir))

	result = wrapper._resolve_base_path(None)

	assert result == str(host_dir)


def test_resolve_base_path_raises_for_missing_explicit_dir(tmp_path):
	missing_path = tmp_path / "does_not_exist"

	with pytest.raises(FileNotFoundError, match="Provided SirGraf path"):
		wrapper._resolve_base_path(str(missing_path))


def test_initialize_toolkit_raises_when_path_cannot_be_resolved(monkeypatch):
	monkeypatch.setattr(wrapper, "_resolve_base_path", lambda _: None)

	with pytest.raises(RuntimeError, match="none stored") as raised:
		wrapper.Initialize_Toolkit(None)
	# explains where the path is stored and that one stored with an older version has to be stored once more
	assert str(sirgraf_config.get_user_config_file()) in str(raised.value)
	assert "store it once more" in str(raised.value)


def test_initialize_toolkit_sets_globals_and_adds_references(monkeypatch, tmp_path):
	resolved_dir = tmp_path / "sirgraf"
	resolved_dir.mkdir()
	add_reference_calls = []

	monkeypatch.setattr(wrapper, "_resolve_base_path", lambda _: str(resolved_dir))
	monkeypatch.setattr(wrapper.net, "AddReference", add_reference_calls.append)
	monkeypatch.setattr(wrapper.sys, "path", [])

	wrapper.Initialize_Toolkit(None)

	assert wrapper.SIR3S_SIRGRAF_DIR == str(resolved_dir)
	assert str(resolved_dir) in wrapper.sys.path
	assert add_reference_calls == [
		"System",
		str(Path(resolved_dir) / "Sir3S_Repository.Utilities"),
		str(Path(resolved_dir) / "Sir3S_Toolkit"),
	]


@pytest.fixture
def config_dirs(monkeypatch, tmp_path):
	"""Package folder and per-user config file of the test (instead of the real ones)."""
	package_dir = tmp_path / "sir3stoolkit"
	package_dir.mkdir()
	monkeypatch.setattr(sirgraf_config, "PACKAGE_DIR", package_dir)
	monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "LocalAppData"))
	monkeypatch.setattr(wrapper, "_read_base_path_from_host_app", lambda: None)
	return package_dir / "config.local.txt", tmp_path / "LocalAppData" / "sir3stoolkit" / "config.txt"


def make_dir(tmp_path, name):
	path = tmp_path / name
	path.mkdir()
	return path


def test_user_config_file_is_outside_the_package_in_local_app_data(config_dirs):
	_, user_file = config_dirs
	assert sirgraf_config.get_user_config_file() == user_file
	assert sirgraf_config.PACKAGE_DIR not in user_file.parents


def test_resolve_base_path_reads_config_local_when_host_absent(config_dirs, tmp_path):
	local_file, _ = config_dirs
	sirgraf_dir = make_dir(tmp_path, "configured_sirgraf")
	local_file.write_text(str(sirgraf_dir), encoding="utf-8")

	assert wrapper._resolve_base_path(None) == str(sirgraf_dir)


def test_resolve_base_path_reads_the_user_config(config_dirs, tmp_path):
	_, user_file = config_dirs
	sirgraf_dir = make_dir(tmp_path, "configured_sirgraf")
	user_file.parent.mkdir(parents=True)
	user_file.write_text(sirgraf_dir.as_posix(), encoding="utf-8")

	assert wrapper._resolve_base_path(None) == sirgraf_dir.as_posix()


def test_read_sirgraf_config_path_returns_none_when_no_config_files(config_dirs):
	assert wrapper.Read_SirGraf_Config_Path() is None


def test_read_sirgraf_config_path_prefers_config_local_over_user_config(config_dirs, tmp_path):
	local_file, user_file = config_dirs
	local_dir = make_dir(tmp_path, "local_sirgraf")
	local_file.write_text(str(local_dir), encoding="utf-8")
	user_file.parent.mkdir(parents=True)
	user_file.write_text(str(make_dir(tmp_path, "other_sirgraf")), encoding="utf-8")

	assert wrapper.Read_SirGraf_Config_Path() == str(local_dir)


def test_read_sirgraf_config_path_raises_for_missing_configured_dir(config_dirs, tmp_path):
	_, user_file = config_dirs
	user_file.parent.mkdir(parents=True)
	user_file.write_text(str(tmp_path / "does_not_exist"), encoding="utf-8")

	with pytest.raises(FileNotFoundError, match="SirGraf path from config"):
		wrapper.Read_SirGraf_Config_Path()


def test_write_sirgraf_config_path_raises_for_missing_dir(tmp_path):
	missing_path = tmp_path / "does_not_exist"

	with pytest.raises(FileNotFoundError, match="Provided SirGraf path"):
		wrapper.Write_SirGraf_Config_Path(str(missing_path))


def test_write_sirgraf_config_path_writes_the_user_config(config_dirs, tmp_path):
	local_file, user_file = config_dirs
	sirgraf_dir = make_dir(tmp_path, "sirgraf")

	wrapper.Write_SirGraf_Config_Path(str(sirgraf_dir))

	# outside the package: kept when sir3stoolkit is updated
	assert user_file.read_text(encoding="utf-8").strip() == Path(str(sirgraf_dir)).as_posix()
	assert not local_file.exists() and list(sirgraf_config.PACKAGE_DIR.iterdir()) == []
	assert wrapper.Read_SirGraf_Config_Path() == Path(str(sirgraf_dir)).as_posix()


def test_write_sirgraf_config_path_prefers_config_local_when_present(config_dirs, tmp_path):
	local_file, user_file = config_dirs
	local_file.write_text("placeholder", encoding="utf-8")
	sirgraf_dir = make_dir(tmp_path, "sirgraf")

	wrapper.Write_SirGraf_Config_Path(str(sirgraf_dir))

	assert local_file.read_text(encoding="utf-8").strip() == Path(str(sirgraf_dir)).as_posix()
	assert not user_file.exists()


def test_write_sirgraf_config_path_normalizes_backslashes(config_dirs, tmp_path):
	_, user_file = config_dirs

	wrapper.Write_SirGraf_Config_Path(str(make_dir(tmp_path, "sirgraf")))

	assert "\\" not in user_file.read_text(encoding="utf-8")


def test_write_sirgraf_config_path_explains_when_it_cannot_write(config_dirs, monkeypatch, tmp_path):
	def no_permission(path):
		raise PermissionError(13, "Permission denied")
	monkeypatch.setattr(sirgraf_config, "write_configured_path", no_permission)

	with pytest.raises(wrapper.SIR3S_ToolkitError, match="Pass it to Initialize_Toolkit"):
		wrapper.Write_SirGraf_Config_Path(str(make_dir(tmp_path, "sirgraf")))


def test_read_sirgraf_config_path_falls_back_to_the_package_config(config_dirs, tmp_path):
	shipped_dir = make_dir(tmp_path, "default_sirgraf")
	sirgraf_config.get_package_config_file().write_text(shipped_dir.as_posix(), encoding="utf-8")

	assert wrapper.Read_SirGraf_Config_Path() == shipped_dir.as_posix()


def test_read_sirgraf_config_path_prefers_the_user_config_over_the_package_config(config_dirs, tmp_path):
	_, user_file = config_dirs
	sirgraf_config.get_package_config_file().write_text(str(make_dir(tmp_path, "default_sirgraf")), encoding="utf-8")
	user_dir = make_dir(tmp_path, "user_sirgraf")
	user_file.parent.mkdir(parents=True)
	user_file.write_text(str(user_dir), encoding="utf-8")

	assert wrapper.Read_SirGraf_Config_Path() == str(user_dir)


def test_missing_shipped_default_explains_how_to_store_the_path(config_dirs, tmp_path):
	sirgraf_config.get_package_config_file().write_text(str(tmp_path / "not_installed_here"), encoding="utf-8")

	with pytest.raises(FileNotFoundError, match="store it once with Write_SirGraf_Config_Path"):
		wrapper.Read_SirGraf_Config_Path()


def test_write_sirgraf_config_path_falls_back_to_the_package_config(config_dirs, monkeypatch, tmp_path):
	blocker = tmp_path / "not_a_folder"
	blocker.write_text("x", encoding="utf-8")
	monkeypatch.setattr(sirgraf_config, "get_user_config_file", lambda: blocker / "sir3stoolkit" / "config.txt")
	sirgraf_dir = make_dir(tmp_path, "sirgraf")

	wrapper.Write_SirGraf_Config_Path(str(sirgraf_dir))

	assert sirgraf_config.get_package_config_file().read_text(encoding="utf-8").strip() == sirgraf_dir.as_posix()
	assert wrapper.Read_SirGraf_Config_Path() == sirgraf_dir.as_posix()
