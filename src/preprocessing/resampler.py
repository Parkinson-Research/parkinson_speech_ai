"""Audio resampler — ensures all recordings are at a uniform sample rate."""

import numpy as np


def resample(audio: np.ndarray, orig_sr: int, target_sr: int) -> np.ndarray:
    """Resample an audio array from orig_sr to target_sr.

    Args:
        audio: 1-D numpy array of audio samples.
        orig_sr: Original sample rate in Hz.
        target_sr: Target sample rate in Hz.

    Returns:
        Resampled 1-D numpy array at target_sr.
    """
    raise NotImplementedError("Implement using librosa.resample or resampy.resample")
