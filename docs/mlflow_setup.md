# MLflow Setup Guide

This project uses [MLflow](https://mlflow.org) for experiment tracking, metric logging, and model registration. The MLflow tracking server is hosted on DagsHub, giving the entire team a shared view of all experiments.

---

## Tracking Modes

| Mode | When to use | Tracking URI |
|------|-------------|--------------|
| **Local** | Solo development, no internet | `mlruns/` (default) |
| **DagsHub** | Team collaboration, shared results | `https://dagshub.com/Parkinson-Research/parkinson_speech_ai.mlflow` |

---

## Prerequisites

- MLflow installed (`pip install mlflow==2.13.2` — in `requirements.txt`)
- DagsHub credentials configured (see `docs/dagshub_setup.md`)
- Environment variables set in `.env`

---

## Local Setup (Development)

No configuration needed. MLflow automatically uses `mlruns/` in the project root.

```bash
# Start the local MLflow UI
mlflow ui --backend-store-uri mlruns/ --port 5000
```

Open: http://localhost:5000

---

## DagsHub Setup (Team Collaboration)

### 1. Set environment variables in `.env`

```ini
MLFLOW_TRACKING_URI=https://dagshub.com/Parkinson-Research/parkinson_speech_ai.mlflow
MLFLOW_TRACKING_USERNAME=your_dagshub_username
MLFLOW_TRACKING_PASSWORD=your_dagshub_token
```

### 2. Load credentials before running any experiment

```python
from src.utils.config import load_env
load_env()  # Reads .env into os.environ
```

### 3. Initialise via DagsHub SDK (recommended)

```python
import dagshub
dagshub.init(
    repo_owner="Parkinson-Research",
    repo_name="parkinson_speech_ai",
    mlflow=True,
)
```

This automatically sets the tracking URI and authenticates.

---

## Experiment Structure

All experiments are organised into named MLflow experiments:

| MLflow Experiment | Pipeline | Dataset |
|------------------|----------|---------|
| `parkinson_speech_ai_traditional_italian` | SVM / RF / XGBoost | Italian |
| `parkinson_speech_ai_traditional_mdvrkcl` | SVM / RF / XGBoost | MDVR-KCL |
| `parkinson_speech_ai_transformer_italian` | Wav2Vec2 / HuBERT / WavLM | Italian |
| `parkinson_speech_ai_transformer_mdvrkcl` | Wav2Vec2 / HuBERT / WavLM | MDVR-KCL |
| `parkinson_speech_ai_cross_corpus` | All models | Cross-dataset |
| `parkinson_speech_ai_baselines` | Majority class, etc. | Both |

These are configured in `configs/mlflow.yaml`.

---

## What Gets Logged Per Run

Every training run automatically logs:

**Parameters**
- All config values (flattened with dot notation): `training.epochs`, `model.backbone`, etc.

**Metrics** (per fold + aggregated)
- `auc_roc`, `auc_roc_mean`, `auc_roc_std`
- `sensitivity`, `specificity`, `f1`, `mcc`, `accuracy`
- `auc_roc_ci_lower`, `auc_roc_ci_upper` (bootstrap 95% CI)

**Artefacts**
- Model checkpoint (`.pt` / `.pkl`)
- Evaluation report (`.json`)
- Confusion matrix figure
- SHAP summary plot (traditional) / attention map (transformer)

**Tags**
- `project`: `parkinson_speech_ai`
- `framework_version`: `0.1.0`
- `git_commit`: HEAD SHA
- `team_member`: set by the runner

---

## Viewing Experiments

### DagsHub UI (shared)

Visit: https://dagshub.com/Parkinson-Research/parkinson_speech_ai.mlflow

### Local UI

```bash
mlflow ui --backend-store-uri mlruns/ --port 5000
```

### Programmatic comparison

```python
from src.utils.mlflow_utils import compare_runs

df = compare_runs(
    experiment_name="parkinson_speech_ai_traditional_italian",
    metrics=["auc_roc", "sensitivity", "specificity"],
)
print(df.sort_values("auc_roc", ascending=False))
```

---

## Model Registry

The best model from each pipeline is registered in the MLflow Model Registry under `parkinson_speech_ai`.

```
parkinson_speech_ai
├── staging      ← current best candidate
└── production   ← validated, deployment-ready
```

To register a model programmatically (via `src/utils/mlflow_utils.py`):

```python
log_model(model, model_name="wav2vec2_italian", framework="pytorch", register=True)
```

---

## Configuration Reference

All MLflow settings are in `configs/mlflow.yaml`. The tracking URI is read from the `MLFLOW_TRACKING_URI` environment variable at runtime, with `mlruns/` as fallback.

---

## Further Reading

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [MLflow + DagsHub](https://dagshub.com/docs/integration_guide/mlflow_tracking/)
- See also: `docs/dagshub_setup.md`, `src/utils/mlflow_utils.py`
