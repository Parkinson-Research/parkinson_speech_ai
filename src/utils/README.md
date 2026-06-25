# src/utils

Shared utility modules used across all pipeline components. Import from here — do not reimplement these in individual modules.

## Modules

| Module | Responsibility |
|--------|---------------|
| `logger.py` | Structured logger — console + optional rotating file handler, respects `LOG_LEVEL` env var |
| `seed.py` | `set_seed()` + `temporary_seed()` context manager — seeds Python, NumPy, PyTorch, Transformers |
| `config.py` | `load_config()`, `load_configs()` (merge), `apply_overrides()`, `get_env()` — loads `.env` via dotenv |
| `paths.py` | All project paths as functions — respects `DATA_ROOT` and `OUTPUTS_ROOT` env vars |
| `device.py` | PyTorch device detection — CUDA > MPS > CPU, with logging and info dict |
| `mlflow_utils.py` | MLflow helpers — `setup_mlflow()`, `log_params()`, `log_metrics()`, `log_model()` (stubs) |
| `logging_utils.py` | Legacy alias for `logger.py` — kept for backwards compatibility |
| `reproducibility.py` | Legacy alias for `seed.py` — kept for backwards compatibility |

## Usage

```python
from src.utils import (
    get_logger,
    set_seed,
    load_config,
    load_configs,
    get_env,
    get_device,
    get_raw_dir,
    get_models_dir,
    ensure_dirs,
)

# Logging
logger = get_logger(__name__)
logger.info("Pipeline started")

# Reproducibility
set_seed(42)

# Config
cfg = load_configs("configs/training.yaml", "configs/svm_italian_mfcc.yaml")
token = get_env("DAGSHUB_TOKEN", required=True)

# Paths
raw_path = get_raw_dir("italian")
model_dir = get_models_dir("svm_italian_mfcc")
ensure_dirs(model_dir)

# Device
device = get_device()
model = model.to(device)
```

## Environment Variables

| Variable | Used by | Default |
|----------|---------|---------|
| `LOG_LEVEL` | `logger.py` | `INFO` |
| `DATA_ROOT` | `paths.py` | `<project_root>/data` |
| `OUTPUTS_ROOT` | `paths.py` | `<project_root>/outputs` |
| `MLFLOW_TRACKING_URI` | `mlflow_utils.py` | `mlruns` |
| `DAGSHUB_USERNAME` | `mlflow_utils.py` | — |
| `DAGSHUB_TOKEN` | `mlflow_utils.py` | — |

Set these in `.env` (see `.env.example`).
