import uvicorn
from src.baby_noise_recorder.action.api import app
from src.baby_noise_recorder.context.config import settings

def main():
    """Run the baby noise recorder application."""
    uvicorn.run(
        "src.baby_noise_recorder.action.api:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )

if __name__ == "__main__":
    main()
