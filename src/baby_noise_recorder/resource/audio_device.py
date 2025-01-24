from typing import Optional, Callable
import json

class AudioDevice:
    """Interface for browser-based audio recording capabilities."""
    
    def __init__(self):
        self.stream_active = False
        self._on_data_callback: Optional[Callable[[bytes], None]] = None

    def to_json(self) -> str:
        """Convert device state to JSON for client."""
        return json.dumps({
            "isRecording": self.stream_active
        })

    async def start_recording(self, websocket) -> None:
        """Start recording audio from the browser."""
        if self.stream_active:
            return
        
        self.stream_active = True
        await websocket.send_json({
            "type": "command",
            "action": "start_recording"
        })

    async def stop_recording(self, websocket) -> None:
        """Stop recording audio from the browser."""
        if not self.stream_active:
            return
        
        self.stream_active = False
        await websocket.send_json({
            "type": "command",
            "action": "stop_recording"
        })

    async def handle_audio_data(self, data: bytes) -> None:
        """Handle incoming audio data from the browser."""
        if self._on_data_callback:
            self._on_data_callback(data)

    def on_data(self, callback: Callable[[bytes], None]) -> None:
        """Set callback for handling incoming audio data."""
        self._on_data_callback = callback
