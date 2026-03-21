"""
Unit tests for power operation.

Tests the core power/exponentiation logic with various input types and edge cases.
"""

import pytest


def power(num1, num2):
    """Helper function to test power operation."""
    return num1 ** num2


class TestPower:
    """Test cases for power operation."""

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        """Test any number to power of zero."""
        assert power(5, 0) == 1

    def test_power_one_exponent(self):
        """Test number to power of one."""
        assert power(7, 1) == 7

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        assert power(2, -2) == pytest.approx(0.25)

    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        assert power(4, 0.5) == pytest.approx(2.0)

    def test_power_float_base(self):
        """Test power with float base."""
        assert power(2.5, 2) == pytest.approx(6.25)

    def test_power_negative_base(self):
        """Test power with negative base."""
        assert power(-2, 3) == -8

    def test_power_negative_base_even_exponent(self):
        """Test power with negative base and even exponent."""
        assert power(-3, 2) == 9

    def test_power_large_numbers(self):
        """Test power with large numbers."""
        assert power(10, 3) == 1000

    def test_power_zero_base(self):
        """Test power with zero base."""
        assert power(0, 5) == 0
