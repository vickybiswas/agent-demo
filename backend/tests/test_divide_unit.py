"""
Unit tests for division operation.

Tests the core division logic with various input types and edge cases.
"""

import pytest


def divide(num1, num2):
    """Helper function to test division."""
    if num2 == 0:
        raise ValueError("Division by zero is not allowed")
    return num1 / num2


class TestDivide:
    """Test cases for division operation."""

    def test_divide_positive_integers(self):
        """Test dividing two positive integers."""
        assert divide(6, 3) == 2

    def test_divide_negative_integers(self):
        """Test dividing two negative integers."""
        assert divide(-6, -3) == 2

    def test_divide_mixed_signs(self):
        """Test dividing positive by negative."""
        assert divide(6, -3) == -2

    def test_divide_floats(self):
        """Test dividing two floating point numbers."""
        assert divide(5.5, 2.0) == pytest.approx(2.75)

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises an error."""
        with pytest.raises(ValueError):
            divide(5, 0)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0

    def test_divide_large_numbers(self):
        """Test dividing large numbers."""
        assert divide(2000000, 1000) == 2000

    def test_divide_to_small_decimal(self):
        """Test division resulting in small decimal."""
        assert divide(1, 10) == pytest.approx(0.1)
