# Docker Validator Skill

Validates Docker Compose orchestration, Dockerfiles, and service networking for the Stranger Things calculator.

## Usage

```
/docker-validator
```

## What It Validates

### 1. Dockerfile Structure

**Frontend Dockerfile (`frontend/Dockerfile`)**:
- ✅ Base image: `node:18-alpine` or compatible
- ✅ Installs dependencies: `npm install` or `npm ci`
- ✅ Exposes port 3004
- ✅ Runs dev server: `npm run dev` or similar
- ✅ Working directory set (`WORKDIR /app`)
- ✅ `.dockerignore` exists (excludes node_modules, .git, etc.)

**Backend Dockerfile (`backend/Dockerfile`)**:
- ✅ Base image: `python:3.11-slim` or compatible
- ✅ Installs dependencies: `pip install -r requirements.txt`
- ✅ Exposes port 8004
- ✅ Runs FastAPI: `python main.py` or `uvicorn main:app`
- ✅ Working directory set (`WORKDIR /app`)
- ✅ `.dockerignore` exists (excludes __pycache__, .git, etc.)

### 2. docker-compose.yaml

**File Structure**:
- ✅ Valid YAML syntax: `docker compose config` passes
- ✅ Version 3.8+
- ✅ Services defined: backend, frontend
- ✅ Volumes section (for hot-reload)
- ✅ Network configured (default bridge network)

**Backend Service**:
- ✅ build: `./backend`
- ✅ ports: `["8004:8004"]` or `"8004:8004"`
- ✅ volumes: `["./backend:/app"]` (code mounted)
- ✅ environment: API_PORT=8004 (or similar)
- ✅ health check configured (optional but recommended)
- ✅ depends_on: not required (frontend can wait)

**Frontend Service**:
- ✅ build: `./frontend`
- ✅ ports: `["3004:3004"]` or `"3004:3004"`
- ✅ volumes: `["./frontend:/app"]` (code mounted)
- ✅ volumes: `["frontend-node_modules:/app/node_modules"]` (preserve node_modules)
- ✅ environment: `NEXT_PUBLIC_API_URL=http://backend:8004`
- ✅ depends_on: backend (frontend waits for backend)

**Volumes**:
- ✅ `frontend-node_modules:` defined (named volume for node_modules)

### 3. Environment Variables

**`.env.example`** (Docker Compose):
- ✅ `API_URL=http://backend:8004` or similar
- ✅ `NODE_ENV=development`
- ✅ `NEXT_PUBLIC_API_URL=http://backend:8004`
- ✅ All required variables documented

**`.env.local.example`** (Local Development):
- ✅ `API_URL=http://localhost:8004`
- ✅ `NODE_ENV=development`
- ✅ `NEXT_PUBLIC_API_URL=http://localhost:8004`
- ✅ Clearly different from .env.example

### 4. Service Communication

- ✅ Frontend can reach backend at `http://backend:8004`
- ✅ CORS headers present (frontend origin allowed)
- ✅ No hardcoded `localhost` in code (uses env vars)
- ✅ Service names resolve correctly (Docker DNS)
- ✅ Ports accessible: 3004 (frontend), 8004 (backend)

### 5. Hot-Reload Configuration

- ✅ Code volumes mounted: `./frontend:/app`, `./backend:/app`
- ✅ Code changes reflected in 1-2 seconds
- ✅ Dev server restarts on file change (npm run dev, uvicorn --reload)
- ✅ No rebuild required for code changes

### 6. Health Checks & Startup

- ✅ Services start without errors
- ✅ No port conflicts (3004, 8004 available)
- ✅ Logs show service startup messages
- ✅ No hanging/stuck processes
- ✅ Services respond to requests after startup

## Validation Steps

1. Check file structure:
   - `docker-compose.yaml` exists
   - `frontend/Dockerfile` exists
   - `backend/Dockerfile` exists
   - `.env.example` and `.env.local.example` exist

2. Validate YAML syntax:
   ```bash
   docker compose config
   ```

3. Build images:
   ```bash
   docker compose build
   ```

4. Start services:
   ```bash
   docker compose up -d
   sleep 5  # Wait for startup
   ```

5. Test service communication:
   ```bash
   curl http://localhost:8004/health
   curl http://localhost:3004
   ```

6. Test frontend → backend:
   ```bash
   curl -X GET "http://localhost:8004/add?num1=5&num2=3"
   # Expected: {"result": 8}
   ```

7. Verify hot-reload:
   - Modify a file
   - Check if changes appear in running container (1-2 seconds)

8. Cleanup:
   ```bash
   docker compose down
   ```

## Pass Criteria

✅ **PASS** if ALL of the following are true:
- Dockerfiles present and valid (node:18-alpine, python:3.11-slim)
- docker-compose.yaml valid YAML and syntax correct
- All services start without errors
- Frontend and backend accessible on ports 3004, 8004
- CORS headers present (frontend → backend works)
- Environment variables documented (.env.example, .env.local.example)
- Hot-reload working (code changes visible without rebuild)
- Service discovery working (backend:8004 reachable from frontend)

❌ **FAIL** if ANY of:
- Dockerfiles missing or invalid syntax
- docker-compose.yaml invalid YAML
- Services fail to start (exit code non-zero)
- Port conflicts or inaccessible ports
- CORS errors preventing frontend ↔ backend communication
- Environment variables missing or misconfigured
- Hot-reload not working (require manual rebuild)

## Output

```
✅ Docker Validator Results

Dockerfiles:
  ✅ frontend/Dockerfile valid (node:18-alpine)
  ✅ backend/Dockerfile valid (python:3.11-slim)
  ✅ .dockerignore files present

docker-compose.yaml:
  ✅ Valid YAML syntax
  ✅ Services defined: backend, frontend
  ✅ Volumes configured for hot-reload
  ✅ Environment variables set correctly

Service Startup:
  ✅ Backend starts on port 8004
  ✅ Frontend starts on port 3004
  ✅ Services healthy (no errors in logs)

Service Communication:
  ✅ Frontend → Backend requests succeed (CORS working)
  ✅ Health checks pass
  ✅ Calculator operation works (5 + 3 = 8)

Environment Variables:
  ✅ .env.example documents Docker Compose vars
  ✅ .env.local.example documents local dev vars
  ✅ NEXT_PUBLIC_API_URL set correctly per environment

Hot-Reload:
  ✅ Code changes visible in 1-2 seconds
  ✅ No manual rebuild required

Result: ✅ PASS - Docker orchestration ready for production
```
