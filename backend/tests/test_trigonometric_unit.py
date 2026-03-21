"""
Unit tests for trigonometric operations (sin, cos, tan).

Tests the core trigonometric logic with various angles in radians.
"""

import pytest
import math


class TestSin:
    """Test cases for sine operation."""

    def test_sin_zero(self):
        """Test sine of zero."""
        assert math.sin(0) == pytest.approx(0.0)

    def test_sin_pi_half(self):
        """Test sine of pi/2 (90 degrees)."""
        assert math.sin(math.pi / 2) == pytest.approx(1.0)

    def test_sin_pi(self):
        """Test sine of pi (180 degrees)."""
        assert math.sin(math.pi) == pytest.approx(0.0, abs=1e-10)

    def test_sin_three_pi_half(self):
        """Test sine of 3pi/2 (270 degrees)."""
        assert math.sin(3 * math.pi / 2) == pytest.approx(-1.0)

    def test_sin_pi_sixth(self):
        """Test sine of pi/6 (30 degrees)."""
        assert math.sin(math.pi / 6) == pytest.approx(0.5)

    def test_sin_negative_angle(self):
        """Test sine of negative angle."""
        assert math.sin(-math.pi / 2) == pytest.approx(-1.0)


class TestCos:
    """Test cases for cosine operation."""

    def test_cos_zero(self):
        """Test cosine of zero."""
        assert math.cos(0) == pytest.approx(1.0)

    def test_cos_pi_half(self):
        """Test cosine of pi/2 (90 degrees)."""
        assert math.cos(math.pi / 2) == pytest.approx(0.0, abs=1e-10)

    def test_cos_pi(self):
        """Test cosine of pi (180 degrees)."""
        assert math.cos(math.pi) == pytest.approx(-1.0)

    def test_cos_three_pi_half(self):
        """Test cosine of 3pi/2 (270 degrees)."""
        assert math.cos(3 * math.pi / 2) == pytest.approx(0.0, abs=1e-10)

    def test_cos_pi_third(self):
        """Test cosine of pi/3 (60 degrees)."""
        assert math.cos(math.pi / 3) == pytest.approx(0.5)

    def test_cos_negative_angle(self):
        """Test cosine of negative angle."""
        assert math.cos(-math.pi) == pytest.approx(-1.0)


class TestTan:
    """Test cases for tangent operation."""

    def test_tan_zero(self):
        """Test tangent of zero."""
        assert math.tan(0) == pytest.approx(0.0)

    def test_tan_pi_fourth(self):
        """Test tangent of pi/4 (45 degrees)."""
        assert math.tan(math.pi / 4) == pytest.approx(1.0)

    def test_tan_pi_sixth(self):
        """Test tangent of pi/6 (30 degrees)."""
        assert math.tan(math.pi / 6) == pytest.approx(1 / math.sqrt(3))

    def test_tan_negative_angle(self):
        """Test tangent of negative angle."""
        assert math.tan(-math.pi / 4) == pytest.approx(-1.0)

    def test_tan_small_angle(self):
        """Test tangent of small angle."""
        assert math.tan(0.1) == pytest.approx(0.10033467)
