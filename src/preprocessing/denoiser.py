"""Noise reduction for audio recordings."""

import numpy as np


def reduce_noise(audio: np.ndarray, sample_rate: int) -> np.ndarray:
    """Apply spectral noise reduction to an audio array.

    Args:
        audio: 1-D numpy array of audio samples.
        sample_rate: Sample rate in Hz.

    Returns:
        Denoised 1-D numpy array.
    """
    raise NotImplementedError("Implement using noisereduce or spectral subtraction")
