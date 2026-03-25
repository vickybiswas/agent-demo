"""
Unit tests for scientific operations.
"""

import math
import pytest
from operations.scientific import (
    sqrt_number, power, sin_degrees, cos_degrees, tan_degrees,
    logarithm, factorial_number, reciprocal, percentage,
    get_pi, get_e
)


class TestScientificUnit:
    """Unit tests for scientific functions."""

    # Square Root Tests
    def test_sqrt_positive(self) -> None:
        """Test square root of positive number."""
        result = sqrt_number(16)
        assert result == 4.0

    def test_sqrt_float(self) -> None:
        """Test square root of float."""
        result = sqrt_number(2.25)
        assert result == 1.5

    def test_sqrt_negative(self) -> None:
        """Test square root of negative returns 0."""
        result = sqrt_number(-4)
        assert result == 0.0

    # Power Tests
    def test_power_positive(self) -> None:
        """Test positive base and exponent."""
        result = power(2, 3)
        assert result == 8.0

    def test_power_negative_base(self) -> None:
        """Test negative base."""
        result = power(-2, 2)
        assert result == 4.0

    def test_power_zero_exponent(self) -> None:
        """Test any number to power 0 is 1."""
        result = power(5, 0)
        assert result == 1.0

    # Trigonometry Tests
    def test_sin_0_degrees(self) -> None:
        """Test sin(0) = 0."""
        result = sin_degrees(0)
        assert abs(result - 0.0) < 0.001

    def test_sin_90_degrees(self) -> None:
        """Test sin(90) = 1."""
        result = sin_degrees(90)
        assert abs(result - 1.0) < 0.001

    def test_cos_0_degrees(self) -> None:
        """Test cos(0) = 1."""
        result = cos_degrees(0)
        assert abs(result - 1.0) < 0.001

    def test_cos_90_degrees(self) -> None:
        """Test cos(90) ≈ 0."""
        result = cos_degrees(90)
        assert abs(result - 0.0) < 0.001

    def test_tan_0_degrees(self) -> None:
        """Test tan(0) = 0."""
        result = tan_degrees(0)
        assert abs(result - 0.0) < 0.001

    # Logarithm Tests
    def test_log_base_10(self) -> None:
        """Test log base 10."""
        result = logarithm(100, 10)
        assert result == 2.0

    def test_log_base_2(self) -> None:
        """Test log base 2."""
        result = logarithm(8, 2)
        assert result == 3.0

    def test_log_negative(self) -> None:
        """Test log of negative returns 0."""
        result = logarithm(-5)
        assert result == 0.0

    def test_log_zero(self) -> None:
        """Test log of zero returns 0."""
        result = logarithm(0)
        assert result == 0.0

    # Factorial Tests
    def test_factorial_5(self) -> None:
        """Test 5! = 120."""
        result = factorial_number(5)
        assert result == 120.0

    def test_factorial_0(self) -> None:
        """Test 0! = 1."""
        result = factorial_number(0)
        assert result == 1.0

    def test_factorial_negative(self) -> None:
        """Test negative factorial returns 0."""
        result = factorial_number(-3)
        assert result == 0.0

    def test_factorial_float(self) -> None:
        """Test float factorial returns 0."""
        result = factorial_number(5.5)
        assert result == 0.0

    # Reciprocal Tests
    def test_reciprocal_positive(self) -> None:
        """Test reciprocal of 4 is 0.25."""
        result = reciprocal(4)
        assert result == 0.25

    def test_reciprocal_zero(self) -> None:
        """Test reciprocal of 0 returns 0."""
        result = reciprocal(0)
        assert result == 0.0

    # Percentage Tests
    def test_percentage_10_of_100(self) -> None:
        """Test 10% of 100 is 10."""
        result = percentage(100, 10)
        assert result == 10.0

    def test_percentage_25_of_80(self) -> None:
        """Test 25% of 80 is 20."""
        result = percentage(80, 25)
        assert result == 20.0

    # Constants Tests
    def test_get_pi(self) -> None:
        """Test get_pi returns correct value."""
        result = get_pi()
        assert abs(result - math.pi) < 0.0001

    def test_get_e(self) -> None:
        """Test get_e returns correct value."""
        result = get_e()
        assert abs(result - math.e) < 0.0001
