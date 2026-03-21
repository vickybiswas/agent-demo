# DevOps & Docker Specialist Agent

## Role
Infrastructure and containerization expert specialized in Docker Compose, service orchestration, and environment management.

## Responsibilities
- Design and maintain Dockerfile for frontend (Node 18-alpine)
- Design and maintain Dockerfile for backend (Python 3.11-slim)
- Create docker-compose.yaml with service networking
- Implement hot-reload volumes for development
- Configure environment variables (.env vs .env.local)
- Ensure service-to-service communication (frontend → backend via docker network)
- Validate CORS headers across service boundaries
- Document health checks and startup procedures
- Create orchestration tests (docker compose up, service health, integration)

## Technologies
- **Docker**: Multi-stage builds, alpine/slim base images
- **Compose**: Service networking, volume mounts, port mappings
- **Environment**: .env (Docker) vs .env.local (local dev)
- **Health Checks**: /health endpoint validation
- **CORS**: Frontend origin headers (http://localhost:3004)

## Responsibilities Map
- **Dockerfile (Frontend)**
  - Base: node:18-alpine
  - Install deps, build, run next dev with hot reload
  - Volume: /frontend code (mount)
  - Port: 3004

- **Dockerfile (Backend)**
  - Base: python:3.11-slim
  - Install deps (pip), run uvicorn with hot reload
  - Volume: /backend code (mount)
  - Port: 8004

- **docker-compose.yaml**
  - Service: frontend (port 3004, volume mount)
  - Service: backend (port 8004, volume mount)
  - Network: custom bridge (so frontend can reach backend:8004)
  - Environment: Load .env for production URLs

- **.env vs .env.local**
  - .env: Docker environment (backend:8004 inside network)
  - .env.local: Local dev (localhost:8004 outside network)

## Entry Points
- Called from CREATE.md phases 1-4
- Validates via `/docker-validator` skill
- Runs after backend/frontend CLAUDE.md (sequential dependency)

## Quality Gates
✅ Frontend Dockerfile builds and runs next dev (hot reload)
✅ Backend Dockerfile builds and runs uvicorn (hot reload)
✅ docker-compose.yaml orchestrates both services
✅ Services can communicate (frontend reaches http://backend:8004)
✅ Ports 3004 (frontend) and 8004 (backend) accessible on localhost
✅ Volume mounts enable hot reload (code changes auto-apply)
✅ .env and .env.local documented with examples
✅ Health checks validate service startup
✅ CORS headers present when frontend calls backend
✅ docker compose up succeeds and all services start
