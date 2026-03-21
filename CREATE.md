# Docker Orchestration Guide (CREATE.md)

## Overview
This document guides the DevOps agent through creating Docker setup for the Stranger Things Calculator:
- **Phase 1**: Frontend Dockerfile (Node 18-alpine)
- **Phase 2**: Backend Dockerfile (Python 3.11-slim)
- **Phase 3**: docker-compose.yaml (service networking)
- **Phase 4**: Integration testing (verify services communicate)

**Prerequisite**: Frontend + Backend agents must complete (see CLAUDE.md Phase 1 & 2)

## Phase 1: Frontend Dockerfile

### Objective
Create a Dockerfile for NextJS frontend with hot-reload support during development.

### Requirements
- Base image: `node:18-alpine` (lightweight)
- Working directory: `/app`
- Copy package.json and package-lock.json
- Install dependencies: `npm install`
- Mount source code as volume (for hot reload)
- Expose port 3004
- Run command: `npm run dev` (NextJS dev server)
- Environment: Load from docker-compose (NEXT_PUBLIC_API_URL)

### Dockerfile Structure
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

# Volume mount for source code (hot reload)
# Defined in docker-compose.yaml, not here

EXPOSE 3004

CMD ["npm", "run", "dev"]
```

### Notes
- **No hardcoded environment variables** — use .env file
- **Hot reload**: docker-compose mounts /frontend volume
- **Port 3004**: Exposed for localhost access
- **Build time**: < 1 minute (alpine is small)

### Validation
- `docker build -t frontend:latest frontend/` succeeds
- No build errors or warnings
- Image size < 500MB

---

## Phase 2: Backend Dockerfile

### Objective
Create a Dockerfile for FastAPI backend with hot-reload support.

### Requirements
- Base image: `python:3.11-slim` (lightweight, security)
- Working directory: `/app`
- Copy requirements.txt (only fastapi + uvicorn)
- Install dependencies: `pip install -r requirements.txt`
- Mount source code as volume (for hot reload)
- Expose port 8004
- Run command: `uvicorn main:app --host 0.0.0.0 --port 8004 --reload`
- Environment: Load from docker-compose

### Dockerfile Structure
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Volume mount for source code (hot reload)
# Defined in docker-compose.yaml, not here

EXPOSE 8004

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004", "--reload"]
```

### Notes
- **No external dependencies** — only fastapi + uvicorn in requirements.txt
- **Hot reload**: `--reload` flag enables auto-restart on code change
- **--host 0.0.0.0**: Listens on all interfaces (needed inside Docker)
- **--port 8004**: Exposed for localhost access

### Validation
- `docker build -t backend:latest backend/` succeeds
- No build errors or warnings
- Image size < 300MB

---

## Phase 3: docker-compose.yaml

### Objective
Orchestrate Frontend + Backend services with networking and environment setup.

### Requirements
- Version: 3.8 or higher
- Two services: frontend and backend
- Custom network for inter-service communication
- Volume mounts for hot reload
- Environment variables (.env or inline)
- Port mappings (3004 for frontend, 8004 for backend)

### docker-compose.yaml Structure
```yaml
version: '3.9'

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: frontend
    ports:
      - "3004:3004"
    volumes:
      - ./frontend:/app
      - /app/node_modules  # Prevent node_modules from being overwritten
    environment:
      - NEXT_PUBLIC_API_URL=http://backend:8004
    networks:
      - app-network
    depends_on:
      - backend

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: backend
    ports:
      - "8004:8004"
    volumes:
      - ./backend:/app
    environment:
      - CORS_ORIGINS=http://localhost:3004,http://frontend:3004
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
```

### Key Points
- **Service names**: Use `backend` and `frontend` (DNS resolution inside network)
- **Volumes**: Mount source code for hot reload (node_modules excluded for frontend)
- **Environment**:
  - Frontend: `NEXT_PUBLIC_API_URL=http://backend:8004` (use service name, not localhost)
  - Backend: `CORS_ORIGINS` includes both localhost (for local dev) and service name (for Docker)
