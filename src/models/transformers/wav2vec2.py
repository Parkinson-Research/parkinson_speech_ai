"""Wav2Vec2 fine-tuning model for Parkinson's Disease classification."""


class Wav2Vec2ForPDClassification:
    """Wav2Vec2 model with a binary classification head for PD detection.

    Wraps ``transformers.Wav2Vec2ForSequenceClassification`` with
    additional support for:
    - Frozen encoder mode (linear probe)
    - Layer-wise learning rate decay
    - Mean pooling vs. attentive pooling

    Args:
        backbone_name: Hugging Face model ID (e.g. ``"facebook/wav2vec2-base"``).
        num_classes: Number of output classes (default: 2).
        mode: ``"frozen_encoder"`` or ``"finetune"``.
        classification_head: ``"linear"`` or ``"mlp"``.
        dropout: Dropout probability for the classification head.

    Example:
        >>> model = Wav2Vec2ForPDClassification(
        ...     backbone_name="facebook/wav2vec2-base",
        ...     mode="finetune",
        ... )
    """

    def __init__(
        self,
        backbone_name: str = "facebook/wav2vec2-base",
        num_classes: int = 2,
        mode: str = "finetune",
        classification_head: str = "linear",
        dropout: float = 0.1,
    ) -> None:
        raise NotImplementedError
