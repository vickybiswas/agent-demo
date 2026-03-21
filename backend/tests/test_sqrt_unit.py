"""
Unit tests for square root operation.

Tests the core square root logic with various input types and edge cases.
"""

import pytest
import math


def sqrt(num1):
    """Helper function to test square root."""
    if num1 < 0:
        raise ValueError("Square root of negative number is not allowed")
    return math.sqrt(num1)


class TestSqrt:
    """Test cases for square root operation."""

    def test_sqrt_positive_integer(self):
        """Test square root of positive integer."""
        assert sqrt(9) == 3.0

    def test_sqrt_zero(self):
        """Test square root of zero."""
        assert sqrt(0) == 0.0

    def test_sqrt_one(self):
        """Test square root of one."""
        assert sqrt(1) == 1.0

    def test_sqrt_float(self):
        """Test square root of floating point number."""
        assert sqrt(2.25) == pytest.approx(1.5)

    def test_sqrt_large_number(self):
        """Test square root of large number."""
        assert sqrt(1000000) == 1000.0

    def test_sqrt_decimal_result(self):
        """Test square root resulting in decimal."""
        assert sqrt(2) == pytest.approx(1.41421356)

    def test_sqrt_small_decimal(self):
        """Test square root of small decimal."""
        assert sqrt(0.25) == pytest.approx(0.5)

    def test_sqrt_negative_raises_error(self):
        """Test that square root of negative raises error."""
        with pytest.raises(ValueError):
            sqrt(-1)

    def test_sqrt_large_negative_raises_error(self):
        """Test that square root of large negative raises error."""
        with pytest.raises(ValueError):
            sqrt(-1000)
