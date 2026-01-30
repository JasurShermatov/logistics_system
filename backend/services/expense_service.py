"""Expense service - expense qo'shish, validatsiya."""
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.expense_repository import ExpenseRepository
from repositories.driver_repository import DriverRepository
from repositories.period_repository import PeriodRepository
from schemas.expense import ExpenseCreate, ExpenseUpdate
from models.expense import ChargedToEnum, Expense
from typing import Optional


class ExpenseService:
    """Expense logika."""
    
    def __init__(self, db: AsyncSession):
        self.expense_repo = ExpenseRepository(db)
        self.driver_repo = DriverRepository(db)
        self.period_repo = PeriodRepository(db)
    
    async def create_expense(self, data: ExpenseCreate) -> Expense:
        """Expense yaratish."""
        # Period tekshirish
        period = await self.period_repo.get(data.period_id)
        if not period:
            raise ValueError("Period topilmadi")
        
        # Driver tekshirish (agar driver_id berilgan bo'lsa)
        if data.driver_id:
            driver = await self.driver_repo.get(data.driver_id)
            if not driver:
                raise ValueError("Driver topilmadi")
        
        # charged_to validatsiya
        if data.charged_to not in [ChargedToEnum.DRIVER, ChargedToEnum.COMPANY, "driver", "company"]:
            raise ValueError("charged_to noto'g'ri")
        
        return await self.expense_repo.create(data.model_dump())
    
    async def update_expense(self, expense_id: int, data: ExpenseUpdate) -> Optional[Expense]:
        """Expense yangilash."""
        update_data = data.model_dump(exclude_unset=True)
        return await self.expense_repo.update(expense_id, update_data)
