"""
Tangent endpoint for calculator.

Provides /tan endpoint for computing tangent (input in radians).
"""

import math
from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/tan")
async def tan_operation(num1: Union[int, float]) -> dict:
    """
    Compute tangent of a number (in radians).

    Args:
        num1: Angle in radians.

    Returns:
        Dictionary with result field containing tangent value.
    """
    result = math.tan(num1)
    return {"result": result}
