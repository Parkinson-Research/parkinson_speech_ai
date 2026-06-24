"""Factory function for building scikit-learn classifier pipelines."""

from sklearn.pipeline import Pipeline
from omegaconf import DictConfig


def build_classifier(model_cfg: DictConfig) -> Pipeline:
    """Build a scikit-learn Pipeline from a model config section.

    The pipeline includes a scaler and the configured classifier.
    Hyperparameter tuning is handled separately in the trainer.

    Args:
        model_cfg: The ``model`` section of a config file, loaded via OmegaConf.
            Must contain a ``classifier`` key and a matching sub-key with
            classifier-specific hyperparameters.

    Returns:
        A scikit-learn Pipeline instance ready for fitting.

    Raises:
        ValueError: If ``model_cfg.classifier`` is not a supported classifier type.

    Example:
        >>> from omegaconf import OmegaConf
        >>> cfg = OmegaConf.load("configs/svm_italian_mfcc.yaml")
        >>> pipeline = build_classifier(cfg.model)
    """
    raise NotImplementedError
