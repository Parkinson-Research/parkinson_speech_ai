"""Project path resolution utilities.

All paths are resolved relative to the project root.
Environment variables DATA_ROOT and OUTPUTS_ROOT can override the defaults,
which is useful when data is stored on a separate volume or network drive.
"""

import os
from pathlib import Path


def get_project_root() -> Path:
    """Return the absolute path to the project root directory.

    Walks up from this file's location until it finds ``pyproject.toml``.

    Returns:
        Absolute path to the project root.

    Raises:
        RuntimeError: If the project root cannot be determined.
    """
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    # Fallback: assume repo root is 3 levels above this file
    return Path(__file__).resolve().parents[2]


def get_data_root() -> Path:
    """Return the data root directory.

    Respects the ``DATA_ROOT`` environment variable if set.
    """
    env_override = os.environ.get("DATA_ROOT")
    if env_override:
        return Path(env_override)
    return get_project_root() / "data"


def get_raw_dir(dataset: str | None = None) -> Path:
    """Return the raw data directory, optionally for a specific dataset.

    Args:
        dataset: Dataset name (e.g. ``"italian"``, ``"mdvr_kcl"``).
            If None, returns the root raw directory.

    Returns:
        Absolute path to ``data/raw/`` or ``data/raw/{dataset}/``.
    """
    raw = get_data_root() / "raw"
    return raw / dataset if dataset else raw


def get_processed_dir(dataset: str | None = None) -> Path:
    """Return the processed data directory, optionally for a specific dataset.

    Args:
        dataset: Dataset name. If None, returns the root processed directory.

    Returns:
        Absolute path to ``data/processed/`` or ``data/processed/{dataset}/``.
    """
    processed = get_data_root() / "processed"
    return processed / dataset if dataset else processed


def get_manifest_path(dataset: str) -> Path:
    """Return the manifest CSV path for a given dataset.

    Args:
        dataset: Dataset name (e.g. ``"italian"``, ``"mdvr_kcl"``).

    Returns:
        Absolute path to ``data/processed/{dataset}_manifest.csv``.
    """
    return get_processed_dir() / f"{dataset}_manifest.csv"


def get_outputs_root() -> Path:
    """Return the outputs root directory.

    Respects the ``OUTPUTS_ROOT`` environment variable if set.
    """
    env_override = os.environ.get("OUTPUTS_ROOT")
    if env_override:
        return Path(env_override)
    return get_project_root() / "outputs"


def get_models_dir(experiment_name: str | None = None) -> Path:
    """Return the models output directory, optionally for a specific experiment.

    Args:
        experiment_name: Experiment name. If None, returns the root models dir.
    """
    models = get_outputs_root() / "models"
    return models / experiment_name if experiment_name else models


def get_reports_dir() -> Path:
    """Return the reports output directory."""
    return get_outputs_root() / "reports"


def get_figures_dir() -> Path:
    """Return the figures output directory."""
    return get_outputs_root() / "figures"


def get_configs_dir() -> Path:
    """Return the configs directory."""
    return get_project_root() / "configs"


def get_logs_dir() -> Path:
    """Return the logs directory. Creates it if it does not exist."""
    logs = get_project_root() / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    return logs


def get_mlruns_dir() -> Path:
    """Return the MLflow tracking directory."""
    return get_project_root() / "mlruns"


def ensure_dirs(*paths: Path) -> None:
    """Create directories if they do not exist.

    Args:
        *paths: One or more Path objects to create.

    Example:
        >>> ensure_dirs(get_models_dir("my_exp"), get_reports_dir())
    """
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
