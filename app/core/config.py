from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )
    
    PROJECT_NAME: str = "AI Business OS"
    ENV: Literal["development", "staging", "production"] = "development"
    DATABASE_URL: str = "postgresql+asyncpg://ai_user:ai123456@localhost:5432/ai_business_os"

settings = Settings()
