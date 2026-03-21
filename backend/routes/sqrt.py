"""
Square root endpoint for calculator.

Provides /sqrt endpoint for computing square root with error handling.
"""

import math
from fastapi import APIRouter, HTTPException
from typing import Union

router = APIRouter()


@router.get("/sqrt")
async def sqrt_operation(num1: Union[int, float]) -> dict:
    """
    Compute square root of a number.

    Args:
        num1: Number to compute square root of.

    Returns:
        Dictionary with result field containing square root.

    Raises:
        HTTPException: If num1 is negative (square root of negative number).
    """
    if num1 < 0:
        raise HTTPException(
            status_code=400,
            detail="Square root of negative number is not allowed"
        )
    result = math.sqrt(num1)
    return {"result": result}
