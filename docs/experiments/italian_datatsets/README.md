# docs/experiments/italian_dataset

Experiment logs, notes, and result summaries for all experiments run on the Italian Speech Dataset.

## Structure

Each experiment gets its own markdown file named after the run:

```
docs/experiments/italian_dataset/
├── README.md               ← this file
├── svm_mfcc_v1.md          ← SVM + MFCC baseline
├── xgboost_egemaps_v1.md   ← XGBoost + eGeMAPS
└── wav2vec2_finetune_v1.md ← Wav2Vec2 fine-tune
```

## Experiment Log Template

When completing a run, create a markdown file with this structure:

```markdown
# Experiment: {name}

**Date:** YYYY-MM-DD
**Author:** Member N
**MLflow Run ID:** abc123
**Config:** configs/{config_file}.yaml

## Setup
- Dataset: Italian Speech Dataset
- Task filter: ...
- Features / Backbone: ...

## Results

| Metric | Mean | Std | 95% CI |
|--------|------|-----|--------|
| AUC-ROC | | | |
| Sensitivity | | | |
| Specificity | | | |
| F1 | | | |

## Key Observations
- ...

## Next Steps
- ...
```
