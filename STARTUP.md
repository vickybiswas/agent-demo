# Stranger Things Calculator - Startup Guide

## Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Start both services
docker compose up

# In another terminal, test the services:
curl http://localhost:8004/health     # Backend
curl http://localhost:3004/           # Frontend
```

**Frontend**: http://localhost:3004
**Backend**: http://localhost:8004
**API Docs**: http://localhost:8004/docs

### Option 2: Local Development (without Docker)

#### Setup Frontend Environment
```bash
cd frontend
cp .env .env.local
# Edit .env.local to use: NEXT_PUBLIC_API_URL=http://localhost:8004
```

#### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
python3 main.py
# Listens on http://localhost:8004
```

#### Frontend (NextJS)
```bash
cd frontend
npm install
npm run dev
# Listens on http://localhost:3004
# Calls backend at http://localhost:8004 (from .env.local)
```

**Important:** Frontend needs `.env.local` with `http://localhost:8004` for local development. In Docker, `.env` is used with `http://backend:8004`.

### Option 3: Automated Startup Script

```bash
chmod +x start-services.sh
./start-services.sh
```

The script will:
- Check if Docker daemon is running
- If yes: Start via `docker compose up`
- If no: Start backend and frontend locally

## Verification

### Backend Health Check
```bash
curl http://localhost:8004/health
# Expected response: {"status":"ok"}
```

### Test an Endpoint
```bash
curl "http://localhost:8004/add?num1=5&num2=3"
# Expected response: {"result": 8, "operation": "add"}
```

### Frontend Loading
```bash
curl http://localhost:3004/
# Should return HTML (calculator page)
```

## Troubleshooting

**Backend not responding?**
- Check if service is running: `curl http://localhost:8004/health`
- Check logs: `docker compose logs backend` (or look at terminal output if running locally)
- Verify port 8004 is not in use: `lsof -i :8004`

**Frontend not loading?**
- Check if service is running: `curl http://localhost:3004/`
- Check npm dependencies: `cd frontend && npm install`
- Clear cache: `rm -rf frontend/.next`

**Frontend can't reach backend (CORS error)?**
- **Local Dev**: Ensure `frontend/.env.local` has `NEXT_PUBLIC_API_URL=http://localhost:8004`
  ```bash
  # Copy and edit:
  cp frontend/.env frontend/.env.local
  # Edit .env.local:
  NEXT_PUBLIC_API_URL=http://localhost:8004
  ```
  Then restart: `npm run dev`
- **Docker**: Ensure `frontend/.env` has `NEXT_PUBLIC_API_URL=http://backend:8004`
- Check browser console for error messages
- Verify backend CORS allows frontend origin: `curl -H "Origin: http://localhost:3004" http://localhost:8004/health`

**Docker Compose failing?**
- Ensure Docker daemon is running: `docker ps`
- Check docker-compose.yaml syntax: `docker compose config`
- Rebuild images: `docker compose build --no-cache`
- Check environment variables: `docker compose config | grep NEXT_PUBLIC_API_URL`

## Architecture

```
calculator/
├── backend/          # FastAPI on port 8004
├── frontend/         # NextJS on port 3004
├── docker-compose.yaml
├── Dockerfile.backend
├── Dockerfile.frontend
└── start-services.sh
```

**Services communicate:**
- Frontend calls: `http://backend:8004` (in Docker) or `http://localhost:8004` (local)
- Health check ensures backend is ready before accepting requests
- Network: `calculator_network`

## Per CLAUDE.md

- **Frontend Phase**: NextJS + SCSS (port 3004)
- **Backend Phase**: FastAPI (port 8004)
- **Docker Phase**: Orchestration with hot-reload volumes
- **Testing**: Playwright e2e + pytest + Docker integration tests

See `CLAUDE.md`, `frontend/CLAUDE.md`, and `backend/CLAUDE.md` for detailed development phases.
