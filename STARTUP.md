# STARTUP.md - Service Startup Guide

Quick reference for starting the Stranger Things Calculator services.

## Option 1: Docker Compose (Recommended for Full Stack)

### Start All Services
```bash
docker compose up
```

**Output**:
```
backend_1   | Uvicorn running on http://0.0.0.0:8004
frontend_1  | ready - started server on 0.0.0.0:3004
```

### Access Services
- Frontend: http://localhost:3004
- Backend: http://localhost:8004

### Stop Services
```bash
docker compose down
```

### View Logs
```bash
docker compose logs -f        # All services
docker compose logs backend   # Backend only
docker compose logs frontend  # Frontend only
```

### Troubleshooting Docker
```bash
# Verify services running
docker compose ps

# Rebuild images
docker compose down
docker compose build --no-cache
docker compose up

# Check network
docker network ls
docker network inspect <network-name>
```

## Option 2: Local Development (Without Docker)

### Prerequisites
- Python 3.9+ installed
- Node 18+ installed
- `pip` and `npm` working

### Setup Environment Variables
Create `.env.local` in project root:
```
API_URL=http://localhost:8004
NEXT_PUBLIC_API_URL=http://localhost:8004
NODE_ENV=development
```

### Terminal 1: Start Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```

**Output**:
```
INFO:     Uvicorn running on http://127.0.0.1:8004
INFO:     Application startup complete
```

### Terminal 2: Start Frontend
```bash
cd frontend
npm install
npm run dev
```

**Output**:
```
ready - started server on 0.0.0.0:3004, url: http://localhost:3004
```

### Access Services
- Frontend: http://localhost:3004
- Backend: http://localhost:8004

### Troubleshooting Local Dev
```bash
# Backend won't start
python -m pip install -r requirements.txt  # Ensure deps installed
lsof -i :8004                             # Check port in use
python main.py                            # Should show FastAPI startup

# Frontend won't start
npm install                               # Reinstall deps
lsof -i :3004                            # Check port in use
npm run dev                              # Should show NextJS startup

# Port conflicts
kill -9 $(lsof -t -i :8004)  # Kill process on 8004
kill -9 $(lsof -t -i :3004)  # Kill process on 3004
```

## Option 3: Automated Script (Optional)

Create `start.sh`:
```bash
#!/bin/bash
set -e

echo "🎮 Starting Stranger Things Calculator..."

# Check prerequisites
command -v python3 >/dev/null 2>&1 || { echo "❌ Python 3 required"; exit 1; }
command -v node >/dev/null 2>&1 || { echo "❌ Node.js required"; exit 1; }

# Create .env.local if missing
if [ ! -f .env.local ]; then
    echo "📝 Creating .env.local..."
    cat > .env.local << EOF
API_URL=http://localhost:8004
NEXT_PUBLIC_API_URL=http://localhost:8004
NODE_ENV=development
EOF
fi

# Start backend
echo "🔧 Starting backend (port 8004)..."
cd backend
pip install -r requirements.txt > /dev/null 2>&1
python main.py &
BACKEND_PID=$!
cd ..

# Wait for backend to be ready
sleep 2
curl -s http://localhost:8004/health > /dev/null || {
    echo "❌ Backend health check failed"
    kill $BACKEND_PID
    exit 1
}
echo "✅ Backend ready"

# Start frontend
echo "🎨 Starting frontend (port 3004)..."
cd frontend
npm install > /dev/null 2>&1
npm run dev &
FRONTEND_PID=$!
cd ..

sleep 3
curl -s http://localhost:3004 > /dev/null || {
    echo "❌ Frontend health check failed"
    kill $BACKEND_PID $FRONTEND_PID
    exit 1
}
echo "✅ Frontend ready"

echo ""
echo "🎮 Stranger Things Calculator is running!"
echo "📱 Frontend: http://localhost:3004"
echo "🔧 Backend: http://localhost:8004"
echo ""
echo "Press Ctrl+C to stop services..."
echo ""

# Wait for interrupt
wait

# Cleanup
kill $BACKEND_PID $FRONTEND_PID 2>/dev/null || true
echo "👋 Services stopped"
```

**Usage**:
```bash
chmod +x start.sh
./start.sh
```

## Health Checks

### Backend Health
```bash
curl http://localhost:8004/health
# Expected: {"status": "ok"} or similar

# Or full health check with dependencies
curl http://localhost:8004/
# Expected: 404 or specific response
```

### Frontend Health
```bash
curl http://localhost:3004
# Expected: HTTP 200 with HTML content

# Or in browser
open http://localhost:3004
```

### Integration Test
```bash
# Test CORS and calculator operation
curl -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3
# Expected: {"result": 8} with CORS headers
```

## CORS Troubleshooting

### Symptoms
- Browser console shows: `Access to XMLHttpRequest blocked by CORS policy`
- Frontend can't reach backend
- `OPTIONS` request fails

### Diagnosis
```bash
# Check if backend is running
curl http://localhost:8004/health

# Check CORS headers
curl -i -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3
# Should see:
# Access-Control-Allow-Origin: *
# Access-Control-Allow-Credentials: true
# Access-Control-Allow-Methods: GET, POST, OPTIONS
```

### Solutions
1. Verify backend FastAPI app has CORS middleware configured
2. Verify frontend is using correct API URL (check .env.local)
3. Ensure backend is actually running and accessible
4. Check firewall isn't blocking 8004

**In Docker**:
```bash
# Verify services can communicate
docker compose exec frontend curl http://backend:8004/health
```

**In Local Dev**:
```bash
# Verify endpoint is accessible
python -m pytest -v tests/test_add_api.py::test_cors_headers
```

## Environment Variables

### Docker Compose (`.env`)
```bash
API_URL=http://backend:8004           # Inside Docker network
NEXT_PUBLIC_API_URL=http://backend:8004
NODE_ENV=production
```

### Local Development (`.env.local`)
```bash
API_URL=http://localhost:8004         # Localhost for dev
NEXT_PUBLIC_API_URL=http://localhost:8004
NODE_ENV=development
```

### Why Different?
- **Docker**: Services communicate via container names (backend:8004)
- **Local**: Services communicate via localhost (localhost:8004)

**Never hardcode localhost in code** — always use environment variables.

## Common Issues

### Port Already in Use
```bash
# Find and kill process on port 8004
lsof -i :8004
kill -9 <PID>

# Or choose different port
NEXT_PUBLIC_API_URL=http://localhost:9004 npm run dev  # Hypothetical
```

### Slow Startup
- First startup takes longer (dependencies install, build runs)
- Subsequent starts are faster
- Watch for "ready" or "Uvicorn running" messages

### Connection Refused
```bash
# Verify services are running
docker compose ps      # For Docker
lsof -i :3004 :8004   # For local dev

# Restart services
docker compose restart
# Or restart processes in separate terminals
```

### Module/Dependency Errors
```bash
# Backend
cd backend
pip install --upgrade pip
pip install -r requirements.txt

# Frontend
cd frontend
npm cache clean --force
npm install
```

## Next Steps

Once services are running:
1. Open http://localhost:3004 in browser
2. Test calculator: 5 + 3 (should = 8)
3. Check browser console (F12) for errors
4. Run tests: `pytest` (backend) and `npx playwright test` (frontend)
5. Before PR: Complete REGRESSION.md checklist
