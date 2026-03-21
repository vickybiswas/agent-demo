"""
Addition endpoint for calculator.

Provides /add endpoint for adding two numbers.
"""

from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/add")
async def add_operation(
    num1: Union[int, float], num2: Union[int, float]
) -> dict:
    """
    Add two numbers.

    Args:
        num1: First number.
        num2: Second number.

    Returns:
        Dictionary with result field containing sum.
    """
    result = num1 + num2
    return {"result": result}
