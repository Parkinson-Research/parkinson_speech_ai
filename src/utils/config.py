"""Configuration loading utilities."""

from pathlib import Path
from typing import Any

from omegaconf import DictConfig, OmegaConf


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


def config_to_dict(cfg: DictConfig) -> dict[str, Any]:
    """Convert an OmegaConf DictConfig to a plain Python dict.

    Args:
        cfg: OmegaConf DictConfig.

    Returns:
        Plain Python dictionary.
    """
    return OmegaConf.to_container(cfg, resolve=True)  # type: ignore[return-value]
