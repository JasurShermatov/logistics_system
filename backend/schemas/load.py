"""Load shemalari."""
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import date, datetime


class LoadBase(BaseModel):
    """Load asosiy schema."""
    load_number: str
    pickup_location: str
    delivery_location: str
    load_date: date
    rate: Decimal


class LoadCreate(LoadBase):
    """Load yaratish uchun schema."""
    driver_id: int
    period_id: int
    delivery_date: Optional[date] = None
    driver_percent: Optional[Decimal] = None


class LoadUpdate(BaseModel):
    """Load yangilash uchun schema."""
    pickup_location: Optional[str] = None
    delivery_location: Optional[str] = None
    load_date: Optional[date] = None
    delivery_date: Optional[date] = None
    rate: Optional[Decimal] = None
    driver_percent: Optional[Decimal] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class LoadResponse(LoadBase):
    """Load javob schema."""
    id: int
    driver_id: int
    period_id: int
    delivery_date: Optional[date]
    driver_percent: Optional[Decimal]
    status: str
    notes: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True
