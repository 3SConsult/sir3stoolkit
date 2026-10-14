from types import SimpleNamespace

import pytest

from sir3stoolkit.core import wrapper


@pytest.fixture(autouse=True)
def _reset_raise_on_error():
	wrapper.Set_Raise_On_Error(None)
	yield
	wrapper.Set_Raise_On_Error(None)
	wrapper._soft_error_depth = 0


@pytest.fixture
def standalone(monkeypatch):
	monkeypatch.setattr(wrapper, "is_host_process", lambda: False)


@pytest.fixture
def in_sirgraf(monkeypatch):
	monkeypatch.setattr(wrapper, "is_host_process", lambda: True)


def test_error_raises_outside_sirgraf(standalone):
	with pytest.raises(wrapper.SIR3S_ToolkitError, match="Property not defined"):
		wrapper._log_message("Error: Property not defined on provided Element Type.")


@pytest.mark.parametrize("message", ["Error : x", "Error while opening the model, x", "Could not start Model Calculation: x"])
def test_all_error_prefixes_raise(standalone, message):
	with pytest.raises(wrapper.SIR3S_ToolkitError):
		wrapper._log_message(message)


def test_explicit_error_level_raises(standalone):
	with pytest.raises(wrapper.SIR3S_ToolkitError):
		wrapper._log_message("[Model Class Initialization] Error in initializing the toolkit", level="error")


@pytest.mark.parametrize("message, level", [("Value is set", None), ("Warning: x", None), ("x", "warning"), ("x", "info")])
def test_non_errors_do_not_raise(standalone, message, level):
	wrapper._log_message(message, level=level)


def test_error_only_logged_inside_sirgraf(in_sirgraf):
	wrapper._log_message("Error: x")


def test_set_raise_on_error_overrides_host_detection(standalone, monkeypatch):
	wrapper.Set_Raise_On_Error(False)
	wrapper._log_message("Error: x")

	monkeypatch.setattr(wrapper, "is_host_process", lambda: True)
	wrapper.Set_Raise_On_Error(True)
	with pytest.raises(wrapper.SIR3S_ToolkitError):
		wrapper._log_message("Error: x")


def _subclass_in_module(module_name):
	def method(self):
		wrapper._log_message("Error: x")
		return "done"

	return type("Sub", (wrapper.SIR3S_Model,), {"__module__": module_name, "method": method})


def test_core_errors_inside_mantle_methods_are_only_logged(standalone):
	cls = _subclass_in_module("sir3stoolkit.mantle.fake")
	assert cls.__new__(cls).method() == "done"
	assert wrapper._soft_error_depth == 0


def test_core_errors_inside_user_subclasses_raise(standalone):
	cls = _subclass_in_module("my_project.models")
	with pytest.raises(wrapper.SIR3S_ToolkitError):
		cls.__new__(cls).method()


def test_soft_error_depth_restored_after_exception():
	@wrapper._soft_errors
	def failing():
		raise ValueError("boom")

	with pytest.raises(ValueError):
		failing()
	assert wrapper._soft_error_depth == 0


STAT = "2026-04-29 14:10:00.000 +02:00"
END = "2026-04-29 14:30:00.000 +02:00"


def _model_with_calc_result(tmp_path, exit_status_stat="0", exit_status_last="0", timestamps=(STAT, END),
							calc_type="LowFreq", termination_time=1200.0, lock_file=False, executed=True):
	model = wrapper.SIR3S_Model.__new__(wrapper.SIR3S_Model)
	model.outputComments = True
	timestamp_stat = STAT if calc_type != "LoopForLoadingCondition" else ""
	model.toolkit = SimpleNamespace(
		ExecCalculation=lambda wait: (executed, "" if executed else "no license"),
		GetTimeStamps=lambda: (list(timestamps), "", timestamp_stat if timestamps else "", "", ""),
	)
	model.ObjectTypes = SimpleNamespace(GeneralSection="GeneralSection")
	model.GetWorkingDirectory = lambda: str(tmp_path)
	model.GetTksofElementType = lambda element_type: ["4711"]
	model.GetCalculationType = lambda: calc_type
	model.GetSimulationTimeFrame = lambda: (6.0, termination_time)
	model.GetResultfortimestamp = lambda t, tk, prop: (exit_status_stat if t == STAT else exit_status_last, "int")
	if lock_file:
		bz = tmp_path / "B1" / "V0" / "BZ1"
		bz.mkdir(parents=True)
		(bz / "M-1-0-1_SirCalcIsRunning.tmp").write_text("SirCalc\n")
	return model


def _calculate(model):
	model.ExecCalculation(waitForSirCalcToExit=True)


@pytest.mark.parametrize("stat, last", [("0", "0"), ("0", "1"), ("0", "2"), ("2", "0"), ("100", "101")])
def test_exec_calculation_accepts_usable_status(standalone, tmp_path, stat, last):
	_calculate(_model_with_calc_result(tmp_path, stat, last))


@pytest.mark.parametrize("stat, last", [("0", "3"), ("3", "0"), ("0", "")])
def test_exec_calculation_raises_on_bad_status_at_stationary_or_last_timestamp(standalone, tmp_path, stat, last):
	with pytest.raises(wrapper.SIR3S_ToolkitError, match="bad or invalid"):
		_calculate(_model_with_calc_result(tmp_path, stat, last))


def test_exec_calculation_warns_on_questionable_transient_results(standalone, tmp_path, caplog):
	_calculate(_model_with_calc_result(tmp_path, "0", "2"))
	assert f"EXSTAT=2 at {END}" in caplog.text


def test_exec_calculation_raises_on_lock_file(standalone, tmp_path):
	with pytest.raises(wrapper.SIR3S_ToolkitError, match="SirCalcIsRunning.tmp"):
		_calculate(_model_with_calc_result(tmp_path, lock_file=True))


def test_exec_calculation_raises_without_results(standalone, tmp_path):
	with pytest.raises(wrapper.SIR3S_ToolkitError, match="no results"):
		_calculate(_model_with_calc_result(tmp_path, timestamps=()))


def test_exec_calculation_raises_on_results_ending_early(standalone, tmp_path):
	# SirCalc crashed during the transient calculation: only the stationary timestamp, with EXSTAT=0
	with pytest.raises(wrapper.SIR3S_ToolkitError, match="1200 s before the end"):
		_calculate(_model_with_calc_result(tmp_path, timestamps=(STAT,)))


@pytest.mark.parametrize("calc_type", ["SteadyState", "LoopForLoadingCondition"])
def test_exec_calculation_skips_time_frame_check_for_non_transient_types(standalone, tmp_path, calc_type):
	_calculate(_model_with_calc_result(tmp_path, timestamps=(STAT,), calc_type=calc_type))


def test_exec_calculation_without_wait_skips_status_check(standalone, tmp_path):
	_model_with_calc_result(tmp_path, timestamps=(), lock_file=True).ExecCalculation(waitForSirCalcToExit=False)


def test_exec_calculation_raises_when_not_started(standalone, tmp_path):
	with pytest.raises(wrapper.SIR3S_ToolkitError, match="no license"):
		_calculate(_model_with_calc_result(tmp_path, executed=False))


def test_parse_timestamp():
	assert (wrapper._parse_timestamp(END) - wrapper._parse_timestamp(STAT)).total_seconds() == 1200
