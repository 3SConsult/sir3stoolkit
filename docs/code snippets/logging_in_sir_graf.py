import logging
import sys

def setup_console_logger(name="sir3stoolkit", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # avoid relying on host/root logger config

    # prevent duplicate handlers if called multiple times
    logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)  # important: stdout, not stderr
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))

    logger.addHandler(handler)
    return logger
logger = setup_console_logger(level=logging.DEBUG)
