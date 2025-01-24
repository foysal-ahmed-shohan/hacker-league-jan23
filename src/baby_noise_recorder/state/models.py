from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class RecordingStatus(str, Enum):
    """Status of the recording."""
    IDLE = "idle"
    RECORDING = "recording"
    PLAYING = "playing"

class RecordingState(BaseModel):
    """Current state of the recording process."""
    status: RecordingStatus = RecordingStatus.IDLE
    start_time: Optional[datetime] = None
    duration: float = 0.0

class AudioFile(BaseModel):
    """Represents a saved audio recording."""
    id: str
    filename: str
    created_at: datetime
    duration: float
    label: Optional[str] = None
    file_path: str
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
