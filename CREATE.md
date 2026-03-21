# CREATE.md - Docker Orchestration Guide (5 Phases)

Build Docker containers and orchestrate frontend + backend with docker-compose.

## Phase 1: Frontend Dockerfile (Node Alpine)

Create a containerized NextJS application using node:18-alpine base image.

### Deliverables
- `frontend/Dockerfile` - Node.js development container
- `frontend/.dockerignore` - Excludes unnecessary files
- Builds successfully: `docker build -f frontend/Dockerfile .`
- Runs on port 3004

### `frontend/Dockerfile` Template
```dockerfile
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Expose port
EXPOSE 3004

# Development mode (hot-reload)
CMD ["npm", "run", "dev"]
```

### `frontend/.dockerignore`
```
node_modules
.next
.git
.gitignore
.dockerignore
*.md
.env.local
.env
```

### Build & Test
```bash
cd frontend
docker build -t calculator-frontend .
docker run -p 3004:3004 calculator-frontend
# Expected: ready - started server on 0.0.0.0:3004
```

### Quality Gate ✅
- Dockerfile syntax valid
- Image builds: `docker build -f frontend/Dockerfile .`
- Container runs on port 3004
- No build errors or warnings

---

## Phase 2: Backend Dockerfile (Python Slim)

Create a containerized FastAPI application using python:3.11-slim base image.

### Deliverables
- `backend/Dockerfile` - Python FastAPI container
- `backend/.dockerignore` - Excludes unnecessary files
- Builds successfully: `docker build -f backend/Dockerfile .`
- Runs on port 8004

### `backend/Dockerfile` Template
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed (none for fastapi)
# RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 8004

# Development mode (auto-reload)
CMD ["python", "main.py"]
```

### `backend/.dockerignore`
```
__pycache__
*.pyc
.pytest_cache
*.egg-info
.venv
venv
.git
.gitignore
.dockerignore
*.md
.env.local
.env
```

### Build & Test
```bash
cd backend
docker build -t calculator-backend .
docker run -p 8004:8004 calculator-backend
# Expected: INFO:     Uvicorn running on http://0.0.0.0:8004
```

### Quality Gate ✅
- Dockerfile syntax valid
- Image builds: `docker build -f backend/Dockerfile .`
- Container runs on port 8004
- No build errors or warnings

---

## Phase 3: docker-compose.yaml (Service Orchestration)

Create docker-compose configuration for local development with service networking.

### Deliverables
- `docker-compose.yaml` - Multi-container orchestration
- Valid YAML syntax: `docker compose config` passes
- Services defined: backend, frontend
- Volumes for hot-reload
- Environment variables configured
- Service networking (backend accessible from frontend as `http://backend:8004`)

### `docker-compose.yaml` Template
```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: calculator-backend
    ports:
      - "8004:8004"
    environment:
      - API_PORT=8004
      - NODE_ENV=development
    volumes:
      - ./backend:/app
      - /app/__pycache__
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8004/health"]
      interval: 10s
      timeout: 5s
      retries: 5

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: calculator-frontend
    ports:
      - "3004:3004"
    environment:
      - NEXT_PUBLIC_API_URL=http://backend:8004
      - NODE_ENV=development
    volumes:
      - ./frontend:/app
      - frontend-node_modules:/app/node_modules
    depends_on:
      backend:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3004"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  frontend-node_modules:

networks:
  default:
    name: calculator-network
    driver: bridge
```

### Key Features

**Backend Service**:
- Builds from `./backend/Dockerfile`
- Exposes port 8004
- Code mounted as volume (hot-reload)
- Health check using `/health` endpoint
- Environment: API_PORT=8004

**Frontend Service**:
- Builds from `./frontend/Dockerfile`
- Exposes port 3004
- Code mounted as volume (hot-reload)
- Environment: NEXT_PUBLIC_API_URL=http://backend:8004
- **Depends on backend** (waits for backend health check)
- node_modules preserved in named volume (prevents reinstall)

**Volumes**:
- `frontend-node_modules` - Named volume to preserve node_modules
- Backend code - Mounted directly for hot-reload
- Frontend code - Mounted directly for hot-reload

