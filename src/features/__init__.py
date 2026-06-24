"""
src.features
============
Acoustic feature extraction for the traditional ML pipeline.
Includes MFCC, prosodic, spectral, and OpenSMILE feature extractors.
"""

from src.features.pipeline import FeatureExtractionPipeline

__all__ = ["FeatureExtractionPipeline"]
