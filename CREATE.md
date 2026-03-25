# Docker Orchestration Guide

## Overview
Complete Docker setup for running the Stranger Things Calculator with hot-reload support.

**Prerequisite**: Frontend and backend code complete (see CLAUDE.md Phase 1 & 2)

## Phase 1: Frontend Dockerfile

Create `frontend/Dockerfile`:

```dockerfile
# Use Node.js LTS on Alpine for small image size
FROM node:22-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Expose development server port
EXPOSE 3004

# Set environment for hot-reload
ENV NODE_ENV=development

# Start development server
CMD ["npm", "run", "dev"]
```

**Key Points**:
- Base image: `node:22-alpine` (fast, small)
- Port: 3004
- Hot-reload enabled via volume mount
- Development mode for debugging

## Phase 2: Backend Dockerfile

Create `backend/Dockerfile`:

```dockerfile
# Use Python slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose API port
EXPOSE 8004

# Set environment
ENV PYTHONUNBUFFERED=1

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004", "--reload"]
```

**Key Points**:
- Base image: `python:3.13-slim` (minimal)
- Port: 8004
- Hot-reload enabled with `--reload`
- Health check compatible

## Phase 3: Docker Compose Configuration

Create `compose.yaml`:

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    container_name: calculator-frontend
    ports:
      - "3004:3004"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8004
      - NODE_ENV=development
    depends_on:
      - backend
    networks:
      - calculator-network

  backend:
    build: ./backend
    container_name: calculator-backend
    ports:
      - "8004:8004"
    volumes:
      - ./backend:/app
    environment:
      - PYTHONUNBUFFERED=1
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8004/health"]
      interval: 10s
      timeout: 5s
      retries: 3
    networks:
      - calculator-network

networks:
  calculator-network:
    driver: bridge
```

**Key Points**:
- Both services on same network bridge
- Frontend port: 3004 (host:container)
- Backend port: 8004 (host:container)
- Volume mounts for hot-reload
- Health check on backend
- Environment variables passed through
- Frontend depends on backend startup

## Phase 4: Integration Testing

### Step 1: Build Images
```bash
docker compose build
```

**Expected Output**:
```
Building frontend
Building backend
```

### Step 2: Start Services
```bash
docker compose up -d
```

**Wait 10-15 seconds for services to fully start**

### Step 3: Verify Frontend
```bash
curl http://localhost:3004/
```

**Expected**: HTML response (NextJS page)

### Step 4: Verify Backend Health
```bash
curl http://localhost:8004/health
```

**Expected**:
```json
{"status": "ok"}
```

### Step 5: Test Endpoint
```bash
curl "http://localhost:8004/add?num1=5&num2=3"
```

**Expected**:
```json
{"result": 8}
```

### Step 6: Test CORS Headers
```bash
curl -H "Origin: http://localhost:3004" \
     -H "Access-Control-Request-Method: GET" \
     http://localhost:8004/add?num1=5&num2=3
```

**Expected CORS Headers**:
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

### Step 7: View Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f frontend
docker compose logs -f backend
```

### Step 8: Test Hot-Reload
**Frontend**: Modify a React component, save → Should reflect in browser without rebuild
**Backend**: Modify an operation, save → Should reflect without restart

### Step 9: Cleanup
```bash
docker compose down
```

## Environment Variables

### .env (Docker Runtime)
Create `.env` in project root:

```
FRONTEND_PORT=3004
BACKEND_PORT=8004
NEXT_PUBLIC_API_URL=http://localhost:8004
PYTHONUNBUFFERED=1
```

### .env.local (Local Development)
Create `.env.local` in project root:

```
FRONTEND_PORT=3004
BACKEND_PORT=8004
API_URL=http://localhost:8004
API_HOST=localhost
API_PORT=8004
```

**Difference**:
- `.env`: Used by Docker services
- `.env.local`: Used by local npm/python development
- Both define `NEXT_PUBLIC_API_URL=http://localhost:8004` (frontend→backend URL)

## Common Commands

| Command | Purpose |
|---------|---------|
| `docker compose up -d` | Start all services |
| `docker compose up -d --build` | Rebuild and start |
| `docker compose down` | Stop all services |
| `docker compose down -v` | Stop and remove volumes |
| `docker compose logs -f` | View live logs |
| `docker compose ps` | List services status |
| `docker compose exec backend bash` | Shell into backend |
| `docker compose exec frontend sh` | Shell into frontend |

## Troubleshooting

### Frontend Not Loading (Port 3004)
```bash
# Check if port in use
lsof -i :3004

# Check frontend logs
docker compose logs frontend

# Rebuild
docker compose down && docker compose up -d --build
```

### Backend Health Check Failing
```bash
# Check backend logs
docker compose logs backend

# Manually test
curl http://localhost:8004/health

# Restart backend
docker compose restart backend
```

### CORS Errors in Frontend
```bash
# Check if backend has CORS middleware
docker compose exec backend grep -n "CORSMiddleware" main.py

# Check CORS headers
curl -v http://localhost:8004/add?num1=5&num2=3 | grep -i access-control
```

### Volume Mount Issues
```bash
# Verify volumes are mounted
docker compose exec frontend ls -la /app

# Check if hot-reload working
docker compose exec backend cat /app/main.py | head -5
```

## Success Criteria
- ✅ Both services start without errors
- ✅ Frontend accessible on localhost:3004
- ✅ Backend accessible on localhost:8004
- ✅ Health check passes
- ✅ CORS headers present in responses
- ✅ End-to-end operation works (5 + 3 = 8)
- ✅ Hot-reload functions for both services
- ✅ No errors in docker compose logs

## Next Steps
1. Verify all tests pass (see CLAUDE.md Phase 4)
2. Complete REGRESSION.md checklist
3. Create PR with all changes
4. Merge to main

---

**See CLAUDE.md for full project orchestration.**
**See REGRESSION.md for pre-PR quality checklist.**
**See STARTUP.md for complete startup procedures.**
