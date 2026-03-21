"""Logarithm base 10 operation route."""

import math
from fastapi import APIRouter, HTTPException

router = APIRouter()


def log_number(num: float) -> float:
    """Calculate logarithm base 10 of a number.

    Args:
        num: Number to calculate logarithm for

    Returns:
        Logarithm base 10 of num

    Raises:
        ValueError: If num is zero or negative
    """
    if num <= 0:
        raise ValueError("Cannot take logarithm of zero or negative number")
    return math.log10(num)


@router.get("/log", tags=["Scientific"])
async def log(num: float) -> dict[str, float]:
    """Calculate logarithm base 10 of a number.

    Args:
        num: Number to calculate logarithm for (query param)

    Returns:
        JSON object with result key

    Raises:
        HTTPException 422: If num is zero or negative
    """
    try:
        result = log_number(num)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
