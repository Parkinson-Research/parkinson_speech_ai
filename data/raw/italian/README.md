# data/raw/italian

Raw, unmodified recordings for the Italian Speech Dataset.

## Expected Structure

```
data/raw/italian/
├── PD/
│   └── {subject_id}/
│       ├── vowel_a.wav
│       ├── vowel_e.wav
│       ├── vowel_i.wav
│       └── running_speech.wav
└── HC/
    └── {subject_id}/
        ├── vowel_a.wav
        ├── vowel_e.wav
        ├── vowel_i.wav
        └── running_speech.wav
```

## Getting the Data

This directory is managed by DVC. After configuring your credentials:

```bash
dvc pull data/raw/italian
```

## Adding New Files

```bash
# After placing files in this directory:
dvc add data/raw/italian
git add data/raw/italian.dvc
git commit -m "data(italian): add raw recordings v1.0"
dvc push
```

## Notes

- Do NOT commit audio files to Git.
- Do NOT modify files in this directory — it is the source-of-truth for raw data.
- All preprocessing reads from here and writes to `data/processed/italian/`.
- See `docs/datasets.md` for the full dataset specification.
