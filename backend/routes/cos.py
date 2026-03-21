"""Cosine operation route."""

import math
from fastapi import APIRouter

router = APIRouter()


def cos_number(num: float, degrees: bool = False) -> float:
    """Calculate cosine of a number.

    Args:
        num: Number to calculate cosine for
        degrees: If True, num is in degrees; if False, in radians

    Returns:
        Cosine of num
    """
    if degrees:
        num = math.radians(num)
    return math.cos(num)


@router.get("/cos", tags=["Scientific"])
async def cos(num: float, degrees: bool = False) -> dict[str, float]:
    """Calculate cosine of a number.

    Args:
        num: Number to calculate cosine for (query param)
        degrees: If True, num is in degrees; if False, in radians (default: False)

    Returns:
        JSON object with result key
    """
    result = cos_number(num, degrees)
    return {"result": result}
