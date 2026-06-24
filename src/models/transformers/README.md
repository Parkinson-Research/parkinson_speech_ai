# src/models/transformers

Hugging Face–based fine-tuning wrappers for self-supervised speech models. Supports Wav2Vec2 (phase 1), HuBERT and WavLM (phase 2).

## Modules

| Module | Responsibility |
|--------|---------------|
| `model_factory.py` | Builds the correct model from config |
| `wav2vec2.py` | Wav2Vec2 + classification head |
| `hubert.py` | HuBERT + classification head (phase 2) |
| `wavlm.py` | WavLM + classification head (phase 2) |
| `trainer.py` | PyTorch training loop with MLflow tracking |

## Supported Backbones

| Model | Hugging Face ID | Phase |
|-------|----------------|-------|
| Wav2Vec2 Base | `facebook/wav2vec2-base` | 1 |
| Wav2Vec2 Large XLSR | `facebook/wav2vec2-large-xlsr-53` | 1 |
| HuBERT Base | `facebook/hubert-base-ls960` | 2 |
| WavLM Base | `microsoft/wavlm-base` | 2 |
| WavLM Base+ | `microsoft/wavlm-base-plus` | 2 |

## Operating Modes

- `frozen_encoder`: Only the classification head is trained. Fast, low data requirement.
- `finetune`: All parameters updated with layer-wise LR decay. Best performance with sufficient data.

## Ownership

This module is maintained by **Member 3** (project lead / transformer models).
