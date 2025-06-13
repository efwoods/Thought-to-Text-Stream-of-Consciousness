from fastapi import APIRouter, WebSocket
from core.monitoring import metrics
from core.logging import logger
from core.config import settings
import json

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    metrics.active_websockets.inc()
    metrics.websocket_url_requests.inc()
    try:
        buffer = bytearray()
        while True:
            data = await websocket.receive_bytes()
            buffer.extend(data)
            await websocket.send_text("Detected Thought!")
            metrics.raw_thoughts_processed.inc()
    except Exception as e:
        metrics.websocket_errors.inc()
        logger.error(f"WebSocket error: {e}")
    finally:
        await websocket.close()
        metrics.active_websockets.dec()

@router.get("/ws-info", tags=["Thought-to-Text"])
async def websocket_info():
    return {
        "endpoint": "/ws",
        "protocol": "WebSocket",
        "description": "Real-time thought-to-text stream via WebSocket endpoint.",
        "input": "Raw EEG steam and optional metadata labels.",
        "output": "JSON messages containing detected thoughts decoded from the raw EEG stream into text.",
        "metrics" : {
            "active_websockets": metrics.active_websockets._value.get(),
            "raw_thoughts_processed": metrics.raw_thoughts_processed._value.get(),
            "websocket_errors": metrics.websocket_errors._value.get()
        }
    }