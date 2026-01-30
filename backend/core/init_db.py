"""Dastlabki ma'lumotlarni to'ldirish (ixtiyoriy)."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user import User
from models.driver import Driver
from models.period import Period
from core.security import hash_password


async def init_default_data(session: AsyncSession):
    """
    Dastlabki default ma'lumotlarni kiritish.
    Misal: admin user va test data'lar.
    """
    
    # Admin user tekshirish va yaratish
    result = await session.execute(
        select(User).where(User.email == "admin@logist.com")
    )
    existing_admin = result.scalar_one_or_none()
    if not existing_admin:
        admin_user = User(
            email="admin@logist.com",
            full_name="Administrator",
            hashed_password=hash_password("admin123"),
            role="admin",
            is_active=True,
        )
        session.add(admin_user)
        await session.commit()
        print("✓ Admin user yaratildi")


async def seed_database():
    """Database'ni initial data'lar bilan to'ldirish."""
    from core.database import async_session_maker
    
    async with async_session_maker() as session:
        await init_default_data(session)
