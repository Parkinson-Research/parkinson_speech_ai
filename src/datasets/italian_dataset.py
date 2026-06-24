"""Dataset class for the Italian Speech Dataset."""

from pathlib import Path
from typing import Any

from src.datasets.base_dataset import BaseAudioDataset


class ItalianSpeechDataset(BaseAudioDataset):
    """PyTorch-compatible Dataset for the Italian Parkinson's Speech Dataset.

    Expected manifest columns: subject_id, label, file_path, sample_rate,
    duration_sec, task, gender, age, dataset.

    Args:
        manifest_path: Path to the Italian dataset manifest CSV.
        preprocessing_pipeline: Optional preprocessing pipeline instance.
        task_filter: Filter to a specific speech task (e.g., "sustained_vowel_a").
        transform: Optional waveform transform callable.

    Example:
        >>> dataset = ItalianSpeechDataset("data/processed/italian_manifest.csv")
        >>> sample = dataset[0]
        >>> print(sample["label"], sample["waveform"].shape)
    """

    DATASET_NAME = "italian"
    REQUIRED_COLUMNS = ["subject_id", "label", "file_path", "sample_rate"]

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, index: int) -> dict[str, Any]:
        raise NotImplementedError

    @property
    def labels(self) -> list[int]:
        raise NotImplementedError

    @property
    def subject_ids(self) -> list[str]:
        raise NotImplementedError
