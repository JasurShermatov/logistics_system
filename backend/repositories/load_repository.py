"""Load repository."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.load import Load
from repositories.base_repository import BaseRepository
from typing import List


class LoadRepository(BaseRepository[Load]):
    """Load'lar uchun repository."""
    
    def __init__(self, db: AsyncSession):
        super().__init__(db, Load)
    
    async def get_by_driver(self, driver_id: int, skip: int = 0, limit: int = 100) -> List[Load]:
        """Driver bo'yicha load'larni olish."""
        result = await self.db.execute(
            select(Load)
            .where(Load.driver_id == driver_id)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
    
    async def get_by_period(self, period_id: int, skip: int = 0, limit: int = 100) -> List[Load]:
        """Period bo'yicha load'larni olish."""
        result = await self.db.execute(
            select(Load)
            .where(Load.period_id == period_id)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
