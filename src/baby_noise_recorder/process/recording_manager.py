from datetime import datetime
from typing import List, Optional
import asyncio

from ..state.models import RecordingState, RecordingStatus, AudioFile
from ..resource.storage import LocalStorage
from ..resource.audio_device import AudioDevice
from ..context.config import settings

class RecordingManager:
    """Manages recording operations and state."""
    
    def __init__(self):
        self.state = RecordingState()
        self.storage = LocalStorage()
        self.audio_device = AudioDevice()
        self._current_recording_data = bytearray()
        
        # Set up audio data handler
        self.audio_device.on_data(self._handle_audio_data)

    def _handle_audio_data(self, data: bytes) -> None:
        """Handle incoming audio data chunks."""
        if self.state.status == RecordingStatus.RECORDING:
            self._current_recording_data.extend(data)
            
            # Update duration
            if self.state.start_time:
                self.state.duration = (
                    datetime.now() - self.state.start_time
                ).total_seconds()
                
            # Check if we've exceeded maximum recording length
            if self.state.duration >= settings.max_recording_length:
                asyncio.create_task(self.stop_recording())

    async def start_recording(self, websocket) -> None:
        """Start a new recording."""
        if self.state.status != RecordingStatus.IDLE:
            return

        self.state.status = RecordingStatus.RECORDING
        self.state.start_time = datetime.now()
        self.state.duration = 0.0
        self._current_recording_data.clear()
        
        await self.audio_device.start_recording(websocket)

    async def stop_recording(self, websocket, label: Optional[str] = None) -> Optional[AudioFile]:
        """Stop the current recording and save it."""
        if self.state.status != RecordingStatus.RECORDING:
            return None

        await self.audio_device.stop_recording(websocket)
        
        # Save recording if we have data
        audio_file = None
        if self._current_recording_data:
            audio_file = self.storage.save_recording(
                bytes(self._current_recording_data),
                self.state.duration,
                label
            )
            self._current_recording_data.clear()

        # Reset state
        self.state.status = RecordingStatus.IDLE
        self.state.start_time = None
        self.state.duration = 0.0
        
        return audio_file

    def get_recording(self, file_id: str) -> Optional[bytes]:
        """Retrieve a recording by ID."""
        return self.storage.get_recording(file_id)

    def delete_recording(self, file_id: str) -> bool:
        """Delete a recording by ID."""
        return self.storage.delete_recording(file_id)

    def list_recordings(self) -> List[AudioFile]:
        """List all saved recordings."""
        return self.storage.list_recordings()

    def get_state(self) -> RecordingState:
        """Get current recording state."""
        return self.state
