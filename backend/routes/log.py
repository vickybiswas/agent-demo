"""
Base-10 logarithm endpoint for calculator.

Provides /log endpoint for computing logarithm base 10 with error handling.
"""

import math
from fastapi import APIRouter, HTTPException
from typing import Union

router = APIRouter()


@router.get("/log")
async def log_operation(num1: Union[int, float]) -> dict:
    """
    Compute base-10 logarithm of a number.

    Args:
        num1: Number to compute logarithm of (must be > 0).

    Returns:
        Dictionary with result field containing log10 value.

    Raises:
        HTTPException: If num1 is zero or negative.
    """
    if num1 <= 0:
        raise HTTPException(
            status_code=400,
            detail="Logarithm of zero or negative number is not allowed"
        )
    result = math.log10(num1)
    return {"result": result}
