"""Abstract base class defining the dataset interface for all PD speech datasets."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import pandas as pd


class BaseAudioDataset(ABC):
    """Abstract base class for Parkinson's Disease speech datasets.

    All concrete dataset classes must inherit from this class and implement
    the required abstract methods. This ensures a consistent interface
    across datasets for use in training, evaluation, and cross-corpus experiments.

    Args:
        manifest_path: Path to the manifest CSV file.
        preprocessing_pipeline: An instantiated PreprocessingPipeline.
            If None, raw waveforms are loaded without preprocessing.
        task_filter: If specified, only include recordings matching this task.
        transform: Optional callable applied to the waveform after loading.

    Attributes:
        manifest: Pandas DataFrame loaded from manifest_path.
    """

    def __init__(
        self,
        manifest_path: str | Path,
        preprocessing_pipeline: Any = None,
        task_filter: str | None = None,
        transform: Any = None,
    ) -> None:
        self.manifest_path = Path(manifest_path)
        self.preprocessing_pipeline = preprocessing_pipeline
        self.task_filter = task_filter
        self.transform = transform
        self.manifest = self._load_manifest()

    def _load_manifest(self) -> pd.DataFrame:
        """Load and validate the manifest CSV.

        Returns:
            Validated pandas DataFrame.

        Raises:
            FileNotFoundError: If the manifest file does not exist.
            ValueError: If required columns are missing.
        """
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of samples in the dataset."""

    @abstractmethod
    def __getitem__(self, index: int) -> dict[str, Any]:
        """Return a single sample.

        Returns:
            A dictionary with at minimum:
                - ``"waveform"``: 1-D float32 numpy array
                - ``"sample_rate"``: int
                - ``"label"``: int (0 = HC, 1 = PD)
                - ``"subject_id"``: str
                - ``"file_path"``: str
        """

    @property
    def labels(self) -> list[int]:
        """Return all labels as a list, used for stratified splitting."""
        raise NotImplementedError

    @property
    def subject_ids(self) -> list[str]:
        """Return all subject IDs, used for speaker-independent splitting."""
        raise NotImplementedError
