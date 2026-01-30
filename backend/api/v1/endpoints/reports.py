"""Reports endpoints."""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from services.report_service import ReportService
from api.deps import get_current_admin
from models.user import User

router = APIRouter()


@router.get("/company/{period_id}")
async def company_profit(
    period_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    service = ReportService(db)
    return await service.get_company_profit(period_id)


@router.get("/driver/{period_id}/{driver_id}")
async def driver_profit(
    period_id: int,
    driver_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    service = ReportService(db)
    return await service.get_driver_net(period_id, driver_id)
