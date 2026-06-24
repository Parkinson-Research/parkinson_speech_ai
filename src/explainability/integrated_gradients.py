"""Integrated Gradients attribution for transformer models using Captum."""

from typing import Any

import numpy as np


def compute_integrated_gradients(
    model: Any,
    input_values: Any,
    target_class: int = 1,
    n_steps: int = 50,
) -> np.ndarray:
    """Compute Integrated Gradients attributions for a single input.

    Attributes the model's prediction to the input waveform features
    using the Integrated Gradients method (Sundararajan et al., 2017).

    Args:
        model: Fine-tuned transformer model.
        input_values: Preprocessed input tensor of shape (1, sequence_length).
        target_class: Class index to explain (0 = HC, 1 = PD).
        n_steps: Number of integration steps. Higher = more accurate.

    Returns:
        Attribution array of same shape as input_values.
    """
    raise NotImplementedError("Implement using captum.attr.IntegratedGradients")
