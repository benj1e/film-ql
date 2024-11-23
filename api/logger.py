import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(logger_name: str, file: str | None = None) -> logging.Logger:
    """
    Creates and returns a logger instance for a specific router/module.

    :param name: Name of the logger (usually the router name).
    :param log_file: The file where logs should be written (default: name of router).
    :return: Configured logger instance.
    """
    # Logger file path

    try:
        base, ext = os.path.splitext(file)
        if not ext and ext != ".log":
            ext = ".log"
            log_file = base + ext
        else:
            log_file = file
    except Exception as e:
        raise e

    log_file_path = os.path.join(LOG_DIR, log_file)
    # Handlers
    stream_handler = logging.StreamHandler()  # Logs to console
    file_handler = RotatingFileHandler(
        log_file_path, maxBytes=5 * 1024 * 1024
    )  # Logs to file

    # Formatter
    formatter = logging.Formatter(
        "%(levelname)-9s %(message)-20s %(asctime)-30s [%(name)s]"
    )

    # Set formatter for handlers
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)

    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)

    return logger
