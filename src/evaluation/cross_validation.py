"""Stratified, speaker-independent cross-validation splits."""

from typing import Generator

import numpy as np


def get_speaker_independent_splits(
    labels: np.ndarray,
    subject_ids: np.ndarray,
    n_splits: int = 10,
    seed: int = 42,
) -> Generator[tuple[np.ndarray, np.ndarray], None, None]:
    """Generate stratified, speaker-independent train/test index splits.

    Ensures no subject appears in both train and test sets within any fold.
    Subjects are grouped first, then folds are stratified by label.

    Args:
        labels: 1-D array of binary labels (0 or 1), one per sample.
        subject_ids: 1-D array of subject ID strings, one per sample.
        n_splits: Number of cross-validation folds.
        seed: Random seed for reproducibility.

    Yields:
        Tuples of (train_indices, test_indices) as 1-D numpy int arrays.
    """
    raise NotImplementedError
