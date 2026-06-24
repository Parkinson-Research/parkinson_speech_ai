"""Custom collate functions for DataLoader batching."""

from typing import Any

import numpy as np


def pad_collate_fn(batch: list[dict[str, Any]], max_length_samples: int | None = None) -> dict[str, Any]:
    """Collate a list of samples into a batch, padding waveforms to equal length.

    Args:
        batch: List of sample dicts from ``BaseAudioDataset.__getitem__``.
        max_length_samples: If specified, truncate/pad all waveforms to exactly
            this many samples. If None, pad to the longest waveform in the batch.

    Returns:
        Batched dictionary with:
            - ``"waveforms"``: 2-D float32 numpy array of shape (batch, max_len)
            - ``"attention_mask"``: 2-D int array of shape (batch, max_len)
            - ``"labels"``: 1-D int array of shape (batch,)
            - ``"subject_ids"``: list of str
    """
    raise NotImplementedError
