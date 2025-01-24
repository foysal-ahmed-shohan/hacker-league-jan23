from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    app_name: str = "Baby Noise Recorder"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    max_recording_length: int = 300  # Maximum recording length in seconds
    storage_path: str = "recordings"  # Path to store recordings

    class Config:
        env_prefix = "BABY_NOISE_"

settings = Settings()
