from app.database.batch_tracking_db import get_farmer_batch_tracking


def fetch_farmer_tracking(farmer_id: str):
    return get_farmer_batch_tracking(farmer_id)