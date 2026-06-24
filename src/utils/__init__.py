"""
src.utils
=========
Shared utility functions used across all pipeline modules.

Modules:
    logger          — Structured logging with console and file handlers
    seed            — Seed management with context manager support
    config          — YAML config loading, merging, env var helpers
    paths           — Project-relative path resolution (env-var overridable)
    device          — PyTorch device detection (CUDA / MPS / CPU)
    mlflow_utils    — MLflow tracking helpers (stubs, not yet implemented)
    logging_utils   — Legacy alias for logger (kept for backwards compat)
    reproducibility — Legacy alias for seed (kept for backwards compat)
"""

from src.utils.config import get_env, load_config, load_configs, apply_overrides, config_to_dict
from src.utils.device import get_device, get_device_info, log_device_info
from src.utils.logger import get_logger
from src.utils.paths import (
    get_project_root,
    get_data_root,
    get_raw_dir,
    get_processed_dir,
    get_manifest_path,
    get_outputs_root,
    get_models_dir,
    get_reports_dir,
    get_figures_dir,
    get_configs_dir,
    get_logs_dir,
    get_mlruns_dir,
    ensure_dirs,
)
from src.utils.seed import set_seed, temporary_seed

__all__ = [
    # Config
    "load_config",
    "load_configs",
    "apply_overrides",
    "config_to_dict",
    "get_env",
    # Logging
    "get_logger",
    # Paths
    "get_project_root",
    "get_data_root",
    "get_raw_dir",
    "get_processed_dir",
    "get_manifest_path",
    "get_outputs_root",
    "get_models_dir",
    "get_reports_dir",
    "get_figures_dir",
    "get_configs_dir",
    "get_logs_dir",
    "get_mlruns_dir",
    "ensure_dirs",
    # Seed
    "set_seed",
    "temporary_seed",
    # Device
    "get_device",
    "get_device_info",
    "log_device_info",
]
