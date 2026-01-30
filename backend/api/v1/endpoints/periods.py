"""Period endpoints."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from repositories.period_repository import PeriodRepository
from schemas.period import PeriodCreate, PeriodUpdate, PeriodResponse
from api.deps import get_current_admin
from models.user import User
from models.period import PeriodStatusEnum

router = APIRouter()


@router.get("/", response_model=list[PeriodResponse])
async def list_periods(db: AsyncSession = Depends(get_db)):
    repo = PeriodRepository(db)
    return await repo.get_all()


@router.post("/", response_model=PeriodResponse, status_code=status.HTTP_201_CREATED)
async def create_period(
    data: PeriodCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    repo = PeriodRepository(db)
    return await repo.create(data.model_dump())


@router.get("/{period_id}", response_model=PeriodResponse)
async def get_period(period_id: int, db: AsyncSession = Depends(get_db)):
    repo = PeriodRepository(db)
    period = await repo.get(period_id)
    if not period:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Period not found")
    return period


@router.put("/{period_id}", response_model=PeriodResponse)
async def update_period(
    period_id: int,
    data: PeriodUpdate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    repo = PeriodRepository(db)
    period = await repo.update(period_id, data.model_dump(exclude_unset=True))
    if not period:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Period not found")
    return period


@router.post("/{period_id}/close", response_model=PeriodResponse)
async def close_period(
    period_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    repo = PeriodRepository(db)
    period = await repo.update(period_id, {"status": PeriodStatusEnum.CLOSED})
    if not period:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Period not found")
    return period


@router.post("/{period_id}/open", response_model=PeriodResponse)
async def open_period(
    period_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    repo = PeriodRepository(db)
    period = await repo.update(period_id, {"status": PeriodStatusEnum.OPEN})
    if not period:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Period not found")
    return period


@router.delete("/{period_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_period(
    period_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    repo = PeriodRepository(db)
    ok = await repo.delete(period_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Period not found")
    return None
