"""
Subtraction endpoint for calculator.

Provides /subtract endpoint for subtracting two numbers.
"""

from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/subtract")
async def subtract_operation(
    num1: Union[int, float], num2: Union[int, float]
) -> dict:
    """
    Subtract two numbers.

    Args:
        num1: First number (minuend).
        num2: Second number (subtrahend).

    Returns:
        Dictionary with result field containing difference.
    """
    result = num1 - num2
    return {"result": result}
