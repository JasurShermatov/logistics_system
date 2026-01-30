"""User shemalari."""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """User asosiy schema."""
    email: EmailStr
    full_name: str
    phone: Optional[str] = None


class UserCreate(UserBase):
    """User yaratish uchun schema."""
    password: str


class UserUpdate(BaseModel):
    """User yangilash uchun schema."""
    full_name: Optional[str] = None
    phone: Optional[str] = None


class UserResponse(UserBase):
    """User javob schema."""
    id: int
    role: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
