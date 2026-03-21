# Docker Validator Skill

Validates Docker Compose setup for correct orchestration and service communication.

## Purpose
Ensures Docker configuration is production-ready with hot-reload development setup.

## Validation Checklist

### Frontend Dockerfile
- [ ] Base image: `node:18-alpine`
- [ ] WORKDIR set to `/app`
- [ ] COPY package.json and package-lock.json
- [ ] RUN npm install
- [ ] COPY remaining code
- [ ] EXPOSE 3004
- [ ] CMD: `npm run dev` or `npm start`
- [ ] .dockerignore excludes node_modules, .next

### Backend Dockerfile
- [ ] Base image: `python:3.11-slim`
- [ ] WORKDIR set to `/app`
- [ ] COPY requirements.txt
- [ ] RUN pip install -r requirements.txt
- [ ] COPY remaining code
- [ ] EXPOSE 8004
- [ ] CMD: `uvicorn main:app --host 0.0.0.0 --port 8004`
- [ ] No hardcoded localhost

### docker-compose.yaml
- [ ] Version: 3.8 or higher
- [ ] Two services: `frontend` and `backend`
- [ ] Frontend service
  - Image/build from Dockerfile
  - Ports: `3004:3004`
  - Volumes: `./frontend:/app` (hot-reload)
  - Environment: NODE_ENV, API_URL
- [ ] Backend service
  - Image/build from Dockerfile
  - Ports: `8004:8004`
  - Volumes: `./backend:/app` (hot-reload)
  - Environment: DEBUG, etc.
- [ ] Networks: services can communicate by name
- [ ] No hardcoded localhost or 127.0.0.1

### Frontend-Backend Integration
- [ ] Frontend uses `http://backend:8004` for API calls
- [ ] No hardcoded `http://localhost:8004`
- [ ] API calls work when running `docker compose up`
- [ ] Error handling for API failures

### Hot-Reload Setup
- [ ] Code changes auto-reflect without rebuild
- [ ] Node.js hot-reload working (--watch or dev server)
- [ ] Python hot-reload working (uvicorn reload)
- [ ] No rebuild required for code changes

### Health Checks
- [ ] Frontend health endpoint (or status page)
- [ ] Backend /health endpoint returns 200
- [ ] Services wait for dependencies before starting

## How to Invoke

```bash
/docker-validator
```

Validator will:
1. Check Dockerfile syntax
2. Validate docker-compose.yaml
3. Build images
4. Run services with `docker compose up`
5. Verify frontend access on port 3004
6. Verify backend access on port 8004
7. Test service communication
8. Verify hot-reload
9. Check health endpoints

## Output Format
- ✅ Passing checks
- ⚠️ Warnings
- ❌ Failing checks (blocks merge)

## Pass Criteria
- `docker compose up` works immediately
- Frontend accessible at http://localhost:3004
- Backend accessible at http://localhost:8004
- Services communicate without errors
- No hardcoded localhost in code
- Hot-reload functional
- All health checks pass
