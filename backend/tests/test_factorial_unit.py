"""Unit tests for factorial operation."""

import pytest
from routes.factorial import factorial_number


class TestFactorialNumbers:
    """Unit tests for factorial operation."""

    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial_number(0) == 1

    def test_factorial_one(self):
        """Test factorial of one."""
        assert factorial_number(1) == 1

    def test_factorial_five(self):
        """Test factorial of five."""
        assert factorial_number(5) == 120

    def test_factorial_ten(self):
        """Test factorial of ten."""
        assert factorial_number(10) == 3628800

    def test_factorial_negative(self):
        """Test factorial of negative raises error."""
        with pytest.raises(ValueError, match="Cannot calculate factorial"):
            factorial_number(-5)

    def test_factorial_decimal(self):
        """Test factorial of decimal raises error."""
        with pytest.raises(ValueError, match="Factorial only works with integers"):
            factorial_number(5.5)

    def test_factorial_large(self):
        """Test factorial of larger number."""
        result = factorial_number(6)
        assert result == 720
