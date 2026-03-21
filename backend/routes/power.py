"""
Power endpoint for calculator.

Provides /power endpoint for exponentiation.
"""

from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/power")
async def power_operation(
    num1: Union[int, float], num2: Union[int, float]
) -> dict:
    """
    Raise a number to a power.

    Args:
        num1: Base number.
        num2: Exponent.

    Returns:
        Dictionary with result field containing num1^num2.
    """
    result = num1 ** num2
    return {"result": result}
