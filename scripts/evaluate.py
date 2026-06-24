"""CLI entry point for evaluating a trained model.

Usage:
    python scripts/evaluate.py --config configs/wav2vec2_italian_finetune.yaml \\
        --checkpoint outputs/models/wav2vec2_italian_finetune/best_model/
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate a trained PD detection model."
    )
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument(
        "--dataset",
        type=str,
        default=None,
        help="Override the dataset in the config for cross-corpus evaluation.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    from src.utils import load_config, get_logger, set_seed

    cfg = load_config(args.config)
    logger = get_logger(__name__)
    set_seed(cfg.experiment.seed)

    logger.info("Evaluating: %s", cfg.experiment.name)
    logger.info("Checkpoint: %s", args.checkpoint)

    # TODO: Implement evaluation pipeline
    raise NotImplementedError("Evaluation pipeline not yet implemented.")


if __name__ == "__main__":
    main()
