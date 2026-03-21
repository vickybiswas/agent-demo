"""Unit tests for add operation."""

import pytest
from routes.add import add_numbers


class TestAddNumbers:
    """Unit tests for add operation."""

    def test_add_positive_integers(self) -> None:
        """Test adding two positive integers."""
        assert add_numbers(5, 3) == 8

    def test_add_negative_numbers(self) -> None:
        """Test adding negative numbers."""
        assert add_numbers(-5, 3) == -2
        assert add_numbers(-5, -3) == -8

    def test_add_decimals(self) -> None:
        """Test adding decimal numbers."""
        assert add_numbers(5.5, 3.2) == pytest.approx(8.7)

    def test_add_zero(self) -> None:
        """Test adding zero."""
        assert add_numbers(5, 0) == 5
        assert add_numbers(0, 0) == 0

    def test_add_large_numbers(self) -> None:
        """Test adding large numbers."""
        assert add_numbers(1e10, 1e10) == 2e10

    def test_add_mixed_signs(self) -> None:
        """Test adding mixed positive and negative numbers."""
        assert add_numbers(10, -7) == 3
        assert add_numbers(-10, 7) == -3

    def test_add_fractional_numbers(self) -> None:
        """Test adding fractional numbers."""
        assert add_numbers(0.1, 0.2) == pytest.approx(0.3)
