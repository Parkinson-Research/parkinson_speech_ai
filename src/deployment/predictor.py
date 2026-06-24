"""Model predictor wrapper for inference."""

from pathlib import Path
from typing import Any


class PDPredictor:
    """Unified inference wrapper for both traditional ML and transformer models.

    Handles preprocessing, inference, and postprocessing in a single call.

    Args:
        model_path: Path to the saved model checkpoint or sklearn .pkl file.
        model_type: ``"traditional"`` or ``"transformer"``.
        preprocessing_config_path: Path to the preprocessing YAML config.

    Example:
        >>> predictor = PDPredictor("outputs/models/wav2vec2_best/", "transformer")
        >>> result = predictor.predict("path/to/recording.wav")
        >>> print(result["pd_probability"], result["label"])
    """

    def __init__(
        self,
        model_path: str | Path,
        model_type: str,
        preprocessing_config_path: str | Path | None = None,
    ) -> None:
        raise NotImplementedError

    def predict(self, audio_path: str | Path) -> dict[str, Any]:
        """Run inference on a single audio file.

        Args:
            audio_path: Path to the input audio file.

        Returns:
            Dictionary with:
                - ``"pd_probability"``: float, probability of PD (0–1)
                - ``"label"``: str, ``"PD"`` or ``"HC"``
                - ``"confidence"``: float, model confidence
        """
        raise NotImplementedError
