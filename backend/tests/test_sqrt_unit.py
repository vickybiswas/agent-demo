"""Unit tests for square root operation."""

import pytest
from routes.sqrt import sqrt_number


class TestSqrtNumbers:
    """Unit tests for square root operation."""

    def test_sqrt_perfect_square(self):
        """Test square root of perfect square."""
        assert sqrt_number(4) == 2
        assert sqrt_number(9) == 3
        assert sqrt_number(16) == 4

    def test_sqrt_zero(self):
        """Test square root of zero."""
        assert sqrt_number(0) == 0

    def test_sqrt_one(self):
        """Test square root of one."""
        assert sqrt_number(1) == 1

    def test_sqrt_decimal(self):
        """Test square root of decimal."""
        result = sqrt_number(2.25)
        assert result == pytest.approx(1.5)

    def test_sqrt_negative(self):
        """Test square root of negative raises error."""
        with pytest.raises(ValueError, match="Cannot take square root of negative"):
            sqrt_number(-4)

    def test_sqrt_large_number(self):
        """Test square root of large number."""
        result = sqrt_number(1000000)
        assert result == pytest.approx(1000)

    def test_sqrt_small_decimal(self):
        """Test square root of small decimal."""
        result = sqrt_number(0.25)
        assert result == pytest.approx(0.5)
