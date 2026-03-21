"""Addition operation route."""

from fastapi import APIRouter

router = APIRouter()


def add_numbers(num1: float, num2: float) -> float:
    """Add two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        Sum of num1 and num2
    """
    return num1 + num2


@router.get("/add", tags=["Operations"])
async def add(num1: float, num2: float) -> dict[str, float]:
    """Add two numbers.

    Args:
        num1: First number (query param)
        num2: Second number (query param)

    Returns:
        JSON object with result key
    """
    result = add_numbers(num1, num2)
    return {"result": result}
