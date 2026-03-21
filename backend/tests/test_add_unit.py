"""
Unit tests for addition operation.

Tests the core addition logic with various input types and edge cases.
"""

import pytest


def add(num1, num2):
    """Helper function to test addition."""
    return num1 + num2


class TestAdd:
    """Test cases for addition operation."""

    def test_add_positive_integers(self):
        """Test adding two positive integers."""
        assert add(5, 3) == 8

    def test_add_negative_integers(self):
        """Test adding two negative integers."""
        assert add(-5, -3) == -8

    def test_add_mixed_signs(self):
        """Test adding positive and negative integers."""
        assert add(5, -3) == 2

    def test_add_floats(self):
        """Test adding two floating point numbers."""
        assert add(5.5, 3.2) == pytest.approx(8.7)

    def test_add_zero(self):
        """Test adding zero to a number."""
        assert add(5, 0) == 5

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        assert add(1000000, 2000000) == 3000000

    def test_add_small_decimals(self):
        """Test adding very small decimal numbers."""
        assert add(0.001, 0.002) == pytest.approx(0.003)

    def test_add_negative_zero(self):
        """Test adding negative zero."""
        assert add(-0.0, 5) == 5
