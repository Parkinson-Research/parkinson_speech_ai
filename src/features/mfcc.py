"""MFCC feature extraction with delta and delta-delta coefficients."""

import numpy as np


def extract_mfcc(
    audio: np.ndarray,
    sample_rate: int,
    n_mfcc: int = 40,
    n_fft: int = 512,
    hop_length: int = 160,
    include_delta: bool = True,
    include_delta_delta: bool = True,
    aggregation: str = "mean_std",
) -> np.ndarray:
    """Extract MFCC features from an audio array.

    Args:
        audio: 1-D float32 numpy array of audio samples.
        sample_rate: Sampling rate in Hz.
        n_mfcc: Number of MFCC coefficients.
        n_fft: FFT window size in samples.
        hop_length: Hop size in samples between frames.
        include_delta: Append first-order delta coefficients.
        include_delta_delta: Append second-order delta-delta coefficients.
        aggregation: How to aggregate frame-level features.
            - ``"mean_std"``: concatenate mean and std over time frames.
            - ``"mean"``: mean over time frames only.
            - ``"full_sequence"``: return the full 2-D feature matrix
              (n_features x n_frames), no aggregation.

    Returns:
        Feature vector (1-D array) if aggregation is ``"mean_std"`` or
        ``"mean"``, or a 2-D array (n_features x n_frames) if
        ``"full_sequence"``.

    Raises:
        ValueError: If audio is empty or aggregation value is invalid.
    """
    raise NotImplementedError("Implement using librosa.feature.mfcc")
