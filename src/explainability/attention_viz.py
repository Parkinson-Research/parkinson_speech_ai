"""Attention weight visualisation for transformer-based models."""

from typing import Any

import numpy as np


def extract_attention_weights(
    model: Any,
    input_values: Any,
    layer: int = -1,
) -> np.ndarray:
    """Extract attention weights from a transformer model for a single input.

    Args:
        model: Fine-tuned transformer model in evaluation mode.
        input_values: Preprocessed input tensor (1, sequence_length).
        layer: Which encoder layer to extract attention from.
            Use -1 for the last layer.

    Returns:
        Attention weight array of shape (n_heads, seq_len, seq_len).
    """
    raise NotImplementedError


def plot_attention_on_waveform(
    attention_weights: np.ndarray,
    waveform: np.ndarray,
    sample_rate: int,
    output_path: str | None = None,
) -> None:
    """Overlay mean attention weights on the input waveform.

    Args:
        attention_weights: Array of shape (n_heads, seq_len, seq_len).
        waveform: Original 1-D audio array.
        sample_rate: Sample rate in Hz.
        output_path: If provided, save the figure to this path.
    """
    raise NotImplementedError
