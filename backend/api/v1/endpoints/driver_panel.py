"""Driver panel endpoints."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from services.report_service import ReportService
from repositories.period_repository import PeriodRepository
from api.deps import get_current_user
from models.user import User, RoleEnum

router = APIRouter()


@router.get("/periods")
async def list_driver_periods(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Driver uchun periodlar ro'yxati."""
    if current_user.role != RoleEnum.DRIVER:
        raise HTTPException(status_code=403, detail="Driver only")
    repo = PeriodRepository(db)
    return await repo.get_all()


@router.get("/periods/{period_id}/summary")
async def driver_period_summary(
    period_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Driver period summary."""
    if current_user.role != RoleEnum.DRIVER:
        raise HTTPException(status_code=403, detail="Driver only")
    service = ReportService(db)
    # current_user.id -> driver_id mapping (driver_id == user_id) logikasi soddalashtirildi
    return await service.get_driver_net(period_id, current_user.id)
