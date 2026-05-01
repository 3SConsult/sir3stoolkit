from pathlib import Path

import pytest

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


def test_resolve_base_path_reads_config_local_when_host_absent(monkeypatch, tmp_path):
	package_root = tmp_path / "sir3stoolkit"
	core_dir = package_root / "core"
	core_dir.mkdir(parents=True)

	config_local = package_root / "config.local.txt"
	sirgraf_dir = tmp_path / "configured_sirgraf"
	sirgraf_dir.mkdir()
	config_local.write_text(str(sirgraf_dir), encoding="utf-8")

	monkeypatch.setattr(wrapper, "_read_base_path_from_host_app", lambda: None)
	monkeypatch.setattr(wrapper, "__file__", str(core_dir / "wrapper.py"))

	result = wrapper._resolve_base_path(None)

	assert result == str(sirgraf_dir)


def test_resolve_base_path_raises_for_missing_explicit_dir(tmp_path):
	missing_path = tmp_path / "does_not_exist"

	with pytest.raises(FileNotFoundError, match="Provided SirGraf path"):
		wrapper._resolve_base_path(str(missing_path))


def test_initialize_toolkit_raises_when_path_cannot_be_resolved(monkeypatch):
	monkeypatch.setattr(wrapper, "_resolve_base_path", lambda _: None)

	with pytest.raises(RuntimeError, match="no valid path could be resolved"):
		wrapper.Initialize_Toolkit(None)


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
