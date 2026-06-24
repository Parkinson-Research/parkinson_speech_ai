"""Dataset class for the MDVR-KCL Dataset."""

from typing import Any

from src.datasets.base_dataset import BaseAudioDataset


class MDVRKCLDataset(BaseAudioDataset):
    """PyTorch-compatible Dataset for the MDVR-KCL Parkinson's Speech Dataset.

    Expected manifest columns: subject_id, label, file_path, sample_rate,
    duration_sec, task, gender, age, medication_state, dataset.

    Args:
        manifest_path: Path to the MDVR-KCL manifest CSV.
        preprocessing_pipeline: Optional preprocessing pipeline instance.
        task_filter: Filter to a specific task (e.g., "reading", "spontaneous").
        transform: Optional waveform transform callable.

    Example:
        >>> dataset = MDVRKCLDataset("data/processed/mdvrkcl_manifest.csv")
        >>> sample = dataset[0]
        >>> print(sample["label"], sample["waveform"].shape)
    """

    DATASET_NAME = "mdvrkcl"
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
