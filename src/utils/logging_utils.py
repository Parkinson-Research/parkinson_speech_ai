"""Logging setup for consistent log formatting across the project."""

import logging
import sys


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Get a configured logger with a consistent format.

    Args:
        name: Logger name, typically ``__name__`` of the calling module.
        level: Logging level (default: INFO).

    Returns:
        Configured Logger instance.

    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("Pipeline started.")
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
