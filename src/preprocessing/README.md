# src/preprocessing

Audio preprocessing pipeline that converts raw recordings into clean, standardised waveforms for downstream feature extraction or model training.

## Modules

| Module | Responsibility |
|--------|---------------|
| `loader.py` | Load audio files into numpy arrays |
| `resampler.py` | Resample to a uniform target rate (default 16 kHz) |
| `denoiser.py` | Spectral noise reduction |
| `vad.py` | Voice activity detection and silence trimming |
| `normalizer.py` | Amplitude normalisation (peak or RMS) |
| `segmenter.py` | Fixed-length windowing |
| `pipeline.py` | Composes all steps into one configurable pipeline |

## Usage

```python
from omegaconf import OmegaConf
from src.preprocessing.pipeline import PreprocessingPipeline, PreprocessingConfig

cfg = OmegaConf.load("configs/wav2vec2_italian_finetune.yaml")
config = PreprocessingConfig.from_dict(cfg.preprocessing)
pipeline = PreprocessingPipeline(config)

waveform, sr = pipeline.process("data/raw/italian/PD_001/vowel_a.wav")
```

## Processing Order

```
Load → Resample → Denoise → Trim Silence → Normalise → Truncate/Pad
```

All steps are parameterised via YAML config. The pipeline computes a hash of its configuration and caches processed files to avoid redundant computation.
