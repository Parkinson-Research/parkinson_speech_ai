# DVC Setup Guide

This guide covers initialising DVC, configuring the DagsHub remote, and managing dataset versions in the Parkinson Speech AI project.

---

## What is DVC?

[DVC (Data Version Control)](https://dvc.org) is Git for data and models. It stores large files (audio recordings, model checkpoints) in a remote storage backend, and commits only small pointer files (`.dvc`) into Git. This keeps the Git repository lightweight while ensuring every experiment is reproducible.

---

## Prerequisites

- Python 3.10+
- Git configured with your credentials
- DVC installed (`pip install dvc==3.51.2` — already in `requirements.txt`)
- A DagsHub account with access to the project repository

---

## One-Time Setup (new machine)

### 1. Clone the repository

```bash
git clone https://github.com/Parkinson-Research/parkinson_speech_ai.git
cd parkinson_speech_ai
```

### 2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in:
```
DAGSHUB_USERNAME=your_dagshub_username
DAGSHUB_TOKEN=your_dagshub_token
```

Get your token at: https://dagshub.com/user/settings/tokens

### 4. Configure DVC credentials (local only — never committed)

```bash
cp .dvc/config.local.example .dvc/config.local
```

Open `.dvc/config.local` and fill in:
```ini
[remote "dagshub"]
    auth = basic
    user = your_dagshub_username
    password = your_dagshub_token
```

### 5. Pull datasets

```bash
dvc pull
```

This downloads all tracked data from the DagsHub remote into `data/raw/` and `data/processed/`.

---

## Daily Workflow

### Pulling the latest data

```bash
git pull
dvc pull
```

Always run `dvc pull` after `git pull` to ensure your data is in sync with the latest `.dvc` pointers.

### Adding a new dataset

```bash
# 1. Place files in the correct directory
#    e.g.: data/raw/new_dataset/

# 2. Track with DVC
dvc add data/raw/new_dataset

# 3. Commit the pointer file to Git
git add data/raw/new_dataset.dvc .gitignore
git commit -m "data(new-dataset): add raw recordings v1.0"

# 4. Push data to remote storage
dvc push

# 5. Push Git commit
git push
```

### Updating an existing dataset

```bash
# After modifying files in data/raw/italian/
dvc add data/raw/italian
git add data/raw/italian.dvc
git commit -m "data(italian): update recordings — added 5 new PD subjects"
dvc push
git push
```

### Checking data status

```bash
dvc status          # Show which tracked files have changed
dvc diff            # Show differences between cached and remote versions
```

---

## Tracked Directories

| Directory | DVC File | Contents |
|-----------|----------|----------|
| `data/raw/italian/` | `data/raw/italian.dvc` | Raw Italian recordings |
| `data/raw/mdvr_kcl/` | `data/raw/mdvr_kcl.dvc` | Raw MDVR-KCL recordings |
| `data/processed/italian/` | `data/processed/italian.dvc` | Preprocessed Italian audio |
| `data/processed/mdvr_kcl/` | `data/processed/mdvr_kcl.dvc` | Preprocessed MDVR-KCL audio |
| `outputs/models/` | `outputs/models.dvc` | Trained model checkpoints |

> `.dvc` pointer files are committed to Git. The actual data lives in DagsHub.

---

## Remote Configuration

The DVC remote is configured in `.dvc/config` (committed to Git):

```ini
[core]
    autostage = true
    remote = dagshub

[remote "dagshub"]
    url = https://dagshub.com/Parkinson-Research/parkinson_speech_ai.dvc
```

Credentials go in `.dvc/config.local` (gitignored). See `.dvc/config.local.example`.

---

## Troubleshooting

**`ERROR: failed to pull data from the cloud`**
→ Check that `.dvc/config.local` has the correct credentials.
→ Verify your DagsHub token has Storage read/write permissions.

**`dvc: command not found`**
→ Activate your virtual environment: `source .venv/bin/activate`

**Files appear modified after `dvc pull`**
→ Run `dvc checkout` to restore files to the cached version.

---

## Further Reading

- [DVC Documentation](https://dvc.org/doc)
- [DagsHub DVC Integration](https://dagshub.com/docs/integration_guide/dvc/)
- See also: `docs/dagshub_setup.md`
