from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SPARC Todo API"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000

settings = Settings()
