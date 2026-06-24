# src/models/traditional

Scikit-learn–compatible classifier pipelines for PD detection using hand-crafted acoustic features (MFCCs, prosodic, spectral, eGeMAPS).

## Modules

| Module | Responsibility |
|--------|---------------|
| `classifier_factory.py` | Factory that builds a scaler + classifier Pipeline from config |
| `trainer.py` | Cross-validation loop, hyperparameter tuning, MLflow logging |

## Supported Classifiers

| Key in config | Classifier |
|---------------|-----------|
| `svm` | Support Vector Machine (RBF / linear kernel) |
| `random_forest` | Random Forest |
| `xgboost` | XGBoost |
| `logistic_regression` | Logistic Regression (L2) |

## Usage

```python
from omegaconf import OmegaConf
from src.models.traditional import build_classifier
from src.models.traditional.trainer import TraditionalMLTrainer

cfg = OmegaConf.load("configs/svm_italian_mfcc.yaml")
pipeline = build_classifier(cfg.model)
trainer = TraditionalMLTrainer(pipeline, cfg, "parkinson_speech_ai")
results = trainer.cross_validate(X, y, groups=subject_ids)
```

## Ownership

This module is maintained by **Member 1** (Italian dataset) and **Member 2** (MDVR-KCL dataset).
