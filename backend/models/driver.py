from __future__ import annotations

from sqlalchemy import BigInteger, Boolean, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.models_base import Base, TimestampMixin


class Driver(Base, TimestampMixin):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    code: Mapped[str | None] = mapped_column(String(50), unique=True)
    first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    truck_no: Mapped[str] = mapped_column(String(50), nullable=False)

    percent: Mapped[float] = mapped_column(Numeric(5, 4), nullable=False, server_default="0.3000")

    phone: Mapped[str | None] = mapped_column(String(30))
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="true")

    user = relationship("User", back_populates="driver", uselist=False)
    loads = relationship("Load", back_populates="driver")
    expenses = relationship("Expense", back_populates="driver")

    def __repr__(self) -> str:
        return f"<Driver id={self.id} code={self.code!r} name={self.first_name} {self.last_name}>"