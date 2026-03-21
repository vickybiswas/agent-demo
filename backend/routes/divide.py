"""Division route handler."""
from fastapi import APIRouter, HTTPException
from typing import Union

router = APIRouter()


@router.get("/divide")
async def divide_numbers(num1: Union[int, float], num2: Union[int, float]) -> dict:
    """
    Divide two numbers.

    Args:
        num1: Dividend (int or float)
        num2: Divisor (int or float)

    Returns:
        Dictionary containing the result and operation name

    Raises:
        HTTPException: If attempting to divide by zero (HTTP 400)
    """
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result: float = num1 / num2
    return {"result": result, "operation": "divide"}
