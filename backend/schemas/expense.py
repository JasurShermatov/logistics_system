"""Expense shemalari."""
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import date, datetime


class ExpenseBase(BaseModel):
    """Expense asosiy schema."""
    expense_type: str
    amount: Decimal
    charged_to: str
    expense_date: date


class ExpenseCreate(ExpenseBase):
    """Expense yaratish uchun schema."""
    period_id: int
    driver_id: Optional[int] = None
    description: Optional[str] = None
    note: Optional[str] = None


class ExpenseUpdate(BaseModel):
    """Expense yangilash uchun schema."""
    expense_type: Optional[str] = None
    amount: Optional[Decimal] = None
    charged_to: Optional[str] = None
    expense_date: Optional[date] = None
    description: Optional[str] = None
    note: Optional[str] = None


class ExpenseResponse(ExpenseBase):
    """Expense javob schema."""
    id: int
    period_id: int
    driver_id: Optional[int]
    description: Optional[str]
    note: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True
