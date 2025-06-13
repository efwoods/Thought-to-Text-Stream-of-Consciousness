from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response
import uvicorn
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from contextlib import asynccontextmanager

# Configuration & Metrics
from core.config import settings
from core.monitoring import metrics
from core.logging import logger

# API Routes
from api.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: 

    yield # Application runs here

    # Shutdown: (optional cleanup)

app = FastAPI(title="Thought-to-Text-Stream-of-Consciousness", root_path="/thought-to-text-api", lifespan=lifespan)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)

@app.get("/")
async def root(request: Request):
    return RedirectResponse(url="/thought-to-text-api/docs")

@app.get("/health")
async def health():
    metrics.health_requests.inc()
    return {"status": "healthy"}

@app.get("/metrics")
async def metrics_endpoint(request: Request):
    metrics.metric_requests.inc()
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.FASTAPI_PORT)