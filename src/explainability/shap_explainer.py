"""SHAP-based explainability for traditional ML classifiers."""

from typing import Any

import numpy as np


class SHAPExplainer:
    """Wrapper around SHAP for explaining traditional ML predictions.

    Uses TreeExplainer for tree-based models (XGBoost, Random Forest)
    and KernelExplainer for other model types (SVM, Logistic Regression).

    Args:
        model: Fitted scikit-learn model or pipeline.
        feature_names: List of feature names for plot labels.
        background_data: Background dataset for KernelExplainer.
            Not required for TreeExplainer.

    Example:
        >>> explainer = SHAPExplainer(fitted_model, feature_names)
        >>> shap_values = explainer.explain(X_test)
        >>> explainer.plot_summary(shap_values, X_test)
    """

    def __init__(
        self,
        model: Any,
        feature_names: list[str],
        background_data: np.ndarray | None = None,
    ) -> None:
        raise NotImplementedError

    def explain(self, X: np.ndarray) -> np.ndarray:
        """Compute SHAP values for a set of samples.

        Args:
            X: Feature matrix of shape (n_samples, n_features).

        Returns:
            SHAP values array of shape (n_samples, n_features).
        """
        raise NotImplementedError

    def plot_summary(self, shap_values: np.ndarray, X: np.ndarray, output_path: str | None = None) -> None:
        """Generate a SHAP summary (beeswarm) plot.

        Args:
            shap_values: SHAP values from ``explain()``.
            X: Feature matrix used to compute shap_values.
            output_path: If provided, save the plot to this path.
        """
        raise NotImplementedError
