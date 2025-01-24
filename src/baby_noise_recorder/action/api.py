from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from typing import List, Optional
import os

from ..process.recording_manager import RecordingManager
from ..state.models import RecordingState, AudioFile
from ..context.config import settings

app = FastAPI(title=settings.app_name)

# Set up static files and templates
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(os.path.dirname(current_dir), "static")
templates_dir = os.path.join(os.path.dirname(current_dir), "templates")

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

# Initialize recording manager
recording_manager = RecordingManager()

@app.get("/")
async def home(request: Request):
    """Render the main application page."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "app_name": settings.app_name}
    )

@app.get("/api/state")
async def get_state() -> RecordingState:
    """Get current recording state."""
    return recording_manager.get_state()

@app.get("/api/recordings")
async def list_recordings() -> List[AudioFile]:
    """List all saved recordings."""
    return recording_manager.list_recordings()

@app.get("/api/recordings/{file_id}")
async def get_recording(file_id: str):
    """Get a specific recording file."""
    data = recording_manager.get_recording(file_id)
    if not data:
        raise HTTPException(status_code=404, detail="Recording not found")
    
    return FileResponse(
        path=f"{settings.storage_path}/{file_id}.wav",
        media_type="audio/wav",
        filename=f"{file_id}.wav"
    )

@app.delete("/api/recordings/{file_id}")
async def delete_recording(file_id: str) -> bool:
    """Delete a specific recording."""
    success = recording_manager.delete_recording(file_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recording not found")
    return success

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time audio streaming."""
    await websocket.accept()
    
    try:
        while True:
            message = await websocket.receive_json()
            
            if message["type"] == "command":
                if message["action"] == "start":
                    await recording_manager.start_recording(websocket)
                elif message["action"] == "stop":
                    label = message.get("label")
                    audio_file = await recording_manager.stop_recording(websocket, label)
                    if audio_file:
                        await websocket.send_json({
                            "type": "recording_saved",
                            "file": audio_file.dict()
                        })
            
            elif message["type"] == "audio_data":
                await recording_manager.audio_device.handle_audio_data(
                    message["data"].encode()
                )
    
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()
