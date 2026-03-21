"""
Unit tests for subtraction operation.

Tests the core subtraction logic with various input types and edge cases.
"""

import pytest


def subtract(num1, num2):
    """Helper function to test subtraction."""
    return num1 - num2


class TestSubtract:
    """Test cases for subtraction operation."""

    def test_subtract_positive_integers(self):
        """Test subtracting two positive integers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_integers(self):
        """Test subtracting two negative integers."""
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_signs(self):
        """Test subtracting positive and negative integers."""
        assert subtract(5, -3) == 8

    def test_subtract_floats(self):
        """Test subtracting two floating point numbers."""
        assert subtract(5.5, 3.2) == pytest.approx(2.3)

    def test_subtract_zero(self):
        """Test subtracting zero from a number."""
        assert subtract(5, 0) == 5

    def test_subtract_same_numbers(self):
        """Test subtracting a number from itself."""
        assert subtract(5, 5) == 0

    def test_subtract_large_numbers(self):
        """Test subtracting large numbers."""
        assert subtract(3000000, 2000000) == 1000000

    def test_subtract_small_decimals(self):
        """Test subtracting very small decimal numbers."""
        assert subtract(0.005, 0.002) == pytest.approx(0.003)
