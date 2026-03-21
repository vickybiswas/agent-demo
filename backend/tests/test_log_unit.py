"""Unit tests for logarithm base 10 operation."""

import pytest
import math
from routes.log import log_number


class TestLogNumbers:
    """Unit tests for logarithm base 10 operation."""

    def test_log_one(self):
        """Test logarithm of one."""
        assert log_number(1) == 0

    def test_log_ten(self):
        """Test logarithm of ten."""
        assert log_number(10) == 1

    def test_log_hundred(self):
        """Test logarithm of hundred."""
        assert log_number(100) == 2

    def test_log_thousand(self):
        """Test logarithm of thousand."""
        assert log_number(1000) == 3

    def test_log_zero(self):
        """Test logarithm of zero raises error."""
        with pytest.raises(ValueError, match="Cannot take logarithm"):
            log_number(0)

    def test_log_negative(self):
        """Test logarithm of negative raises error."""
        with pytest.raises(ValueError, match="Cannot take logarithm"):
            log_number(-10)

    def test_log_decimal(self):
        """Test logarithm of decimal."""
        result = log_number(0.1)
        assert result == pytest.approx(-1.0)
