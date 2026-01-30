"""Expense modeli - Xarajatlar."""
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from core.models_base import Base, TimestampMixin
import enum


class ExpenseTypeEnum(str, enum.Enum):
    """Xaraja turlari."""
    FUEL = "fuel"
    MAINTENANCE = "maintenance"
    TOLL = "toll"
    INSURANCE = "insurance"
    FINE = "fine"
    OTHER = "other"


class ChargedToEnum(str, enum.Enum):
    """Kim tomonidan to'lanishi."""
    DRIVER = "driver"
    COMPANY = "company"


class Expense(Base, TimestampMixin):
    """Xaraja modeli."""
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True)
    expense_type = Column(SQLEnum(ExpenseTypeEnum), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    charged_to = Column(SQLEnum(ChargedToEnum), nullable=False)  # driver yoki company
    
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=True)
    period_id = Column(Integer, ForeignKey("periods.id"), nullable=False)
    
    expense_date = Column(Date, nullable=False)
    description = Column(String(255), nullable=True)
    note = Column(Text, nullable=True)
    
    # Relationships
    driver = relationship("Driver", back_populates="expenses")
    period = relationship("Period", back_populates="expenses")
    
    def __repr__(self):
        return f"<Expense(id={self.id}, type={self.expense_type}, amount={self.amount})>"
