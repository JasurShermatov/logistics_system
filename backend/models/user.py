from __future__ import annotations

import enum

from sqlalchemy import BigInteger, Boolean, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.models_base import Base, TimestampMixin
from backend.models.driver import Driver


class UserRole(str, enum.Enum):

    superadmin = "superadmin"
    admin = "admin"
    driver = "driver"


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    username: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"),
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30))

    driver_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("drivers.id", ondelete="SET NULL"),
        unique=True,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="true")

    from typing import Optional

    driver: Mapped[Optional["Driver"]] = relationship(
        "Driver",
        back_populates="user",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username!r} role={self.role.value} active={self.is_active}>"