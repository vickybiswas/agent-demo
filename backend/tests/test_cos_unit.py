"""Unit tests for cosine operation."""

import pytest
import math
from routes.cos import cos_number


class TestCosineNumbers:
    """Unit tests for cosine operation."""

    def test_cos_zero(self):
        """Test cosine of zero."""
        assert cos_number(0) == pytest.approx(1.0)

    def test_cos_90_degrees(self):
        """Test cosine of 90 degrees."""
        result = cos_number(90, degrees=True)
        assert result == pytest.approx(0, abs=1e-10)

    def test_cos_180_degrees(self):
        """Test cosine of 180 degrees."""
        result = cos_number(180, degrees=True)
        assert result == pytest.approx(-1.0)

    def test_cos_radians(self):
        """Test cosine with radians."""
        result = cos_number(0)
        assert result == pytest.approx(1.0)

    def test_cos_negative_angle(self):
        """Test cosine of negative angle."""
        result = cos_number(-90, degrees=True)
        assert result == pytest.approx(0, abs=1e-10)

    def test_cos_360_degrees(self):
        """Test cosine of 360 degrees."""
        result = cos_number(360, degrees=True)
        assert result == pytest.approx(1.0)

    def test_cos_positive_radian(self):
        """Test cosine with positive radian."""
        result = cos_number(math.pi / 3)
        assert result == pytest.approx(0.5)
