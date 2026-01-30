"""Driver modeli - Haydovchilar."""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from core.models_base import Base, TimestampMixin


class Driver(Base, TimestampMixin):
    """Haydovchi modeli."""
    __tablename__ = "drivers"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    truck_number = Column(String(50), unique=True, nullable=False, index=True)
    truck_model = Column(String(100), nullable=True)
    default_percent = Column(Numeric(5, 2), default=50.00, nullable=False)  # Foiz
    phone = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    status = Column(String(20), default="active", nullable=False)  # active, inactive, on_leave
    
    # Relationships
    user = relationship("User", backref="driver")
    loads = relationship("Load", back_populates="driver")
    expenses = relationship("Expense", back_populates="driver")
    
    def __repr__(self):
        return f"<Driver(id={self.id}, truck={self.truck_number}, percent={self.default_percent})>"
