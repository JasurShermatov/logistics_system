"""Driver repository."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.driver import Driver
from repositories.base_repository import BaseRepository
from typing import Optional


class DriverRepository(BaseRepository[Driver]):
    """Driver'lar uchun repository."""
    
    def __init__(self, db: AsyncSession):
        super().__init__(db, Driver)
    
    async def get_by_truck_number(self, truck_number: str) -> Optional[Driver]:
        """Truck number bo'yicha driver olish."""
        result = await self.db.execute(
            select(Driver).where(Driver.truck_number == truck_number)
        )
        return result.scalar_one_or_none()
    
    async def get_by_user_id(self, user_id: int) -> Optional[Driver]:
        """User ID bo'yicha driver olish."""
        result = await self.db.execute(
            select(Driver).where(Driver.user_id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_active_drivers(self, skip: int = 0, limit: int = 100):
        """Faol driver'larni olish."""
        result = await self.db.execute(
            select(Driver)
            .where(Driver.status == "active")
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
