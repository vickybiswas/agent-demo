# Service Startup Guide

## Quick Start

Choose one of three options below based on your workflow.

---

## Option 1: Docker Compose (Recommended for Production)

### Start All Services
```bash
docker compose up -d
```

### Access Services
- **Frontend**: http://localhost:3004
- **Backend Health**: http://localhost:8004/health
- **Calculate**: http://localhost:8004/add?num1=5&num2=3

### View Logs
```bash
docker compose logs -f        # All services
docker compose logs -f frontend  # Frontend only
docker compose logs -f backend   # Backend only
```

### Stop Services
```bash
docker compose down
```

### Rebuild (After Code Changes)
```bash
docker compose up -d --build
```

---

## Option 2: Local Development (Terminal Windows)

### Terminal 1: Backend
```bash
cd backend
pip install -r requirements.txt
python3 main.py
```

Waits for output:
```
Uvicorn running on http://0.0.0.0:8004
```

### Terminal 2: Frontend
```bash
cd frontend
npm install
npm run dev
```

Expected output:
```
> next dev
  - Local: http://localhost:3004
```

### Access Services
- **Frontend**: http://localhost:3004
- **Backend**: http://localhost:8004/health

### Advantages
- Direct visibility of logs in each terminal
- Hot-reload works for both services
- Easy to debug code

---

## Option 3: Automated Startup Script

Create `startup.sh`:

```bash
#!/bin/bash

echo "Starting Stranger Things Calculator..."

# Start backend in background
echo "Starting backend on port 8004..."
cd backend
python3 main.py &
BACKEND_PID=$!

# Start frontend in background
echo "Starting frontend on port 3004..."
cd ../frontend
npm run dev &
FRONTEND_PID=$!

echo ""
echo "✅ Services started:"
echo "   Frontend:  http://localhost:3004"
echo "   Backend:   http://localhost:8004/health"
echo ""
echo "PID info:"
echo "   Backend PID:  $BACKEND_PID"
echo "   Frontend PID: $FRONTEND_PID"
echo ""
echo "To stop services:"
echo "   kill $BACKEND_PID $FRONTEND_PID"
echo ""

# Wait for both processes
wait
```

Make executable:
```bash
chmod +x startup.sh
```

Run:
```bash
./startup.sh
```

---

## Environment Variables

### Docker (.env)
```
FRONTEND_PORT=3004
BACKEND_PORT=8004
NEXT_PUBLIC_API_URL=http://localhost:8004
PYTHONUNBUFFERED=1
```

### Local Development (.env.local)
```
FRONTEND_PORT=3004
BACKEND_PORT=8004
API_URL=http://localhost:8004
API_HOST=localhost
API_PORT=8004
```

**Difference**:
- `.env`: Used by Docker services
- `.env.local`: Used by local npm/python development

---

## Verification Commands

### Frontend Health
```bash
curl http://localhost:3004/
# Should return HTML
```

### Backend Health
```bash
curl http://localhost:8004/health
# Should return {"status": "ok"}
```

### Calculate Example
```bash
curl "http://localhost:8004/add?num1=5&num2=3"
# Should return {"result": 8}
```

### CORS Headers
```bash
curl -H "Origin: http://localhost:3004" \
     http://localhost:8004/add?num1=5&num2=3
# Should include Access-Control-Allow-* headers
```

---

## CORS Troubleshooting

### Frontend Gets CORS Error
Ensure backend has CORS middleware configured:
```bash
grep -n "CORSMiddleware" backend/main.py
```

Should show:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Fix: Add CORS to Backend
If missing, add to `backend/main.py`:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use specific origins
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Port Configuration

### Default Ports
- Frontend: **3004**
- Backend: **8004**

### Change Frontend Port
```bash
# Docker
export FRONTEND_PORT=3005
docker compose up -d

# Local
npm run dev -- -p 3005
```

### Change Backend Port
```bash
# Docker
export BACKEND_PORT=8005
docker compose up -d

# Local
python3 main.py --port 8005  # If configured to accept port argument
```

**Note**: Update `NEXT_PUBLIC_API_URL` if backend port changes.

---

## Performance Tips

### For Docker
```bash
# Use development image with hot-reload
docker compose up -d

# Monitor resource usage
docker stats
```

### For Local Development
```bash
# Clean node_modules cache
rm -rf frontend/node_modules/.cache

# Restart dev server if unresponsive
# Ctrl+C and npm run dev again

# Check for port conflicts
lsof -i :3004
lsof -i :8004
```

---

## Cleanup & Reset

### Remove All Docker Containers
```bash
docker compose down -v
```

### Reset Frontend Cache
```bash
cd frontend
rm -rf .next node_modules
npm install
npm run dev
```

### Reset Backend Cache
```bash
cd backend
rm -rf __pycache__ .pytest_cache
pip install -r requirements.txt
python3 main.py
```

---

## Common Issues

| Issue | Solution |
|-------|----------|
| Port 3004 already in use | `lsof -i :3004` then `kill -9 <PID>` |
| Port 8004 already in use | `lsof -i :8004` then `kill -9 <PID>` |
| Frontend not updating | Clear `.next/` and restart `npm run dev` |
| Backend not updating | Restart Python process or use `--reload` flag |
| CORS errors | Check CORS middleware in backend/main.py |
| API URL wrong | Verify `NEXT_PUBLIC_API_URL` in .env.local |

---

## Next Steps

1. **Choose startup method** (Docker, Local, or Script)
2. **Start services** using commands above
3. **Verify health** using verification commands
4. **Test calculator** by performing operations
5. **Complete REGRESSION.md** before creating PR
6. **See CLAUDE.md** for full project details

---

## Quick Reference

```bash
# Docker (1 command)
docker compose up -d

# Local (2 terminals)
Terminal 1: cd backend && python3 main.py
Terminal 2: cd frontend && npm run dev

# Check status
curl http://localhost:3004/
curl http://localhost:8004/health

# Stop Docker
docker compose down

# View logs
docker compose logs -f
```

---

**Need help?** See REGRESSION.md for comprehensive testing guide.
