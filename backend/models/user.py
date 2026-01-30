"""User modeli - Foydalanuvchilar va rollar."""
from sqlalchemy import Column, Integer, String, Boolean, Enum as SQLEnum
from core.models_base import Base, TimestampMixin
import enum


class RoleEnum(str, enum.Enum):
    """Foydalanuvchi rollari."""
    ADMIN = "admin"
    MANAGER = "manager"
    DRIVER = "driver"
    ACCOUNTANT = "accountant"


class User(Base, TimestampMixin):
    """Foydalanuvchi modeli."""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(SQLEnum(RoleEnum), default=RoleEnum.DRIVER, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    phone = Column(String(20), nullable=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"
