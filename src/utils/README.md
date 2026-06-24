# src/utils

Shared utilities used across all pipeline modules. Import from here rather than duplicating logic in individual modules.

## Modules

| Module | Responsibility |
|--------|---------------|
| `config.py` | Load YAML configs via OmegaConf |
| `logging_utils.py` | Consistent logger setup with timestamps |
| `reproducibility.py` | Seed all random sources (Python, NumPy, PyTorch) |
| `paths.py` | Resolve project-relative paths programmatically |

## Usage

```python
from src.utils import load_config, get_logger, set_seed

logger = get_logger(__name__)
set_seed(42)
cfg = load_config("configs/wav2vec2_italian_finetune.yaml")
logger.info("Config loaded: %s", cfg.experiment.name)
```
