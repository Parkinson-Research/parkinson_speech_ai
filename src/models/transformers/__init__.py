"""
src.models.transformers
=======================
Hugging Face–based fine-tuning wrappers for self-supervised speech models.

Supported backbones:
    - facebook/wav2vec2-base
    - facebook/wav2vec2-large-xlsr-53
    - facebook/hubert-base-ls960
    - microsoft/wavlm-base
    - microsoft/wavlm-base-plus
"""

from src.models.transformers.model_factory import build_transformer_model

__all__ = ["build_transformer_model"]
