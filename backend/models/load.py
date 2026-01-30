"""Load modeli - Yuklar."""
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from core.models_base import Base, TimestampMixin


class Load(Base, TimestampMixin):
    """Yuk modeli."""
    __tablename__ = "loads"
    
    id = Column(Integer, primary_key=True)
    load_number = Column(String(50), unique=True, nullable=False, index=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    period_id = Column(Integer, ForeignKey("periods.id"), nullable=False)
    
    pickup_location = Column(String(255), nullable=False)
    delivery_location = Column(String(255), nullable=False)
    load_date = Column(Date, nullable=False)
    delivery_date = Column(Date, nullable=True)
    
    rate = Column(Numeric(12, 2), nullable=False)  # Yuk miqdori
    driver_percent = Column(Numeric(5, 2), nullable=True)  # Haydovchi foizi
    status = Column(String(50), default="in_transit", nullable=False)  # in_transit, delivered, cancelled
    notes = Column(Text, nullable=True)
    
    # Relationships
    driver = relationship("Driver", back_populates="loads")
    period = relationship("Period", back_populates="loads")
    
    def __repr__(self):
        return f"<Load(id={self.id}, load_number={self.load_number}, rate={self.rate})>"
