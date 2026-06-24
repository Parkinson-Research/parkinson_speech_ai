"""Device detection and configuration utilities for PyTorch training.

Provides a single, consistent way to resolve the compute device (CPU / CUDA / MPS)
across all training scripts and model modules.
"""

import os
from typing import Literal

from src.utils.logger import get_logger

logger = get_logger(__name__)

DeviceType = Literal["cpu", "cuda", "mps"]


def get_device(prefer_gpu: bool = True) -> "torch.device":  # type: ignore[name-defined]
    """Resolve and return the best available compute device.

    Resolution order (when ``prefer_gpu=True``):
    1. CUDA (NVIDIA GPU) — respects ``CUDA_VISIBLE_DEVICES`` env var
    2. MPS (Apple Silicon) — if available and PyTorch ≥ 2.0
    3. CPU fallback

    Args:
        prefer_gpu: If False, always returns CPU regardless of available hardware.

    Returns:
        A ``torch.device`` object.

    Example:
        >>> device = get_device()
        >>> model = model.to(device)
    """
    try:
        import torch
    except ImportError as e:
        raise ImportError("PyTorch is required for device detection.") from e

    if not prefer_gpu:
        logger.info("Device: CPU (GPU preference disabled)")
        return torch.device("cpu")

    if torch.cuda.is_available():
        device = torch.device("cuda")
        gpu_name = torch.cuda.get_device_name(0)
        gpu_count = torch.cuda.device_count()
        vram_gb = torch.cuda.get_device_properties(0).total_memory / 1e9
        logger.info(
            "Device: CUDA | GPU: %s | Count: %d | VRAM: %.1f GB",
            gpu_name, gpu_count, vram_gb,
        )
        return device

    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        device = torch.device("mps")
        logger.info("Device: MPS (Apple Silicon)")
        return device

    logger.info("Device: CPU (no GPU detected)")
    return torch.device("cpu")


def get_device_info() -> dict[str, str | int | float | bool]:
    """Return a dictionary of device information for logging/tracking.

    Returns:
        Dictionary with keys: ``device``, ``cuda_available``,
        ``cuda_device_name``, ``cuda_device_count``, ``vram_gb``,
        ``mps_available``.
    """
    try:
        import torch
    except ImportError:
        return {"device": "unknown", "cuda_available": False}

    info: dict[str, str | int | float | bool] = {
        "cuda_available": torch.cuda.is_available(),
        "mps_available": (
            hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
        ),
    }

    if torch.cuda.is_available():
        info["device"] = "cuda"
        info["cuda_device_name"] = torch.cuda.get_device_name(0)
        info["cuda_device_count"] = torch.cuda.device_count()
        info["vram_gb"] = round(
            torch.cuda.get_device_properties(0).total_memory / 1e9, 1
        )
    elif info["mps_available"]:
        info["device"] = "mps"
    else:
        info["device"] = "cpu"

    return info


def log_device_info() -> None:
    """Log detailed device information at INFO level.

    Useful to call at the start of any training script.
    """
    info = get_device_info()
    logger.info("=" * 50)
    logger.info("Compute Device Configuration")
    logger.info("=" * 50)
    for key, value in info.items():
        logger.info("  %-25s %s", key + ":", value)
    logger.info("=" * 50)
