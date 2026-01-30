"""Driver service - driver qo'shish/foiz o'zgartirish."""
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.driver_repository import DriverRepository
from repositories.user_repository import UserRepository
from schemas.driver import DriverCreate, DriverUpdate
from models.driver import Driver
from typing import Optional


class DriverService:
    """Driver logika."""
    
    def __init__(self, db: AsyncSession):
        self.driver_repo = DriverRepository(db)
        self.user_repo = UserRepository(db)
    
    async def create_driver(self, data: DriverCreate) -> Driver:
        """Driver yaratish."""
        # User mavjudligini tekshirish
        user = await self.user_repo.get(data.user_id)
        if not user:
            raise ValueError("User topilmadi")
        
        # Truck number unikalligini tekshirish
        existing = await self.driver_repo.get_by_truck_number(data.truck_number)
        if existing:
            raise ValueError("Truck number allaqachon mavjud")
        
        return await self.driver_repo.create(data.model_dump())
    
    async def update_driver(self, driver_id: int, data: DriverUpdate) -> Optional[Driver]:
        """Driver yangilash."""
        update_data = data.model_dump(exclude_unset=True)
        return await self.driver_repo.update(driver_id, update_data)
    
    async def change_percent(self, driver_id: int, percent: float) -> Optional[Driver]:
        """Haydovchi foizini yangilash."""
        if percent < 0 or percent > 100:
            raise ValueError("Foiz 0-100 oralig'ida bo'lishi kerak")
        return await self.driver_repo.update(driver_id, {"default_percent": percent})
