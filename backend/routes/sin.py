"""Sine operation route."""

import math
from fastapi import APIRouter

router = APIRouter()


def sin_number(num: float, degrees: bool = False) -> float:
    """Calculate sine of a number.

    Args:
        num: Number to calculate sine for
        degrees: If True, num is in degrees; if False, in radians

    Returns:
        Sine of num
    """
    if degrees:
        num = math.radians(num)
    return math.sin(num)


@router.get("/sin", tags=["Scientific"])
async def sin(num: float, degrees: bool = False) -> dict[str, float]:
    """Calculate sine of a number.

    Args:
        num: Number to calculate sine for (query param)
        degrees: If True, num is in degrees; if False, in radians (default: False)

    Returns:
        JSON object with result key
    """
    result = sin_number(num, degrees)
    return {"result": result}
