# Service Startup Guide (STARTUP.md)

## Overview
This guide shows how to start the Stranger Things Calculator services in different configurations:
1. **Docker Compose** (Recommended for full stack)
2. **Local Development** (Frontend + Backend running separately)
3. **Automated Script** (One-command startup)

---

## Option 1: Docker Compose (Recommended)

### Setup
```bash
# Ensure Docker and Docker Compose are installed
docker --version
docker-compose --version

# Build services (first time only)
docker compose build
```

### Start Services
```bash
docker compose up
```

### Verify Services
```bash
# In another terminal

# Check frontend
curl http://localhost:3004

# Check backend
curl http://localhost:8004/add?num1=5&num2=3
```

**Expected Output**:
- Frontend: HTML page with calculator UI
- Backend: `{"result": 8}`

### Access Services
- **Frontend**: http://localhost:3004
- **Backend**: http://localhost:8004

### Logs
```bash
# View frontend logs
docker compose logs frontend

# View backend logs
docker compose logs backend

# Follow logs in real-time
docker compose logs -f frontend
docker compose logs -f backend
```

### Stop Services
```bash
docker compose down
```

### Troubleshooting Docker
```bash
# Clean up Docker resources
docker system prune -a

# Rebuild without cache
docker compose build --no-cache

# Check service health
docker compose ps

# Inspect service logs for errors
docker compose logs backend | grep -i error
```

---

## Option 2: Local Development (Separate Terminals)

### Terminal 1: Backend (Python)
```bash
cd backend

# Create virtual environment (first time only)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (first time only)
pip install -r requirements.txt

# Start backend
python3 main.py
# or with uvicorn directly:
uvicorn main:app --reload --port 8004
```

**Expected Output**:
```
Uvicorn running on http://127.0.0.1:8004
Uvicorn server is running. Press CTRL+C to quit.
```

### Terminal 2: Frontend (Node)
```bash
cd frontend

# Install dependencies (first time only)
npm install

# Create .env.local for local development
echo "NEXT_PUBLIC_API_URL=http://localhost:8004" > .env.local

# Start frontend dev server
npm run dev
```

**Expected Output**:
```
  ▲ Next.js 14.x.x
  - Local:        http://localhost:3004
  - Environments: .env.local
```

### Verify Services
```bash
# Terminal 3: Test backend
curl http://localhost:8004/add?num1=5&num2=3
# Expected: {"result": 8}

# Test frontend loads
curl http://localhost:3004
# Expected: HTML with calculator UI
```

### Access Services
- **Frontend**: http://localhost:3004
- **Backend**: http://localhost:8004

### Stop Services
```bash
# In each terminal running a service, press Ctrl+C
```

### Troubleshooting Local Development

#### Backend Port Already in Use
```bash
# Find process using port 8004
lsof -i :8004

# Kill the process (if needed)
kill -9 <PID>
```

#### Frontend Port Already in Use
```bash
# Find process using port 3004
lsof -i :3004

# Kill the process (if needed)
kill -9 <PID>

# Or run on different port
npm run dev -- -p 3005
```

#### Virtual Environment Issues
```bash
# Delete old environment and recreate
rm -rf backend/venv
cd backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

#### npm Install Fails
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and lock file
rm -rf frontend/node_modules frontend/package-lock.json

# Reinstall
cd frontend && npm install
```

---

## Option 3: Automated Startup Script

### Create startup.sh
```bash
#!/bin/bash

# Start backend in background
cd backend
source venv/bin/activate 2>/dev/null || (python3 -m venv venv && source venv/bin/activate)
pip install -r requirements.txt >/dev/null 2>&1
python3 main.py &
BACKEND_PID=$!

# Start frontend in background
cd ../frontend
npm install >/dev/null 2>&1
echo "NEXT_PUBLIC_API_URL=http://localhost:8004" > .env.local
npm run dev &
FRONTEND_PID=$!

# Wait for services to start
sleep 5

# Verify services
echo "Verifying services..."
curl -s http://localhost:8004/health >/dev/null && echo "✓ Backend running on :8004" || echo "✗ Backend failed to start"
curl -s http://localhost:3004 >/dev/null && echo "✓ Frontend running on :3004" || echo "✗ Frontend failed to start"

echo ""
echo "Services started:"
echo "  Frontend: http://localhost:3004"
echo "  Backend:  http://localhost:8004"
echo ""
echo "Press Ctrl+C to stop"

# Keep script alive
wait
```

### Make Executable & Run
```bash
chmod +x startup.sh
./startup.sh
```

