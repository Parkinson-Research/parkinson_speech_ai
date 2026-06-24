"""Amplitude normalisation for audio arrays."""

import numpy as np


def normalize_amplitude(audio: np.ndarray, method: str = "peak") -> np.ndarray:
    """Normalise the amplitude of an audio array.

    Args:
        audio: 1-D numpy array of audio samples.
        method: Normalisation method.
            - ``"peak"``: Scale so the peak absolute value is 1.0.
            - ``"rms"``: Scale so the RMS value is 0.1.

    Returns:
        Amplitude-normalised audio array.

    Raises:
        ValueError: If method is not recognised, or if audio is silent (all zeros).
    """
    raise NotImplementedError
