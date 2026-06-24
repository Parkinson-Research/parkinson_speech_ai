"""Unit tests for src/preprocessing modules."""

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def sine_wave() -> np.ndarray:
    """Generate a 1-second 440 Hz sine wave at 16 kHz as test audio."""
    sample_rate = 16000
    duration = 1.0
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return (np.sin(2 * np.pi * 440 * t) * 0.5).astype(np.float32)


@pytest.fixture()
def silent_audio() -> np.ndarray:
    """Generate a 1-second silent signal at 16 kHz."""
    return np.zeros(16000, dtype=np.float32)


# ---------------------------------------------------------------------------
# Tests — Normalizer
# ---------------------------------------------------------------------------

class TestNormalizeAmplitude:
    def test_peak_normalisation_max_is_one(self, sine_wave: np.ndarray) -> None:
        """Peak-normalised audio should have a max absolute value of 1.0."""
        pytest.skip("Implement after normalizer.py is complete.")

    def test_silent_audio_raises(self, silent_audio: np.ndarray) -> None:
        """Normalising a silent signal should raise ValueError."""
        pytest.skip("Implement after normalizer.py is complete.")


# ---------------------------------------------------------------------------
# Tests — VAD / Silence Trimming
# ---------------------------------------------------------------------------

class TestTrimSilence:
    def test_trim_returns_shorter_audio(self, sine_wave: np.ndarray) -> None:
        """Padded-with-silence audio should be shorter after trimming."""
        pytest.skip("Implement after vad.py is complete.")


# ---------------------------------------------------------------------------
# Tests — Segmenter
# ---------------------------------------------------------------------------

class TestSegmentAudio:
    def test_segment_count(self, sine_wave: np.ndarray) -> None:
        """A 2-second audio should produce 2 one-second non-overlapping segments."""
        pytest.skip("Implement after segmenter.py is complete.")

    def test_segment_length(self, sine_wave: np.ndarray) -> None:
        """Each segment should have exactly the expected number of samples."""
        pytest.skip("Implement after segmenter.py is complete.")


# ---------------------------------------------------------------------------
# Tests — Preprocessing Pipeline
# ---------------------------------------------------------------------------

class TestPreprocessingPipeline:
    def test_output_sample_rate(self, sine_wave: np.ndarray) -> None:
        """Pipeline output should always be at the target sample rate."""
        pytest.skip("Implement after pipeline.py is complete.")
