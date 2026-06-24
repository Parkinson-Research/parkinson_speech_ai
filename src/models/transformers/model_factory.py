"""Factory for building transformer-based classification models."""

from omegaconf import DictConfig


def build_transformer_model(model_cfg: DictConfig) -> "torch.nn.Module":  # type: ignore[name-defined]
    """Instantiate a pre-trained transformer model with a classification head.

    Loads the specified backbone from Hugging Face Hub and attaches a
    classification head as configured.

    Args:
        model_cfg: The ``model`` section of a config file. Must contain:
            - ``backbone``: Hugging Face model ID (str)
            - ``mode``: ``"frozen_encoder"`` or ``"finetune"``
            - ``classification_head``: ``"linear"`` or ``"mlp"``
            - ``num_classes``: Number of output classes (typically 2)
            - ``dropout``: Dropout probability for the classification head

    Returns:
        A PyTorch Module ready for training.

    Raises:
        ValueError: If backbone or mode is not supported.
    """
    raise NotImplementedError
