"""Period modeli - Settlement period'lari."""
from sqlalchemy import Column, Integer, Date, String, Enum as SQLEnum
from sqlalchemy.orm import relationship
from core.models_base import Base, TimestampMixin
from datetime import date
import enum


class PeriodStatusEnum(str, enum.Enum):
    """Period holatlari."""
    OPEN = "open"
    CLOSED = "closed"
    FINALIZED = "finalized"


class Period(Base, TimestampMixin):
    """Settlement period modeli."""
    __tablename__ = "periods"
    
    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False, index=True)
    end_date = Column(Date, nullable=False)
    report_date = Column(Date, nullable=False)
    status = Column(SQLEnum(PeriodStatusEnum), default=PeriodStatusEnum.OPEN, nullable=False)
    description = Column(String(255), nullable=True)
    
    # Relationships
    loads = relationship("Load", back_populates="period")
    expenses = relationship("Expense", back_populates="period")
    
    def __repr__(self):
        return f"<Period(id={self.id}, {self.start_date} - {self.end_date}, status={self.status})>"
