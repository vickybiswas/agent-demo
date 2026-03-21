"""Tangent operation route."""

import math
from fastapi import APIRouter

router = APIRouter()


def tan_number(num: float, degrees: bool = False) -> float:
    """Calculate tangent of a number.

    Args:
        num: Number to calculate tangent for
        degrees: If True, num is in degrees; if False, in radians

    Returns:
        Tangent of num
    """
    if degrees:
        num = math.radians(num)
    return math.tan(num)


@router.get("/tan", tags=["Scientific"])
async def tan(num: float, degrees: bool = False) -> dict[str, float]:
    """Calculate tangent of a number.

    Args:
        num: Number to calculate tangent for (query param)
        degrees: If True, num is in degrees; if False, in radians (default: False)

    Returns:
        JSON object with result key
    """
    result = tan_number(num, degrees)
    return {"result": result}
