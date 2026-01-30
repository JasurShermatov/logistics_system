"""Driver shemalari."""
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime


class DriverBase(BaseModel):
    """Driver asosiy schema."""
    truck_number: str
    truck_model: Optional[str] = None
    default_percent: Decimal
    phone: Optional[str] = None
    address: Optional[str] = None


class DriverCreate(DriverBase):
    """Driver yaratish uchun schema."""
    user_id: int


class DriverUpdate(BaseModel):
    """Driver yangilash uchun schema."""
    truck_number: Optional[str] = None
    truck_model: Optional[str] = None
    default_percent: Optional[Decimal] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    status: Optional[str] = None


class DriverResponse(DriverBase):
    """Driver javob schema."""
    id: int
    user_id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
