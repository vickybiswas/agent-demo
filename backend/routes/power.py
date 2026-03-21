"""Power operation route."""

from fastapi import APIRouter

router = APIRouter()


def power_numbers(base: float, exponent: float) -> float:
    """Raise base to the power of exponent.

    Args:
        base: Base number
        exponent: Exponent

    Returns:
        base raised to the power of exponent
    """
    return base ** exponent


@router.get("/power", tags=["Operations"])
async def power(base: float, exponent: float) -> dict[str, float]:
    """Raise base to the power of exponent.

    Args:
        base: Base number (query param)
        exponent: Exponent (query param)

    Returns:
        JSON object with result key
    """
    result = power_numbers(base, exponent)
    return {"result": result}