- **Network**: Custom bridge network for service discovery
- **depends_on**: Frontend depends on backend (startup order)

### Local .env vs Docker
- **.env** (production/Docker): `NEXT_PUBLIC_API_URL=http://backend:8004` (service name)
- **.env.local** (local dev): `NEXT_PUBLIC_API_URL=http://localhost:8004` (localhost)

### Validation
- `docker compose config` shows valid YAML
- No errors in structure

---

## Phase 4: Integration Testing

### Objective
Verify that docker-compose setup works end-to-end:
1. Build both services
2. Start services
3. Validate service communication
4. Test end-to-end operation

### Steps

#### Step 1: Build & Start
```bash
docker compose build   # Build both services
docker compose up      # Start both services
```

**Expected Output**:
- Frontend logs: "ready - started server on 0.0.0.0:3004"
- Backend logs: "Application startup complete"
- No error messages in logs

#### Step 2: Verify Service Health
```bash
# Check frontend accessibility
curl http://localhost:3004

# Check backend health endpoint
curl http://localhost:8004/health

# Or just endpoint
curl "http://localhost:8004/add?num1=5&num2=3"
```

**Expected**:
- Frontend returns HTML (calculator UI)
- Backend returns JSON ({"result": 8})

#### Step 3: Verify CORS & Service Communication
```bash
# Frontend calling backend (inside Docker network)
docker compose exec frontend curl http://backend:8004/add?num1=5&num2=3

# Frontend from localhost calling backend
curl -H "Origin: http://localhost:3004" "http://localhost:8004/add?num1=5&num2=3" -v
```

**Expected**:
- Response includes CORS headers (Access-Control-Allow-Origin)
- Backend returns {"result": 8}

#### Step 4: Test End-to-End Operation
Use Playwright (or browser) to:
1. Open http://localhost:3004
2. Click calculator buttons (5 + 3)
3. Verify result appears (8)
4. Verify CORS headers in Network tab

**Expected**:
- Frontend loads Stranger Things theme
- Animations play smoothly
- Backend call succeeds (no CORS errors)
- Result displays correctly

#### Step 5: Verify Logs
```bash
docker compose logs frontend | grep "ready"
docker compose logs backend | grep "startup complete"
```

**Expected**: Both services report successful startup.

### Troubleshooting

#### Services Won't Start
```bash
docker compose logs frontend  # See frontend errors
docker compose logs backend   # See backend errors

# Rebuild with no-cache
docker compose build --no-cache

# Clean up and retry
docker system prune -a
docker compose up --build
```

#### CORS Errors in Browser
1. Check backend CORS middleware in main.py
2. Verify environment variable is set: `docker compose exec backend env | grep CORS_ORIGINS`
3. Check that frontend URL is in CORS_ORIGINS list

#### Port Conflicts
```bash
# Find process using port 3004 or 8004
lsof -i :3004
lsof -i :8004

# If ports are in use, either kill the process or change docker-compose port mapping
```

#### Hot Reload Not Working
1. Verify volumes are correctly mounted: `docker inspect frontend | grep Mounts`
2. For Python: `--reload` flag should be in CMD
3. For Node: Make sure node_modules is excluded from mount

## Summary

**Deliverables**:
- ✅ frontend/Dockerfile (Node 18-alpine)
- ✅ backend/Dockerfile (Python 3.11-slim)
- ✅ docker-compose.yaml (with service networking)
- ✅ .env.example (production environment template)
- ✅ .env.local.example (development environment template)
- ✅ docker compose up succeeds
- ✅ Services communicate (frontend → backend)
- ✅ End-to-end operation verified

## Next Steps
1. Ensure Phase 1 & 2 (Frontend + Backend) complete
2. Execute Phase 1: Frontend Dockerfile
3. Execute Phase 2: Backend Dockerfile
4. Execute Phase 3: docker-compose.yaml
5. Execute Phase 4: Integration testing
6. Run REGRESSION.md Phase 4 (Docker verification)
7. Create PR when all tests pass
