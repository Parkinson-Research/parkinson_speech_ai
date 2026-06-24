"""Project path resolution utilities."""

from pathlib import Path


def get_project_root() -> Path:
    """Return the absolute path to the project root directory.

    Returns:
        Path to the directory containing pyproject.toml.
    """
    return Path(__file__).resolve().parents[2]


def get_data_dir() -> Path:
    """Return the absolute path to the data/ directory."""
    return get_project_root() / "data"


def get_outputs_dir() -> Path:
    """Return the absolute path to the outputs/ directory."""
    return get_project_root() / "outputs"


def get_configs_dir() -> Path:
    """Return the absolute path to the configs/ directory."""
    return get_project_root() / "configs"
