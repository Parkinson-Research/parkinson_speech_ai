"""Composes all feature extractors into a single configurable pipeline."""

from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class FeatureConfig:
    """Configuration for the feature extraction pipeline.

    Attributes:
        mfcc_enabled: Extract MFCC features.
        n_mfcc: Number of MFCC coefficients.
        include_delta: Include first-order delta MFCCs.
        include_delta_delta: Include second-order delta-delta MFCCs.
        prosodic_enabled: Extract prosodic features (F0, jitter, shimmer, HNR).
        spectral_enabled: Extract spectral features.
        opensmile_enabled: Extract OpenSMILE features.
        opensmile_feature_set: OpenSMILE feature set name.
        normalizer_method: Feature normalisation method.
    """

    mfcc_enabled: bool = True
    n_mfcc: int = 40
    include_delta: bool = True
    include_delta_delta: bool = True
    prosodic_enabled: bool = True
    spectral_enabled: bool = True
    opensmile_enabled: bool = False
    opensmile_feature_set: str = "eGeMAPSv02"
    normalizer_method: str = "standard"
    feature_names: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, cfg: dict[str, Any]) -> "FeatureConfig":
        """Instantiate from a config dictionary."""
        raise NotImplementedError


class FeatureExtractionPipeline:
    """Combines all enabled feature extractors into one feature vector.

    Args:
        config: FeatureConfig instance. Defaults to MFCCs + prosodic + spectral.

    Example:
        >>> pipeline = FeatureExtractionPipeline(config)
        >>> features = pipeline.extract(waveform, sample_rate=16000)
        >>> print(features.shape)   # e.g. (203,)
    """

    def __init__(self, config: FeatureConfig | None = None) -> None:
        self.config = config or FeatureConfig()

    def extract(self, audio: np.ndarray, sample_rate: int) -> np.ndarray:
        """Extract all configured features and return a single feature vector.

        Args:
            audio: 1-D float32 numpy array of audio samples.
            sample_rate: Sampling rate in Hz.

        Returns:
            1-D numpy array of concatenated, normalised features.
        """
        raise NotImplementedError

    @property
    def feature_dim(self) -> int:
        """Return the dimensionality of the output feature vector."""
        raise NotImplementedError
