# DagsHub Setup Guide

DagsHub is the collaboration platform used by this project for:
- **DVC remote storage** — hosting all dataset files and model checkpoints
- **MLflow tracking server** — hosting all experiment runs, metrics, and artefacts
- **Repository mirroring** — syncing with GitHub

---

## Prerequisites

- A DagsHub account at [dagshub.com](https://dagshub.com)
- Access granted to the project repository: `Parkinson-Research/parkinson_speech_ai`
- DagsHub Python SDK installed (`pip install dagshub==0.6.9` — in `requirements.txt`)

---

## Step 1 — Get Your Access Token

1. Log in at [dagshub.com](https://dagshub.com)
2. Navigate to **Settings → Access Tokens**
3. Click **Generate new token**
4. Give it a name (e.g. `parkinson_speech_ai`) and enable:
   - ✅ Read repository
   - ✅ Write repository
   - ✅ Read storage
   - ✅ Write storage
5. Copy the token — you will not see it again

---

## Step 2 — Configure Environment Variables

```bash
cp .env.example .env
```

Fill in your credentials in `.env`:

```ini
DAGSHUB_USERNAME=your_dagshub_username
DAGSHUB_TOKEN=your_token_here
MLFLOW_TRACKING_URI=https://dagshub.com/Parkinson-Research/parkinson_speech_ai.mlflow
MLFLOW_TRACKING_USERNAME=your_dagshub_username
MLFLOW_TRACKING_PASSWORD=your_token_here
```

> `.env` is gitignored. Never commit it.

---

## Step 3 — Configure DVC Credentials

```bash
cp .dvc/config.local.example .dvc/config.local
```

Edit `.dvc/config.local`:

```ini
[remote "dagshub"]
    auth = basic
    user = your_dagshub_username
    password = your_token_here
```

> `.dvc/config.local` is gitignored by DVC automatically.

---

## Step 4 — Verify the Setup

```bash
# Test DVC remote connectivity
dvc remote list
# Expected output:
# dagshub   https://dagshub.com/Parkinson-Research/parkinson_speech_ai.dvc

# Test DagsHub SDK authentication
python -c "
import os; from dotenv import load_dotenv; load_dotenv()
import dagshub
dagshub.auth.add_app_token(os.environ['DAGSHUB_TOKEN'])
print('DagsHub authentication OK')
"

# Test MLflow connectivity
python -c "
import os; from dotenv import load_dotenv; load_dotenv()
import mlflow
mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])
print('MLflow tracking URI:', mlflow.get_tracking_uri())
"
```

---

## Step 5 — Push Data (first time only)

After adding datasets with `dvc add`:

```bash
dvc push
```

All subsequent team members only need `dvc pull`.

---

## DagsHub Project URLs

| Resource | URL |
|----------|-----|
| Repository | https://dagshub.com/Parkinson-Research/parkinson_speech_ai |
| MLflow UI | https://dagshub.com/Parkinson-Research/parkinson_speech_ai.mlflow |
| DVC Storage | https://dagshub.com/Parkinson-Research/parkinson_speech_ai.dvc |

---

## Programmatic Initialisation (in training scripts)

The `src/utils/mlflow_utils.py` module handles DagsHub initialisation automatically when credentials are set in the environment:

```python
from src.utils.config import load_env
from src.utils.mlflow_utils import setup_mlflow

load_env()  # loads .env
setup_mlflow(experiment_name="parkinson_speech_ai_transformer_italian")
```

Alternatively, use the DagsHub SDK directly:

```python
import dagshub
dagshub.init(
    repo_owner="Parkinson-Research",
    repo_name="parkinson_speech_ai",
    mlflow=True,
)
```

---

## Collaboration Notes

- Only team members with DagsHub repository access can push data.
- New collaborators must complete Steps 1–4 before running `dvc pull`.
- DagsHub storage quota: check project settings if `dvc push` fails with a quota error.

---

## Further Reading

- [DagsHub Documentation](https://dagshub.com/docs)
- [DagsHub + MLflow Guide](https://dagshub.com/docs/integration_guide/mlflow_tracking/)
- [DagsHub + DVC Guide](https://dagshub.com/docs/integration_guide/dvc/)
- See also: `docs/dvc_setup.md`, `docs/mlflow_setup.md`
