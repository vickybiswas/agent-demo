"""Unit tests for natural logarithm operation."""

import pytest
import math
from routes.ln import ln_number


class TestLnNumbers:
    """Unit tests for natural logarithm operation."""

    def test_ln_one(self):
        """Test natural logarithm of one."""
        assert ln_number(1) == 0

    def test_ln_e(self):
        """Test natural logarithm of e."""
        result = ln_number(math.e)
        assert result == pytest.approx(1.0)

    def test_ln_ten(self):
        """Test natural logarithm of ten."""
        result = ln_number(10)
        assert result == pytest.approx(math.log(10))

    def test_ln_half(self):
        """Test natural logarithm of 0.5."""
        result = ln_number(0.5)
        assert result == pytest.approx(math.log(0.5))

    def test_ln_zero(self):
        """Test natural logarithm of zero raises error."""
        with pytest.raises(ValueError, match="Cannot take logarithm"):
            ln_number(0)

    def test_ln_negative(self):
        """Test natural logarithm of negative raises error."""
        with pytest.raises(ValueError, match="Cannot take logarithm"):
            ln_number(-5)

    def test_ln_large_number(self):
        """Test natural logarithm of large number."""
        result = ln_number(1000)
        assert result == pytest.approx(math.log(1000))
