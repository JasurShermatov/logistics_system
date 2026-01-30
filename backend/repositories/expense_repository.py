"""Expense repository."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.expense import Expense
from repositories.base_repository import BaseRepository
from typing import List


class ExpenseRepository(BaseRepository[Expense]):
    """Expense'lar uchun repository."""
    
    def __init__(self, db: AsyncSession):
        super().__init__(db, Expense)
    
    async def get_by_driver(self, driver_id: int, skip: int = 0, limit: int = 100) -> List[Expense]:
        """Driver bo'yicha expense'larni olish."""
        result = await self.db.execute(
            select(Expense)
            .where(Expense.driver_id == driver_id)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
    
    async def get_by_period(self, period_id: int, skip: int = 0, limit: int = 100) -> List[Expense]:
        """Period bo'yicha expense'larni olish."""
        result = await self.db.execute(
            select(Expense)
            .where(Expense.period_id == period_id)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
