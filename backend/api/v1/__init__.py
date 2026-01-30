"""API v1 router."""
from fastapi import APIRouter
from api.v1.endpoints import auth, drivers, periods, loads, expenses, reports, driver_panel

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(drivers.router, prefix="/drivers", tags=["drivers"])
api_router.include_router(periods.router, prefix="/periods", tags=["periods"])
api_router.include_router(loads.router, prefix="/loads", tags=["loads"])
api_router.include_router(expenses.router, prefix="/expenses", tags=["expenses"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
api_router.include_router(driver_panel.router, prefix="/driver", tags=["driver-panel"])
