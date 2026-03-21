"""Modulo operation route."""

from fastapi import APIRouter, HTTPException

router = APIRouter()


def modulo_numbers(num1: float, num2: float) -> float:
    """Calculate remainder of num1 divided by num2.

    Args:
        num1: Dividend
        num2: Divisor

    Returns:
        num1 % num2

    Raises:
        ValueError: If num2 is zero
    """
    if num2 == 0:
        raise ValueError("Division by zero")
    return num1 % num2


@router.get("/modulo", tags=["Operations"])
async def modulo(num1: float, num2: float) -> dict[str, float]:
    """Calculate remainder of num1 divided by num2.

    Args:
        num1: Dividend (query param)
        num2: Divisor (query param)

    Returns:
        JSON object with result key

    Raises:
        HTTPException 422: If num2 is zero
    """
    try:
        result = modulo_numbers(num1, num2)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
