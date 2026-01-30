"""Period shemalari."""
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class PeriodBase(BaseModel):
    """Period asosiy schema."""
    start_date: date
    end_date: date
    report_date: date
    description: Optional[str] = None


class PeriodCreate(PeriodBase):
    """Period yaratish uchun schema."""
    pass


class PeriodUpdate(BaseModel):
    """Period yangilash uchun schema."""
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    report_date: Optional[date] = None
    status: Optional[str] = None
    description: Optional[str] = None


class PeriodResponse(PeriodBase):
    """Period javob schema."""
    id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
