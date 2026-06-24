# src/datasets

Dataset abstraction layer. All dataset classes implement the same `BaseAudioDataset` interface so that the rest of the pipeline (training, evaluation, cross-corpus experiments) is completely dataset-agnostic.

## Modules

| Module | Responsibility |
|--------|---------------|
| `base_dataset.py` | Abstract base class defining the dataset interface |
| `italian_dataset.py` | Dataset class for the Italian Speech Dataset |
| `mdvrkcl_dataset.py` | Dataset class for the MDVR-KCL Dataset |
| `collator.py` | Custom collate function for DataLoader batching (padding) |

## Interface Contract

Every dataset returns samples as a dictionary:

```python
{
    "waveform":   np.ndarray,   # 1-D float32, normalised to [-1, 1]
    "sample_rate": int,          # always 16000 after preprocessing
    "label":      int,           # 0 = HC, 1 = PD
    "subject_id": str,           # anonymised subject identifier
    "file_path":  str,           # path to the processed audio file
}
```

## Usage

```python
from src.datasets import ItalianSpeechDataset
from torch.utils.data import DataLoader
from src.datasets.collator import pad_collate_fn

dataset = ItalianSpeechDataset(
    manifest_path="data/processed/italian_manifest.csv",
    task_filter="sustained_vowel_a",
)

loader = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True,
    collate_fn=pad_collate_fn,
)
```
