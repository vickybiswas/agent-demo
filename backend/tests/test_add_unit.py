"""
Unit tests for add operation.
"""

import pytest
from operations.add import add_numbers


class TestAddUnit:
    """Unit tests for add_numbers function."""

    def test_add_positive_numbers(self) -> None:
        """Test adding two positive numbers."""
        result = add_numbers(5, 3)
        assert result == 8

    def test_add_negative_numbers(self) -> None:
        """Test adding two negative numbers."""
        result = add_numbers(-5, -3)
        assert result == -8

    def test_add_mixed_signs(self) -> None:
        """Test adding numbers with mixed signs."""
        result = add_numbers(10, -3)
        assert result == 7

    def test_add_floats(self) -> None:
        """Test adding floating point numbers."""
        result = add_numbers(5.5, 3.2)
        assert abs(result - 8.7) < 0.01

    def test_add_zero(self) -> None:
        """Test adding with zero."""
        result = add_numbers(5, 0)
        assert result == 5
