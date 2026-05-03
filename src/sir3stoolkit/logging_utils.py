import ctypes
import importlib
import logging
import os
import sys
from functools import lru_cache


class _HostAwarePrintFallbackHandler(logging.Handler):
    """Fallback handler: host print, otherwise standard Python logging."""

    def emit(self, record: logging.LogRecord) -> None:
        logger = logging.getLogger(record.name)
        if _has_external_handlers(logger):
            return
        if not is_host_process():
            _emit_via_default_python_logging(record)
            return
        try:
            msg = self.format(record)
            print(msg)
        except Exception:
            self.handleError(record)


def _emit_via_default_python_logging(record: logging.LogRecord) -> None:
    """Emit via root logger with a default stream handler when none is configured."""
    root_logger = logging.getLogger()

    if not root_logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("[%(asctime)s] %(levelname)s in %(name)s: %(message)s")
        )
        root_logger.addHandler(handler)

    # Keep root permissive so module logger levels govern effective verbosity.
    if root_logger.level > logging.DEBUG:
        root_logger.setLevel(logging.DEBUG)

    root_logger.handle(record)


def _iter_effective_handlers(logger: logging.Logger):
    current = logger
    while current is not None:
        for handler in current.handlers:
            yield handler
        if not current.propagate:
            break
        current = current.parent


def _has_external_handlers(logger: logging.Logger) -> bool:
    return any(
        not isinstance(handler, _HostAwarePrintFallbackHandler)
        for handler in _iter_effective_handlers(logger)
    )


def get_logger(name: str) -> logging.Logger:
    """Create/get module logger with a host-aware fallback print handler."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    has_fallback = any(
        isinstance(handler, _HostAwarePrintFallbackHandler)
        for handler in logger.handlers
    )
    if not has_fallback:
        handler = _HostAwarePrintFallbackHandler()
        handler.setFormatter(
            logging.Formatter("[%(asctime)s] %(levelname)s in %(name)s: %(message)s")
        )
        logger.addHandler(handler)
    return logger


@lru_cache(maxsize=1)
def is_host_process() -> bool:
    """Return True when running inside SirGraf host process."""
    exe_name = get_process_executable_name().lower()
    return exe_name == "sirgraf.exe"


def get_process_executable_path() -> str | None:
    """Get absolute path to current process executable when available."""
    host_path = _get_process_executable_path_via_pythonnet()
    if host_path:
        return host_path

    if sys.platform.startswith("win"):
        try:
            buffer_len = 32768
            buffer = ctypes.create_unicode_buffer(buffer_len)
            kernel32 = ctypes.windll.kernel32
            size = kernel32.GetModuleFileNameW(None, buffer, buffer_len)
            if size > 0:
                return str(buffer.value)
        except Exception:
            pass

    if sys.executable:
        return str(sys.executable)
    return None


def get_process_executable_name() -> str:
    """Get executable name of current process when available."""
    process_path = get_process_executable_path()
    if not process_path:
        return ""
    return os.path.basename(process_path)


def _get_process_executable_path_via_pythonnet() -> str | None:
    """Try to resolve process executable path via pythonnet when available."""
    try:
        system_module = importlib.import_module("System")
        process = system_module.Diagnostics.Process.GetCurrentProcess()
        main_module = process.MainModule
        if main_module is None or not main_module.FileName:
            return None
        return str(main_module.FileName)
    except Exception:
        return None


def emit_message(logger: logging.Logger, message) -> None:
    """Emit a legacy message with level inference."""
    text = str(message)
    lower_text = text.lower()
    if lower_text.startswith("error") or lower_text.startswith("could not"):
        logger.error(text)
    elif lower_text.startswith("warning"):
        logger.warning(text)
    else:
        logger.info(text)
