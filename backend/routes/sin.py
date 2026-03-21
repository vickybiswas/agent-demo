"""
Sine endpoint for calculator.

Provides /sin endpoint for computing sine (input in radians).
"""

import math
from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/sin")
async def sin_operation(num1: Union[int, float]) -> dict:
    """
    Compute sine of a number (in radians).

    Args:
        num1: Angle in radians.

    Returns:
        Dictionary with result field containing sine value.
    """
    result = math.sin(num1)
    return {"result": result}
