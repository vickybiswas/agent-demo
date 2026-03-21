"""Absolute value operation route."""

from fastapi import APIRouter

router = APIRouter()


def abs_number(num: float) -> float:
    """Calculate absolute value of a number.

    Args:
        num: Number to calculate absolute value for

    Returns:
        Absolute value of num
    """
    return abs(num)


@router.get("/abs", tags=["Scientific"])
async def abs_op(num: float) -> dict[str, float]:
    """Calculate absolute value of a number.

    Args:
        num: Number to calculate absolute value for (query param)

    Returns:
        JSON object with result key
    """
    result = abs_number(num)
    return {"result": result}
