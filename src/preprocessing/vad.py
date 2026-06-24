"""Voice Activity Detection — trims leading and trailing silence."""

import numpy as np


def trim_silence(
    audio: np.ndarray,
    sample_rate: int,
    top_db: float = 40.0,
) -> np.ndarray:
    """Trim leading and trailing silence from an audio array.

    Args:
        audio: 1-D numpy array of audio samples.
        sample_rate: Sample rate in Hz.
        top_db: Threshold (in dB below peak) below which audio is
            considered silence.

    Returns:
        Trimmed 1-D numpy array with silence removed.
    """
    raise NotImplementedError("Implement using librosa.effects.trim")
