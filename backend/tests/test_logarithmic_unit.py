"""
Unit tests for logarithmic operations (log, ln).

Tests the core logarithmic logic with various numeric inputs.
"""

import pytest
import math


class TestLog:
    """Test cases for base-10 logarithm operation."""

    def test_log_one(self):
        """Test log10 of one."""
        assert math.log10(1) == pytest.approx(0.0)

    def test_log_ten(self):
        """Test log10 of ten."""
        assert math.log10(10) == pytest.approx(1.0)

    def test_log_hundred(self):
        """Test log10 of one hundred."""
        assert math.log10(100) == pytest.approx(2.0)

    def test_log_thousand(self):
        """Test log10 of one thousand."""
        assert math.log10(1000) == pytest.approx(3.0)

    def test_log_small_decimal(self):
        """Test log10 of small decimal."""
        assert math.log10(0.1) == pytest.approx(-1.0)

    def test_log_fractional(self):
        """Test log10 of fractional number."""
        assert math.log10(5) == pytest.approx(0.69897)

    def test_log_zero_raises_error(self):
        """Test that log of zero raises error."""
        with pytest.raises(ValueError):
            math.log10(0)

    def test_log_negative_raises_error(self):
        """Test that log of negative raises error."""
        with pytest.raises(ValueError):
            math.log10(-5)


class TestLn:
    """Test cases for natural logarithm operation."""

    def test_ln_one(self):
        """Test ln of one."""
        assert math.log(1) == pytest.approx(0.0)

    def test_ln_e(self):
        """Test ln of e (natural constant)."""
        assert math.log(math.e) == pytest.approx(1.0)

    def test_ln_e_squared(self):
        """Test ln of e^2."""
        assert math.log(math.e ** 2) == pytest.approx(2.0)

    def test_ln_small_number(self):
        """Test ln of small number."""
        assert math.log(0.5) == pytest.approx(-0.69314718)

    def test_ln_large_number(self):
        """Test ln of large number."""
        assert math.log(1000) == pytest.approx(6.90775527)

    def test_ln_fractional(self):
        """Test ln of fractional number."""
        assert math.log(5) == pytest.approx(1.60943791)

    def test_ln_zero_raises_error(self):
        """Test that ln of zero raises error."""
        with pytest.raises(ValueError):
            math.log(0)

    def test_ln_negative_raises_error(self):
        """Test that ln of negative raises error."""
        with pytest.raises(ValueError):
            math.log(-10)
