# Contributing to Parkinson Speech AI

Thank you for contributing. This document defines every workflow convention team members must follow to keep the repository clean, reviewable, and reproducible.

---

## Table of Contents

1. [Branch Strategy](#branch-strategy)
2. [Commit Message Conventions](#commit-message-conventions)
3. [Pull Request Process](#pull-request-process)
4. [Dataset Versioning Rules](#dataset-versioning-rules)
5. [DVC Workflow](#dvc-workflow)
6. [MLflow Workflow](#mlflow-workflow)
7. [Code Style Guidelines](#code-style-guidelines)
8. [Documentation Expectations](#documentation-expectations)
9. [Testing Requirements](#testing-requirements)

---

## Branch Strategy

### Branch Hierarchy

```
main        ← protected, tagged releases only (never commit directly)
  └─ develop  ← integration branch, CI must pass before any merge
       ├─ feature/<feature-name>     ← new features or model components
       ├─ bugfix/<bug-description>   ← bug fixes
       ├─ research/<experiment-name> ← exploratory work (may not merge)
       ├─ data/<dataset-name>        ← dataset additions or updates
       ├─ docs/<topic>               ← documentation only
       ├─ refactor/<description>     ← code restructure, no behaviour change
       ├─ test/<description>         ← adding or fixing tests
       └─ ci/<description>           ← CI/CD changes
```

### Rules

- **Never commit directly to `main` or `develop`.**
- Branch from `develop` for all work.
- Use lowercase and hyphens only — no underscores, no camelCase.
- Keep names short (3–5 words max).

### Examples

```bash
feature/wav2vec2-finetuning
bugfix/mfcc-extraction-nan-values
research/hubert-layer-probing
data/italian-dataset-v1
docs/dvc-setup-guide
```

### Creating a branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/my-feature
```

---

## Commit Message Conventions

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification.

```
<type>(optional scope): <short summary>

[optional body — explain WHY, not WHAT]

[optional footer — Closes #issue, Breaking-Change: ...]
```

### Types

| Type | Purpose |
|------|---------|
| `feat` | New feature or pipeline component |
| `fix` | Bug fix |
| `data` | Dataset additions, updates, or DVC changes |
| `docs` | Documentation only |
| `style` | Formatting (no logic change) |
| `refactor` | Restructure without behaviour change |
| `test` | New or updated tests |
| `ci` | CI/CD configuration |
| `chore` | Maintenance (dependency updates, cleanup) |
| `exp` | Experimental change not yet production-ready |

### Examples

```
feat(models): add Wav2Vec2 classification head
fix(preprocessing): handle NaN values in MFCC extraction
data(italian): add 10 new PD subjects — update to v1.1
docs(mlflow): add experiment tracking setup guide
exp(research): probe HuBERT layer representations
```

### Rules

- Summary line ≤ 72 characters.
- Use the imperative mood: "add", "fix" — not "added" or "adding".
- Reference issues in the footer: `Closes #12`.

---

## Pull Request Process

1. **Branch from `develop`**, not from `main`.

2. **Make focused commits** — one logical change per commit.

3. **Push and open a PR** against `develop`:
   ```bash
   git push -u origin feature/my-feature
   ```

4. **Fill out the PR template** completely — no blank sections.

5. **Ensure CI passes** before requesting review.

6. **Request review** from at least one team member.

7. **Address all review comments** explicitly before merging.

8. **Squash merge** to keep `develop` history linear.

9. **`main` merges** happen only from `develop` via a team-reviewed PR, for stable milestones, tagged with a version.

### PR Checklist

- [ ] `black`, `isort`, `ruff` pass (`pre-commit run --all-files`)
- [ ] `mypy` passes (or missing stubs documented in the PR)
- [ ] `pytest tests/ -m "not integration"` passes
- [ ] New behaviour is covered by at least one test
- [ ] New functions and classes have Google-style docstrings
- [ ] No hardcoded paths, credentials, or magic numbers
- [ ] Config changes are documented in `configs/README.md`
- [ ] Experiment results logged to `docs/experiments/`
- [ ] No dataset files or secrets in the diff (check `git diff --stat`)

---

## Dataset Versioning Rules

Datasets are managed with DVC. **No audio files, CSV manifests, or model checkpoints are ever committed to Git.**

### Rules

1. Any new dataset or dataset update **must be tracked with DVC** before being pushed.
2. Dataset changes require a `data/` branch and a `data(...)` commit message.
3. The dataset version (DVC pointer) and the code that uses it must be committed together.
4. Always include a `README.md` in each new dataset directory describing its contents.
5. Register new datasets in `configs/dataset.yaml`.

### Dataset versioning workflow

```bash
# Add new data
dvc add data/raw/italian
git add data/raw/italian.dvc .gitignore
git commit -m "data(italian): add 10 new PD subjects — v1.1"
dvc push
git push
```

### Checking out a historical data version

```bash
git checkout <commit-sha>   # Go to the commit with the data version you need
dvc checkout                # Restore the matching data from DVC cache
```

---

## DVC Workflow

See `docs/dvc_setup.md` for the full setup guide.

### Essential commands

| Task | Command |
|------|---------|
| Pull latest data | `dvc pull` |
| Check data status | `dvc status` |
| Track new data | `dvc add data/raw/<dataset>` |
| Push data to remote | `dvc push` |
| Restore cached data | `dvc checkout` |
| Inspect remote | `dvc remote list` |

### DVC configuration files

| File | Purpose | Committed? |
|------|---------|-----------|
| `.dvc/config` | Remote URL, defaults | ✅ Yes |
| `.dvc/config.local` | Credentials (username, token) | ❌ No — gitignored |
| `.dvc/config.local.example` | Template for config.local | ✅ Yes |
| `*.dvc` | Data pointer files | ✅ Yes |
| `dvc.yaml` | Pipeline definition (future) | ✅ Yes |
| `dvc.lock` | Pipeline lock file | ✅ Yes |

---

## MLflow Workflow

See `docs/mlflow_setup.md` for the full setup guide.

### Before running experiments

1. Ensure `.env` is configured with `MLFLOW_TRACKING_URI` and credentials.
2. Call `load_env()` at the start of any training script.
3. Use `setup_mlflow(experiment_name=...)` (from `src/utils/mlflow_utils.py`) before logging anything.

### Required logging per run

Every experiment run **must log**:
- All config parameters via `log_params(cfg)`
- All evaluation metrics (per-fold and aggregated) via `log_metrics(results)`
- The trained model artefact via `log_model(model, ...)`
- A git commit tag so the code version is traceable

### After a run

Document the result in `docs/experiments/<dataset>/` using the template from the directory `README.md`:

```bash
git add docs/experiments/
git commit -m "docs(experiments): log SVM-MFCC Italian v1 — AUC-ROC 0.93"
```

---

## Code Style Guidelines

### Toolchain

| Tool | Purpose | Config location |
|------|---------|----------------|
| `black` | Auto-formatter | `pyproject.toml` |
| `isort` | Import sorting | `pyproject.toml` |
| `ruff` | Linter | `pyproject.toml` |
| `mypy` | Static type checking | `pyproject.toml` |
| `pre-commit` | Git hook runner | `.pre-commit-config.yaml` |

### Running checks

```bash
# All checks at once (same as pre-commit)
pre-commit run --all-files

# Individual tools
black src/ tests/ scripts/
isort src/ tests/ scripts/
ruff check src/ tests/ scripts/
mypy src/
```

### Python rules

- **Python 3.10+** — use union types (`X | Y`) and `match` statements.
- **Type annotations required** on all function signatures.
- **Google-style docstrings** required for all public functions and classes.
- Maximum line length: **88 characters** (Black default).
- No wildcard imports (`from module import *`).
- No hardcoded paths — use `src/utils/paths.py`.
- No hardcoded credentials — use `src/utils/config.get_env()`.

### Docstring template

```python
def extract_mfcc(
    audio: np.ndarray,
    sample_rate: int,
    n_mfcc: int = 40,
) -> np.ndarray:
    """Extract MFCC features from an audio array.

    Args:
        audio: 1-D numpy array of audio samples.
        sample_rate: Sampling rate in Hz.
        n_mfcc: Number of MFCC coefficients to extract.

    Returns:
        2-D numpy array of shape (n_mfcc, time_frames).

    Raises:
        ValueError: If audio is empty or contains NaN values.
    """
```

---

## Documentation Expectations

- Every new Python package (folder) needs a `README.md`.
- Every new Python file needs a module-level docstring.
- All experiments must be tracked in MLflow **and** documented in `docs/experiments/`.
- No print-only experiment tracking — use `src/utils/mlflow_utils.py`.
- Notebooks must be stripped of outputs before committing (enforced by pre-commit).
- Architecture changes must be reflected in `docs/architecture.md`.
- Dataset format changes must be reflected in `docs/datasets.md`.
- New configuration parameters must be documented in the relevant YAML config file.

---

## Testing Requirements

- Unit tests live in `tests/` and mirror the `src/` structure.
- Test runner: `pytest`
- Minimum coverage: **70%** for `src/`
- Tests must use synthetic fixtures — never real patient data.
- Integration tests (GPU, real data): `@pytest.mark.integration`

```bash
# Fast unit tests only
pytest tests/ -m "not integration and not gpu"

# All tests
pytest tests/

# With coverage
pytest tests/ --cov=src --cov-report=html
```
