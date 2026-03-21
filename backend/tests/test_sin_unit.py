"""Unit tests for sine operation."""

import pytest
import math
from routes.sin import sin_number


class TestSineNumbers:
    """Unit tests for sine operation."""

    def test_sin_zero(self):
        """Test sine of zero."""
        assert sin_number(0) == 0

    def test_sin_90_degrees(self):
        """Test sine of 90 degrees."""
        result = sin_number(90, degrees=True)
        assert result == pytest.approx(1.0)

    def test_sin_180_degrees(self):
        """Test sine of 180 degrees."""
        result = sin_number(180, degrees=True)
        assert result == pytest.approx(0, abs=1e-10)

    def test_sin_radians(self):
        """Test sine with radians."""
        result = sin_number(math.pi / 2)
        assert result == pytest.approx(1.0)

    def test_sin_negative_angle(self):
        """Test sine of negative angle."""
        result = sin_number(-90, degrees=True)
        assert result == pytest.approx(-1.0)

    def test_sin_large_angle(self):
        """Test sine with large angle."""
        result = sin_number(360, degrees=True)
        assert result == pytest.approx(0, abs=1e-10)

    def test_sin_positive_radian(self):
        """Test sine with positive radian."""
        result = sin_number(math.pi / 6)
        assert result == pytest.approx(0.5)
