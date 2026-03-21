"""Unit tests for multiply operation."""

import pytest
from routes.multiply import multiply_numbers


class TestMultiplyNumbers:
    """Unit tests for multiply operation."""

    def test_multiply_positive_integers(self) -> None:
        """Test multiplying two positive integers."""
        assert multiply_numbers(5, 3) == 15

    def test_multiply_negative_numbers(self) -> None:
        """Test multiplying negative numbers."""
        assert multiply_numbers(-5, 3) == -15
        assert multiply_numbers(-5, -3) == 15

    def test_multiply_decimals(self) -> None:
        """Test multiplying decimal numbers."""
        assert multiply_numbers(5.5, 2.0) == pytest.approx(11.0)

    def test_multiply_by_zero(self) -> None:
        """Test multiplying by zero."""
        assert multiply_numbers(5, 0) == 0
        assert multiply_numbers(0, 0) == 0

    def test_multiply_by_one(self) -> None:
        """Test multiplying by one."""
        assert multiply_numbers(5, 1) == 5
        assert multiply_numbers(1, 1) == 1

    def test_multiply_large_numbers(self) -> None:
        """Test multiplying large numbers."""
        assert multiply_numbers(1e5, 1e5) == 1e10

    def test_multiply_fractional_result(self) -> None:
        """Test multiplication resulting in fractional number."""
        assert multiply_numbers(0.5, 0.5) == pytest.approx(0.25)
