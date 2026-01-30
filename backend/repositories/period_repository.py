"""Period repository."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.period import Period, PeriodStatusEnum
from repositories.base_repository import BaseRepository
from typing import Optional
from datetime import date


class PeriodRepository(BaseRepository[Period]):
    """Period'lar uchun repository."""
    
    def __init__(self, db: AsyncSession):
        super().__init__(db, Period)
    
    async def get_open_period(self) -> Optional[Period]:
        """Hozirgi ochiq periodni olish."""
        result = await self.db.execute(
            select(Period).where(Period.status == PeriodStatusEnum.OPEN)
        )
        return result.scalar_one_or_none()
    
    async def get_by_date(self, target_date: date) -> Optional[Period]:
        """Berilgan sana bo'yicha period olish."""
        result = await self.db.execute(
            select(Period)
            .where(Period.start_date <= target_date)
            .where(Period.end_date >= target_date)
        )
        return result.scalar_one_or_none()
