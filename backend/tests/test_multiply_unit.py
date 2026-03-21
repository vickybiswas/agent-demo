"""
Unit tests for multiplication operation.

Tests the core multiplication logic with various input types and edge cases.
"""

import pytest


def multiply(num1, num2):
    """Helper function to test multiplication."""
    return num1 * num2


class TestMultiply:
    """Test cases for multiplication operation."""

    def test_multiply_positive_integers(self):
        """Test multiplying two positive integers."""
        assert multiply(5, 3) == 15

    def test_multiply_negative_integers(self):
        """Test multiplying two negative integers."""
        assert multiply(-5, -3) == 15

    def test_multiply_mixed_signs(self):
        """Test multiplying positive and negative integers."""
        assert multiply(5, -3) == -15

    def test_multiply_floats(self):
        """Test multiplying two floating point numbers."""
        assert multiply(5.5, 2.0) == pytest.approx(11.0)

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0

    def test_multiply_by_one(self):
        """Test multiplying by one."""
        assert multiply(5, 1) == 5

    def test_multiply_large_numbers(self):
        """Test multiplying large numbers."""
        assert multiply(1000, 2000) == 2000000

    def test_multiply_small_decimals(self):
        """Test multiplying very small decimal numbers."""
        assert multiply(0.1, 0.2) == pytest.approx(0.02)
