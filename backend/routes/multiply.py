"""Multiplication route handler."""
from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/multiply")
async def multiply_numbers(num1: Union[int, float], num2: Union[int, float]) -> dict:
    """
    Multiply two numbers.

    Args:
        num1: First number (int or float)
        num2: Second number (int or float)

    Returns:
        Dictionary containing the result and operation name
    """
    result: Union[int, float] = num1 * num2
    return {"result": result, "operation": "multiply"}
