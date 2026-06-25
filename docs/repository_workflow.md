# Repository Workflow

This document describes the end-to-end workflow for every collaborator — from cloning the repository to completing a training run and sharing results with the team.

---

## Overview

```
Clone repo → Configure env → Pull datasets → Develop on branch →
Run experiments → Push results → Open PR → Merge to develop
```

---

## 1. Cloning the Repository

```bash
git clone https://github.com/Parkinson-Research/parkinson_speech_ai.git
cd parkinson_speech_ai
```

---

## 2. Environment Setup

### Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows
```

### Install all dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### Configure credentials

```bash
cp .env.example .env
```

Edit `.env` with your DagsHub credentials:
```ini
DAGSHUB_USERNAME=your_username
DAGSHUB_TOKEN=your_token
MLFLOW_TRACKING_URI=https://dagshub.com/Parkinson-Research/parkinson_speech_ai.mlflow
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_token
```

### Configure DVC local credentials

```bash
cp .dvc/config.local.example .dvc/config.local
# Edit .dvc/config.local — fill in your username and token
```

### Install pre-commit hooks

```bash
pre-commit install
```

---

## 3. Pulling Datasets

```bash
dvc pull
```

This fetches all tracked data from DagsHub:
- `data/raw/italian/`
- `data/raw/mdvr_kcl/`
- `data/processed/italian/`
- `data/processed/mdvr_kcl/`
- `outputs/models/` (if any checkpoints are tracked)

---

## 4. Branch Strategy

All work happens on branches — **never commit directly to `main` or `develop`**.

```
main        ← stable, tagged releases only
  └─ develop  ← integration branch, always passing CI
       ├─ feature/<name>   ← new features
       ├─ bugfix/<name>    ← bug fixes
       ├─ research/<name>  ← exploratory experiments
       ├─ data/<name>      ← dataset changes
       └─ docs/<name>      ← documentation only
```

### Creating a branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/mfcc-extraction
```

---

## 5. Development Cycle

### Running preprocessing

```bash
python scripts/preprocess.py --dataset italian --config configs/svm_italian_mfcc.yaml
```

### Running a training experiment

```bash
python scripts/train.py --config configs/svm_italian_mfcc.yaml
```

### Running evaluation

```bash
python scripts/evaluate.py \
    --config configs/svm_italian_mfcc.yaml \
    --checkpoint outputs/models/svm_italian_mfcc/best_model.pkl
```

### Checking code quality before committing

```bash
black src/ tests/ scripts/
isort src/ tests/ scripts/
ruff check src/ tests/ scripts/
mypy src/
pytest tests/ -m "not integration"
```

Pre-commit hooks run these automatically on `git commit`.

---

## 6. Dataset Versioning Workflow

### Adding a new dataset version

```bash
# Place updated files in data/raw/<dataset>/
dvc add data/raw/italian
git add data/raw/italian.dvc
git commit -m "data(italian): add 10 new PD subjects — v1.1"
dvc push
git push
```

### Pulling a specific dataset version

```bash
# Check out a historical commit
git checkout <commit-sha>
dvc checkout    # Restore the data that matches that commit
```

---

## 7. Experiment Tracking Workflow

Every training run is automatically tracked to MLflow. After a run:

1. Open the DagsHub MLflow UI:
   https://dagshub.com/Parkinson-Research/parkinson_speech_ai.mlflow

2. Find your run and copy the **Run ID**.

3. Create an experiment log in `docs/experiments/<dataset>/`:
   ```bash
   # e.g.:
   docs/experiments/italian_dataset/svm_mfcc_v1.md
   ```
   Use the template in the corresponding `README.md`.

4. Commit the experiment log:
   ```bash
   git add docs/experiments/
   git commit -m "docs(experiments): log SVM-MFCC Italian v1 results"
   ```

---

## 8. Pull Request Workflow

```bash
# Push your branch
git push -u origin feature/mfcc-extraction

# Open a PR on GitHub against `develop`
# Fill in the PR template completely
# Request review from at least one team member
# Address all comments
# Squash merge into develop
```

### PR checklist (also in `.github/PULL_REQUEST_TEMPLATE.md`)

- [ ] `black`, `isort`, `ruff` pass
- [ ] `mypy` passes (or known stubs documented)
- [ ] Tests pass: `pytest tests/ -m "not integration"`
- [ ] New code has docstrings
- [ ] `configs/` changes are documented
- [ ] Experiment logs committed to `docs/experiments/`
- [ ] No secrets or data files in the diff

---

## 9. Release Workflow (main branch)

Only the project lead merges to `main`.

```bash
# On GitHub: open a PR from develop → main
# After approval:
git checkout main
git pull origin main
git tag v0.2.0 -m "Release v0.2.0: SVM + Wav2Vec2 baselines complete"
git push origin main --tags
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Pull latest code + data | `git pull && dvc pull` |
| Run quality checks | `pre-commit run --all-files` |
| Run unit tests | `pytest tests/ -m "not integration"` |
| Start MLflow UI (local) | `mlflow ui --backend-store-uri mlruns/` |
| Check DVC status | `dvc status` |
| Add dataset to DVC | `dvc add data/raw/<dataset> && dvc push` |
| Push experiment data | `dvc push` |

---

## Further Reading

- `docs/dvc_setup.md` — DVC configuration in detail
- `docs/dagshub_setup.md` — DagsHub credentials and access
- `docs/mlflow_setup.md` — MLflow experiments and model registry
- `CONTRIBUTING.md` — Code style, commit conventions, PR process
