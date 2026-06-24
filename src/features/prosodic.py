"""Prosodic feature extraction: F0, jitter, shimmer, HNR."""

import numpy as np


def extract_prosodic_features(
    audio: np.ndarray,
    sample_rate: int,
    f0_min_hz: float = 75.0,
    f0_max_hz: float = 600.0,
) -> dict[str, float]:
    """Extract prosodic features from voiced speech.

    Extracts fundamental frequency (F0) statistics, jitter (period
    perturbation), shimmer (amplitude perturbation), and
    Harmonics-to-Noise Ratio (HNR).

    Args:
        audio: 1-D float32 numpy array of audio samples.
        sample_rate: Sampling rate in Hz.
        f0_min_hz: Minimum F0 for pitch tracking (Hz).
        f0_max_hz: Maximum F0 for pitch tracking (Hz).

    Returns:
        Dictionary of feature names to scalar values. Keys include:
        ``f0_mean``, ``f0_std``, ``f0_min``, ``f0_max``, ``f0_range``,
        ``jitter_local``, ``jitter_rap``, ``shimmer_local``,
        ``shimmer_apq3``, ``hnr_mean``, ``nhr_mean``.
    """
    raise NotImplementedError("Implement using parselmouth (Praat) or librosa")
