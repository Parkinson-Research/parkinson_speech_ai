"""
src.models.traditional
======================
Scikit-learn–compatible classifier pipelines for PD detection
using hand-crafted acoustic features.

Available classifiers: SVM, Random Forest, XGBoost, Logistic Regression.
"""

from src.models.traditional.classifier_factory import build_classifier

__all__ = ["build_classifier"]
