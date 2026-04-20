from fastapi import APIRouter
from app.services.revenue_service import fetch_farmer_revenue

router = APIRouter(prefix="/revenue", tags=["Revenue"])


@router.get("/farmer/{farmer_id}")
def farmer_revenue(farmer_id: str):
    return fetch_farmer_revenue(farmer_id)