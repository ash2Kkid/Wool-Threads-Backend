from app.database.tracking_db import get_tracking, update_tracking


from fastapi import HTTPException
from app.database.tracking_db import get_tracking, update_tracking

def fetch_tracking(order_id: str):
    tracking = get_tracking(order_id)

    if tracking is None:
        raise HTTPException(
            status_code=404,
            detail=f"No tracking found for order {order_id}"
        )

    return tracking


def update_shipment(order_id: str, location: str, status: str):
    update_tracking(order_id, location, status)
    return {"message": "Tracking updated"}