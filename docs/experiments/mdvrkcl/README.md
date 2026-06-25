# docs/experiments/mdvrkcl

Experiment logs, notes, and result summaries for all experiments run on the MDVR-KCL Dataset.

## Structure

```
docs/experiments/mdvrkcl/
├── README.md                  ← this file
├── xgboost_egemaps_v1.md      ← XGBoost + eGeMAPS baseline
├── svm_mfcc_v1.md             ← SVM + MFCC
└── wav2vec2_finetune_v1.md    ← Wav2Vec2 fine-tune
```

## Experiment Log Template

```markdown
# Experiment: {name}

**Date:** YYYY-MM-DD
**Author:** Member N
**MLflow Run ID:** abc123
**Config:** configs/{config_file}.yaml

## Setup
- Dataset: MDVR-KCL
- Task filter: reading | spontaneous | all
- Features / Backbone: ...
- Medication state: on | off | mixed

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
