from fastapi import APIRouter
from app.services.manufacturer_service import fetch_manufacturers

router = APIRouter(prefix="/manufacturers", tags=["Manufacturers"])


@router.get("/")
def all_manufacturers():
    return fetch_manufacturers()