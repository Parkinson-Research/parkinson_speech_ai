"""Classification metrics for binary PD detection."""

from typing import Any

import numpy as np


def compute_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: np.ndarray | None = None,
) -> dict[str, float]:
    """Compute binary classification metrics.

    Args:
        y_true: Ground-truth binary labels (0 = HC, 1 = PD).
        y_pred: Predicted binary labels.
        y_prob: Predicted probabilities for the positive class (PD).
            Required for AUC-ROC computation.

    Returns:
        Dictionary with keys: ``accuracy``, ``sensitivity``, ``specificity``,
        ``f1``, ``mcc``, ``auc_roc`` (if y_prob provided),
        ``precision``, ``balanced_accuracy``.
    """
    raise NotImplementedError


def bootstrap_ci(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    metric: str = "auc_roc",
    n_bootstrap: int = 1000,
    ci: float = 0.95,
    seed: int = 42,
) -> dict[str, float]:
    """Compute bootstrap confidence interval for a given metric.

    Args:
        y_true: Ground-truth binary labels.
        y_prob: Predicted probabilities for the positive class.
        metric: Metric to bootstrap. One of ``"auc_roc"``, ``"f1"``,
            ``"sensitivity"``, ``"specificity"``, ``"accuracy"``.
        n_bootstrap: Number of bootstrap resamples.
        ci: Confidence level (e.g. 0.95 for 95% CI).
        seed: Random seed for reproducibility.

    Returns:
        Dictionary with keys: ``mean``, ``lower``, ``upper``.
    """
    raise NotImplementedError
