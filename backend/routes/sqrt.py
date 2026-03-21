"""Square root operation route."""

import math
from fastapi import APIRouter, HTTPException

router = APIRouter()


def sqrt_number(num: float) -> float:
    """Calculate square root of a number.

    Args:
        num: Number to calculate square root for

    Returns:
        Square root of num

    Raises:
        ValueError: If num is negative
    """
    if num < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(num)


@router.get("/sqrt", tags=["Scientific"])
async def sqrt(num: float) -> dict[str, float]:
    """Calculate square root of a number.

    Args:
        num: Number to calculate square root for (query param)

    Returns:
        JSON object with result key

    Raises:
        HTTPException 422: If num is negative
    """
    try:
        result = sqrt_number(num)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
