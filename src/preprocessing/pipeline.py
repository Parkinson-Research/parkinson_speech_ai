"""Orchestrates the full audio preprocessing chain."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np


@dataclass
class PreprocessingConfig:
    """Configuration for the preprocessing pipeline.

    Attributes:
        target_sample_rate: Desired sample rate in Hz.
        mono: Convert to mono if True.
        normalize: Apply amplitude normalisation if True.
        trim_silence: Apply VAD-based silence trimming if True.
        silence_threshold_db: Top-dB threshold for silence trimming.
        max_duration_sec: Maximum duration to keep; None means no limit.
        pad_short_recordings: Pad recordings shorter than max_duration_sec.
    """

    target_sample_rate: int = 16000
    mono: bool = True
    normalize: bool = True
    trim_silence: bool = True
    silence_threshold_db: float = 40.0
    max_duration_sec: float | None = 10.0
    pad_short_recordings: bool = True

    @classmethod
    def from_dict(cls, cfg: dict[str, Any]) -> "PreprocessingConfig":
        """Instantiate from a config dictionary (e.g., loaded from YAML)."""
        return cls(**{k: v for k, v in cfg.items() if k in cls.__dataclass_fields__})


class PreprocessingPipeline:
    """End-to-end audio preprocessing pipeline.

    Applies resampling, denoising, silence trimming, and amplitude
    normalisation in a configurable, reproducible sequence.

    Args:
        config: A PreprocessingConfig instance. If None, defaults are used.

    Example:
        >>> pipeline = PreprocessingPipeline(config)
        >>> waveform, sr = pipeline.process("path/to/recording.wav")
    """

    def __init__(self, config: PreprocessingConfig | None = None) -> None:
        self.config = config or PreprocessingConfig()

    def process(self, file_path: str | Path) -> tuple[np.ndarray, int]:
        """Run the full preprocessing chain on a single audio file.

        Args:
            file_path: Path to the input audio file.

        Returns:
            A tuple of (waveform, sample_rate) after all preprocessing steps.
        """
        raise NotImplementedError

    def process_batch(self, file_paths: list[str | Path]) -> list[tuple[np.ndarray, int]]:
        """Run the preprocessing chain on a list of audio files.

        Args:
            file_paths: List of paths to audio files.

        Returns:
            List of (waveform, sample_rate) tuples, one per input file.
        """
        raise NotImplementedError
