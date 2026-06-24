# System Architecture

This document describes the end-to-end architecture of the Parkinson Speech AI framework. The system is designed to be modular so that individual components can be swapped, extended, or replaced without affecting the rest of the pipeline.

---

## High-Level Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Audio Input                                  │
│  (Raw .wav / .mp3 / .flac recordings — sustained vowels or          │
│   continuous speech passages)                                       │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       Preprocessing                                 │
│  • Resampling (target: 16 kHz)                                      │
│  • Channel normalisation (mono)                                     │
│  • Noise reduction (spectral subtraction / noisereduce)             │
│  • Silence trimming (energy-based VAD)                              │
│  • Amplitude normalisation (peak / RMS)                             │
│  • Fixed-length segmentation (for batching)                         │
└──────────┬───────────────────────────────────────┬──────────────────┘
           │                                       │
           ▼                                       ▼
┌─────────────────────┐               ┌────────────────────────────────┐
│  Traditional Path   │               │      Transformer Path          │
│                     │               │                                │
│  Acoustic Feature   │               │  Pre-trained Encoder           │
│  Extraction:        │               │  (Wav2Vec2 / HuBERT / WavLM)   │
│  • MFCCs (Δ, ΔΔ)   │               │                                │
│  • Jitter, Shimmer  │               │  • Feature extraction mode     │
│  • HNR, NHR         │               │    (frozen encoder)            │
│  • F0 statistics    │               │  • Fine-tuning mode            │
│  • Spectral features│               │    (end-to-end)                │
│  • Prosodic features│               │  • Classification head         │
│  • OpenSMILE feats  │               │    (linear probe / MLP)        │
└─────────┬───────────┘               └──────────────┬─────────────────┘
          │                                          │
          ▼                                          ▼
┌─────────────────────┐               ┌────────────────────────────────┐
│  Feature            │               │  Embedding                     │
│  Normalisation      │               │  Aggregation                   │
│  • StandardScaler   │               │  • Mean pooling                │
│  • RobustScaler     │               │  • Attentive pooling           │
│  • PCA (optional)   │               │  • CLS token (if applicable)   │
└─────────┬───────────┘               └──────────────┬─────────────────┘
          │                                          │
          ▼                                          ▼
┌─────────────────────┐               ┌────────────────────────────────┐
│  Classifier         │               │  Classification Head           │
│  • SVM (RBF kernel) │               │  • Binary output (PD / HC)     │
│  • Random Forest    │               │  • Sigmoid activation          │
│  • XGBoost          │               │  • BCEWithLogitsLoss           │
│  • Logistic Reg.    │               │                                │
└─────────┬───────────┘               └──────────────┬─────────────────┘
          │                                          │
          └──────────────────┬───────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         Evaluation                                  │
│  • Binary classification metrics: AUC-ROC, Accuracy,               │
│    Sensitivity (Recall), Specificity, F1, MCC                       │
│  • Stratified k-fold cross-validation (k=5 or k=10)                │
│  • Threshold calibration (Youden's J / cost-sensitive)              │
│  • Bootstrap confidence intervals                                   │
│  • McNemar's test for model comparison                              │
│  • Cross-corpus generalisation experiments                          │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       Explainability                                │
│  Traditional Path:                                                  │
│  • SHAP TreeExplainer / KernelExplainer                             │
│  • Feature importance ranking                                       │
│  • Partial dependence plots                                         │
│                                                                     │
│  Transformer Path:                                                  │
│  • Attention weight visualisation (per-layer, per-head)             │
│  • Integrated Gradients (Captum)                                    │
│  • GradCAM on spectrogram representations                           │
│  • Saliency maps projected back to waveform                         │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         Deployment                                  │
│  • FastAPI REST inference server                                    │
│  • ONNX model export for cross-platform serving                     │
│  • Docker container for reproducible inference                      │
│  • /predict endpoint: accepts audio file → returns PD probability   │
│  • /health endpoint: server health check                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Component Descriptions

### 1. Preprocessing (`src/preprocessing/`)

Responsible for converting raw audio recordings into a clean, standardised format. All preprocessing is deterministic and parameterised via config files to ensure full reproducibility.

| Module | Responsibility |
|--------|---------------|
| `loader.py` | Load audio files into numpy arrays using librosa/soundfile |
| `resampler.py` | Resample to a uniform target rate (default 16 kHz) |
| `denoiser.py` | Spectral noise reduction |
| `vad.py` | Voice Activity Detection and silence trimming |
| `normalizer.py` | Amplitude normalisation |
| `segmenter.py` | Fixed-length windowing for consistent input shape |
| `pipeline.py` | Orchestrates the full preprocessing chain |

### 2. Datasets (`src/datasets/`)

Dataset abstraction layer decoupling data loading from model training.

| Module | Responsibility |
|--------|---------------|
| `base_dataset.py` | Abstract base class defining the dataset interface |
| `italian_dataset.py` | Dataset class for Italian Speech Dataset |
| `mdvrkcl_dataset.py` | Dataset class for MDVR-KCL Dataset |
| `collator.py` | Custom collate functions for DataLoader batching |

### 3. Feature Extraction (`src/features/`)

Used by the traditional ML path only.

| Module | Responsibility |
|--------|---------------|
| `mfcc.py` | MFCC extraction with delta and delta-delta coefficients |
| `prosodic.py` | F0, jitter, shimmer, HNR computation |
| `spectral.py` | Spectral centroid, bandwidth, rolloff, flux |
| `opensmile_features.py` | OpenSMILE feature set wrapper (eGeMAPS, ComParE) |
| `pipeline.py` | Combines all feature extractors into a single feature vector |

### 4. Models (`src/models/`)

#### Traditional (`src/models/traditional/`)
Scikit-learn–compatible pipelines wrapping classical classifiers.

#### Transformers (`src/models/transformers/`)
Hugging Face–based fine-tuning wrappers for Wav2Vec2, HuBERT, and WavLM.

### 5. Evaluation (`src/evaluation/`)

Statistically rigorous evaluation utilities shared across both pipelines.

### 6. Explainability (`src/explainability/`)

Post-hoc and intrinsic interpretability methods for both pipelines.

### 7. Deployment (`src/deployment/`)

FastAPI server and ONNX export utilities for production inference.

### 8. Utilities (`src/utils/`)

Shared helpers: logging, config loading, seed management, path utilities.

---

## Data Flow Summary

```
data/raw/
  └── {dataset}/{subject_id}/{recording}.wav
        │
        ▼ (src/preprocessing/pipeline.py)
data/processed/
  └── {dataset}/{subject_id}/{recording}_preprocessed.wav
        │
        ├── Traditional path ──► features/{dataset}_features.parquet
        │
        └── Transformer path ──► raw waveform fed directly to model
```

---

## Configuration-Driven Design

Every pipeline stage is parameterised by a YAML config file in `configs/`. This means no training parameters, feature settings, or file paths are hardcoded in the source code. See `configs/` for examples.

---

## Experiment Tracking

All experiments are logged to MLflow (`mlruns/`). Each run records:
- Hyperparameters
- Evaluation metrics (per fold and aggregated)
- Model artefacts
- Preprocessing config hash (for reproducibility checks)
