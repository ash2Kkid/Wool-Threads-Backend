from fastapi import APIRouter
from app.services.tracking_service import fetch_tracking, update_shipment

router = APIRouter(prefix="/tracking", tags=["Tracking"])


@router.get("/{order_id}")
def track_order(order_id: str):
    return fetch_tracking(order_id)


@router.post("/{order_id}/update")
def update(order_id: str, location: str, status: str):
    return update_shipment(order_id, location, status)