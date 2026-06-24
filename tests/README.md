# tests

Unit and integration test suite. Structure mirrors `src/` so test files are easy to locate.

## Running Tests

```bash
# Unit tests only (fast, no GPU, no data required)
pytest tests/ -m "not integration and not gpu"

# All tests
pytest tests/

# With coverage report
pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html
```

## Test File Map

| Test File | Covers |
|-----------|--------|
| `test_preprocessing.py` | `src/preprocessing/` |
| `test_features.py` | `src/features/` |
| `test_evaluation.py` | `src/evaluation/` |
| `test_utils.py` | `src/utils/` |

## Conventions

- Tests use `pytest.skip()` until the implementation is ready — this is intentional.
- All tests use synthetic data fixtures — never real patient data.
- Integration tests (requiring real data or GPU) must be marked with `@pytest.mark.integration`.
