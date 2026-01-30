"""Audit modeli - Audit log'lar."""
from sqlalchemy import Column, Integer, String, DateTime, Text
from core.models_base import Base, TimestampMixin
from datetime import datetime


class Audit(Base):
    """Audit log modeli."""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=True)
    action = Column(String(100), nullable=False)  # create, update, delete
    model = Column(String(100), nullable=False)  # model nomi
    record_id = Column(Integer, nullable=False)
    changes = Column(Text, nullable=True)  # JSON format'da o'zgarishlar
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    ip_address = Column(String(50), nullable=True)
    
    def __repr__(self):
        return f"<Audit(id={self.id}, action={self.action}, model={self.model})>"
