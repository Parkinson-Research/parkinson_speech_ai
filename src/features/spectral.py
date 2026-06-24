"""Spectral feature extraction: centroid, bandwidth, rolloff, flux, etc."""

import numpy as np


def extract_spectral_features(
    audio: np.ndarray,
    sample_rate: int,
    n_fft: int = 512,
    hop_length: int = 160,
) -> dict[str, float]:
    """Extract spectral features from an audio array.

    Args:
        audio: 1-D float32 numpy array of audio samples.
        sample_rate: Sampling rate in Hz.
        n_fft: FFT window size in samples.
        hop_length: Hop size in samples.

    Returns:
        Dictionary of feature names to scalar values (aggregated over frames).
        Keys include: ``spectral_centroid_mean``, ``spectral_centroid_std``,
        ``spectral_bandwidth_mean``, ``spectral_rolloff_mean``,
        ``zero_crossing_rate_mean``, ``spectral_flatness_mean``.
    """
    raise NotImplementedError("Implement using librosa.feature.*")
