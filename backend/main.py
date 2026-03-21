"""FastAPI application for Stranger Things Calculator API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import (
    add, subtract, multiply, divide,
    sin, cos, tan, sqrt, ln, log, power, factorial, abs, modulo
)

app = FastAPI(
    title="Stranger Things Calculator",
    description="A retro-themed calculator API",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        JSON object with status key
    """
    return {"status": "ok"}


# Include route modules
app.include_router(add.router)
app.include_router(subtract.router)
app.include_router(multiply.router)
app.include_router(divide.router)

# Scientific operations
app.include_router(sin.router)
app.include_router(cos.router)
app.include_router(tan.router)
app.include_router(sqrt.router)
app.include_router(ln.router)
app.include_router(log.router)
app.include_router(power.router)
app.include_router(factorial.router)
app.include_router(abs.router)
app.include_router(modulo.router)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    """Root endpoint.

    Returns:
        JSON object with message key
    """
    return {"message": "Stranger Things Calculator API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004, reload=True)
