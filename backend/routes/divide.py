"""
Division endpoint for calculator.

Provides /divide endpoint for dividing two numbers with error handling.
"""

from fastapi import APIRouter, HTTPException
from typing import Union

router = APIRouter()


@router.get("/divide")
async def divide_operation(
    num1: Union[int, float], num2: Union[int, float]
) -> dict:
    """
    Divide two numbers.

    Args:
        num1: First number (dividend).
        num2: Second number (divisor).

    Returns:
        Dictionary with result field containing quotient.

    Raises:
        HTTPException: If num2 is zero (division by zero).
    """
    if num2 == 0:
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed"
        )
    result = num1 / num2
    return {"result": result}
