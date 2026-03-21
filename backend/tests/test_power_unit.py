"""Unit tests for power operation."""

import pytest
from routes.power import power_numbers


class TestPowerNumbers:
    """Unit tests for power operation."""

    def test_power_basic(self):
        """Test basic power operation."""
        assert power_numbers(2, 3) == 8
        assert power_numbers(5, 2) == 25

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        assert power_numbers(5, 0) == 1
        assert power_numbers(100, 0) == 1

    def test_power_one_exponent(self):
        """Test power with one exponent."""
        assert power_numbers(5, 1) == 5
        assert power_numbers(100, 1) == 100

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        result = power_numbers(2, -1)
        assert result == pytest.approx(0.5)

    def test_power_decimal_base(self):
        """Test power with decimal base."""
        result = power_numbers(2.5, 2)
        assert result == pytest.approx(6.25)

    def test_power_decimal_exponent(self):
        """Test power with decimal exponent."""
        result = power_numbers(4, 0.5)
        assert result == pytest.approx(2.0)

    def test_power_negative_base(self):
        """Test power with negative base."""
        result = power_numbers(-2, 3)
        assert result == pytest.approx(-8)
