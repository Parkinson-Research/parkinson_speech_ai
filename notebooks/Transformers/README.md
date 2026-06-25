# notebooks/Transformers

Exploratory and experimental notebooks for transformer-based models. Maintained by **Member 3** (project lead).

## Planned Notebooks

| Notebook | Purpose |
|----------|---------|
| `001_wav2vec2_feature_probing.ipynb` | Layer-wise feature probing — what does each Wav2Vec2 layer encode? |
| `002_wav2vec2_frozen_baseline.ipynb` | Linear probe on frozen Wav2Vec2 features |
| `003_wav2vec2_finetune.ipynb` | Full fine-tuning run with Italian dataset |
| `004_hubert_finetune.ipynb` | HuBERT fine-tuning (phase 2) |
| `005_wavlm_finetune.ipynb` | WavLM fine-tuning (phase 2) |
| `006_attention_visualisation.ipynb` | Attention weight analysis across PD vs HC samples |
| `007_cross_corpus_evaluation.ipynb` | Cross-corpus generalisation experiments |

## Notebook Conventions

- Strip outputs before committing: `nbstripout` is configured via pre-commit.
- Name notebooks with a 3-digit index prefix for consistent ordering.
- Use `src/utils` imports — do not reimplement utility logic inside notebooks.
- Each notebook must have a markdown title cell and a brief description cell.
