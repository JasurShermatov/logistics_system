"""Auth shemalari - Login, register, token."""
from pydantic import BaseModel, EmailStr
from typing import Optional


class LoginRequest(BaseModel):
    """Login so'rovi."""
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Token javob."""
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    """Refresh token so'rovi."""
    refresh_token: str


class RegisterRequest(BaseModel):
    """Registratsiya so'rovi."""
    email: EmailStr
    full_name: str
    password: str
    phone: Optional[str] = None
