import io
import logging

import pytest

from sir3stoolkit import logging_utils


@pytest.fixture(autouse=True)
def _restore_root_logger_state():
    """Keep root logger state isolated across tests."""
    root_logger = logging.getLogger()
    original_handlers = list(root_logger.handlers)
    original_level = root_logger.level

    yield

    root_logger.handlers[:] = original_handlers
    root_logger.setLevel(original_level)


def _setup_clean_logger(name: str):
    logger = logging.getLogger(name)
    original_handlers = list(logger.handlers)
    original_level = logger.level
    original_propagate = logger.propagate

    logger.handlers[:] = []
    logger.setLevel(logging.NOTSET)
    logger.propagate = False

    return logger, original_handlers, original_level, original_propagate


def _restore_logger(logger, original_handlers, original_level, original_propagate):
    logger.handlers[:] = original_handlers
    logger.setLevel(original_level)
    logger.propagate = original_propagate


def test_get_logger_attaches_fallback_only_once():
    logger_name = "sir3stoolkit.tests.logging.single_fallback"
    logger, original_handlers, original_level, original_propagate = _setup_clean_logger(logger_name)

    try:
        logging_utils.get_logger(logger_name)
        logging_utils.get_logger(logger_name)

        fallback_handlers = [
            handler
            for handler in logger.handlers
            if isinstance(handler, logging_utils._HostAwarePrintFallbackHandler)
        ]
        assert len(fallback_handlers) == 1
    finally:
        _restore_logger(logger, original_handlers, original_level, original_propagate)


def test_fallback_prints_when_host_and_no_external_handlers(monkeypatch, capsys):
    logger_name = "sir3stoolkit.tests.logging.host_print"
    logger, original_handlers, original_level, original_propagate = _setup_clean_logger(logger_name)

    try:
        monkeypatch.setattr(logging_utils, "is_host_process", lambda: True)
        monkeypatch.setattr(logging_utils, "_has_external_handlers", lambda _: False)

        logger = logging_utils.get_logger(logger_name)
        logger.info("host-print-check")

        captured = capsys.readouterr()
        assert "host-print-check" in captured.out
    finally:
        _restore_logger(logger, original_handlers, original_level, original_propagate)


def test_external_handler_short_circuits_fallback(monkeypatch):
    logger_name = "sir3stoolkit.tests.logging.external_handler"
    logger, original_handlers, original_level, original_propagate = _setup_clean_logger(logger_name)

    stream = io.StringIO()
    external_handler = logging.StreamHandler(stream)
    external_handler.setFormatter(logging.Formatter("%(message)s"))

    try:
        monkeypatch.setattr(logging_utils, "is_host_process", lambda: True)

        logger = logging_utils.get_logger(logger_name)
        logger.addHandler(external_handler)
        logger.info("external-handler-check")

        assert "external-handler-check" in stream.getvalue()
    finally:
        _restore_logger(logger, original_handlers, original_level, original_propagate)


def test_non_host_root_fallback_filters_to_toolkit_records(capsys):
    root_logger = logging.getLogger()
    root_logger.handlers[:] = []
    root_logger.setLevel(logging.WARNING)

    toolkit_record = logging.LogRecord(
        "sir3stoolkit.mantle.dataframes",
        logging.INFO,
        __file__,
        1,
        "toolkit-log-visible",
        (),
        None,
    )
    external_record = logging.LogRecord(
        "fiona.env",
        logging.DEBUG,
        __file__,
        1,
        "third-party-log-hidden",
        (),
        None,
    )

    logging_utils._emit_via_default_python_logging(toolkit_record)
    logging_utils._emit_via_default_python_logging(external_record)

    captured = capsys.readouterr()
    assert "toolkit-log-visible" in captured.err
    assert "third-party-log-hidden" not in captured.err

    fallback_handlers = [
        handler
        for handler in root_logger.handlers
        if getattr(handler, "_sir3stoolkit_fallback", False)
    ]
    assert len(fallback_handlers) == 1
