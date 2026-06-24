# src/features

Acoustic feature extraction module for the traditional ML pipeline. All extractors return numpy arrays and are fully parameterised via config.

## Modules

| Module | Features Extracted |
|--------|--------------------|
| `mfcc.py` | 40 MFCCs + Δ + ΔΔ (aggregated to mean/std) |
| `prosodic.py` | F0 stats, jitter (local, RAP), shimmer (local, APQ3), HNR, NHR |
| `spectral.py` | Spectral centroid, bandwidth, rolloff, ZCR, flatness |
| `opensmile_features.py` | eGeMAPS v02 (88 features) or ComParE 2016 (6373 features) |
| `pipeline.py` | Combines all extractors → single feature vector |

## Usage

```python
from src.features import FeatureExtractionPipeline
from src.features.pipeline import FeatureConfig

config = FeatureConfig(
    mfcc_enabled=True,
    prosodic_enabled=True,
    spectral_enabled=True,
    opensmile_enabled=False,
)
pipeline = FeatureExtractionPipeline(config)
features = pipeline.extract(waveform, sample_rate=16000)
print(features.shape)   # e.g. (203,)
```

## Notes

- All features are computed per recording (not per frame) by aggregating frame-level statistics (mean + std).
- Feature normalisation (StandardScaler / RobustScaler) is applied inside the training pipeline, not here.
- Feature names are stored in `FeatureConfig.feature_names` for SHAP interpretability.
