from __future__ import annotations

import enum
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Enum,
    ForeignKey,
    Numeric,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.models_base import Base, TimestampMixin


class ExpenseType(str, enum.Enum):
    admin_fee = "admin_fee"
    insurance = "insurance"
    fuel = "fuel"
    toll = "toll"
    repair = "repair"
    penalty = "penalty"
    other = "other"


class ChargedTo(str, enum.Enum):
    driver = "driver"
    company = "company"


class Expense(Base, TimestampMixin):
    __tablename__ = "expenses"

    __table_args__ = (
        CheckConstraint(
            "(charged_to <> 'driver') OR (driver_id IS NOT NULL)",
            name="ck_expenses_driver_required_when_charged_to_driver",
        ),
        CheckConstraint(
            "(type <> 'other') OR (note IS NOT NULL AND length(trim(note)) > 0)",
            name="ck_expenses_note_required_when_type_other",
        ),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    period_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("periods.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    driver_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("drivers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    type: Mapped[ExpenseType] = mapped_column(
        Enum(ExpenseType, name="expense_type"),
        nullable=False,
    )

    charged_to: Mapped[ChargedTo] = mapped_column(
        Enum(ChargedTo, name="charged_to"),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    note: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    period = relationship("Period", back_populates="expenses", lazy="selectin")
    driver = relationship("Driver", back_populates="expenses", lazy="selectin")

    def __repr__(self) -> str:
        return f"<Expense id={self.id} type={self.type.value} charged_to={self.charged_to.value} amount={self.amount}>"