import uvicorn
from src.sparc_demo.action.api import app
from src.sparc_demo.context.config import settings

def main():
    uvicorn.run(
        "src.sparc_demo.action.api:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )

if __name__ == "__main__":
    main()
