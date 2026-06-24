"""Configuration loading, merging, and validation utilities.

Supports:
- Loading individual YAML configs via OmegaConf
- Merging base configs with experiment-specific overrides
- Loading environment variables from .env via python-dotenv
- Runtime config overrides from CLI key=value strings
"""

import os
from pathlib import Path
from typing import Any

from omegaconf import DictConfig, OmegaConf


def load_env(env_file: str | Path = ".env") -> None:
    """Load environment variables from a .env file using python-dotenv.

    Does nothing if ``python-dotenv`` is not installed or the file
    does not exist (fails silently to keep the import optional).

    Args:
        env_file: Path to the .env file. Defaults to ``.env`` in the
            current working directory.
    """
    try:
        from dotenv import load_dotenv
        load_dotenv(dotenv_path=str(env_file), override=False)
    except ImportError:
        pass  # python-dotenv is optional


def load_config(config_path: str | Path) -> DictConfig:
    """Load a YAML config file using OmegaConf.

    Args:
        config_path: Path to the YAML configuration file.

    Returns:
        OmegaConf DictConfig object.

    Raises:
        FileNotFoundError: If the config file does not exist.
    """
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    return OmegaConf.load(config_path)


def load_configs(*config_paths: str | Path) -> DictConfig:
    """Load and merge multiple YAML config files.

    Later configs override earlier ones (right-most wins).
    Useful for combining a base config with an experiment override.

    Args:
        *config_paths: One or more paths to YAML config files.

    Returns:
        Merged OmegaConf DictConfig.

    Example:
        >>> cfg = load_configs(
        ...     "configs/training.yaml",
        ...     "configs/model.yaml",
        ...     "configs/wav2vec2_italian_finetune.yaml",
        ... )
    """
    configs = [load_config(p) for p in config_paths]
    return OmegaConf.merge(*configs)


def apply_overrides(cfg: DictConfig, overrides: list[str]) -> DictConfig:
    """Apply CLI-style key=value overrides to a config.

    Args:
        cfg: Existing DictConfig to modify.
        overrides: List of override strings in ``key.subkey=value`` format.
            E.g. ``["training.epochs=30", "model.dropout=0.2"]``.

    Returns:
        New DictConfig with overrides applied.

    Example:
        >>> cfg = apply_overrides(cfg, ["training.epochs=30"])
    """
    override_cfg = OmegaConf.from_dotlist(overrides)
    return OmegaConf.merge(cfg, override_cfg)


def config_to_dict(cfg: DictConfig) -> dict[str, Any]:
    """Convert an OmegaConf DictConfig to a plain Python dict.

    Args:
        cfg: OmegaConf DictConfig.

    Returns:
        Plain Python dictionary with all values resolved.
    """
    return OmegaConf.to_container(cfg, resolve=True)  # type: ignore[return-value]


def get_env(key: str, default: str | None = None, required: bool = False) -> str | None:
    """Read an environment variable with optional required enforcement.

    Args:
        key: Environment variable name.
        default: Default value if the variable is not set.
        required: If True, raise ValueError when the variable is absent.

    Returns:
        The environment variable value, or ``default``.

    Raises:
        ValueError: If ``required=True`` and the variable is not set.

    Example:
        >>> token = get_env("DAGSHUB_TOKEN", required=True)
    """
    value = os.environ.get(key, default)
    if required and not value:
        raise ValueError(
            f"Required environment variable '{key}' is not set. "
            f"Copy .env.example to .env and fill in the value."
        )
    return value
