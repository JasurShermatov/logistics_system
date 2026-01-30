"""Driver endpoints."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from services.driver_service import DriverService
from repositories.driver_repository import DriverRepository
from schemas.driver import DriverCreate, DriverUpdate, DriverResponse
from api.deps import get_current_admin
from models.user import User

router = APIRouter()


@router.get("/", response_model=list[DriverResponse])
async def list_drivers(db: AsyncSession = Depends(get_db)):
    repo = DriverRepository(db)
    return await repo.get_all()


@router.post("/", response_model=DriverResponse, status_code=status.HTTP_201_CREATED)
async def create_driver(
    data: DriverCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    service = DriverService(db)
    try:
        return await service.create_driver(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{driver_id}", response_model=DriverResponse)
async def get_driver(driver_id: int, db: AsyncSession = Depends(get_db)):
    repo = DriverRepository(db)
    driver = await repo.get(driver_id)
    if not driver:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver not found")
    return driver


@router.put("/{driver_id}", response_model=DriverResponse)
async def update_driver(
    driver_id: int,
    data: DriverUpdate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    service = DriverService(db)
    driver = await service.update_driver(driver_id, data)
    if not driver:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver not found")
    return driver


@router.delete("/{driver_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_driver(
    driver_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    repo = DriverRepository(db)
    ok = await repo.delete(driver_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver not found")
    return None
