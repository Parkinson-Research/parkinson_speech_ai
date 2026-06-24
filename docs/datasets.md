# Datasets

This document specifies the expected dataset formats, metadata schemas, download instructions, and ethical considerations for all datasets used in this project.

---

## Overview

| Dataset | Language | Subjects (PD / HC) | Task Type | Access |
|---------|----------|---------------------|-----------|--------|
| Italian Speech Dataset | Italian | TBD | Sustained vowels + running speech | Restricted — contact authors |
| MDVR-KCL | English | 42 PD / 21 HC | Reading passage + spontaneous speech | Restricted — contact KCL |

---

## Standard Manifest Format

All datasets are normalised to a unified manifest format (CSV or JSON lines) stored in `data/processed/`. This allows all pipeline code to be dataset-agnostic.

### CSV Schema

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `subject_id` | `str` | Unique anonymised subject identifier | `PD_001`, `HC_042` |
| `label` | `int` | Binary label: 1 = PD, 0 = Healthy Control | `1` |
| `label_str` | `str` | Human-readable label | `"PD"`, `"HC"` |
| `file_path` | `str` | Relative path to the preprocessed audio file | `data/processed/italian/PD_001_vowel_a.wav` |
| `original_file_path` | `str` | Relative path to the original raw audio file | `data/raw/italian/PD_001/vowel_a.wav` |
| `sample_rate` | `int` | Sampling rate in Hz (after preprocessing: always 16000) | `16000` |
| `duration_sec` | `float` | Duration of the recording in seconds | `3.54` |
| `task` | `str` | Speech task type | `"sustained_vowel_a"`, `"reading"`, `"spontaneous"` |
| `gender` | `str` | Subject gender (`M` / `F` / `unknown`) | `"M"` |
| `age` | `float` | Subject age in years (`NaN` if unavailable) | `67.0` |
| `updrs_motor` | `float` | UPDRS Motor Score (`NaN` if unavailable) | `24.5` |
| `disease_duration_years` | `float` | Years since diagnosis (`NaN` if unavailable) | `4.0` |
| `medication_state` | `str` | Medication state during recording (`on` / `off` / `unknown`) | `"on"` |
| `dataset` | `str` | Source dataset identifier | `"italian"`, `"mdvrkcl"` |
| `split` | `str` | Predefined split assignment (if applicable) | `"train"`, `"test"`, `"val"` |

### Example Manifest Row (CSV)

```
subject_id,label,label_str,file_path,original_file_path,sample_rate,duration_sec,task,gender,age,updrs_motor,disease_duration_years,medication_state,dataset,split
PD_001,1,PD,data/processed/italian/PD_001_vowel_a.wav,data/raw/italian/PD_001/vowel_a.wav,16000,3.54,sustained_vowel_a,M,67.0,24.5,4.0,on,italian,train
```

---

## Italian Speech Dataset

### Description
A corpus of sustained vowel phonations and continuous speech recordings collected from Italian-speaking Parkinson's patients and age/gender-matched healthy controls.

### Directory Structure (expected)

```
data/raw/italian/
├── PD/
│   ├── {subject_id}/
│   │   ├── vowel_a.wav
│   │   ├── vowel_e.wav
│   │   ├── vowel_i.wav
│   │   └── running_speech.wav
└── HC/
    └── {subject_id}/
        ├── vowel_a.wav
        └── ...
```

### Notes
- Target resampling: 16 kHz mono.
- Sustained vowels are typically 3–7 seconds; trim leading/trailing silence.
- Document exact version/release of the corpus used in `data/README.md`.

---

## MDVR-KCL Dataset

### Description
The Mobile Device Voice Recordings at King's College London (MDVR-KCL) dataset contains voice recordings from Parkinson's patients and healthy controls, recorded in both controlled and uncontrolled (home) environments using mobile devices.

### Reference
> Jaeger, H., et al. (2019). *Detecting Parkinson's Disease from Continuous Speech Using Deep Learning*. Interspeech 2019.

### Directory Structure (expected)

```
data/raw/mdvrkcl/
├── PD/
│   ├── {subject_id}/
│   │   ├── reading.wav
│   │   └── spontaneous.wav
└── HC/
    └── {subject_id}/
        ├── reading.wav
        └── spontaneous.wav
```

### Notes
- Contains both controlled and home-environment recordings — document recording condition in metadata.
- Resampling to 16 kHz required (original sample rates vary).
- Some recordings contain background noise; apply denoising pipeline.

---

## Data Access and Ethics

> **This section must be completed by the team member responsible for each dataset before any data is committed or shared.**

- [ ] Confirm data use agreements are in place for each dataset.
- [ ] Confirm no raw patient data is committed to the repository (data is gitignored).
- [ ] Confirm DVC remote storage access is restricted to authorised team members.
- [ ] Confirm IRB / Ethics committee approval is documented (if applicable).
- [ ] All subject identifiers in manifest files must be anonymised.

---

## Data Version Control

Dataset files are tracked with DVC, not Git. After obtaining the datasets:

```bash
# Add a dataset file or folder to DVC tracking
dvc add data/raw/italian/

# Push data to the remote (requires configured DVC remote)
dvc push

# Pull data on a new machine
dvc pull
```

Configure the DVC remote in `.dvc/config` (not committed if it contains credentials).

---

## Preprocessing Output Convention

After running the preprocessing pipeline, processed files follow this naming pattern:

```
data/processed/{dataset}/{subject_id}_{task}_preprocessed.wav
```

And the generated manifest is saved as:

```
data/processed/{dataset}_manifest.csv
```
