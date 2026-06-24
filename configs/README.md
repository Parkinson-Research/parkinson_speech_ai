# Configs

This directory contains YAML configuration files for all experiments. Each file fully specifies a single experiment run — no parameters are hardcoded in source.

## Naming Convention

```
{model_type}_{dataset}_{variant}.yaml
```

Examples:
- `wav2vec2_italian_finetune.yaml`
- `svm_mdvrkcl_mfcc.yaml`
- `hubert_italian_frozen.yaml`
- `xgboost_mdvrkcl_egemaps.yaml`

## Loading Configs

Configs are loaded using Hydra or OmegaConf:

```python
from omegaconf import OmegaConf

cfg = OmegaConf.load("configs/wav2vec2_italian_finetune.yaml")
print(cfg.training.learning_rate)
```

Or via the CLI scripts:

```bash
python scripts/train.py --config configs/wav2vec2_italian_finetune.yaml
```

## Config Sections

Every config file should contain these top-level sections:

| Section | Description |
|---------|-------------|
| `experiment` | Name, seed, output directory |
| `data` | Dataset name, manifest path, label column |
| `preprocessing` | Sample rate, normalisation, silence trimming |
| `model` | Model type, backbone, head architecture |
| `training` | Epochs, batch size, LR, optimiser settings |
| `evaluation` | CV folds, metrics, bootstrap settings |
| `tracking` | MLflow experiment name, artifact logging |

See `docs/pipeline_design.md` for a full annotated example.
