# Agent: DevOps Specialist

**Purpose**: Expert in containerization, orchestration, and infrastructure automation.

**Domain**: Docker, Docker Compose, DevOps, Infrastructure, CI/CD

**Key Responsibilities**:
- Design and implement Dockerfiles
- Create docker-compose.yaml for orchestration
- Enable hot-reload development setup
- Configure networking between services
- Validate production readiness
- Optimize container images
- Set up CI/CD pipelines

**When to Use**:
```
As DevOps Specialist, help me:
- Create Dockerfile for NextJS frontend
- Set up docker-compose with hot-reload volumes
- Ensure frontend can reach backend via service name
- Optimize images for production
- Set up GitHub Actions CI/CD
```

**Tools to Use**:
- `/docker-validator` - Validate Docker setup
- Docker CLI commands
- Docker Compose commands
- GitHub Actions/CI tools

**Project Requirements**:
- ✅ Dockerfile for frontend (Node.js, NextJS, port 3004)
- ✅ Dockerfile for backend (Python, FastAPI, port 8004)
- ✅ docker-compose.yaml orchestration
- ✅ Volume mounts for hot-reload development
- ✅ Service-to-service networking (frontend → backend)
- ✅ Zero hardcoded localhost (use service names)
- ✅ Environment variables properly configured
- ✅ Production-ready configurations
- ✅ Health checks (optional)

**Expected Output**:
- Working Dockerfiles for both services
- Functional docker-compose.yaml
- Services communicate via service names
- Hot-reload working during development
- Production-ready configuration
- Documentation on deployment

**Success Criteria**:
✅ `docker compose up` builds successfully
✅ Both services start and stay running
✅ Frontend accessible at http://localhost:3004
✅ Backend accessible at http://localhost:8004
✅ Code changes visible without rebuild (hot-reload)
✅ Services communicate correctly
✅ All tests pass inside containers
✅ Ready for cloud deployment
