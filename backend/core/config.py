"""Pydantic Settings: Muhit o'zgaruvchilari va konfiguratsiya."""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Loyihaning asosiy sozlamalari."""
    
    # Asosiy parametrlar
    PROJECT_NAME: str = "Logist System"
    DEBUG: bool = False
    VERSION: str = "1.0.0"
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/logist_db"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
