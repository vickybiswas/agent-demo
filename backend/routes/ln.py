"""Natural logarithm operation route."""

import math
from fastapi import APIRouter, HTTPException

router = APIRouter()


def ln_number(num: float) -> float:
    """Calculate natural logarithm of a number.

    Args:
        num: Number to calculate natural logarithm for

    Returns:
        Natural logarithm of num

    Raises:
        ValueError: If num is zero or negative
    """
    if num <= 0:
        raise ValueError("Cannot take logarithm of zero or negative number")
    return math.log(num)


@router.get("/ln", tags=["Scientific"])
async def ln(num: float) -> dict[str, float]:
    """Calculate natural logarithm of a number.

    Args:
        num: Number to calculate natural logarithm for (query param)

    Returns:
        JSON object with result key

    Raises:
        HTTPException 422: If num is zero or negative
    """
    try:
        result = ln_number(num)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
