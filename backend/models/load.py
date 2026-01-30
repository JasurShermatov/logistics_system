from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Optional

from sqlalchemy import BigInteger, Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.models_base import Base, TimestampMixin


class Load(Base, TimestampMixin):
    __tablename__ = "loads"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    load_number: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    pickup_date: Mapped[date] = mapped_column(Date, nullable=False)

    pickup_location: Mapped[str] = mapped_column(String(30), nullable=False)
    delivery_location: Mapped[str] = mapped_column(String(30), nullable=False)

    rate: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)


    percent: Mapped[Optional[Decimal]] = mapped_column(Numeric(5, 4), nullable=True)

    driver_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("drivers.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    period_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("periods.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    driver_gross: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        server_default="0",
    )
    company_gross: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        server_default="0",
    )

    driver = relationship("Driver", back_populates="loads", lazy="selectin")
    period = relationship("Period", back_populates="loads", lazy="selectin")

    def __repr__(self) -> str:
        return f"<Load id={self.id} load_number={self.load_number!r} rate={self.rate}>"