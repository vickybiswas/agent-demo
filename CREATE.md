# Docker Orchestration Guide - Stranger Things Calculator

This guide covers Phase 3 of the project: containerizing and orchestrating the frontend and backend with Docker Compose.

## Prerequisite
- Phase 1 (Frontend) COMPLETE and TESTED
- Phase 2 (Backend) COMPLETE and TESTED
- Both pass their respective validators

## Project Structure
```
.
├── frontend/               # NextJS app (from Phase 1)
├── backend/                # FastAPI app (from Phase 2)
├── Dockerfile.frontend     # Frontend container image
├── Dockerfile.backend      # Backend container image
├── docker-compose.yaml     # Orchestration config
└── .dockerignore          # Docker build exclusions
```

## Phase 1: Frontend Dockerfile

**File**: `Dockerfile.frontend`

```dockerfile
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY frontend/package.json frontend/package-lock.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY frontend/ .

# Expose port
EXPOSE 3004

# Start dev server
CMD ["npm", "run", "dev"]
```

**Validation**:
- Base image: node:18-alpine (lightweight)
- WORKDIR: /app (consistent path)
- npm install succeeds
- Code mounted in EXPOSE 3004
- Dev server starts on port 3004

## Phase 2: Backend Dockerfile

**File**: `Dockerfile.backend`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY backend/requirements.txt .

# Install dependencies (fastapi, uvicorn only)
RUN pip install -r requirements.txt

# Copy source code
COPY backend/ .

# Expose port
EXPOSE 8004

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004", "--reload"]
```

**Validation**:
- Base image: python:3.11-slim
- requirements.txt contains only fastapi, uvicorn
- pip install succeeds
- Code mounted in EXPOSE 8004
- Uvicorn starts with reload for dev

## Phase 3: docker-compose.yaml

**File**: `docker-compose.yaml`

```yaml
version: '3.8'

services:
  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "3004:3004"
    volumes:
      - ./frontend:/app
    environment:
      - NODE_ENV=development
    depends_on:
      - backend

  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "8004:8004"
    volumes:
      - ./backend:/app
    environment:
      - DEBUG=True
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8004/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

networks:
  default:
    name: calculator_network
```

**Key Features**:
- Both services on same network (can communicate by service name)
- Volumes for hot-reload (code changes without rebuild)
- Frontend depends_on backend (startup order)
- Backend health check for readiness
- Ports exposed: 3003 and 8004

## Phase 4: Integration Testing

### Test 1: Services Start
```bash
docker compose up -d
docker compose ps
# Should show both services running
```

### Test 2: Frontend Accessible
```bash
curl http://localhost:3004
# Should return HTML (or 404 with correct headers)
```

### Test 3: Backend Accessible
```bash
curl http://localhost:8004/health
# Should return {"status": "ok"} or similar
```

### Test 4: Service Communication
```bash
# Test from frontend to backend
# Frontend code should call http://backend:8004/add?num1=5&num2=3
# Should return result without errors
```

### Test 5: Hot-Reload
```bash
# While running:
# 1. Edit frontend/pages/index.tsx (add a console.log)
# 2. Browser should refresh automatically
# 3. Edit backend/routes/add.py (change return format)
# 4. Uvicorn should auto-reload
```

### Test 6: Calculator Operations
```bash
# Test each operation end-to-end
curl http://localhost:3004  # Frontend loads
# Click buttons in browser, verify calculations
```

## Troubleshooting

### Ports Already in Use
```bash
# Port 3004 or 8004 in use
lsof -i :3004
lsof -i :8004
# Kill process or use different ports in docker-compose.yaml
```

### Services Can't Communicate
```bash
# Check network
docker network ls
docker network inspect calculator_network

# Check service names resolve
docker compose exec frontend ping backend
docker compose exec backend ping frontend
```

### Hot-Reload Not Working
```bash
# Restart services
docker compose restart

# Check volumes are mounted
docker compose exec frontend pwd  # Should be /app
ls  # Should show src/, pages/, etc.
```

### Health Check Failing
```bash
# Check backend is listening
docker compose logs backend
# Should see "Uvicorn running on..."

# Test endpoint directly
docker compose exec backend curl http://localhost:8004/health
```

## Success Checklist
- ✅ `docker compose up` completes without errors
- ✅ Both frontend and backend services running
- ✅ Frontend accessible at http://localhost:3004
- ✅ Backend accessible at http://localhost:8004
- ✅ Services communicate (frontend → backend)
- ✅ Hot-reload working (code changes reflect immediately)
- ✅ All calculator operations work end-to-end
- ✅ No hardcoded localhost in code (use service names)
- ✅ Health checks passing

## Next Steps
1. Run `/docker-validator` to validate configuration
2. QA Specialist tests entire flow
3. Prepare for production (if needed)

## Production Notes
- Remove `--reload` from uvicorn command
- Set NODE_ENV=production
- Use docker-compose.prod.yaml for production secrets
- Don't mount code volumes in production