### Create Cleanup Script
```bash
#!/bin/bash

echo "Stopping services..."
pkill -f "python3 main.py"
pkill -f "npm run dev"
echo "Services stopped"
```

---

## Environment Variables

### .env (Docker Production)
**Location**: Root directory (for docker-compose.yaml)
```
NEXT_PUBLIC_API_URL=http://backend:8004
CORS_ORIGINS=http://localhost:3004,http://frontend:3004
```

**Why these values?**
- Frontend accesses backend via `backend` (DNS name inside Docker network)
- CORS allows both localhost (for local testing) and service name (for Docker)

### .env.local (Local Development)
**Location**: `frontend/.env.local`
```
NEXT_PUBLIC_API_URL=http://localhost:8004
```

**Why these values?**
- Frontend accesses backend via `localhost:8004` (outside Docker network)
- No port forwarding needed, services on same machine

### .env.example (Template)
**Location**: Root directory
```
# Frontend API URL (change based on environment)
NEXT_PUBLIC_API_URL=http://backend:8004

# Backend CORS allowed origins
CORS_ORIGINS=http://localhost:3004,http://frontend:3004
```

---

## CORS Troubleshooting

### Symptom: CORS Error in Browser
```
Access to fetch at 'http://localhost:8004/add?num1=5&num2=3' from origin 'http://localhost:3004'
has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

### Check CORS Headers
```bash
curl -i -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3
```

**Expected Response Headers**:
```
Access-Control-Allow-Origin: http://localhost:3004
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

### Fix CORS (Backend)
1. Ensure FastAPI CORS middleware is configured in `main.py`:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3004", "http://localhost:8004"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

2. Check environment variable `CORS_ORIGINS` is being used:
```python
import os
origins = os.getenv("CORS_ORIGINS", "http://localhost:3004").split(",")
```

3. Restart backend service

### Fix CORS (Frontend)
1. Ensure frontend uses `NEXT_PUBLIC_API_URL` environment variable:
```javascript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8004';
```

2. Check `.env.local` exists with correct URL:
```bash
cat frontend/.env.local  # Should output NEXT_PUBLIC_API_URL=http://localhost:8004
```

3. Restart frontend service

---

## Health Checks

### Backend Health
```bash
# Check if backend is running
curl -s http://localhost:8004/health | jq .
# or
curl -s http://localhost:8004/add?num1=1&num2=1 | jq .
```

### Frontend Health
```bash
# Check if frontend is running
curl -s http://localhost:3004 | head -20
```

### Docker Health
```bash
# Check service status
docker compose ps

# Check service logs
docker compose logs --tail=20 backend
docker compose logs --tail=20 frontend
```

---

## Performance Tips

### Faster Docker Startup
```bash
# Pre-build images
docker compose build

# Then start without rebuilding
docker compose up
```

### Faster npm Install
```bash
# Use npm ci instead of npm install (faster, more reliable)
npm ci

# Clean cache
npm cache clean --force
```

### Faster Python Install
```bash
# Cache pip packages
pip install --cache-dir ~/.cache/pip -r requirements.txt
```

---

## Development Workflow

### Day 1: Initial Setup
```bash
# Clone repo
git clone <repo-url>
cd agent-demo

# Option A: Docker Compose
docker compose up

# Option B: Local development
# Terminal 1
cd backend && source venv/bin/activate && python3 main.py

# Terminal 2
cd frontend && npm install && npm run dev
```

### Day 2+: Resume Development
```bash
# Option A: Docker
docker compose up

# Option B: Local
# Services continue running from yesterday, or restart as needed
```

### Before PR: Run Regression
```bash
# Follow REGRESSION.md checklist
# Includes: tests, CORS, Docker, code quality
```

---

## Summary Table

| Task | Command | Output |
|------|---------|--------|
| **Start (Docker)** | `docker compose up` | Both services running on ports 3004, 8004 |
| **Start (Local)** | Terminal 1: `python3 main.py` + Terminal 2: `npm run dev` | Both services running |
| **Test Backend** | `curl http://localhost:8004/add?num1=5&num2=3` | `{"result": 8}` |
| **Test Frontend** | `curl http://localhost:3004` | HTML page returned |
| **Test CORS** | `curl -H "Origin: ..." http://localhost:8004/add...` | CORS headers in response |
| **Stop (Docker)** | `docker compose down` | Services stopped |
| **Stop (Local)** | Ctrl+C in each terminal | Services stopped |
| **Logs (Docker)** | `docker compose logs -f backend` | Real-time logs |
| **Logs (Local)** | Check terminal output | Real-time logs |
