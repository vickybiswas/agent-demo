"""Multiplication operation route."""

from fastapi import APIRouter

router = APIRouter()


def multiply_numbers(num1: float, num2: float) -> float:
    """Multiply two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        Product of num1 and num2
    """
    return num1 * num2


@router.get("/multiply", tags=["Operations"])
async def multiply(num1: float, num2: float) -> dict[str, float]:
    """Multiply two numbers.

    Args:
        num1: First number (query param)
        num2: Second number (query param)

    Returns:
        JSON object with result key
    """
    result = multiply_numbers(num1, num2)
    return {"result": result}
