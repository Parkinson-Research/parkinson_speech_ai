"""WavLM fine-tuning model for Parkinson's Disease classification."""


class WavLMForPDClassification:
    """WavLM model with a binary classification head for PD detection.

    Args:
        backbone_name: Hugging Face model ID
            (e.g. ``"microsoft/wavlm-base"`` or ``"microsoft/wavlm-base-plus"``).
        num_classes: Number of output classes.
        mode: ``"frozen_encoder"`` or ``"finetune"``.
        classification_head: ``"linear"`` or ``"mlp"``.
        dropout: Dropout probability.

    Note:
        To be implemented after HuBERT pipeline is validated.
    """

    def __init__(
        self,
        backbone_name: str = "microsoft/wavlm-base",
        num_classes: int = 2,
        mode: str = "finetune",
        classification_head: str = "linear",
        dropout: float = 0.1,
    ) -> None:
        raise NotImplementedError
