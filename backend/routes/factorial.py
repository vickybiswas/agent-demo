"""Factorial operation route."""

import math
from fastapi import APIRouter, HTTPException

router = APIRouter()


def factorial_number(num: float) -> float:
    """Calculate factorial of a number.

    Args:
        num: Number to calculate factorial for

    Returns:
        Factorial of num

    Raises:
        ValueError: If num is negative or not an integer
    """
    if num < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if num != int(num):
        raise ValueError("Factorial only works with integers")
    return float(math.factorial(int(num)))


@router.get("/factorial", tags=["Scientific"])
async def factorial(num: float) -> dict[str, float]:
    """Calculate factorial of a number.

    Args:
        num: Number to calculate factorial for (query param)

    Returns:
        JSON object with result key

    Raises:
        HTTPException 422: If num is negative or not an integer
    """
    try:
        result = factorial_number(num)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
