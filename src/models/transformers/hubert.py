"""HuBERT fine-tuning model for Parkinson's Disease classification."""


class HuBERTForPDClassification:
    """HuBERT model with a binary classification head for PD detection.

    Args:
        backbone_name: Hugging Face model ID (e.g. ``"facebook/hubert-base-ls960"``).
        num_classes: Number of output classes.
        mode: ``"frozen_encoder"`` or ``"finetune"``.
        classification_head: ``"linear"`` or ``"mlp"``.
        dropout: Dropout probability.

    Note:
        To be implemented after Wav2Vec2 pipeline is validated.
    """

    def __init__(
        self,
        backbone_name: str = "facebook/hubert-base-ls960",
        num_classes: int = 2,
        mode: str = "finetune",
        classification_head: str = "linear",
        dropout: float = 0.1,
    ) -> None:
        raise NotImplementedError
