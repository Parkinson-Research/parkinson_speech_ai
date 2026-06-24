"""Fixed-length segmentation for consistent model input size."""

from typing import List

import numpy as np


def segment_audio(
    audio: np.ndarray,
    sample_rate: int,
    segment_length_sec: float,
    hop_length_sec: float | None = None,
    pad_last: bool = True,
) -> List[np.ndarray]:
    """Split an audio array into fixed-length segments.

    Args:
        audio: 1-D numpy array of audio samples.
        sample_rate: Sample rate in Hz.
        segment_length_sec: Length of each segment in seconds.
        hop_length_sec: Step size between segments in seconds.
            Defaults to segment_length_sec (non-overlapping).
        pad_last: If True, zero-pad the final segment if it is shorter
            than segment_length_sec. If False, discard the final segment.

    Returns:
        List of 1-D numpy arrays, each of length
        ``int(segment_length_sec * sample_rate)``.
    """
    raise NotImplementedError
