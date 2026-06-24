# data/raw/mdvr_kcl

Raw, unmodified recordings for the MDVR-KCL (Mobile Device Voice Recordings at King's College London) Dataset.

## Expected Structure

```
data/raw/mdvr_kcl/
├── PD/
│   └── {subject_id}/
│       ├── reading.wav
│       └── spontaneous.wav
└── HC/
    └── {subject_id}/
        ├── reading.wav
        └── spontaneous.wav
```

## Getting the Data

This directory is managed by DVC. After configuring your credentials:

```bash
dvc pull data/raw/mdvr_kcl
```

## Adding New Files

```bash
dvc add data/raw/mdvr_kcl
git add data/raw/mdvr_kcl.dvc
git commit -m "data(mdvr-kcl): add raw recordings v1.0"
dvc push
```

## Reference

Jaeger, H., et al. (2019). *Detecting Parkinson's Disease from Continuous Speech Using Deep Learning*. Interspeech 2019.

## Notes

- Contains both controlled-environment and home-environment recordings.
- Original sample rates vary — preprocessing pipeline resamples to 16 kHz.
- See `docs/datasets.md` for the full dataset specification.
