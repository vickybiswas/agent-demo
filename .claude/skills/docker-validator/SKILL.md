# Docker Validator Skill

## Purpose
Validate Docker setup (Dockerfiles and docker-compose.yaml) against INSTRUCTIONS.md and CREATE.md requirements.

## Triggered On
- Docker file creation/modification
- Manual invocation: `/docker-validator`

## Validation Checklist

### Frontend Dockerfile
- [ ] Base image: node:18-alpine
- [ ] Working directory set (/app)
- [ ] package.json and package-lock.json copied
- [ ] npm dependencies installed
- [ ] Source code volume mounted (for hot reload)
- [ ] EXPOSE 3004
- [ ] CMD runs `npm run dev` (next dev with hot reload)
- [ ] No hardcoded environment variables (use .env)
- [ ] Build succeeds without errors

### Backend Dockerfile
- [ ] Base image: python:3.11-slim
- [ ] Working directory set (/app)
- [ ] requirements.txt copied (only fastapi + uvicorn)
- [ ] pip dependencies installed
- [ ] Source code volume mounted (for hot reload)
- [ ] EXPOSE 8004
- [ ] CMD runs `uvicorn main:app --host 0.0.0.0 --port 8004 --reload`
- [ ] No hardcoded environment variables
- [ ] Build succeeds without errors

### docker-compose.yaml
- [ ] Version 3.8+ or 3.9+
- [ ] Two services: frontend and backend
- [ ] Frontend service:
  - [ ] Image: built from frontend/Dockerfile
  - [ ] Ports: 3004:3004 (expose on localhost)
  - [ ] Volumes: code mount for hot reload
  - [ ] Environment: NEXT_PUBLIC_API_URL=http://backend:8004
- [ ] Backend service:
  - [ ] Image: built from backend/Dockerfile
  - [ ] Ports: 8004:8004 (expose on localhost)
  - [ ] Volumes: code mount for hot reload
  - [ ] Environment: CORS_ORIGINS configured
- [ ] Custom network for inter-service communication
- [ ] No hardcoded localhost (use service names: backend, frontend)
- [ ] Health checks for both services (optional but recommended)

### Environment Configuration
- [ ] .env.example provided with production values
- [ ] .env.local.example provided with development values
- [ ] NEXT_PUBLIC_API_URL documented:
  - [ ] Production (.env): http://backend:8004 (or API gateway URL)
  - [ ] Local dev (.env.local): http://localhost:8004
- [ ] CORS_ORIGINS documented for backend
- [ ] .gitignore includes .env and .env.local

### Service Communication
- [ ] Frontend can reach backend at http://backend:8004 (inside docker network)
- [ ] Frontend on localhost:3004 accessible from host
- [ ] Backend on localhost:8004 accessible from host
- [ ] CORS headers allow frontend origin

### Health & Startup
- [ ] `docker compose build` succeeds for both services
- [ ] `docker compose up` starts both services without errors
- [ ] Frontend logs show "ready - started server on..." or similar
- [ ] Backend logs show "Application startup complete" or similar
- [ ] Services remain running (no crashes)
- [ ] Health check endpoint responds (frontend and backend)

### Integration Testing
- [ ] Docker Compose logs show no errors after startup
- [ ] Frontend loads at http://localhost:3004
- [ ] Backend responds to http://localhost:8004/health or similar
- [ ] Frontend can call backend (5 + 3 operation works)
- [ ] CORS headers present in cross-origin requests

## Pass/Fail Criteria
✅ **PASS**: All checked items pass, services start and communicate
❌ **FAIL**: Any checked items fail or services don't start

## Outputs
- Checklist results (passed/failed items)
- Docker build logs
- docker compose logs
- Service health status
- Integration test results
