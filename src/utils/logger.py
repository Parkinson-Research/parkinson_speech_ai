"""Production-grade logging setup for the Parkinson Speech AI framework.

Provides a structured logger with:
- Timestamped, levelled console output
- Optional file handler (rotated daily)
- LOG_LEVEL control via environment variable
"""

import logging
import logging.handlers
import os
import sys
from pathlib import Path


_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(
    name: str,
    level: int | None = None,
    log_file: str | Path | None = None,
) -> logging.Logger:
    """Get a configured logger with consistent formatting.

    The log level is resolved in this order:
    1. The ``level`` argument (if provided)
    2. The ``LOG_LEVEL`` environment variable
    3. ``INFO`` (default fallback)

    Args:
        name: Logger name. Pass ``__name__`` from the calling module for
            automatic hierarchical naming.
        level: Override log level. Accepts ``logging.DEBUG``, ``logging.INFO``,
            etc. If None, reads from the ``LOG_LEVEL`` env variable.
        log_file: Optional path to a log file. If provided, a
            ``TimedRotatingFileHandler`` (daily rotation, 7 days retention)
            is attached in addition to the console handler.

    Returns:
        Configured ``logging.Logger`` instance.

    Example:
        >>> from src.utils.logger import get_logger
        >>> logger = get_logger(__name__)
        >>> logger.info("Preprocessing started.")
        >>> logger.warning("Low memory: consider reducing batch_size.")
    """
    if level is None:
        env_level = os.environ.get("LOG_LEVEL", "INFO").upper()
        level = getattr(logging, env_level, logging.INFO)

    logger = logging.getLogger(name)

    # Avoid adding duplicate handlers if get_logger is called multiple times
    if logger.handlers:
        return logger

    logger.setLevel(level)
    formatter = logging.Formatter(fmt=_LOG_FORMAT, datefmt=_DATE_FORMAT)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # Optional file handler
    if log_file is not None:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=str(log_path),
            when="midnight",
            backupCount=7,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

    # Prevent propagation to root logger to avoid duplicate output
    logger.propagate = False

    return logger
