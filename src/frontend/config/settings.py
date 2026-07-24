from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_url: str = "http://localhost:8000"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"