"""Load endpoints."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from services.load_service import LoadService
from repositories.load_repository import LoadRepository
from schemas.load import LoadCreate, LoadUpdate, LoadResponse
from api.deps import get_current_admin
from models.user import User

router = APIRouter()


@router.get("/", response_model=list[LoadResponse])
async def list_loads(db: AsyncSession = Depends(get_db)):
    repo = LoadRepository(db)
    return await repo.get_all()


@router.post("/", response_model=LoadResponse, status_code=status.HTTP_201_CREATED)
async def create_load(
    data: LoadCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    service = LoadService(db)
    try:
        return await service.create_load(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{load_id}", response_model=LoadResponse)
async def get_load(load_id: int, db: AsyncSession = Depends(get_db)):
    repo = LoadRepository(db)
    load = await repo.get(load_id)
    if not load:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Load not found")
    return load


@router.put("/{load_id}", response_model=LoadResponse)
async def update_load(
    load_id: int,
    data: LoadUpdate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    service = LoadService(db)
    load = await service.update_load(load_id, data)
    if not load:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Load not found")
    return load


@router.delete("/{load_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_load(
    load_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    repo = LoadRepository(db)
    ok = await repo.delete(load_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Load not found")
    return None
