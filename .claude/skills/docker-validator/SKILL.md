# Docker Validator Skill

## Purpose
Validate Docker orchestration configuration and ensure services communicate correctly.

## Validation Rules

### Dockerfile: Frontend
- ✅ Base image: node:22-alpine
- ✅ WORKDIR set to /app
- ✅ Dependencies installed: npm install
- ✅ Build step: npm run build (if applicable)
- ✅ Port exposed: 3004
- ✅ Volume mount support for code
- ✅ Environment variables passed

### Dockerfile: Backend
- ✅ Base image: python:3.13-slim
- ✅ WORKDIR set to /app
- ✅ Dependencies installed: pip install fastapi uvicorn
- ✅ Server runs: uvicorn main:app --host 0.0.0.0 --port 8004
- ✅ Port exposed: 8004
- ✅ Volume mount support for code
- ✅ PYTHONUNBUFFERED=1 set

### docker-compose.yaml
- ✅ Version: 3.8+
- ✅ Two services: frontend, backend
- ✅ Frontend port mapping: 3004:3004
- ✅ Backend port mapping: 8004:8004
- ✅ Volume mounts for hot-reload
- ✅ Environment variables passed
- ✅ depends_on relationship (frontend → backend)
- ✅ Health check on backend

### Environment Configuration
- ✅ .env file for Docker runtime
- ✅ .env.local file for local development
- ✅ NEXT_PUBLIC_API_URL set correctly
- ✅ Both files documented
- ✅ No secrets in .env (use .env.local)

### Service Networking
- ✅ Frontend accessible on localhost:3004
- ✅ Backend accessible on localhost:8004
- ✅ Frontend can call backend at localhost:8004
- ✅ CORS headers present in responses
- ✅ No hostname-based networking (use localhost)

### Hot-Reload Configuration
- ✅ Frontend volume: ./frontend:/app
- ✅ Backend volume: ./backend:/app
- ✅ Code changes reflected without rebuild
- ✅ npm dev runs in frontend
- ✅ uvicorn server runs in backend

### Health Checks
- ✅ Backend /health endpoint returns 200 OK
- ✅ Health check interval: 10s
- ✅ Health check timeout: 5s
- ✅ Failed checks trigger restart

## Validation Checklist

### Pre-Launch Validation
```bash
# 1. Syntax check
docker-compose config

# 2. Build images
docker compose build

# 3. Start services
docker compose up -d

# 4. Check frontend (wait 10-15 seconds)
curl http://localhost:3004/

# 5. Check backend health
curl http://localhost:8004/health

# 6. Test endpoint
curl "http://localhost:8004/add?num1=5&num2=3"

# 7. Check logs
docker compose logs -f

# 8. Stop services
docker compose down

# Review checklist
- [ ] docker-compose.yaml valid
- [ ] Both images build successfully
- [ ] Services start without errors
- [ ] Frontend loads on :3004
- [ ] Backend responds on :8004
- [ ] Health check passes
- [ ] CORS headers present
- [ ] Hot-reload works
- [ ] Logs show no errors
```

## Service Communication Test
```bash
# Frontend can reach backend (from host machine)
curl -H "Origin: http://localhost:3004" \
     -H "Access-Control-Request-Method: GET" \
     http://localhost:8004/add?num1=5&num2=3

# Should include CORS headers:
# Access-Control-Allow-Origin: *
# Access-Control-Allow-Methods: GET, POST, OPTIONS
```

## Failure Cases
Validation fails if:
- docker-compose.yaml invalid syntax
- Images fail to build
- Services don't start
- Ports not accessible
- CORS headers missing
- Health check fails
- Environment variables not set
- Hot-reload doesn't work
- Volumes not mounted

## Success Criteria
- docker-compose.yaml ✅ valid
- Both images ✅ build
- Services ✅ start
- Frontend ✅ accessible :3004
- Backend ✅ accessible :8004
- Health check ✅ passes
- CORS headers ✅ present
- Hot-reload ✅ works
- Logs ✅ clean

## Environment Files Example

### .env (Docker)
```
FRONTEND_PORT=3004
BACKEND_PORT=8004
NEXT_PUBLIC_API_URL=http://localhost:8004
PYTHONUNBUFFERED=1
```

### .env.local (Local Dev)
```
FRONTEND_PORT=3004
BACKEND_PORT=8004
API_URL=http://localhost:8004
API_HOST=localhost
API_PORT=8004
```

## Key Commands
```bash
# Build and start
docker compose up -d --build

# View logs
docker compose logs -f

# View specific service
docker compose logs -f backend
docker compose logs -f frontend

# Stop all services
docker compose down

# Clean up volumes
docker compose down -v

# Rebuild images
docker compose build --no-cache

# Run command in container
docker compose exec backend python3 -m pytest tests/

# Shell into container
docker compose exec backend /bin/sh
```

## Integration with CLAUDE.md
This validator runs at the end of CREATE.md (Docker Phases).

## Usage
```bash
claude run docker-validator
```

Or invoke from CREATE.md:
```markdown
## Phase 4: Integration Testing
Run `/docker-validator` to verify:
- [ ] docker-compose.yaml valid
- [ ] Services start
- [ ] CORS verified
- [ ] Frontend↔Backend communication works
```
