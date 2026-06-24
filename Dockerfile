# =============================================================================
# Parkinson Speech AI — Dockerfile
# Base image: Python 3.11 slim with CUDA-compatible torch installed separately
# For GPU support, swap base image to: nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
# =============================================================================

FROM python:3.11-slim

# ---------------------------------------------------------------------------
# Labels
# ---------------------------------------------------------------------------
LABEL maintainer="Parkinson Speech AI Team"
LABEL description="Research framework for Parkinson's Disease detection from speech"
LABEL version="0.1.0"

# ---------------------------------------------------------------------------
# System dependencies
# ---------------------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    ffmpeg \
    libsndfile1 \
    libsndfile1-dev \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------------------------
# Set working directory
# ---------------------------------------------------------------------------
WORKDIR /app

# ---------------------------------------------------------------------------
# Install Python dependencies
# Install requirements first to leverage Docker layer caching
# ---------------------------------------------------------------------------
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------------------------------------------------------------------------
# Copy project source
# ---------------------------------------------------------------------------
COPY . .

# Install project package in editable mode
RUN pip install --no-cache-dir -e .

# ---------------------------------------------------------------------------
# Environment variables
# ---------------------------------------------------------------------------
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app

# ---------------------------------------------------------------------------
# Default port for FastAPI inference server
# ---------------------------------------------------------------------------
EXPOSE 8000

# ---------------------------------------------------------------------------
# Default command — override at runtime for training vs. inference
# ---------------------------------------------------------------------------
CMD ["uvicorn", "src.deployment.app:app", "--host", "0.0.0.0", "--port", "8000"]
