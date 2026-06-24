# src/deployment

FastAPI inference server and ONNX export utilities. To be implemented after the best-performing model is selected.

## Modules

| Module | Responsibility |
|--------|---------------|
| `app.py` | FastAPI REST server with `/predict` and `/health` endpoints |
| `predictor.py` | Unified inference wrapper for both pipeline types |
| `onnx_export.py` | Export PyTorch models to ONNX for cross-platform serving |

## Running the Server

```bash
uvicorn src.deployment.app:app --host 0.0.0.0 --port 8000 --reload
```

Or via Docker:
```bash
docker run --gpus all -p 8000:8000 -v $(pwd)/outputs:/app/outputs parkinson-speech-ai
```

## API Endpoints (planned)

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/predict` | Upload .wav file, get PD probability |
| `GET` | `/health` | Server health check |
| `GET` | `/model-info` | Loaded model metadata |