**Networking**:
- Default bridge network created (calculator-network)
- Frontend can reach backend via `http://backend:8004`
- Services communicate by container names, not localhost

### Validation
```bash
# Validate YAML syntax
docker compose config

# Build all images
docker compose build

# Start services
docker compose up

# Check service health
docker compose ps
# Expected: All services "Up"

# View logs
docker compose logs -f

# Stop services
docker compose down
```

### Quality Gate ✅
- `docker compose config` passes (valid YAML)
- `docker compose build` succeeds
- `docker compose up` starts all services
- `docker compose ps` shows all services "Up"
- Backend health check passes
- Frontend health check passes

---

## Phase 4: Integration Testing (Services Communication)

Test that frontend and backend containers communicate correctly.

### Deliverables
- Docker Compose services start without errors
- Backend responds on http://localhost:8004
- Frontend responds on http://localhost:3004
- Frontend → Backend requests succeed (CORS working)
- Calculator operation end-to-end test (5 + 3 = 8)
- All services healthy and logging correctly

### Integration Tests

**Test 1: Backend Health**
```bash
docker compose up -d
sleep 3  # Wait for startup

# Test backend health
curl http://localhost:8004/health
# Expected: {"status": "ok"}
```

**Test 2: Frontend Health**
```bash
curl http://localhost:3004
# Expected: HTTP 200 with HTML content
```

**Test 3: Backend API Endpoint**
```bash
curl "http://localhost:8004/add?num1=5&num2=3"
# Expected: {"result": 8}
```

**Test 4: Service-to-Service Communication**
```bash
# From frontend container, reach backend
docker compose exec frontend curl http://backend:8004/health
# Expected: {"status": "ok"}

# This proves frontend → backend communication works
```

**Test 5: CORS Headers (from host)**
```bash
curl -i -H "Origin: http://localhost:3004" \
  "http://localhost:8004/add?num1=5&num2=3"
# Expected: Response includes CORS headers
# Access-Control-Allow-Origin: *
```

**Test 6: Calculator End-to-End (Browser)**
```bash
# Open http://localhost:3004 in browser
# Click: 5 + 3 =
# Expected: Display shows 8

# Check browser console (F12) → Console
# Expected: No CORS errors
```

### Troubleshooting

**Services won't start**:
```bash
# Check logs
docker compose logs backend
docker compose logs frontend

# Check port conflicts
lsof -i :8004
lsof -i :3004

# Rebuild from scratch
docker compose down
docker compose build --no-cache
docker compose up
```

**Frontend can't reach backend**:
```bash
# Test connectivity from frontend container
docker compose exec frontend curl http://backend:8004/health

# Check service network
docker network inspect calculator-network

# Verify environment variable
docker compose exec frontend env | grep NEXT_PUBLIC_API_URL
# Expected: NEXT_PUBLIC_API_URL=http://backend:8004
```

**CORS errors in browser**:
```bash
# Verify CORS headers are returned
curl -i -H "Origin: http://localhost:3004" \
  "http://localhost:8004/add?num1=5&num2=3"

# Check response headers for:
# Access-Control-Allow-Origin
# Access-Control-Allow-Methods
# Access-Control-Allow-Credentials
```

### Quality Gate ✅
- Services start: `docker compose up` (no errors)
- Backend responds: `curl http://localhost:8004/health` (HTTP 200)
- Frontend responds: `curl http://localhost:3004` (HTTP 200)
- CORS headers present: `curl -H "Origin: ..." http://localhost:8004/...`
- Frontend → Backend works: `docker compose exec frontend curl http://backend:8004/health`
- End-to-end test: 5 + 3 = 8 displays in browser

---

## Phase 5: Environment Variables & Configuration

Document and validate environment variable configuration.

### Deliverables
- `.env.example` - Docker Compose environment variables
- `.env.local.example` - Local development environment variables
- Environment variables properly documented
- Services use correct URLs based on environment

### `.env` (Docker Compose)
```bash
# Copy this to .env for docker-compose
NEXT_PUBLIC_API_URL=http://backend:8004
NODE_ENV=development
API_URL=http://backend:8004
API_PORT=8004
```

