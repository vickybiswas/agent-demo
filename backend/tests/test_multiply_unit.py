"""
Unit tests for multiply operation.
"""

import pytest
from operations.multiply import multiply_numbers


class TestMultiplyUnit:
    """Unit tests for multiply_numbers function."""

    def test_multiply_positive_numbers(self) -> None:
        """Test multiplying two positive numbers."""
        result = multiply_numbers(4, 5)
        assert result == 20

    def test_multiply_negative_numbers(self) -> None:
        """Test multiplying negative numbers."""
        result = multiply_numbers(-4, -5)
        assert result == 20

    def test_multiply_mixed_signs(self) -> None:
        """Test multiplying with mixed signs."""
        result = multiply_numbers(4, -5)
        assert result == -20

    def test_multiply_floats(self) -> None:
        """Test multiplying floating point numbers."""
        result = multiply_numbers(2.5, 4.0)
        assert result == 10.0

    def test_multiply_by_zero(self) -> None:
        """Test multiplying by zero."""
        result = multiply_numbers(5, 0)
        assert result == 0
