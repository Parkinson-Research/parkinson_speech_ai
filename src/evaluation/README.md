# src/evaluation

Shared evaluation utilities used by both the traditional ML and transformer pipelines. Centralising evaluation here ensures fair, consistent comparisons across all models.

## Modules

| Module | Responsibility |
|--------|---------------|
| `metrics.py` | AUC-ROC, sensitivity, specificity, F1, MCC, accuracy |
| `cross_validation.py` | Stratified, speaker-independent k-fold splits |
| `statistical_tests.py` | McNemar's test for pairwise model comparison |

## Primary Metric

**AUC-ROC** — threshold-independent, robust to class imbalance, and standard in clinical ML literature.

## Usage

```python
from src.evaluation.metrics import compute_metrics, bootstrap_ci

metrics = compute_metrics(y_true, y_pred, y_prob)
ci = bootstrap_ci(y_true, y_prob, metric="auc_roc", n_bootstrap=1000)
print(f"AUC-ROC: {metrics['auc_roc']:.3f} "
      f"[{ci['lower']:.3f}, {ci['upper']:.3f}]")
```

## Notes

- All results are logged to MLflow automatically via the trainer classes.
- Bootstrap CIs use stratified resampling to preserve class balance.
- McNemar's test requires predictions from both models on the **same** test folds.