**Why `backend:8004` instead of `localhost:8004`?**
- Inside Docker containers, services communicate via container names
- `backend` is the service name in docker-compose.yaml
- Frontend container can't access `localhost:8004` (localhost inside container is the container itself)

### `.env.local` (Local Development)
```bash
# Copy this to .env.local for local dev (without Docker)
NEXT_PUBLIC_API_URL=http://localhost:8004
NODE_ENV=development
API_URL=http://localhost:8004
API_PORT=8004
```

**Why `localhost:8004` for local dev?**
- Both backend and frontend run on host machine
- They communicate via localhost
- Port 8004 is exposed on host by docker-compose

### Loading Environment Variables

**In docker-compose.yaml**:
```yaml
environment:
  - NEXT_PUBLIC_API_URL=http://backend:8004
  - NODE_ENV=development
```

Or load from file:
```yaml
env_file: .env
```

**In Frontend Code**:
```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8004';
```

**In Backend Code**:
```python
import os
API_PORT = os.getenv('API_PORT', '8004')
```

### Validation
```bash
# Verify docker-compose has correct env vars
docker compose config | grep NEXT_PUBLIC_API_URL
# Expected: NEXT_PUBLIC_API_URL=http://backend:8004

# Verify running container has env var
docker compose exec frontend env | grep NEXT_PUBLIC_API_URL
# Expected: NEXT_PUBLIC_API_URL=http://backend:8004
```

### Quality Gate ✅
- `.env.example` documents Docker Compose variables
- `.env.local.example` documents local development variables
- Environment variables are used in code (not hardcoded)
- Services use correct URLs based on environment:
  - Docker: `http://backend:8004`
  - Local: `http://localhost:8004`

---

## Full Integration Test Checklist

Before moving to REGRESSION.md, verify all 5 phases:

- [ ] **Phase 1**: Frontend Dockerfile builds
- [ ] **Phase 2**: Backend Dockerfile builds
- [ ] **Phase 3**: docker-compose.yaml valid YAML
- [ ] **Phase 4**: All services start and communicate
  - [ ] Backend health: `curl http://localhost:8004/health` (200)
  - [ ] Frontend health: `curl http://localhost:3004` (200)
  - [ ] CORS headers present
  - [ ] Frontend → Backend works: `docker compose exec frontend curl http://backend:8004/health`
  - [ ] Calculator: 5 + 3 = 8 in browser
- [ ] **Phase 5**: Environment variables configured correctly
  - [ ] `.env.example` exists
  - [ ] `.env.local.example` exists
  - [ ] Services use NEXT_PUBLIC_API_URL correctly

---

## Commands Reference

```bash
# Build images
docker compose build
docker compose build --no-cache  # Force rebuild

# Start services
docker compose up                 # Foreground
docker compose up -d             # Background
docker compose up --detach       # Same as -d

# View status
docker compose ps
docker compose logs -f           # All logs
docker compose logs backend      # Backend only
docker compose logs frontend     # Frontend only

# Execute commands in container
docker compose exec backend python main.py
docker compose exec frontend npm run dev
docker compose exec frontend curl http://backend:8004/health

# Stop services
docker compose stop              # Graceful stop
docker compose down              # Stop and remove
docker compose down -v           # Remove volumes too

# Remove everything
docker compose down --remove-orphans --volumes

# Inspect services
docker compose config            # View merged config
docker network inspect calculator-network
```

---

## Success Criteria

✅ **Docker orchestration is production-ready if:**
- ✅ Phase 1: Frontend Dockerfile builds (node:18-alpine)
- ✅ Phase 2: Backend Dockerfile builds (python:3.11-slim)
- ✅ Phase 3: docker-compose.yaml valid and services start
- ✅ Phase 4: Integration tests pass (backend, frontend, CORS, end-to-end)
- ✅ Phase 5: Environment variables configured correctly

---

## Next Steps

Once all 5 phases are complete:
1. Frontend must be complete (see frontend/CLAUDE.md)
2. Backend must be complete (see backend/CLAUDE.md)
3. Run REGRESSION.md Phase 5 checks (Docker orchestration verification)
4. All phases must pass before PR can be created
