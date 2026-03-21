"""
Factorial endpoint for calculator.

Provides /factorial endpoint for computing factorial with error handling.
"""

import math
from fastapi import APIRouter, HTTPException
from typing import Union

router = APIRouter()


@router.get("/factorial")
async def factorial_operation(num1: Union[int, float]) -> dict:
    """
    Compute factorial of a number.

    Args:
        num1: Number to compute factorial of (must be non-negative integer).

    Returns:
        Dictionary with result field containing factorial value.

    Raises:
        HTTPException: If num1 is negative, float, or not an integer.
    """
    if not isinstance(num1, int) or isinstance(num1, bool):
        # Check if it's a float that equals an integer
        if isinstance(num1, float):
            if num1 != int(num1):
                raise HTTPException(
                    status_code=400,
                    detail="Factorial is only defined for non-negative integers"
                )
            num1 = int(num1)
        else:
            raise HTTPException(
                status_code=400,
                detail="Factorial is only defined for non-negative integers"
            )

    if num1 < 0:
        raise HTTPException(
            status_code=400,
            detail="Factorial of negative number is not allowed"
        )

    result = math.factorial(num1)
    return {"result": result}
