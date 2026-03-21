"""Subtraction operation route."""

from fastapi import APIRouter

router = APIRouter()


def subtract_numbers(num1: float, num2: float) -> float:
    """Subtract two numbers.

    Args:
        num1: First number (minuend)
        num2: Second number (subtrahend)

    Returns:
        Difference of num1 and num2
    """
    return num1 - num2


@router.get("/subtract", tags=["Operations"])
async def subtract(num1: float, num2: float) -> dict[str, float]:
    """Subtract two numbers.

    Args:
        num1: First number (query param)
        num2: Second number (query param)

    Returns:
        JSON object with result key
    """
    result = subtract_numbers(num1, num2)
    return {"result": result}
