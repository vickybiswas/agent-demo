"""
Stranger Things Calculator API
FastAPI backend with CORS support for add, subtract, multiply, divide operations.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from operations.add import add_numbers
from operations.subtract import subtract_numbers
from operations.multiply import multiply_numbers
from operations.divide import divide_numbers
from operations.scientific import (
    sqrt_number, power, sin_degrees, cos_degrees, tan_degrees,
    logarithm, factorial_number, reciprocal, percentage,
    get_pi, get_e
)

app = FastAPI(
    title="Stranger Things Calculator API",
    description="A themed calculator API with add, subtract, multiply, divide operations",
    version="1.0.0"
)

# Add CORS middleware - allows all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict:
    """
    Health check endpoint to verify API is running.

    Returns:
        dict: Status response
    """
    return {"status": "ok"}


@app.get("/add")
def add(num1: float, num2: float) -> dict:
    """
    Add two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        dict: Result of addition
    """
    result = add_numbers(num1, num2)
    return {"result": result}


@app.get("/subtract")
def subtract(num1: float, num2: float) -> dict:
    """
    Subtract two numbers.

    Args:
        num1: First number
        num2: Second number to subtract

    Returns:
        dict: Result of subtraction
    """
    result = subtract_numbers(num1, num2)
    return {"result": result}


@app.get("/multiply")
def multiply(num1: float, num2: float) -> dict:
    """
    Multiply two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        dict: Result of multiplication
    """
    result = multiply_numbers(num1, num2)
    return {"result": result}


@app.get("/divide")
def divide(num1: float, num2: float) -> dict:
    """
    Divide two numbers.

    Args:
        num1: Dividend
        num2: Divisor

    Returns:
        dict: Result of division (0 if dividing by zero)
    """
    result = divide_numbers(num1, num2)
    return {"result": result}


# Scientific Operations
@app.get("/sqrt")
def sqrt(num: float) -> dict:
    """Square root of a number."""
    result = sqrt_number(num)
    return {"result": result}


@app.get("/power")
def pow_endpoint(base: float, exp: float) -> dict:
    """Raise base to the power of exponent."""
    result = power(base, exp)
    return {"result": result}


@app.get("/sin")
def sin(angle: float) -> dict:
    """Sine of angle (in degrees)."""
    result = sin_degrees(angle)
    return {"result": result}


@app.get("/cos")
def cos(angle: float) -> dict:
    """Cosine of angle (in degrees)."""
    result = cos_degrees(angle)
    return {"result": result}


@app.get("/tan")
def tan(angle: float) -> dict:
    """Tangent of angle (in degrees)."""
    result = tan_degrees(angle)
    return {"result": result}


@app.get("/log")
def log(num: float, base: float = 10) -> dict:
    """Logarithm of a number with given base (default 10)."""
    result = logarithm(num, base)
    return {"result": result}


@app.get("/factorial")
def factorial(num: float) -> dict:
    """Factorial of a number."""
    result = factorial_number(num)
    return {"result": result}


@app.get("/reciprocal")
def recip(num: float) -> dict:
    """Reciprocal (1/x) of a number."""
    result = reciprocal(num)
    return {"result": result}


@app.get("/percentage")
def percent(num: float, percent_val: float) -> dict:
    """Calculate percentage of a number."""
    result = percentage(num, percent_val)
    return {"result": result}


@app.get("/pi")
def pi() -> dict:
    """Get the value of PI."""
    result = get_pi()
    return {"result": result}


@app.get("/e")
def euler() -> dict:
    """Get the value of Euler's number (e)."""
    result = get_e()
    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
