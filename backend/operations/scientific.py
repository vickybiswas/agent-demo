"""
Scientific operations module for advanced calculator functions.
Includes trigonometry, logarithms, roots, and other advanced math.
"""

import math


def sqrt_number(num: float) -> float:
    """
    Calculate square root of a number.

    Args:
        num: Number to find square root of (must be >= 0)

    Returns:
        float: Square root of the number (0 if negative)
    """
    if num < 0:
        return 0.0
    return math.sqrt(num)


def power(base: float, exponent: float) -> float:
    """
    Raise base to the power of exponent.

    Args:
        base: Base number
        exponent: Power/exponent

    Returns:
        float: Result of base^exponent
    """
    try:
        return base ** exponent
    except (ValueError, OverflowError):
        return 0.0


def sin_degrees(angle: float) -> float:
    """
    Calculate sine of angle in degrees.

    Args:
        angle: Angle in degrees

    Returns:
        float: Sine of the angle
    """
    radians = math.radians(angle)
    return round(math.sin(radians), 10)


def cos_degrees(angle: float) -> float:
    """
    Calculate cosine of angle in degrees.

    Args:
        angle: Angle in degrees

    Returns:
        float: Cosine of the angle
    """
    radians = math.radians(angle)
    return round(math.cos(radians), 10)


def tan_degrees(angle: float) -> float:
    """
    Calculate tangent of angle in degrees.

    Args:
        angle: Angle in degrees

    Returns:
        float: Tangent of the angle
    """
    radians = math.radians(angle)
    try:
        return round(math.tan(radians), 10)
    except ValueError:
        return 0.0


def logarithm(num: float, base: float = 10) -> float:
    """
    Calculate logarithm of a number with given base.

    Args:
        num: Number to find logarithm of (must be > 0)
        base: Base of logarithm (default 10)

    Returns:
        float: Logarithm of the number (0 if invalid)
    """
    if num <= 0 or base <= 0 or base == 1:
        return 0.0
    try:
        return math.log(num, base)
    except ValueError:
        return 0.0


def factorial_number(num: float) -> float:
    """
    Calculate factorial of a number.

    Args:
        num: Number to find factorial of (must be non-negative integer)

    Returns:
        float: Factorial of the number (0 if negative or not integer)
    """
    if num < 0 or num != int(num):
        return 0.0
    try:
        return float(math.factorial(int(num)))
    except (ValueError, OverflowError):
        return 0.0


def reciprocal(num: float) -> float:
    """
    Calculate reciprocal (1/x) of a number.

    Args:
        num: Number to find reciprocal of

    Returns:
        float: Reciprocal of the number (0 if dividing by zero)
    """
    if num == 0:
        return 0.0
    return 1.0 / num


def percentage(num: float, percent: float) -> float:
    """
    Calculate percentage of a number.

    Args:
        num: Base number
        percent: Percentage value

    Returns:
        float: Percentage of the number
    """
    return (num * percent) / 100.0


def get_pi() -> float:
    """
    Get the value of PI.

    Returns:
        float: Pi (3.14159...)
    """
    return math.pi


def get_e() -> float:
    """
    Get the value of Euler's number (e).

    Returns:
        float: Euler's number (2.71828...)
    """
    return math.e
