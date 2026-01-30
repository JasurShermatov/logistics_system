"""Report service - profit va driver net hisoblash, export."""
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.load_repository import LoadRepository
from repositories.expense_repository import ExpenseRepository
from repositories.driver_repository import DriverRepository
from repositories.period_repository import PeriodRepository
from decimal import Decimal
from typing import Dict, List


class ReportService:
    """Hisobotlar logikasi."""
    
    def __init__(self, db: AsyncSession):
        self.load_repo = LoadRepository(db)
        self.expense_repo = ExpenseRepository(db)
        self.driver_repo = DriverRepository(db)
        self.period_repo = PeriodRepository(db)
    
    async def get_company_profit(self, period_id: int) -> Dict:
        """Kompaniya profit hisoblash."""
        loads = await self.load_repo.get_by_period(period_id)
        expenses = await self.expense_repo.get_by_period(period_id)
        
        total_revenue = sum([load.rate for load in loads])
        total_expenses = sum([exp.amount for exp in expenses if exp.charged_to == "company"])
        profit = total_revenue - total_expenses
        
        return {
            "total_revenue": total_revenue,
            "total_expenses": total_expenses,
            "profit": profit,
        }
    
    async def get_driver_net(self, period_id: int, driver_id: int) -> Dict:
        """Haydovchi net hisoblash."""
        loads = await self.load_repo.get_by_driver(driver_id)
        expenses = await self.expense_repo.get_by_driver(driver_id)
        
        # Period filter
        loads = [l for l in loads if l.period_id == period_id]
        expenses = [e for e in expenses if e.period_id == period_id]
        
        total_gross = sum([(l.rate * l.driver_percent) / Decimal(100) for l in loads])
        total_deductions = sum([e.amount for e in expenses if e.charged_to == "driver"])
        net = total_gross - total_deductions
        
        return {
            "total_gross": total_gross,
            "total_deductions": total_deductions,
            "net": net,
        }
