# Stranger Things Calculator Backend

FastAPI-based calculator service with CORS support and comprehensive test coverage.

## Setup

### Prerequisites
- Python 3.11+ (tested with Python 3.14)
- pip package manager

### Installation

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Set the following environment variables:

```bash
# CORS_ORIGINS: Comma-separated list of allowed origins
CORS_ORIGINS=http://localhost:3004,http://frontend:3004
```

Default: `http://localhost:3004,http://frontend:3004`

## Running the Server

### Development Mode

```bash
python3 main.py
```

Or with hot-reload:

```bash
uvicorn main:app --reload --port 8004
```

**Expected Output**:
```
Uvicorn running on http://0.0.0.0:8004
```

### Health Check

```bash
curl http://localhost:8004/health
# Response: {"status":"ok"}
```

## API Endpoints

### Addition: /add

Add two numbers.

**Endpoint**: `GET /add`

**Query Parameters**:
- `num1` (number): First number
- `num2` (number): Second number

**Response** (200 OK):
```json
{"result": 8}
```

**Example**:
```bash
curl "http://localhost:8004/add?num1=5&num2=3"
```

### Subtraction: /subtract

Subtract two numbers.

**Endpoint**: `GET /subtract`

**Query Parameters**:
- `num1` (number): Minuend
- `num2` (number): Subtrahend

**Response** (200 OK):
```json
{"result": 2}
```

**Example**:
```bash
curl "http://localhost:8004/subtract?num1=5&num2=3"
```

### Multiplication: /multiply

Multiply two numbers.

**Endpoint**: `GET /multiply`

**Query Parameters**:
- `num1` (number): Multiplicand
- `num2` (number): Multiplier

**Response** (200 OK):
```json
{"result": 15}
```

**Example**:
```bash
curl "http://localhost:8004/multiply?num1=5&num2=3"
```

### Division: /divide

Divide two numbers.

**Endpoint**: `GET /divide`

**Query Parameters**:
- `num1` (number): Dividend
- `num2` (number): Divisor

**Response** (200 OK):
```json
{"result": 1.6666}
```

**Error** (400 Bad Request - Division by Zero):
```json
{"detail": "Division by zero is not allowed"}
```

**Example**:
```bash
curl "http://localhost:8004/divide?num1=5&num2=3"
curl "http://localhost:8004/divide?num1=5&num2=0"  # Error
```

## HTTP Status Codes

- **200 OK**: Successful calculation
- **400 Bad Request**: Invalid request (e.g., division by zero)
- **422 Unprocessable Entity**: Invalid parameter type (e.g., `?num1=abc`)
- **500 Internal Server Error**: Unexpected server error

## Testing

### Run All Tests

```bash
pytest tests/ -v
```

### Run Unit Tests Only

```bash
pytest tests/test_*_unit.py -v
```

### Run API Tests Only

```bash
pytest tests/test_*_api.py -v
```

### Run with Coverage Report

```bash
pytest tests/ -v --cov=routes --cov=main --cov-report=term-missing
```

### Expected Test Results

- **Total Tests**: 64
- **Unit Tests**: 32 (8 per operation)
- **API Tests**: 32 (8 per endpoint)
- **Coverage**: 100% on production code (routes/*, main.py health endpoint)

**Example Output**:
```
tests/test_add_unit.py::TestAdd::test_add_positive_integers PASSED
tests/test_add_api.py::TestAddAPI::test_add_api_positive PASSED
...
======================= 64 passed in 1.23s ========================

Name                  Stmts   Miss  Cover
routes/add.py             7      0   100%
routes/subtract.py        7      0   100%
routes/multiply.py        7      0   100%
routes/divide.py          9      0   100%
main.py                  17      3    82%  (82% due to __main__ block)
TOTAL                    47      3    94%
```

## Code Quality

### PEP8 Compliance

```bash
flake8 main.py routes/ --max-line-length=100
```

Result: No issues found

### Type Hints

All functions have type hints:

```python
def add_operation(num1: Union[int, float], num2: Union[int, float]) -> dict:
    """Add two numbers."""
    return {"result": num1 + num2}
```

### Docstrings

All functions have Google-style docstrings:

```python
def add_operation(num1: Union[int, float], num2: Union[int, float]) -> dict:
    """
    Add two numbers.

    Args:
        num1: First number.
        num2: Second number.

    Returns:
        Dictionary with result field containing sum.
    """
    return {"result": num1 + num2}
```

## Project Structure

```
backend/
├── main.py                 # FastAPI app, CORS middleware, health endpoint
├── routes/
│   ├── __init__.py
│   ├── add.py             # /add endpoint
│   ├── subtract.py        # /subtract endpoint
│   ├── multiply.py        # /multiply endpoint
│   └── divide.py          # /divide endpoint (with error handling)
├── tests/
│   ├── test_add_unit.py   # 8 unit tests for addition
│   ├── test_add_api.py    # 8 API tests for /add endpoint
│   ├── test_subtract_unit.py
│   ├── test_subtract_api.py
│   ├── test_multiply_unit.py
│   ├── test_multiply_api.py
│   ├── test_divide_unit.py
│   ├── test_divide_api.py
│   └── test_regression.py # Regression test suite
├── requirements.txt       # FastAPI, uvicorn, httpx, pytest
├── .gitignore            # Python, venv, __pycache__
└── README.md             # This file
```

## CORS Configuration

The backend includes CORS middleware to allow frontend communication.

### Allowed Origins

By default:
- `http://localhost:3004` (local development)
- `http://frontend:3004` (Docker service)

### Customization

Set the `CORS_ORIGINS` environment variable:

```bash
export CORS_ORIGINS="http://localhost:3004,http://frontend:3004,https://example.com"
python3 main.py
```

### Verify CORS Headers

```bash
curl -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3 -v
```

Expected headers in response:
```
Access-Control-Allow-Origin: http://localhost:3004
Access-Control-Allow-Credentials: true
```

## Docker

### Build

```bash
docker build -t calculator-backend:latest .
```

### Run

```bash
docker run -p 8004:8004 -e CORS_ORIGINS="http://localhost:3004" calculator-backend:latest
```

### Docker Compose

See `docker-compose.yaml` in the root directory.

```bash
docker compose up backend
```

## Troubleshooting

### ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'fastapi'`

**Solution**:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### CORS Issues

**Error**: Browser blocks requests with CORS error

**Solution**:
1. Verify `CORS_ORIGINS` environment variable:
   ```bash
   echo $CORS_ORIGINS
   ```
2. Ensure frontend origin is in the list
3. Check HTTP headers:
   ```bash
   curl -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3 -v
   ```

### Port Already in Use

**Error**: `Address already in use`

**Solution**:
```bash
# Kill process on port 8004
lsof -ti:8004 | xargs kill -9
# or use a different port
uvicorn main:app --port 8005
```

## Development Workflow

1. Make code changes
2. Run tests to verify: `pytest tests/ -v`
3. Check PEP8: `flake8 main.py routes/`
4. Check coverage: `pytest tests/ --cov=routes --cov=main`
5. Commit changes

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [CORS Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
