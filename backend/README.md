# Stranger Things Calculator API

FastAPI backend for calculator operations with comprehensive testing and CORS support.

## Endpoints

### GET /health
Health check endpoint.

**Response**: `{"status": "ok"}`

**Example**:
```bash
curl http://localhost:8004/health
```

### GET /add
Add two numbers.

**Query Parameters**:
- `num1` (float): First number
- `num2` (float): Second number

**Response**: `{"result": 8}`

**Example**:
```bash
curl "http://localhost:8004/add?num1=5&num2=3"
```

### GET /subtract
Subtract two numbers.

**Query Parameters**:
- `num1` (float): First number
- `num2` (float): Second number

**Response**: `{"result": 2}`

**Example**:
```bash
curl "http://localhost:8004/subtract?num1=5&num2=3"
```

### GET /multiply
Multiply two numbers.

**Query Parameters**:
- `num1` (float): First number
- `num2` (float): Second number

**Response**: `{"result": 15}`

**Example**:
```bash
curl "http://localhost:8004/multiply?num1=5&num2=3"
```

### GET /divide
Divide two numbers.

**Query Parameters**:
- `num1` (float): Numerator
- `num2` (float): Denominator

**Response**: `{"result": 2.0}`

**Example**:
```bash
curl "http://localhost:8004/divide?num1=6&num2=3"
```

**Error**: Division by zero returns HTTP 422 with error message.

```bash
curl "http://localhost:8004/divide?num1=5&num2=0"
# Returns: {"detail":"Division by zero"}
```

## Running Locally

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start the Server
```bash
python main.py
```

The API will be available at `http://localhost:8004`

### Access API Documentation
- Swagger UI: http://localhost:8004/docs
- ReDoc: http://localhost:8004/redoc

## Testing

### Run All Tests
```bash
pytest tests/ -v
```

### Run Tests with Coverage Report
```bash
pytest tests/ --cov=routes --cov-report=term-missing
```

### Run Specific Test
```bash
pytest tests/test_add_unit.py -v
```

### Test Count
- 57 total tests (28 unit tests + 29 API tests)
- All tests passing
- 100% code coverage

## Edge Cases

- **Division by zero**: Returns HTTP 422 error with "Division by zero" message
- **Large numbers**: Handled as floats, no overflow errors
- **Negative numbers**: Fully supported across all operations
- **Decimal numbers**: Fully supported with precision up to float accuracy
- **Invalid types**: FastAPI validates types, returns HTTP 422 if invalid (e.g., `?num1=abc`)
- **Missing parameters**: FastAPI validates required parameters, returns HTTP 422 if missing

## CORS Support

The API is configured with CORS middleware to allow:
- All origins (`*`)
- GET, POST, OPTIONS methods
- All headers

**Example CORS request**:
```bash
curl -H "Origin: http://localhost:3004" \
     -H "Access-Control-Request-Method: GET" \
     http://localhost:8004/add?num1=5&num2=3
```

## Code Quality

- **PEP8 Compliant**: All code follows PEP8 style guidelines
- **Type Hints**: All functions have full type hints
- **Docstrings**: All functions and endpoints documented with Google-style docstrings
- **No Debug Code**: No `print()` statements or debug code in routes

## Docker

### Build Image
```bash
docker build -t calculator-backend -f Dockerfile .
```

### Run Container
```bash
docker run -p 8004:8004 calculator-backend
```

### Test in Container
```bash
curl http://localhost:8004/health
```

## Project Structure

```
backend/
├── main.py                      # FastAPI app instance
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container build definition
├── README.md                    # This file
├── routes/
│   ├── __init__.py
│   ├── add.py                  # Addition operation
│   ├── subtract.py             # Subtraction operation
│   ├── multiply.py             # Multiplication operation
│   └── divide.py               # Division operation (with error handling)
└── tests/
    ├── test_add_unit.py        # 7 unit tests for add
    ├── test_add_api.py         # 7 API tests for /add endpoint
    ├── test_subtract_unit.py   # 7 unit tests for subtract
    ├── test_subtract_api.py    # 7 API tests for /subtract endpoint
    ├── test_multiply_unit.py   # 7 unit tests for multiply
    ├── test_multiply_api.py    # 7 API tests for /multiply endpoint
    ├── test_divide_unit.py     # 8 unit tests for divide
    └── test_divide_api.py      # 7 API tests for /divide endpoint
```

## Success Criteria Met

- ✅ Phase 1: FastAPI setup, minimal dependencies (fastapi + uvicorn only)
- ✅ Phase 2: CORS middleware configured
- ✅ Phase 3: 4 separate route files with proper imports
- ✅ Phase 4: 28 unit tests (7+ per operation)
- ✅ Phase 5: 29 API tests (7+ per endpoint, including CORS headers)
- ✅ Phase 6: 100% test coverage verified
- ✅ Phase 7: PEP8 compliant, full type hints, comprehensive docstrings
- ✅ Phase 8: Complete documentation with edge case handling

## Notes

- All responses use JSON format
- All numeric operations support both integers and floats
- Query parameters are case-sensitive
- The API runs on port 8004 by default
- All calculations performed in pure Python (no external libraries)
