# Contributing to Parkinson Speech AI

Thank you for contributing to this project. This document defines the workflow conventions all team members must follow to keep the repository clean, reviewable, and reproducible.

---

## Table of Contents

1. [Branch Naming Conventions](#branch-naming-conventions)
2. [Commit Message Conventions](#commit-message-conventions)
3. [Pull Request Workflow](#pull-request-workflow)
4. [Code Style Guidelines](#code-style-guidelines)
5. [Documentation Expectations](#documentation-expectations)
6. [Testing Requirements](#testing-requirements)

---

## Branch Naming Conventions

All branches must follow this pattern:

```
<type>/<short-description>
```

| Type | When to use |
|------|-------------|
| `feat/` | New feature or model pipeline |
| `fix/` | Bug fix |
| `data/` | Data processing or dataset changes |
| `exp/` | Exploratory experiment (not merged to main directly) |
| `docs/` | Documentation-only changes |
| `refactor/` | Code restructure without behaviour change |
| `test/` | Adding or updating tests |
| `ci/` | CI/CD pipeline changes |

**Examples:**
```
feat/wav2vec2-finetuning
fix/mfcc-extraction-nan-values
data/italian-dataset-preprocessing
exp/hubert-layer-probing
docs/dataset-format-spec
```

**Rules:**
- Use lowercase and hyphens only — no underscores, no camelCase.
- Keep descriptions short (3–5 words max).
- Never commit directly to `main` or `develop`. Always use a branch and open a PR.

---

## Commit Message Conventions

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification.

```
<type>(optional scope): <short summary>

[optional body]

[optional footer]
```

**Types:**

| Type | Purpose |
|------|---------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `data` | Data pipeline or dataset changes |
| `docs` | Documentation only |
| `style` | Formatting changes (no logic change) |
| `refactor` | Code restructure without behaviour change |
| `test` | Adding or modifying tests |
| `ci` | CI/CD configuration |
| `chore` | Maintenance tasks (deps update, etc.) |
| `exp` | Experimental change not yet production-ready |

**Examples:**
```
feat(models): add Wav2Vec2 classification head

fix(preprocessing): handle NaN values in MFCC extraction

data(italian): add segment-level labelling logic

docs(datasets): document MDVR-KCL file structure
```

**Rules:**
- Summary line must be ≤ 72 characters.
- Use the imperative mood: "add", "fix", "update" — not "added" or "adding".
- Reference relevant issue numbers in the footer: `Closes #12`.

---

## Pull Request Workflow

1. **Create a branch** from `develop` (not `main`):
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feat/my-feature
   ```

2. **Make focused commits** — one logical change per commit.

3. **Push your branch** and open a PR against `develop`:
   ```bash
   git push -u origin feat/my-feature
   ```

4. **Fill out the PR template** completely. Do not leave sections blank.

5. **Request review** from at least one other team member before merging.

6. **Address all review comments** before merging. Resolve conversations explicitly.

7. **Squash or rebase** before merging to keep history linear and clean.

8. **Merges to `main`** happen only from `develop` after all team members approve, and only for stable, tested milestones.

### PR Checklist

Before opening a PR, confirm:

- [ ] All new functions and classes have docstrings
- [ ] `black` and `isort` have been run
- [ ] `flake8` / `ruff` returns zero errors
- [ ] Relevant tests pass locally (`pytest tests/`)
- [ ] New behaviour is covered by at least one test
- [ ] Config changes are documented
- [ ] `CHANGELOG.md` entry added (if applicable)

---

## Code Style Guidelines

### Formatter and Linter

| Tool | Purpose | Config |
|------|---------|--------|
| `black` | Auto-formatter | `pyproject.toml` |
| `isort` | Import sorting | `pyproject.toml` |
| `ruff` | Fast linter | `pyproject.toml` |
| `mypy` | Static type checking | `pyproject.toml` |

Run all checks before committing:

```bash
black src/ tests/ scripts/
isort src/ tests/ scripts/
ruff check src/ tests/ scripts/
mypy src/
```

### General Python Rules

- **Python 3.10+** — use `match` statements and union types (`X | Y`) where appropriate.
- **Type annotations are required** for all function signatures.
- **Docstrings** must follow [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
- Maximum line length: **88 characters** (Black default).
- Prefer explicit imports over wildcard imports (`from module import *` is forbidden).
- Configuration values must never be hardcoded — use config files or environment variables.

### Docstring Template

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
        ValueError: If audio array is empty or contains NaN values.
    """
```

---

## Documentation Expectations

- Every new module (folder) must have a `README.md` explaining its purpose, inputs, outputs, and any usage examples.
- Every new Python file must have a module-level docstring.
- Experiments must be logged to MLflow or Weights & Biases — no print-only experiment tracking.
- Notebooks must have a descriptive title cell and be cleaned of outputs before committing (`nbstripout`).
- Any change to the system architecture must be reflected in `docs/architecture.md`.
- Dataset format changes must be reflected in `docs/datasets.md`.

---

## Testing Requirements

- Unit tests live in `tests/` and mirror the `src/` structure.
- Use `pytest` as the test runner.
- Minimum coverage target: **70%** for `src/`.
- Tests must not depend on actual dataset files — use synthetic fixtures.
- Integration tests should be tagged with `@pytest.mark.integration` and skipped by default in CI unless explicitly enabled.

```bash
# Run unit tests only
pytest tests/ -m "not integration"

# Run all tests including integration
pytest tests/
```
