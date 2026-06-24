# outputs

All generated artefacts. This directory is **gitignored** — use DVC or MLflow for artefact versioning.

## Structure

```
outputs/
├── models/     # Trained model checkpoints (.pt, .pkl, .onnx)
├── reports/    # Evaluation reports (CSV, JSON, HTML)
└── figures/    # Visualisation outputs (PNG, SVG)
```

## Artefact Tracking

- Model checkpoints are logged to MLflow (`mlruns/`) with the experiment run that produced them.
- Use `mlflow ui` to browse experiments and download artefacts.
- ONNX exports are placed in `outputs/models/{experiment_name}/model.onnx`.
