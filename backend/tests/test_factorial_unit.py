"""
Unit tests for factorial operation.

Tests the core factorial logic with various input types and edge cases.
"""

import pytest
import math


def factorial(num1):
    """Helper function to test factorial."""
    if isinstance(num1, float):
        if num1 != int(num1):
            raise ValueError(
                "Factorial is only defined for non-negative integers"
            )
        num1 = int(num1)

    if not isinstance(num1, int) or isinstance(num1, bool):
        raise ValueError(
            "Factorial is only defined for non-negative integers"
        )

    if num1 < 0:
        raise ValueError("Factorial of negative number is not allowed")

    return math.factorial(num1)


class TestFactorial:
    """Test cases for factorial operation."""

    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of one."""
        assert factorial(1) == 1

    def test_factorial_five(self):
        """Test factorial of five."""
        assert factorial(5) == 120

    def test_factorial_ten(self):
        """Test factorial of ten."""
        assert factorial(10) == 3628800

    def test_factorial_small_number(self):
        """Test factorial of small number."""
        assert factorial(3) == 6

    def test_factorial_four(self):
        """Test factorial of four."""
        assert factorial(4) == 24

    def test_factorial_float_whole_number(self):
        """Test factorial of float that is whole number."""
        assert factorial(5.0) == 120

    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative raises error."""
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_float_non_integer_raises_error(self):
        """Test that factorial of non-integer float raises error."""
        with pytest.raises(ValueError):
            factorial(5.5)

    def test_factorial_large_number(self):
        """Test factorial of larger number."""
        assert factorial(12) == 479001600
