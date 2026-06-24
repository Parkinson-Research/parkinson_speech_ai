# Research Questions

This document formalises the research framing for the Parkinson Speech AI project. It should be treated as a living document and updated as the project evolves.

---

## Main Research Question

> **Can speech biomarkers extracted from short vocal recordings reliably discriminate between individuals with Parkinson's Disease and healthy controls across different languages, recording environments, and speech tasks — and do transformer-based self-supervised speech representations outperform hand-crafted acoustic features for this task?**

---

## Sub-Questions

1. **Feature Effectiveness**
   > Which acoustic feature domains (prosodic, spectral, cepstral, voice quality) carry the most discriminative information for PD detection?

2. **Model Comparison**
   > Do fine-tuned transformer models (Wav2Vec2, HuBERT, WavLM) achieve significantly higher classification performance than traditional ML classifiers trained on hand-crafted features?

3. **Cross-Corpus Generalisation**
   > Do models trained on one dataset (e.g., Italian dataset) generalise to another dataset (e.g., MDVR-KCL) without retraining, and vice versa?

4. **Data Efficiency**
   > At what training set size do transformer models begin to outperform traditional classifiers? (Relevant given the small-scale nature of clinical speech datasets.)

5. **Explainability**
   > What temporal regions and spectral characteristics do transformer attention heads attend to, and do these correspond to clinically known PD speech biomarkers?

---

## Hypotheses

| # | Hypothesis | Rationale |
|---|-----------|-----------|
| H1 | Fine-tuned Wav2Vec2 will achieve a higher AUC-ROC than any traditional ML baseline on both datasets. | Transformer models learn rich contextual representations from raw waveforms, potentially capturing subtle temporal patterns missed by frame-level features. |
| H2 | HuBERT and WavLM will outperform Wav2Vec2 due to their improved pre-training objectives. | HuBERT's discrete prediction targets and WavLM's masked speech denoising provide richer pre-training signal. |
| H3 | Models will show a significant performance drop under cross-corpus evaluation, indicating dataset-specific bias. | Recording conditions, demographics, and speech tasks differ substantially between datasets. |
| H4 | MFCC + prosodic features will form the strongest traditional feature combination. | Established clinical literature consistently identifies F0 instability, jitter, and shimmer as key PD biomarkers. |
| H5 | Transformer attention will localise to voiced phoneme regions, particularly sustained vowels. | PD-related dysphonia primarily affects phonation, which is most prominent in voiced segments. |

---

## Expected Contributions

1. **Benchmark comparison** of traditional ML vs. transformer-based methods on two independent PD speech datasets using a unified, reproducible evaluation protocol.

2. **Open-source framework** providing reusable, modular pipelines for speech-based PD detection research, lowering the barrier for future studies.

3. **Cross-corpus analysis** quantifying how well models trained on one linguistic/demographic context transfer to another.

4. **Explainability insights** linking model decisions to established clinical knowledge, improving trust and interpretability for clinical stakeholders.

5. **Practical guidelines** on when transformer models are justified versus traditional ML approaches, given dataset size constraints common in clinical settings.

---

## Evaluation Strategy

### Primary Metric
- **AUC-ROC** — threshold-independent measure of discriminative ability, robust to class imbalance.

### Secondary Metrics
- **Sensitivity (Recall)** — proportion of true PD cases correctly identified (clinically critical: false negatives are costly).
- **Specificity** — proportion of true healthy controls correctly identified.
- **F1 Score** — harmonic mean of precision and recall.
- **Matthews Correlation Coefficient (MCC)** — balanced metric for binary classification under imbalance.
- **Accuracy** — reported for comparability with prior literature.

### Validation Protocol
- **Stratified 10-fold cross-validation** as primary evaluation scheme (speaker-independent splits to prevent data leakage).
- **Bootstrap 95% confidence intervals** (n=1000) for all reported metrics.
- **McNemar's test** for pairwise model comparison (significance threshold: p < 0.05).
- **Cross-corpus evaluation** — train on Dataset A, test on Dataset B, and vice versa.

### Baselines
| Baseline | Description |
|---------|-------------|
| Majority class | Always predicts the majority class |
| MFCC + SVM | 40 MFCCs + linear SVM (common literature baseline) |
| eGeMAPS + XGBoost | OpenSMILE eGeMAPS feature set with XGBoost |
| Wav2Vec2 (frozen) | Wav2Vec2 features, frozen encoder, linear probe only |

---

## Future Work

1. **Multi-task learning** — joint prediction of PD diagnosis and disease severity (UPDRS motor score).

2. **Multi-modal fusion** — combining speech features with accelerometer/gait data from wearables.

3. **Longitudinal modelling** — tracking speech biomarker trajectories over time to model disease progression.

4. **Few-shot adaptation** — investigating meta-learning approaches to handle the extreme data scarcity typical in clinical PD datasets.

5. **Multilingual generalisation** — extending cross-corpus experiments to datasets in additional languages (Spanish, German, Mandarin).

6. **Federated learning** — enabling privacy-preserving model training across multiple clinical institutions without centralising patient data.

7. **Clinical validation study** — prospective validation of the best-performing model in a real clinical screening scenario.

---

## Related Work

Key prior studies this project builds upon:

- Little et al. (2009) — *Suitability of dysphonia measurements for telemonitoring of Parkinson's disease* (Oxford PD dataset, UCI benchmark)
- Orozco-Arroyave et al. (2016) — *New Spanish speech corpus for PD research* (PC-GITA dataset)
- Chlasta & Wołk (2021) — *Towards computer-aided diagnosis of Parkinson's disease using speech analysis*
- Favaro et al. (2023) — *Automated speech-based screening of PD using self-supervised transformers*

> Update this section as you conduct your literature review.
