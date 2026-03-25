"""
Division operation module.
"""


def divide_numbers(num1: float, num2: float) -> float:
    """
    Divide two numbers.

    Args:
        num1: Dividend
        num2: Divisor

    Returns:
        float: Quotient (returns 0 if dividing by zero)
    """
    if num2 == 0:
        return 0.0
    return num1 / num2
