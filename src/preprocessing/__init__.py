"""
src.preprocessing
=================
Audio preprocessing pipeline: loading, resampling, denoising,
voice activity detection, normalisation, and segmentation.
"""

from src.preprocessing.pipeline import PreprocessingPipeline

__all__ = ["PreprocessingPipeline"]
