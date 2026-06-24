"""CLI entry point for running the preprocessing pipeline on a raw dataset.

Usage:
    python scripts/preprocess.py --dataset italian --config configs/svm_italian_mfcc.yaml
    python scripts/preprocess.py --dataset mdvrkcl --config configs/xgboost_mdvrkcl_egemaps.yaml
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preprocess a raw dataset and generate a manifest CSV."
    )
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        choices=["italian", "mdvrkcl"],
        help="Dataset to preprocess.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Config file specifying preprocessing parameters.",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=None,
        help="Override the raw data directory. Defaults to data/raw/{dataset}/.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Override the output directory. Defaults to data/processed/.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    from src.utils import load_config, get_logger

    cfg = load_config(args.config)
    logger = get_logger(__name__)

    logger.info("Preprocessing dataset: %s", args.dataset)

    # TODO: Implement preprocessing pipeline invocation
    raise NotImplementedError("Preprocessing script not yet implemented.")


if __name__ == "__main__":
    main()
