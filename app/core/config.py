from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import ConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:password@db:5432/qna_db"
    DEBUG: bool = False

    model_config = ConfigDict(env_file = ".env")

settings = Settings()