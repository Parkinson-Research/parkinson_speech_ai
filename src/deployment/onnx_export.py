"""ONNX model export utilities for cross-platform deployment."""

from pathlib import Path
from typing import Any


def export_to_onnx(
    model: Any,
    output_path: str | Path,
    sample_rate: int = 16000,
    max_duration_sec: float = 10.0,
    opset_version: int = 17,
) -> None:
    """Export a PyTorch transformer model to ONNX format.

    Args:
        model: Fitted PyTorch model in evaluation mode.
        output_path: Path to save the .onnx file.
        sample_rate: Input sample rate (determines input shape for tracing).
        max_duration_sec: Maximum audio duration used for dummy input shape.
        opset_version: ONNX opset version.

    Raises:
        RuntimeError: If ONNX export fails.
    """
    raise NotImplementedError
