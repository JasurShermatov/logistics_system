"""Load service - load yaratish, period tekshirish, hisoblash."""
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.load_repository import LoadRepository
from repositories.driver_repository import DriverRepository
from repositories.period_repository import PeriodRepository
from schemas.load import LoadCreate, LoadUpdate
from models.load import Load
from typing import Optional
from decimal import Decimal


class LoadService:
    """Load logika."""
    
    def __init__(self, db: AsyncSession):
        self.load_repo = LoadRepository(db)
        self.driver_repo = DriverRepository(db)
        self.period_repo = PeriodRepository(db)
    
    async def create_load(self, data: LoadCreate) -> Load:
        """Load yaratish."""
        # Driver tekshirish
        driver = await self.driver_repo.get(data.driver_id)
        if not driver:
            raise ValueError("Driver topilmadi")
        
        # Period tekshirish
        period = await self.period_repo.get(data.period_id)
        if not period:
            raise ValueError("Period topilmadi")
        
        # Driver foizi
        driver_percent = data.driver_percent or driver.default_percent
        
        load_data = data.model_dump()
        load_data["driver_percent"] = driver_percent
        return await self.load_repo.create(load_data)
    
    async def update_load(self, load_id: int, data: LoadUpdate) -> Optional[Load]:
        """Load yangilash."""
        update_data = data.model_dump(exclude_unset=True)
        return await self.load_repo.update(load_id, update_data)
    
    def calculate_driver_gross(self, rate: Decimal, percent: Decimal) -> Decimal:
        """Haydovchi gross hisoblash."""
        return (rate * percent) / Decimal(100)
