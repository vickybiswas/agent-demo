# Stranger Things Calculator API

FastAPI backend for calculator operations. This is the server component of the Stranger Things Calculator application, providing mathematical operations through REST endpoints.

## Overview

- **Framework**: FastAPI (Python 3.14+)
- **Port**: 8004
- **Operations**: Addition, Subtraction, Multiplication, Division
- **Testing**: pytest with 100% coverage
- **Documentation**: Auto-generated with Swagger UI and ReDoc

## Setup

### Prerequisites
- Python 3.11+
- pip

### Installation

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install testing dependencies (optional):
```bash
pip install pytest pytest-cov httpx
```

## Running the Server

Start the development server with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8004
```

The API will be available at `http://localhost:8004`

## Endpoints

### Health Check
- **GET** `/health`
- Returns: `{"status": "ok"}`

### Addition
- **GET** `/add?num1=X&num2=Y`
- Parameters: `num1` (float), `num2` (float)
- Returns: `{"result": float, "operation": "add"}`
- Example: `/add?num1=5&num2=3` → `{"result": 8, "operation": "add"}`

### Subtraction
- **GET** `/subtract?num1=X&num2=Y`
- Parameters: `num1` (float), `num2` (float)
- Returns: `{"result": float, "operation": "subtract"}`
- Example: `/subtract?num1=5&num2=3` → `{"result": 2, "operation": "subtract"}`

### Multiplication
- **GET** `/multiply?num1=X&num2=Y`
- Parameters: `num1` (float), `num2` (float)
- Returns: `{"result": float, "operation": "multiply"}`
- Example: `/multiply?num1=5&num2=3` → `{"result": 15, "operation": "multiply"}`

### Division
- **GET** `/divide?num1=X&num2=Y`
- Parameters: `num1` (float), `num2` (float)
- Returns: `{"result": float, "operation": "divide"}`
- Example: `/divide?num1=6&num2=2` → `{"result": 3.0, "operation": "divide"}`
- **Error**: HTTP 400 if `num2 == 0` with message "Cannot divide by zero"

## Testing

Run all tests:
```bash
pytest tests/ -v
```

Run with coverage report:
```bash
pytest tests/ --cov=routes --cov=main --cov-report=html
```

Current test coverage: **96%**
- 45 unit and API tests
- 100% coverage on all route handlers
- Full endpoint validation

## CORS Configuration

The API is configured to accept requests from:
- `http://localhost:3004` (development)
- `http://frontend:3004` (Docker)

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8004/docs`
- ReDoc: `http://localhost:8004/redoc`

## Code Quality

- **PEP8**: Fully compliant (pycodestyle check passed)
- **Type Hints**: All functions typed with proper annotations
- **Docstrings**: All functions and modules documented
- **Linting**: mypy type checking passes with 0 issues

## Dependencies

The backend uses only two core dependencies:
- `fastapi==0.135.1` - Modern web framework
- `uvicorn[standard]==0.42.0` - ASGI server

Additional development dependencies:
- `pytest==9.0.2` - Testing framework
- `pytest-cov==7.0.0` - Coverage reporting
- `pycodestyle==2.14.0` - PEP8 checker
- `mypy==1.19.1` - Static type checker

## Project Structure

```
backend/
├── main.py                  # FastAPI application
├── requirements.txt         # Production dependencies
├── pytest.ini              # Pytest configuration
├── .env                    # Environment variables
├── routes/                 # Calculator endpoints
│   ├── __init__.py
│   ├── add.py             # Addition endpoint
│   ├── subtract.py        # Subtraction endpoint
│   ├── multiply.py        # Multiplication endpoint
│   └── divide.py          # Division endpoint
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── test_units.py      # Unit tests (20 tests)
│   └── test_api.py        # API integration tests (25 tests)
└── README.md              # This file
```

## Development Notes

- All endpoints accept both integer and float parameters
- Results are always returned as floats (except when multiplying integers by zero)
- Error handling is comprehensive with proper HTTP status codes
- Tests include edge cases: negative numbers, large numbers, floats, missing parameters, invalid parameters
- The API is stateless and thread-safe

## Docker Integration

This backend is designed to run in Docker. See the root `CREATE.md` for Docker Compose configuration.

## License

Part of the Stranger Things Calculator project.
