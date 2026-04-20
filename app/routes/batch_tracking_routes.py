from fastapi import APIRouter
from app.services.batch_tracking_service import fetch_farmer_tracking

router = APIRouter(prefix="/farmer-tracking", tags=["Farmer Tracking"])


@router.get("/{farmer_id}")
def farmer_tracking(farmer_id: str):
    return fetch_farmer_tracking(farmer_id)