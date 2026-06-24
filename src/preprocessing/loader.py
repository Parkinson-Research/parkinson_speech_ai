"""Audio file loader — converts audio files to numpy waveform arrays."""

from pathlib import Path
from typing import Tuple

import numpy as np


def load_audio(file_path: str | Path, target_sr: int = 16000, mono: bool = True) -> Tuple[np.ndarray, int]:
    """Load an audio file and return waveform and sample rate.

    Args:
        file_path: Path to the audio file (.wav, .mp3, .flac, etc.).
        target_sr: Target sample rate in Hz. If different from the file's
            native rate, the audio will be resampled. Pass None to skip resampling.
        mono: If True, convert multi-channel audio to mono.

    Returns:
        A tuple of (waveform, sample_rate) where waveform is a 1-D float32
        numpy array and sample_rate is the (possibly resampled) rate in Hz.

    Raises:
        FileNotFoundError: If the audio file does not exist.
        ValueError: If the file cannot be decoded.
    """
    raise NotImplementedError("Implement using librosa.load or soundfile.read")
