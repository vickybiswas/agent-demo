"""Unit tests for calculator operations."""
import pytest


# Test addition
def test_add_positive() -> None:
    """Test addition of positive numbers."""
    assert 5 + 3 == 8


def test_add_negative() -> None:
    """Test addition with negative numbers."""
    assert -5 + 3 == -2


def test_add_zero() -> None:
    """Test addition with zero."""
    assert 5 + 0 == 5


def test_add_floats() -> None:
    """Test addition with decimal numbers."""
    assert 5.5 + 3.2 == pytest.approx(8.7)


def test_add_large_numbers() -> None:
    """Test addition with large numbers."""
    assert 999999 + 1 == 1000000


# Test subtraction
def test_subtract_positive() -> None:
    """Test subtraction of positive numbers."""
    assert 5 - 3 == 2


def test_subtract_negative() -> None:
    """Test subtraction with negative numbers."""
    assert 5 - (-3) == 8


def test_subtract_zero() -> None:
    """Test subtraction with zero."""
    assert 5 - 0 == 5


def test_subtract_floats() -> None:
    """Test subtraction with decimal numbers."""
    assert 5.5 - 3.2 == pytest.approx(2.3)


def test_subtract_large() -> None:
    """Test subtraction with large numbers."""
    assert 1000000 - 1 == 999999


# Test multiplication
def test_multiply_positive() -> None:
    """Test multiplication of positive numbers."""
    assert 5 * 3 == 15


def test_multiply_negative() -> None:
    """Test multiplication with negative numbers."""
    assert -5 * 3 == -15


def test_multiply_zero() -> None:
    """Test multiplication with zero."""
    assert 5 * 0 == 0


def test_multiply_floats() -> None:
    """Test multiplication with decimal numbers."""
    assert 2.5 * 4 == 10.0


def test_multiply_large() -> None:
    """Test multiplication with large numbers."""
    assert 1000 * 1000 == 1000000


# Test division
def test_divide_positive() -> None:
    """Test division of positive numbers."""
    assert 6 / 2 == 3


def test_divide_negative() -> None:
    """Test division with negative numbers."""
    assert -6 / 2 == -3


def test_divide_floats() -> None:
    """Test division with decimal numbers."""
    assert 7.5 / 2.5 == 3


def test_divide_by_zero() -> None:
    """Test division by zero raises error."""
    with pytest.raises(ZeroDivisionError):
        6 / 0


def test_divide_remainder() -> None:
    """Test division with remainder."""
    assert 7 / 2 == 3.5
