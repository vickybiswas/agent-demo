# API Endpoints Reference

Complete reference for all calculator API endpoints.

## Health Check

```
GET /health
```

### Response
- **Status**: 200 OK
- **Body**: `{"status": "ok"}`

### Use Case
Container health check for Docker deployments.

---

## Addition

```
GET /add?num1=<number>&num2=<number>
```

### Parameters
- `num1` (required): First number (int or float)
- `num2` (required): Second number (int or float)

### Response (Success)
- **Status**: 200 OK
- **Body**: `{"result": <float>, "operation": "add"}`

### Response (Error)
- **Missing parameter**: 422 Unprocessable Entity
- **Invalid parameter**: 422 Unprocessable Entity

### Examples

```bash
# Positive integers
curl "http://localhost:8004/add?num1=5&num2=3"
# Response: {"result": 8, "operation": "add"}

# Floats
curl "http://localhost:8004/add?num1=5.5&num2=3.2"
# Response: {"result": 8.7, "operation": "add"}

# Negative numbers
curl "http://localhost:8004/add?num1=-5&num2=3"
# Response: {"result": -2, "operation": "add"}
```

---

## Subtraction

```
GET /subtract?num1=<number>&num2=<number>
```

### Parameters
- `num1` (required): First number (int or float)
- `num2` (required): Second number (int or float)

### Response (Success)
- **Status**: 200 OK
- **Body**: `{"result": <float>, "operation": "subtract"}`

### Response (Error)
- **Missing parameter**: 422 Unprocessable Entity
- **Invalid parameter**: 422 Unprocessable Entity

### Examples

```bash
# Basic subtraction
curl "http://localhost:8004/subtract?num1=5&num2=3"
# Response: {"result": 2, "operation": "subtract"}

# Subtraction with negative numbers
curl "http://localhost:8004/subtract?num1=5&num2=-3"
# Response: {"result": 8, "operation": "subtract"}

# Float subtraction
curl "http://localhost:8004/subtract?num1=5.5&num2=3.2"
# Response: {"result": 2.3, "operation": "subtract"}
```

---

## Multiplication

```
GET /multiply?num1=<number>&num2=<number>
```

### Parameters
- `num1` (required): First number (int or float)
- `num2` (required): Second number (int or float)

### Response (Success)
- **Status**: 200 OK
- **Body**: `{"result": <float>, "operation": "multiply"}`

### Response (Error)
- **Missing parameter**: 422 Unprocessable Entity
- **Invalid parameter**: 422 Unprocessable Entity

### Examples

```bash
# Basic multiplication
curl "http://localhost:8004/multiply?num1=5&num2=3"
# Response: {"result": 15, "operation": "multiply"}

# Multiplication by zero
curl "http://localhost:8004/multiply?num1=5&num2=0"
# Response: {"result": 0, "operation": "multiply"}

# Float multiplication
curl "http://localhost:8004/multiply?num1=2.5&num2=4"
# Response: {"result": 10.0, "operation": "multiply"}
```

---

## Division

```
GET /divide?num1=<number>&num2=<number>
```

### Parameters
- `num1` (required): Dividend (int or float)
- `num2` (required): Divisor (int or float)

### Response (Success)
- **Status**: 200 OK
- **Body**: `{"result": <float>, "operation": "divide"}`

### Response (Error - Division by Zero)
- **Status**: 400 Bad Request
- **Body**: `{"detail": "Cannot divide by zero"}`

### Response (Error - Missing/Invalid Parameter)
- **Status**: 422 Unprocessable Entity

### Examples

```bash
# Basic division
curl "http://localhost:8004/divide?num1=6&num2=2"
# Response: {"result": 3.0, "operation": "divide"}

# Division with remainder
curl "http://localhost:8004/divide?num1=7&num2=2"
# Response: {"result": 3.5, "operation": "divide"}

# Division by zero (error)
curl "http://localhost:8004/divide?num1=6&num2=0"
# Response: {"detail": "Cannot divide by zero"}
# Status: 400 Bad Request

# Float division
curl "http://localhost:8004/divide?num1=7.5&num2=2.5"
# Response: {"result": 3.0, "operation": "divide"}
```

---

## Response Schema

All successful responses follow this schema:

```json
{
  "result": <number>,
  "operation": <string>
}
```

### Fields
- `result`: The numeric result of the operation (float)
- `operation`: The name of the operation performed ("add", "subtract", "multiply", or "divide")

---

## Error Responses

### 400 Bad Request
Returned when attempting invalid operations:
```json
{
  "detail": "Cannot divide by zero"
}
```

### 422 Unprocessable Entity
Returned when parameters are missing or invalid:
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["query", "num2"],
      "msg": "Field required"
    }
  ]
}
```

---

## Request/Response Examples

### Using Python
```python
import requests

# Addition
response = requests.get("http://localhost:8004/add", params={"num1": 5, "num2": 3})
print(response.json())  # {"result": 8, "operation": "add"}

# Division with error handling
response = requests.get("http://localhost:8004/divide", params={"num1": 6, "num2": 0})
if response.status_code == 400:
    print(response.json())  # {"detail": "Cannot divide by zero"}
```

### Using JavaScript
```javascript
// Addition
fetch('http://localhost:8004/add?num1=5&num2=3')
  .then(res => res.json())
  .then(data => console.log(data)); // {result: 8, operation: "add"}

// Division
fetch('http://localhost:8004/divide?num1=6&num2=0')
  .then(res => res.json())
  .then(data => console.log(data)); // {detail: "Cannot divide by zero"}
```

---

## CORS Headers

All endpoints support the following CORS origins:
- `http://localhost:3004`
- `http://frontend:3004`

Credentials, all HTTP methods, and all headers are allowed.

---

## Rate Limiting

No rate limiting is currently implemented. Each endpoint can be called as frequently as needed.

---

## Versioning

Current API version: **1.0.0**

Future versions will maintain backward compatibility with existing endpoints.
