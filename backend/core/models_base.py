"""SQLAlchemy deklarativ Base va umumiy mixinlar."""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, func
from datetime import datetime


Base = declarative_base()


class TimestampMixin:
    """Vaqt cho'plari uchun mixin."""
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
