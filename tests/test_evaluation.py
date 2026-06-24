"""Unit tests for src/evaluation modules."""

import numpy as np
import pytest


@pytest.fixture()
def binary_predictions() -> dict[str, np.ndarray]:
    """Provide synthetic ground-truth and prediction arrays."""
    rng = np.random.default_rng(42)
    y_true = rng.integers(0, 2, size=100)
    y_prob = np.clip(y_true * 0.6 + rng.normal(0, 0.2, size=100), 0, 1)
    y_pred = (y_prob >= 0.5).astype(int)
    return {"y_true": y_true, "y_prob": y_prob, "y_pred": y_pred}


class TestComputeMetrics:
    def test_keys_present(self, binary_predictions: dict) -> None:
        """compute_metrics should return all required metric keys."""
        pytest.skip("Implement after metrics.py is complete.")

    def test_auc_between_0_and_1(self, binary_predictions: dict) -> None:
        """AUC-ROC should be between 0 and 1."""
        pytest.skip("Implement after metrics.py is complete.")

    def test_sensitivity_plus_specificity(self, binary_predictions: dict) -> None:
        """Sensitivity and specificity should each be in [0, 1]."""
        pytest.skip("Implement after metrics.py is complete.")


class TestBootstrapCI:
    def test_ci_bounds_ordering(self, binary_predictions: dict) -> None:
        """Lower CI bound should be <= mean <= upper CI bound."""
        pytest.skip("Implement after metrics.py is complete.")


class TestSpeakerIndependentSplits:
    def test_no_subject_leakage(self) -> None:
        """No subject should appear in both train and test within a fold."""
        pytest.skip("Implement after cross_validation.py is complete.")
