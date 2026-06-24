"""
src.evaluation
==============
Shared evaluation utilities for both traditional ML and transformer pipelines.
Includes classification metrics, cross-validation, statistical tests,
and bootstrap confidence intervals.
"""

from src.evaluation.metrics import compute_metrics

__all__ = ["compute_metrics"]
