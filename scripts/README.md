# scripts

CLI entry-point scripts. All scripts accept a `--config` argument pointing to a YAML file in `configs/`.

| Script | Purpose |
|--------|---------|
| `preprocess.py` | Run preprocessing pipeline and generate manifest CSV |
| `train.py` | Train a model (traditional or transformer) |
| `evaluate.py` | Evaluate a trained model; supports cross-corpus mode |

## Typical Workflow

```bash
# 1. Preprocess raw data
python scripts/preprocess.py --dataset italian --config configs/svm_italian_mfcc.yaml

# 2. Train a model
python scripts/train.py --config configs/svm_italian_mfcc.yaml

# 3. Evaluate
python scripts/evaluate.py \
    --config configs/svm_italian_mfcc.yaml \
    --checkpoint outputs/models/svm_italian_mfcc/best_model.pkl
```
