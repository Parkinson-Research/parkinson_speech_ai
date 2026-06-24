"""Seed management for reproducible experiments.

Wraps the reproducibility module with additional DL-framework support
and a context manager for temporary seed overrides.
"""

import contextlib
import random
from contextlib import contextmanager
from typing import Generator

from src.utils.logger import get_logger

logger = get_logger(__name__)


def set_seed(seed: int = 42, deterministic: bool = False) -> None:
    """Set random seeds across all relevant libraries for reproducibility.

    Seeds: Python ``random``, NumPy, PyTorch (CPU + all GPUs), and
    Hugging Face ``transformers``.

    Args:
        seed: Integer seed value.
        deterministic: If True, configure PyTorch to use only deterministic
            algorithms (``torch.use_deterministic_algorithms(True)``).
            This guarantees bit-exact reproducibility at the cost of
            potential performance reduction and may raise errors for
            operations without a deterministic implementation.

    Example:
        >>> from src.utils.seed import set_seed
        >>> set_seed(42)
    """
    random.seed(seed)
    logger.debug("Python random seed set to %d", seed)

    try:
        import numpy as np
        np.random.seed(seed)
        logger.debug("NumPy seed set to %d", seed)
    except ImportError:
        pass

    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        if deterministic:
            torch.use_deterministic_algorithms(True)
            import os
            os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
            logger.info("PyTorch deterministic mode enabled.")
        logger.debug("PyTorch seed set to %d", seed)
    except ImportError:
        pass

    try:
        import transformers
        transformers.set_seed(seed)
        logger.debug("Transformers seed set to %d", seed)
    except ImportError:
        pass

    logger.info("Global seed set to %d", seed)


@contextmanager
def temporary_seed(seed: int) -> Generator[None, None, None]:
    """Context manager for a temporary seed override.

    Saves the current random state, applies the given seed, yields,
    then restores the original state. Useful for generating reproducible
    test fixtures without affecting the global experiment seed.

    Args:
        seed: Temporary seed to apply within the context block.

    Example:
        >>> with temporary_seed(0):
        ...     X_test = np.random.randn(10, 5)
    """
    import numpy as np

    py_state = random.getstate()
    np_state = np.random.get_state()

    try:
        import torch
        torch_state = torch.get_rng_state()
        has_torch = True
    except ImportError:
        has_torch = False
        torch_state = None

    try:
        set_seed(seed)
        yield
    finally:
        random.setstate(py_state)
        np.random.set_state(np_state)
        if has_torch and torch_state is not None:
            import torch
            torch.set_rng_state(torch_state)
