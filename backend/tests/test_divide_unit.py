"""
Unit tests for divide operation.
"""

import pytest
from operations.divide import divide_numbers


class TestDivideUnit:
    """Unit tests for divide_numbers function."""

    def test_divide_positive_numbers(self) -> None:
        """Test dividing two positive numbers."""
        result = divide_numbers(20, 4)
        assert result == 5

    def test_divide_negative_numbers(self) -> None:
        """Test dividing negative numbers."""
        result = divide_numbers(-20, -4)
        assert result == 5

    def test_divide_mixed_signs(self) -> None:
        """Test dividing with mixed signs."""
        result = divide_numbers(20, -4)
        assert result == -5

    def test_divide_floats(self) -> None:
        """Test dividing floating point numbers."""
        result = divide_numbers(10.0, 2.5)
        assert abs(result - 4.0) < 0.01

    def test_divide_by_zero(self) -> None:
        """Test dividing by zero returns 0."""
        result = divide_numbers(10, 0)
        assert result == 0
