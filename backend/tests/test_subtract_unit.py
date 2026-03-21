"""Unit tests for subtract operation."""

import pytest
from routes.subtract import subtract_numbers


class TestSubtractNumbers:
    """Unit tests for subtract operation."""

    def test_subtract_positive_integers(self) -> None:
        """Test subtracting two positive integers."""
        assert subtract_numbers(5, 3) == 2

    def test_subtract_negative_numbers(self) -> None:
        """Test subtracting negative numbers."""
        assert subtract_numbers(-5, 3) == -8
        assert subtract_numbers(-5, -3) == -2

    def test_subtract_decimals(self) -> None:
        """Test subtracting decimal numbers."""
        assert subtract_numbers(8.7, 3.2) == pytest.approx(5.5)

    def test_subtract_zero(self) -> None:
        """Test subtracting zero."""
        assert subtract_numbers(5, 0) == 5
        assert subtract_numbers(0, 0) == 0

    def test_subtract_large_numbers(self) -> None:
        """Test subtracting large numbers."""
        assert subtract_numbers(1e10, 5e9) == 5e9

    def test_subtract_same_numbers(self) -> None:
        """Test subtracting same numbers."""
        assert subtract_numbers(7, 7) == 0

    def test_subtract_results_in_negative(self) -> None:
        """Test subtraction resulting in negative number."""
        assert subtract_numbers(3, 5) == -2
