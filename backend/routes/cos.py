"""
Cosine endpoint for calculator.

Provides /cos endpoint for computing cosine (input in radians).
"""

import math
from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/cos")
async def cos_operation(num1: Union[int, float]) -> dict:
    """
    Compute cosine of a number (in radians).

    Args:
        num1: Angle in radians.

    Returns:
        Dictionary with result field containing cosine value.
    """
    result = math.cos(num1)
    return {"result": result}
