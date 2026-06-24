# data

This directory holds all dataset files. Raw and processed data are **not tracked by Git** (see `.gitignore`). Use DVC for data versioning and sharing.

## Directory Structure

```
data/
├── raw/           # Original, unmodified recordings — never alter these
├── processed/     # Preprocessed audio and manifest CSV files
└── README.md
```

## Data Access

All data is managed with DVC. After configuring the DVC remote:

```bash
# Pull all data
dvc pull

# Pull a specific dataset
dvc pull data/raw/italian.dvc
```

Contact the project lead for DVC remote credentials.

## Manifest Format

Processed datasets are described by manifest CSV files in `data/processed/`. See `docs/datasets.md` for the full schema.

```
data/processed/
├── italian_manifest.csv
└── mdvrkcl_manifest.csv
```

## Ethics and Privacy

- All subject identifiers are anonymised (e.g., `PD_001`, `HC_042`).
- No raw patient data is committed to this repository.
- Data use is governed by each dataset's original data use agreement.
- Do not share data outside the team without written permission from the data custodian.
