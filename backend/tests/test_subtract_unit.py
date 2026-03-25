"""
Unit tests for subtract operation.
"""

import pytest
from operations.subtract import subtract_numbers


class TestSubtractUnit:
    """Unit tests for subtract_numbers function."""

    def test_subtract_positive_numbers(self) -> None:
        """Test subtracting two positive numbers."""
        result = subtract_numbers(10, 3)
        assert result == 7

    def test_subtract_negative_numbers(self) -> None:
        """Test subtracting negative numbers."""
        result = subtract_numbers(-5, -3)
        assert result == -2

    def test_subtract_mixed_signs(self) -> None:
        """Test subtracting with mixed signs."""
        result = subtract_numbers(10, -3)
        assert result == 13

    def test_subtract_floats(self) -> None:
        """Test subtracting floating point numbers."""
        result = subtract_numbers(10.5, 3.2)
        assert abs(result - 7.3) < 0.01

    def test_subtract_zero(self) -> None:
        """Test subtracting with zero."""
        result = subtract_numbers(5, 0)
        assert result == 5
