"""Unit tests for divide operation."""

import pytest
from routes.divide import divide_numbers


class TestDivideNumbers:
    """Unit tests for divide operation."""

    def test_divide_positive_integers(self) -> None:
        """Test dividing positive integers."""
        assert divide_numbers(6, 3) == 2.0

    def test_divide_with_remainder(self) -> None:
        """Test division with remainder."""
        assert divide_numbers(5, 2) == pytest.approx(2.5)

    def test_divide_negative_numbers(self) -> None:
        """Test dividing negative numbers."""
        assert divide_numbers(-6, 3) == -2.0
        assert divide_numbers(6, -3) == -2.0
        assert divide_numbers(-6, -3) == 2.0

    def test_divide_by_zero(self) -> None:
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Division by zero"):
            divide_numbers(5, 0)

    def test_divide_decimals(self) -> None:
        """Test dividing decimal numbers."""
        assert divide_numbers(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_by_one(self) -> None:
        """Test dividing by one."""
        assert divide_numbers(5, 1) == 5.0

    def test_divide_zero_by_number(self) -> None:
        """Test dividing zero by a number."""
        assert divide_numbers(0, 5) == 0.0

    def test_divide_small_numbers(self) -> None:
        """Test dividing small numbers."""
        assert divide_numbers(0.1, 0.2) == pytest.approx(0.5)
