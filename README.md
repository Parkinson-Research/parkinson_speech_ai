# Parkinson Speech AI

> A research-grade, modular framework for Parkinson's Disease detection from speech recordings.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## Overview

Parkinson Speech AI is a collaborative research project that investigates the use of speech biomarkers for automated Parkinson's Disease (PD) detection. The project builds and evaluates two complementary families of models:

1. **Traditional ML pipelines** — hand-crafted acoustic features (MFCCs, jitter, shimmer, HNR, etc.) fed into classical classifiers (SVM, Random Forest, XGBoost).
2. **Transformer-based pipelines** — fine-tuning self-supervised speech models (Wav2Vec2, HuBERT, WavLM) end-to-end on raw waveforms.

Both pipelines are evaluated on two independent datasets to assess cross-corpus generalisability and reduce dataset-specific bias.

---

## Research Motivation

Parkinson's Disease affects approximately 10 million people worldwide. Speech impairment (dysarthria, hypophonia, dysphonia) is one of the earliest and most consistent symptoms, often appearing years before motor symptoms become clinically diagnosable. Automated, non-invasive speech-based screening can:

- Enable large-scale, low-cost screening programs
- Provide objective biomarkers for disease progression monitoring
- Complement wearable sensor data for multi-modal PD assessment

---

## Team

| Member | Role | Dataset | Pipeline |
|--------|------|---------|----------|
| **Aamir Sarang** | Research Engineer | Italian Speech Dataset | Traditional ML |
| **Maitreya Pawar** | Research Engineer | MDVR-KCL Dataset | Traditional ML |
| **Nishant Narudkar** | Research Lead | Both | Transformer Models (Wav2Vec2, HuBERT, WavLM) |

---

## Repository Structure

```
parkinson-speech-ai/
│
├── .github/                    # GitHub Actions CI/CD, issue & PR templates
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│
├── configs/                    # YAML configuration files for all experiments
│
├── data/                       # Dataset storage (gitignored — use DVC)
│   ├── raw/                    # Original, unmodified recordings
│   ├── processed/              # Preprocessed audio & feature files
│   └── README.md
│
├── docs/                       # Project documentation
│   ├── architecture.md
│   ├── research_questions.md
│   ├── pipeline_design.md
│   └── datasets.md
│
├── notebooks/                  # Exploratory analysis notebooks
│   ├── Italian_dataset/
│   └── MDVRKCL/
│
├── outputs/                    # All generated artefacts (gitignored)
│   ├── models/
│   ├── reports/
│   └── figures/
│
├── scripts/                    # CLI entry-point scripts for training & evaluation
│
├── src/                        # Core Python package
│   ├── preprocessing/          # Audio loading, denoising, segmentation
│   ├── datasets/               # Dataset classes & data loaders
│   ├── features/               # Acoustic feature extraction
│   ├── models/
│   │   ├── traditional/        # SVM, RF, XGBoost pipelines
│   │   └── transformers/       # Wav2Vec2, HuBERT, WavLM fine-tuning
│   ├── evaluation/             # Metrics, cross-validation, significance tests
│   ├── explainability/         # SHAP, attention visualisation, saliency maps
│   ├── deployment/             # FastAPI inference server, ONNX export
│   └── utils/                  # Logging, config loading, reproducibility helpers
│
├── tests/                      # Unit & integration tests
│
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Planned Pipelines

### Traditional ML Pipeline
```
Raw Audio → Preprocessing → Acoustic Feature Extraction → 
Feature Normalisation → Classifier (SVM / RF / XGBoost) → 
Evaluation (AUC, Sensitivity, Specificity)
```

### Transformer Pipeline
```
Raw Audio → Preprocessing → Wav2Vec2 / HuBERT / WavLM Encoder → 
Classification Head Fine-tuning → 
Evaluation (AUC, Sensitivity, Specificity) → 
Attention-based Explainability
```

---

## Installation

### Prerequisites
- Python 3.10 or higher
- `ffmpeg` installed and available on PATH
- CUDA 11.8+ (optional, for GPU training)

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-org>/parkinson-speech-ai.git
cd parkinson-speech-ai

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install the project package in editable mode
pip install -e .
```

### Docker

```bash
docker build -t parkinson-speech-ai .
docker run --gpus all -v $(pwd)/data:/app/data parkinson-speech-ai
```

---

## Configuration

All experiments are driven by YAML configuration files stored in `configs/`. Example:

```bash
python scripts/train.py --config configs/wav2vec2_italian.yaml
```

---

## Datasets

See [`data/README.md`](data/README.md) and [`docs/datasets.md`](docs/datasets.md) for dataset format specifications, download instructions, and preprocessing steps.

> **Note:** Raw and processed data are **not** committed to this repository. Use DVC to pull data after setup.

```bash
dvc pull
```

---

## Roadmap

- [x] Repository scaffolding and documentation
- [ ] Data preprocessing pipeline (noise reduction, segmentation, resampling)
- [ ] Traditional ML pipeline — Italian dataset (Member 1)
- [ ] Traditional ML pipeline — MDVR-KCL dataset (Member 2)
- [ ] Acoustic feature extraction module (MFCCs, prosodic, spectral features)
- [ ] Wav2Vec2 fine-tuning pipeline
- [ ] HuBERT fine-tuning pipeline
- [ ] WavLM fine-tuning pipeline
- [ ] Cross-corpus evaluation experiments
- [ ] Explainability module (SHAP + attention maps)
- [ ] REST API deployment (FastAPI + ONNX)
- [ ] Technical paper write-up

---

## Citation

If you use this framework in your research, please cite:

```bibtex
@software{parkinson_speech_ai_2025,
  title  = {Parkinson Speech AI: A Modular Framework for PD Detection from Speech},
  author = {Your Team},
  year   = {2025},
  url    = {https://github.com/<your-org>/parkinson-speech-ai}
}
```

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
