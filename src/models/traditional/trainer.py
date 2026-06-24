"""Training loop for traditional ML classifiers with cross-validation."""

from typing import Any

import numpy as np
from sklearn.pipeline import Pipeline


class TraditionalMLTrainer:
    """Manages training, hyperparameter tuning, and artefact saving for
    scikit-learn–based classifiers.

    Args:
        pipeline: A scikit-learn Pipeline (scaler + classifier).
        config: Full experiment config loaded via OmegaConf.
        experiment_name: MLflow experiment name for tracking.

    Example:
        >>> trainer = TraditionalMLTrainer(pipeline, config)
        >>> results = trainer.cross_validate(X, y, groups)
    """

    def __init__(self, pipeline: Pipeline, config: Any, experiment_name: str) -> None:
        self.pipeline = pipeline
        self.config = config
        self.experiment_name = experiment_name

    def cross_validate(
        self,
        X: np.ndarray,
        y: np.ndarray,
        groups: np.ndarray | None = None,
    ) -> dict[str, Any]:
        """Run stratified, speaker-independent cross-validation.

        Args:
            X: Feature matrix of shape (n_samples, n_features).
            y: Binary label array of shape (n_samples,).
            groups: Subject ID array for speaker-independent splits.

        Returns:
            Dictionary of aggregated evaluation metrics (mean ± std, CIs).
        """
        raise NotImplementedError

    def tune_hyperparameters(
        self,
        X: np.ndarray,
        y: np.ndarray,
    ) -> Pipeline:
        """Run hyperparameter search as configured in config.model.hyperparameter_tuning.

        Args:
            X: Feature matrix.
            y: Label array.

        Returns:
            Refitted Pipeline with best hyperparameters.
        """
        raise NotImplementedError
