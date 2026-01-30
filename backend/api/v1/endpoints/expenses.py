"""Expense endpoints."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from services.expense_service import ExpenseService
from repositories.expense_repository import ExpenseRepository
from schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse
from api.deps import get_current_admin
from models.user import User

router = APIRouter()


@router.get("/", response_model=list[ExpenseResponse])
async def list_expenses(db: AsyncSession = Depends(get_db)):
    repo = ExpenseRepository(db)
    return await repo.get_all()


@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
async def create_expense(
    data: ExpenseCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    service = ExpenseService(db)
    try:
        return await service.create_expense(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{expense_id}", response_model=ExpenseResponse)
async def get_expense(expense_id: int, db: AsyncSession = Depends(get_db)):
    repo = ExpenseRepository(db)
    expense = await repo.get(expense_id)
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    return expense


@router.put("/{expense_id}", response_model=ExpenseResponse)
async def update_expense(
    expense_id: int,
    data: ExpenseUpdate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    service = ExpenseService(db)
    expense = await service.update_expense(expense_id, data)
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    return expense


@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense(
    expense_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    repo = ExpenseRepository(db)
    ok = await repo.delete(expense_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    return None
