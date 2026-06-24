# src/explainability

Post-hoc and intrinsic interpretability methods for both pipelines. Explainability is treated as a first-class citizen in this framework, not an afterthought.

## Modules

| Module | Pipeline | Method |
|--------|----------|--------|
| `shap_explainer.py` | Traditional ML | SHAP Tree/Kernel Explainer |
| `attention_viz.py` | Transformers | Attention weight visualisation |
| `integrated_gradients.py` | Transformers | Integrated Gradients (Captum) |

## Outputs

All explainability plots are saved to `outputs/figures/`.

## Usage

```python
# Traditional ML — SHAP
from src.explainability.shap_explainer import SHAPExplainer

explainer = SHAPExplainer(fitted_model, feature_names=pipeline.feature_names)
shap_values = explainer.explain(X_test)
explainer.plot_summary(shap_values, X_test, output_path="outputs/figures/shap_summary.png")

# Transformer — Attention
from src.explainability.attention_viz import extract_attention_weights, plot_attention_on_waveform

attn = extract_attention_weights(model, input_values, layer=-1)
plot_attention_on_waveform(attn, waveform, sample_rate=16000)
```
