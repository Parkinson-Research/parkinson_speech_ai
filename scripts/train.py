"""CLI entry point for training a model from a config file.

Usage:
    python scripts/train.py --config configs/wav2vec2_italian_finetune.yaml
    python scripts/train.py --config configs/svm_italian_mfcc.yaml
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train a PD detection model from a YAML config file."
    )
    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Path to the experiment YAML config file.",
    )
    parser.add_argument(
        "--override",
        nargs="*",
        default=[],
        help="Override config values in key=value format. E.g. training.epochs=30",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    from src.utils import load_config, get_logger, set_seed

    cfg = load_config(args.config)
    logger = get_logger(__name__)
    set_seed(cfg.experiment.seed)

    logger.info("Starting experiment: %s", cfg.experiment.name)
    logger.info("Model type: %s", cfg.model.type)

    if cfg.model.type == "traditional":
        # TODO: Wire up traditional ML training pipeline
        raise NotImplementedError("Traditional ML training not yet implemented.")
    elif cfg.model.type == "transformer":
        # TODO: Wire up transformer training pipeline
        raise NotImplementedError("Transformer training not yet implemented.")
    else:
        raise ValueError(f"Unknown model type: {cfg.model.type}")


if __name__ == "__main__":
    main()
