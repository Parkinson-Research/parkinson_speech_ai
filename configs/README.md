# configs

All experiment and infrastructure configuration files. No parameters are hardcoded in source code — everything is configurable here.

## Config Files

### Infrastructure (shared across experiments)

| File | Purpose |
|------|---------|
| `paths.yaml` | All directory paths — data, outputs, logs, mlruns |
| `dataset.yaml` | Dataset registry, manifest schema, split config |
| `training.yaml` | Shared training defaults (CV folds, seeds, scheduler) |
| `model.yaml` | Model registry and default hyperparameters |
| `mlflow.yaml` | MLflow tracking URI, experiment names, logging flags |

### Experiment configs (one per run)

| File | Pipeline | Dataset |
|------|----------|---------|
| `svm_italian_mfcc.yaml` | SVM + MFCC | Italian |
| `xgboost_mdvrkcl_egemaps.yaml` | XGBoost + eGeMAPS | MDVR-KCL |
| `wav2vec2_italian_finetune.yaml` | Wav2Vec2 fine-tuning | Italian |

## Naming Convention

```
{model_type}_{dataset}_{variant}.yaml
```

Examples: `hubert_italian_finetune.yaml`, `svm_mdvrkcl_mfcc.yaml`

## Loading Configs

### Single config

```python
from src.utils import load_config
cfg = load_config("configs/wav2vec2_italian_finetune.yaml")
```

### Merged configs (base + experiment override)

```python
from src.utils import load_configs
cfg = load_configs(
    "configs/training.yaml",
    "configs/model.yaml",
    "configs/wav2vec2_italian_finetune.yaml",  # overrides win
)
```

### CLI overrides

```python
from src.utils import apply_overrides
cfg = apply_overrides(cfg, ["training.epochs=30", "model.dropout=0.2"])
```

### Via CLI scripts

```bash
python scripts/train.py --config configs/wav2vec2_italian_finetune.yaml \
    --override training.epochs=30
```

## Environment Variable Interpolation

Config values can reference environment variables using OmegaConf syntax:

```yaml
mlflow:
  tracking_uri: ${oc.env:MLFLOW_TRACKING_URI,mlruns}
```

This reads `MLFLOW_TRACKING_URI` from the environment and falls back to `mlruns` if unset.

## Required Sections in Every Experiment Config

| Section | Description |
|---------|-------------|
| `experiment` | Name, seed, output directory |
| `data` | Dataset name, manifest path, label/ID columns |
| `preprocessing` | Sample rate, normalisation, silence trimming |
| `model` | Model type, backbone/classifier, head config |
| `training` | Epochs/HPO, batch size, LR, optimiser settings |
| `evaluation` | CV folds, metrics, bootstrap settings |
| `tracking` | MLflow experiment name, logging flags |
