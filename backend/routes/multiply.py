"""
Multiplication endpoint for calculator.

Provides /multiply endpoint for multiplying two numbers.
"""

from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/multiply")
async def multiply_operation(
    num1: Union[int, float], num2: Union[int, float]
) -> dict:
    """
    Multiply two numbers.

    Args:
        num1: First number (multiplicand).
        num2: Second number (multiplier).

    Returns:
        Dictionary with result field containing product.
    """
    result = num1 * num2
    return {"result": result}
