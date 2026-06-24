"""Statistical significance tests for model comparison."""

import numpy as np


def mcnemar_test(
    y_true: np.ndarray,
    y_pred_a: np.ndarray,
    y_pred_b: np.ndarray,
) -> dict[str, float]:
    """Perform McNemar's test to compare two binary classifiers.

    Tests whether two models make significantly different errors on the
    same test set.

    Args:
        y_true: Ground-truth binary labels.
        y_pred_a: Predictions from model A.
        y_pred_b: Predictions from model B.

    Returns:
        Dictionary with ``statistic`` (chi-squared) and ``p_value``.
    """
    raise NotImplementedError
