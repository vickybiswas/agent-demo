"""Unit tests for absolute value operation."""

import pytest
from routes.abs import abs_number


class TestAbsNumbers:
    """Unit tests for absolute value operation."""

    def test_abs_positive(self):
        """Test absolute value of positive number."""
        assert abs_number(5) == 5
        assert abs_number(100) == 100

    def test_abs_negative(self):
        """Test absolute value of negative number."""
        assert abs_number(-5) == 5
        assert abs_number(-100) == 100

    def test_abs_zero(self):
        """Test absolute value of zero."""
        assert abs_number(0) == 0

    def test_abs_decimal_positive(self):
        """Test absolute value of decimal positive."""
        assert abs_number(5.5) == 5.5

    def test_abs_decimal_negative(self):
        """Test absolute value of decimal negative."""
        assert abs_number(-5.5) == 5.5

    def test_abs_small_number(self):
        """Test absolute value of small number."""
        result = abs_number(-0.001)
        assert result == pytest.approx(0.001)

    def test_abs_large_number(self):
        """Test absolute value of large number."""
        assert abs_number(-1000000) == 1000000
