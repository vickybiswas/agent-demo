"""
Natural logarithm endpoint for calculator.

Provides /ln endpoint for computing natural logarithm with error handling.
"""

import math
from fastapi import APIRouter, HTTPException
from typing import Union

router = APIRouter()


@router.get("/ln")
async def ln_operation(num1: Union[int, float]) -> dict:
    """
    Compute natural logarithm of a number.

    Args:
        num1: Number to compute logarithm of (must be > 0).

    Returns:
        Dictionary with result field containing natural log value.

    Raises:
        HTTPException: If num1 is zero or negative.
    """
    if num1 <= 0:
        raise HTTPException(
            status_code=400,
            detail="Natural logarithm of zero or negative number is not allowed"
        )
    result = math.log(num1)
    return {"result": result}
