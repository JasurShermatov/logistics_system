from __future__ import annotations

from typing import Optional

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.models_base import Base, TimestampMixin


class AuditLog(Base, TimestampMixin):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    actor_user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    entity_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    entity_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)

    action: Mapped[str] = mapped_column(String(10), nullable=False)

    diff: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)

    actor = relationship("User", lazy="selectin")

    def __repr__(self) -> str:
        return f"<AuditLog id={self.id} actor_user_id={self.actor_user_id} {self.action} {self.entity_type}:{self.entity_id}>"