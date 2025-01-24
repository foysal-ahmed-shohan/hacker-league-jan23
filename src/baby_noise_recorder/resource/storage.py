import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from uuid import uuid4

from ..context.config import settings
from ..state.models import AudioFile

class LocalStorage:
    """Handles local file system operations for audio recordings."""
    
    def __init__(self):
        self.storage_path = Path(settings.storage_path)
        self._ensure_storage_directory()

    def _ensure_storage_directory(self):
        """Create storage directory if it doesn't exist."""
        os.makedirs(self.storage_path, exist_ok=True)

    def save_recording(self, audio_data: bytes, duration: float, label: Optional[str] = None) -> AudioFile:
        """Save a new recording to storage."""
        file_id = str(uuid4())
        filename = f"{file_id}.wav"
        file_path = self.storage_path / filename

        with open(file_path, "wb") as f:
            f.write(audio_data)

        audio_file = AudioFile(
            id=file_id,
            filename=filename,
            created_at=datetime.now(),
            duration=duration,
            label=label,
            file_path=str(file_path)
        )
        return audio_file

    def get_recording(self, file_id: str) -> Optional[bytes]:
        """Retrieve a recording by its ID."""
        file_path = self.storage_path / f"{file_id}.wav"
        if not file_path.exists():
            return None
        
        with open(file_path, "rb") as f:
            return f.read()

    def delete_recording(self, file_id: str) -> bool:
        """Delete a recording by its ID."""
        file_path = self.storage_path / f"{file_id}.wav"
        if not file_path.exists():
            return False
        
        os.remove(file_path)
        return True

    def list_recordings(self) -> List[AudioFile]:
        """List all saved recordings."""
        recordings = []
        for file_path in self.storage_path.glob("*.wav"):
            file_id = file_path.stem
            # In a real app, we'd store metadata separately
            # Here we're just using file stats
            stats = file_path.stat()
            recordings.append(AudioFile(
                id=file_id,
                filename=file_path.name,
                created_at=datetime.fromtimestamp(stats.st_ctime),
                duration=0.0,  # Would need audio processing to get real duration
                file_path=str(file_path)
            ))
        return sorted(recordings, key=lambda x: x.created_at, reverse=True)
