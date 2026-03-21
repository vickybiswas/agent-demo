---
name: docker-validator
description: Validate Docker and Docker Compose orchestration for the calculator app. Use this skill to check compose.yaml structure, Dockerfiles for frontend and backend, port mappings (3004 frontend, 8004 backend), volume mounts for hot reloading, inter-container networking, build contexts, and readiness for production deployment. Run whenever creating or updating Docker configuration, before testing with compose, or during deployment preparation.
compatibility:
  - code-review-graph (for file analysis)
---

# Docker Validator

This skill validates your Docker and Docker Compose setup for the Stranger Things Calculator.

## What This Skill Does

Validates that your Docker orchestration meets these requirements:
- **compose.yaml structure** - proper service definitions, networking, volumes
- **Frontend Dockerfile** - builds NextJS app, runs on port 3004, hot-reload ready
- **Backend Dockerfile** - builds FastAPI app, runs on port 8004, hot-reload ready
- **Port mapping** - 3004 for frontend, 8004 for backend
- **Volume mounts** - code mounted for hot reloading in both services
- **Networking** - frontend can reach backend via docker hostname
- **Build context** - correct COPY and RUN commands
- **Environment variables** - properly passed to services
- **Dependencies** - backend service available when frontend starts
- **Health checks** - optional but recommended for production
- **Production readiness** - can build and run with `docker compose up`

## How to Use This Skill

**Check your Docker setup:**
```
/docker-validator
Validate my docker-compose.yaml and Dockerfiles.
Make sure frontend and backend can talk to each other.
```

**Before first compose up:**
```
/docker-validator
Check everything - will docker compose up work?
Are the ports mapped correctly? Can they communicate?
```

**After adding new service:**
```
/docker-validator
I just added a postgres service. Validate the entire setup.
Make sure all services can communicate and volumes work.
```

## Validation Checklist

The skill will check these items:

### docker-compose.yaml Structure
- [ ] Valid YAML syntax (no tabs, proper indentation)
- [ ] version specified (3.8+ recommended)
- [ ] services section defined
- [ ] frontend service defined
- [ ] backend service defined
- [ ] networks section optional but recommended
- [ ] volumes section for mount definitions (optional)

### Frontend Service Configuration
- [ ] Service name: frontend or web
- [ ] Build context: ./frontend (or correct path)
- [ ] Ports mapping: "3004:3004" (host:container)
- [ ] Volumes mounted: code mounted for hot reload
  - Example: `./frontend:/app` or `./frontend/src:/app/src`
- [ ] Working directory inside container: /app
- [ ] Command to start: `npm run dev` or similar
- [ ] Environment variables: API_URL or similar pointing to backend:8004
- [ ] No stdin_open/tty unless interactive
- [ ] Depends_on backend (optional but good practice)

### Backend Service Configuration
- [ ] Service name: backend or api
- [ ] Build context: ./backend (or correct path)
- [ ] Ports mapping: "8004:8004" (host:container)
- [ ] Volumes mounted: code mounted for hot reload
  - Example: `./backend:/app` or `./backend/app:/app/app`
- [ ] Working directory inside container: /app
- [ ] Command to start: `uvicorn main:app --host 0.0.0.0 --port 8004` or similar
- [ ] Environment variables: proper configuration
- [ ] Expose port 8004 internally
- [ ] No stdin_open/tty unless interactive

### Frontend Dockerfile
- [ ] Base image: node:18-alpine or similar
- [ ] Working directory set: WORKDIR /app
- [ ] Copy package files: COPY package*.json ./
- [ ] Install dependencies: RUN npm install
- [ ] Copy source code: COPY . .
- [ ] Build command if needed: RUN npm run build (or skip for dev)
- [ ] Expose port: EXPOSE 3004
- [ ] Start command: CMD ["npm", "run", "dev"] or equivalent
- [ ] No hardcoded localhost (use 0.0.0.0 or let framework handle)
- [ ] .dockerignore file excludes node_modules, .next, .git

### Backend Dockerfile
- [ ] Base image: python:3.11-slim or similar
- [ ] Working directory set: WORKDIR /app
- [ ] Install pip dependencies: RUN pip install fastapi uvicorn
- [ ] Copy requirements: COPY requirements.txt .
- [ ] Install from requirements: RUN pip install -r requirements.txt
- [ ] Copy source code: COPY . .
- [ ] Expose port: EXPOSE 8004
- [ ] Start command: CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004"]
- [ ] No hardcoded localhost
- [ ] .dockerignore excludes __pycache__, .pyc, venv, .git

### Networking
- [ ] Frontend can reach backend at: http://backend:8004 (via service name)
- [ ] Backend accessible from frontend using docker DNS
- [ ] Both services on same network (default or custom)
- [ ] No hardcoded IPs (use service names)
- [ ] Custom network optional but good for isolation

### Volume Mounts for Hot Reload
- [ ] Frontend code mounted as volume (not copied)
- [ ] Backend code mounted as volume (not copied)
- [ ] node_modules excluded from frontend mount (volume or .dockerignore)
- [ ] __pycache__ excluded from backend mount
- [ ] Can modify code on host and see changes in container without rebuild
- [ ] Clear mount paths (e.g., `./frontend:/app`)

