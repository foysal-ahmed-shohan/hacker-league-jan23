import uvicorn
from calculator.api.app import app

def main():
    uvicorn.run(
        "calculator.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()
