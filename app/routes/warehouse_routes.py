from fastapi import APIRouter
from app.services.warehouse_service import (
    fetch_all_warehouses,
    fetch_nearby_warehouses
)

router = APIRouter(prefix="/warehouses", tags=["Warehouses"])


@router.get("/")
def all_warehouses():
    return fetch_all_warehouses()


@router.get("/near/{city}")
def nearby(city: str):
    return fetch_nearby_warehouses(city)