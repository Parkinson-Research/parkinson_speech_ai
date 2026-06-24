"""OpenSMILE feature set wrapper (eGeMAPS, ComParE)."""

import numpy as np


def extract_opensmile_features(
    audio: np.ndarray,
    sample_rate: int,
    feature_set: str = "eGeMAPSv02",
) -> np.ndarray:
    """Extract OpenSMILE features from an audio array.

    Args:
        audio: 1-D float32 numpy array of audio samples.
        sample_rate: Sampling rate in Hz.
        feature_set: OpenSMILE feature set to use.
            Supported values: ``"eGeMAPSv02"`` (88 features),
            ``"ComParE_2016"`` (6373 features).

    Returns:
        1-D numpy array of feature values. Feature names can be retrieved
        via the opensmile library's feature extractor object.

    Raises:
        ImportError: If the ``opensmile`` Python package is not installed.
        ValueError: If feature_set is not recognised.
    """
    raise NotImplementedError("Implement using opensmile Python package")
