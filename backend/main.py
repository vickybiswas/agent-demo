"""
Stranger Things Calculator Backend.

FastAPI application with CORS middleware and calculator endpoints.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from routes import add, subtract, multiply, divide, sqrt, power, sin, cos, tan, log, ln, factorial


app = FastAPI(
    title="Stranger Things Calculator",
    version="1.0.0",
    description="A spooky calculator with Demogorgon vibes"
)

# CORS Middleware Configuration
# Allow frontend origin (both local dev and Docker)
cors_origins = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:3004,http://frontend:3004"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check() -> dict:
    """
    Health check endpoint.

    Returns:
        Dictionary with status.
    """
    return {"status": "ok"}


# Import and include routers
app.include_router(add.router)
app.include_router(subtract.router)
app.include_router(multiply.router)
app.include_router(divide.router)
app.include_router(sqrt.router)
app.include_router(power.router)
app.include_router(sin.router)
app.include_router(cos.router)
app.include_router(tan.router)
app.include_router(log.router)
app.include_router(ln.router)
app.include_router(factorial.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
