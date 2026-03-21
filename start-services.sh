#!/bin/bash
# Start Stranger Things Calculator Services

set -e

echo "🚀 Starting Stranger Things Calculator..."
echo ""

# Check if Docker daemon is running
if ! docker info > /dev/null 2>&1; then
    echo "⚠️  Docker daemon is not running. Attempting local startup..."
    echo ""
    echo "Starting backend locally (http://localhost:8004)..."
    cd backend
    python3 main.py &
    BACKEND_PID=$!
    echo "Backend PID: $BACKEND_PID"
    sleep 2

    echo ""
    echo "Starting frontend locally (http://localhost:3004)..."
    cd ../frontend
    npm run dev &
    FRONTEND_PID=$!
    echo "Frontend PID: $FRONTEND_PID"
    sleep 2

    echo ""
    echo "✅ Services started locally!"
    echo "📍 Backend:  http://localhost:8004"
    echo "📍 Frontend: http://localhost:3004"
    echo ""
    echo "Press Ctrl+C to stop services"
    wait
else
    echo "✅ Docker daemon is running"
    echo ""
    echo "Starting services via Docker Compose..."
    docker compose up
fi
