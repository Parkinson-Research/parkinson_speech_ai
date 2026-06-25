# docs/experiments/transformers

Experiment logs, notes, and result summaries for all transformer-based experiments (Wav2Vec2, HuBERT, WavLM) across both datasets.

## Structure

```
docs/experiments/transformers/
├── README.md                          ← this file
├── wav2vec2_italian_finetune_v1.md
├── wav2vec2_mdvrkcl_finetune_v1.md
├── wav2vec2_cross_corpus_v1.md
├── hubert_italian_finetune_v1.md      ← phase 2
└── wavlm_italian_finetune_v1.md       ← phase 2
```

## Experiment Log Template

```markdown
# Experiment: {name}

**Date:** YYYY-MM-DD
**Author:** Member 3
**MLflow Run ID:** abc123
**Config:** configs/{config_file}.yaml

## Setup
- Dataset: Italian | MDVR-KCL | Cross-corpus
- Backbone: facebook/wav2vec2-base | ...
- Mode: frozen_encoder | finetune
- Classification head: linear | mlp

## Training
- Epochs: N (early stop at epoch M)
- Best val AUC-ROC: ...
- Training time: ...h ...m

## Test Results

| Metric | Mean | Std | 95% CI |
|--------|------|-----|--------|
| AUC-ROC | | | |
| Sensitivity | | | |
| Specificity | | | |
| F1 | | | |

## Attention Analysis
- Dominant attended regions: ...

## Key Observations
- ...

## Comparison to Traditional Baseline
| Model | AUC-ROC | p-value (McNemar) |
|-------|---------|-------------------|
| Wav2Vec2 | | |
| SVM + MFCC | | |

## Next Steps
- ...
```
