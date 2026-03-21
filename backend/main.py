"""Stranger Things Calculator API - Main Application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import add, subtract, multiply, divide

app = FastAPI(
    title="Stranger Things Calculator",
    description="A simple calculator API for the Stranger Things theme",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3004", "http://frontend:3004"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health() -> dict:
    """
    Health check endpoint for Docker container.

    Returns:
        dict: Status response with ok status.
    """
    return {"status": "ok"}


# Include route handlers
app.include_router(add.router)
app.include_router(subtract.router)
app.include_router(multiply.router)
app.include_router(divide.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
