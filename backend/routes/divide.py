"""Division operation route."""

from fastapi import APIRouter, HTTPException

router = APIRouter()


def divide_numbers(num1: float, num2: float) -> float:
    """Divide two numbers.

    Args:
        num1: Numerator
        num2: Denominator

    Returns:
        num1 / num2

    Raises:
        ValueError: If num2 is zero
    """
    if num2 == 0:
        raise ValueError("Division by zero")
    return num1 / num2


@router.get("/divide", tags=["Operations"])
async def divide(num1: float, num2: float) -> dict[str, float]:
    """Divide two numbers.

    Args:
        num1: Numerator (query param)
        num2: Denominator (query param)

    Returns:
        JSON object with result key

    Raises:
        HTTPException: 422 error if num2 is zero
    """
    try:
        result = divide_numbers(num1, num2)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
