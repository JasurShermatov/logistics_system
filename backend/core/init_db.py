from __future__ import annotations

import os

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.security import hash_password
from backend.models.user import User, UserRole


async def ensure_superadmin(db: AsyncSession) -> None:
    username = os.getenv("SUPERADMIN_USERNAME", "admin")
    password = os.getenv("SUPERADMIN_PASSWORD", "admin")
    full_name = os.getenv("SUPERADMIN_FULL_NAME", "Super Admin")

    res = await db.execute(select(User).where(User.username == username))
    exists = res.scalar_one_or_none()
    if exists:
        return

    user = User(
        username=username,
        password_hash=hash_password(password),
        role=UserRole.superadmin,
        full_name=full_name,
        is_active=True,
    )
    db.add(user)
    await db.commit()