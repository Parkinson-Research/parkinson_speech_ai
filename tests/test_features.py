"""Unit tests for src/features modules."""

import numpy as np
import pytest


@pytest.fixture()
def voiced_signal() -> tuple[np.ndarray, int]:
    """Generate a 2-second voiced signal (harmonic series) at 16 kHz."""
    sr = 16000
    duration = 2.0
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    f0 = 150.0  # Hz — female speech range
    signal = sum(
        (1.0 / k) * np.sin(2 * np.pi * k * f0 * t) for k in range(1, 6)
    )
    return (signal / np.max(np.abs(signal)) * 0.5).astype(np.float32), sr


class TestMFCCExtraction:
    def test_output_shape_mean_std(self, voiced_signal: tuple[np.ndarray, int]) -> None:
        """With mean_std aggregation and 40 MFCCs + Δ + ΔΔ, output should be 1-D (240,)."""
        pytest.skip("Implement after mfcc.py is complete.")

    def test_no_nan_values(self, voiced_signal: tuple[np.ndarray, int]) -> None:
        """MFCC output should contain no NaN values."""
        pytest.skip("Implement after mfcc.py is complete.")


class TestSpectralFeatures:
    def test_returns_dict(self, voiced_signal: tuple[np.ndarray, int]) -> None:
        """Spectral extractor should return a non-empty dict of float values."""
        pytest.skip("Implement after spectral.py is complete.")


class TestFeaturePipeline:
    def test_feature_vector_is_1d(self, voiced_signal: tuple[np.ndarray, int]) -> None:
        """Pipeline output should be a 1-D numpy array."""
        pytest.skip("Implement after features/pipeline.py is complete.")

    def test_feature_dim_consistency(self, voiced_signal: tuple[np.ndarray, int]) -> None:
        """Feature dimension should be consistent across multiple calls."""
        pytest.skip("Implement after features/pipeline.py is complete.")
