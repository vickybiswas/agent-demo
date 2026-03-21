"""Unit tests for modulo operation."""

import pytest
from routes.modulo import modulo_numbers


class TestModuloNumbers:
    """Unit tests for modulo operation."""

    def test_modulo_basic(self):
        """Test basic modulo operation."""
        assert modulo_numbers(5, 3) == 2
        assert modulo_numbers(10, 3) == 1

    def test_modulo_zero_remainder(self):
        """Test modulo with zero remainder."""
        assert modulo_numbers(10, 5) == 0
        assert modulo_numbers(8, 2) == 0

    def test_modulo_negative_dividend(self):
        """Test modulo with negative dividend."""
        result = modulo_numbers(-5, 3)
        assert result == pytest.approx(1)

    def test_modulo_negative_divisor(self):
        """Test modulo with negative divisor."""
        result = modulo_numbers(5, -3)
        assert result == pytest.approx(-1)

    def test_modulo_both_negative(self):
        """Test modulo with both negative."""
        result = modulo_numbers(-5, -3)
        assert result == pytest.approx(-2)

    def test_modulo_by_zero(self):
        """Test modulo by zero raises error."""
        with pytest.raises(ValueError, match="Division by zero"):
            modulo_numbers(5, 0)

    def test_modulo_decimal(self):
        """Test modulo with decimal numbers."""
        result = modulo_numbers(5.5, 2)
        assert result == pytest.approx(1.5)
