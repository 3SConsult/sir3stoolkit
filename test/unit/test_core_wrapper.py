from pathlib import Path

import pytest

from sir3stoolkit.core import wrapper

# Init
"""
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

	with pytest.raises(FileNotFoundError):
		wrapper._resolve_base_path(str(missing_path))


def test_initialize_toolkit_raises_when_path_cannot_be_resolved(monkeypatch):
	monkeypatch.setattr(wrapper, "_resolve_base_path", lambda _: None)

	with pytest.raises(RuntimeError):
		wrapper.Initialize_Toolkit(None)


def test_initialize_toolkit_sets_globals_and_adds_references(monkeypatch, tmp_path):
	resolved_dir = tmp_path / "sirgraf"
	resolved_dir.mkdir()

	calls = []

	def fake_add_reference(value):
		calls.append(value)

	monkeypatch.setattr(wrapper, "_resolve_base_path", lambda _: str(resolved_dir))
	monkeypatch.setattr(wrapper.net, "AddReference", fake_add_reference)

	wrapper.Initialize_Toolkit(None)

	assert wrapper.SIR3S_SIRGRAF_DIR == str(resolved_dir)
	assert str(resolved_dir) in wrapper.sys.path
	assert calls[0] == "System"
	assert calls[1] == str(Path(resolved_dir) / "Sir3S_Repository.Utilities")
	assert calls[2] == str(Path(resolved_dir) / "Sir3S_Toolkit")


def test_start_transaction_prints_default_success_message(opened_model, capsys):
	model = opened_model["model class instance"]
	toolkit = opened_model["toolkit"]

	model.outputComments = True
	model.StartTransaction("unit-test")

	output = capsys.readouterr().out
	assert "Now you can make changes to the model" in output
	assert toolkit.start_transaction_calls[-1] == "unit-test"


def test_end_transaction_prints_error_message_on_failure(opened_model, capsys):
	model = opened_model["model class instance"]

	model.EndTransaction()

	output = capsys.readouterr().out
	assert "No open transaction" in output


def test_open_model_calls_toolkit_with_converted_provider_and_prints_success(opened_model):
	params = opened_model["params"]
	toolkit = opened_model["toolkit"]

	assert len(toolkit.open_model_calls) == 1
	assert toolkit.open_model_calls[0] == (
		params["db_name"],
		"dotnet:SQLITE",
		params["mid"],
		params["save_currently_open_model"],
		params["named_instance"],
		params["user_id"],
		params["password"],
	)



def test_get_value(opened_model):
	model = opened_model["model class instance"]

	
"""