"""Reproducibility helpers — seed setting across all relevant libraries."""

import random


def set_seed(seed: int = 42) -> None:
    """Set random seeds for Python, NumPy, and PyTorch for reproducibility.

    Args:
        seed: Integer seed value. Default is 42.

    Note:
        Even with seeds set, full determinism may not be possible on GPU
        due to CUDA non-deterministic operations. Use
        ``torch.use_deterministic_algorithms(True)`` if strict
        determinism is required (may reduce performance).
    """
    random.seed(seed)

    try:
        import numpy as np
        np.random.seed(seed)
    except ImportError:
        pass

    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass

    try:
        import transformers
        transformers.set_seed(seed)
    except ImportError:
        pass