### Environment Variables
- [ ] FRONTEND_API_URL or similar set to http://backend:8004
- [ ] Backend CORS enabled for http://frontend:3004 or wildcard for dev
- [ ] Can override with .env file if needed
- [ ] Secrets not hardcoded (no API keys, tokens)
- [ ] Development vs production configs considered

### Health Checks (Optional)
- [ ] Frontend health check: GET http://localhost:3004/
- [ ] Backend health check: GET http://localhost:8004/health
- [ ] Reasonable timeouts (5-10 second startup)
- [ ] Interval: 10-30 seconds

### Build & Run Readiness
- [ ] Can build frontend: `docker build ./frontend -t frontend`
- [ ] Can build backend: `docker build ./backend -t backend`
- [ ] Can start all: `docker compose up` (builds and runs)
- [ ] Can stop all: `docker compose down`
- [ ] No missing dependencies or build errors
- [ ] Images tagged appropriately if pushed to registry

### Port Accessibility
- [ ] Frontend accessible at http://localhost:3004
- [ ] Backend accessible at http://localhost:8004
- [ ] No port conflicts with host
- [ ] Ports match service internal ports (3004:3004, 8004:8004)

### File Organization
- [ ] Project root has docker-compose.yaml
- [ ] frontend/ directory has Dockerfile
- [ ] backend/ directory has Dockerfile
- [ ] frontend/ has .dockerignore
- [ ] backend/ has .dockerignore
- [ ] Both have proper directory structures

### Documentation
- [ ] README explains how to start: `docker compose up`
- [ ] README explains port mappings
- [ ] README explains how to access services
- [ ] README explains volume mounts for development
- [ ] Comments in compose.yaml explaining service roles

## How the Skill Works

1. **YAML Validation**: Checks compose.yaml syntax and structure
2. **Service Analysis**: Validates frontend and backend configurations
3. **Dockerfile Review**: Checks build instructions and setup
4. **Port & Networking**: Verifies port mappings and service communication
5. **Volume Analysis**: Ensures hot-reload volumes are configured
6. **Build Validation**: Tests if docker compose can start services
7. **Accessibility Check**: Verifies services are reachable
8. **Report**: Generates checklist with recommendations

## Output Format

The skill produces a validation report with:
- **Status**: ✅ Pass, ⚠️ Warnings, ❌ Failures
- **Category**: which area was checked
- **Finding**: what was found
- **Action**: how to fix if needed
- **Severity**: Critical, High, Medium, Low

### Example Report
```
DOCKER VALIDATION REPORT
==================================

✅ docker-compose.yaml Structure (5/5)
  ✅ Valid YAML syntax
  ✅ Services defined correctly
  ✅ Networks configured

✅ Frontend Service (6/6)
  ✅ Port 3004 mapped correctly
  ✅ Code volumes mounted
  ✅ Backend dependency set

⚠️ Backend Dockerfile (3/4)
  ✅ Python 3.11 base image
  ✅ Dependencies installed
  ❌ Hardcoded localhost in command
    Action: Use 0.0.0.0 instead of 127.0.0.1
    Severity: High

❌ Networking (1/2)
  ✅ Services on same network
  ❌ Frontend trying to reach localhost:8004 instead of backend:8004
    Action: Use http://backend:8004 in frontend API calls
    Severity: Critical
```

## When to Run This

- **Initial setup**: After creating compose.yaml and Dockerfiles
- **During development**: When adding services or changing configuration
- **Before testing**: Before running docker compose up
- **Before deployment**: Ensure production readiness
- **Troubleshooting**: When services can't communicate

## Pro Tips

1. **Use .dockerignore** - exclude node_modules, __pycache__, .git to speed up builds
2. **Multi-stage builds** - separate build stage from runtime for smaller images
3. **Service names in docker** - use service name instead of localhost (e.g., http://backend:8004)
4. **Volume best practices** - bind mount source code, use named volumes for databases
5. **Health checks** - add them for production deployments
6. **Environment files** - use .env for local development, ConfigMaps for Kubernetes
7. **Logs** - check with `docker compose logs frontend` / `docker compose logs backend`

## Troubleshooting

**"Services can't communicate"**: Verify they're on same network, use service name not localhost

**"Port already in use"**: Change host port (left side): "3005:3004" uses 3005 on host

**"Hot reload not working"**: Check volume mounts, ensure -v or volumes bind the source directory

**"npm install fails in Docker"**: Use .dockerignore to exclude node_modules, or run before copy

**"Backend not accessible from frontend"**: Use http://backend:8004 not http://localhost:8004

**"docker compose up fails"**: Run `docker compose up --build` to rebuild, check logs

**"Can't connect on localhost:3004"**: Verify ports in compose.yaml and Dockerfile EXPOSE match

**"Permissions denied on mounted volumes"**: May need to adjust Docker socket access or run as different user
