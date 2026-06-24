"""
src.datasets
============
Dataset abstraction layer — PyTorch Dataset classes and DataLoader utilities
for the Italian Speech Dataset and MDVR-KCL Dataset.
"""

from src.datasets.base_dataset import BaseAudioDataset
from src.datasets.italian_dataset import ItalianSpeechDataset
from src.datasets.mdvrkcl_dataset import MDVRKCLDataset

__all__ = ["BaseAudioDataset", "ItalianSpeechDataset", "MDVRKCLDataset"]
