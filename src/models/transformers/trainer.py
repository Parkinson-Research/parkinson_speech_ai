"""PyTorch training loop for transformer-based PD classification models."""

from typing import Any


class TransformerTrainer:
    """Manages training, evaluation, and checkpointing for transformer models.

    Wraps either Hugging Face ``Trainer`` or a custom PyTorch training loop.
    Supports mixed-precision training, gradient clipping, warmup scheduling,
    early stopping, and MLflow experiment tracking.

    Args:
        model: Instantiated transformer classification model.
        config: Full experiment config loaded via OmegaConf.
        train_dataset: Training dataset instance.
        eval_dataset: Validation dataset instance.

    Example:
        >>> trainer = TransformerTrainer(model, cfg, train_ds, eval_ds)
        >>> trainer.train()
    """

    def __init__(
        self,
        model: Any,
        config: Any,
        train_dataset: Any,
        eval_dataset: Any,
    ) -> None:
        raise NotImplementedError

    def train(self) -> dict[str, float]:
        """Run the full training loop.

        Returns:
            Dictionary of final evaluation metrics on the validation set.
        """
        raise NotImplementedError

    def evaluate(self, dataset: Any) -> dict[str, float]:
        """Evaluate the model on a given dataset.

        Args:
            dataset: A BaseAudioDataset instance.

        Returns:
            Dictionary of evaluation metrics.
        """
        raise NotImplementedError

    def save_checkpoint(self, output_dir: str) -> None:
        """Save model weights and tokenizer to output_dir.

        Args:
            output_dir: Directory path for saving the checkpoint.
        """
        raise NotImplementedError
