"""Unit tests for src/utils modules."""

from pathlib import Path

import pytest


class TestLoadConfig:
    def test_loads_valid_yaml(self, tmp_path: Path) -> None:
        """load_config should return a DictConfig from a valid YAML file."""
        config_file = tmp_path / "test.yaml"
        config_file.write_text("experiment:\n  name: test\n  seed: 42\n")

        from src.utils.config import load_config

        cfg = load_config(config_file)
        assert cfg.experiment.name == "test"
        assert cfg.experiment.seed == 42

    def test_raises_on_missing_file(self, tmp_path: Path) -> None:
        """load_config should raise FileNotFoundError for a missing file."""
        from src.utils.config import load_config

        with pytest.raises(FileNotFoundError):
            load_config(tmp_path / "nonexistent.yaml")


class TestSetSeed:
    def test_numpy_reproducibility(self) -> None:
        """Setting the same seed twice should produce identical numpy random sequences."""
        from src.utils.reproducibility import set_seed
        import numpy as np

        set_seed(42)
        a = np.random.random(5)
        set_seed(42)
        b = np.random.random(5)
        np.testing.assert_array_equal(a, b)


class TestGetLogger:
    def test_returns_logger(self) -> None:
        """get_logger should return a Logger with the correct name."""
        import logging
        from src.utils.logging_utils import get_logger

        logger = get_logger("test_module")
        assert isinstance(logger, logging.Logger)
        assert logger.name == "test_module"
