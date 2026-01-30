from __future__ import annotations

import enum
from datetime import date
from typing import List

from sqlalchemy import BigInteger, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.models_base import Base, TimestampMixin
from backend.models.expense import Expense
from backend.models.load import Load


class PeriodStatus(str, enum.Enum):
    open = "open"
    locked = "locked"


class Period(Base, TimestampMixin):
    __tablename__ = "periods"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)

    report_date: Mapped[date | None] = mapped_column(Date, nullable=True)

    status: Mapped[PeriodStatus] = mapped_column(
        Enum(PeriodStatus, name="period_status"),
        nullable=False,
        server_default="open",
    )


    loads: Mapped[List["Load"]] = relationship(
        "Load",
        back_populates="period",
        cascade="all,delete-orphan",
        lazy="selectin",
    )
    expenses: Mapped[List["Expense"]] = relationship(
        "Expense",
        back_populates="period",
        cascade="all,delete-orphan",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<Period id={self.id} {self.start_date}..{self.end_date} status={self.status.value}>"