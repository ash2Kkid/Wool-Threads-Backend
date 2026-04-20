from app.database.farmer_db import create_farmer, get_farmer
from app.database.wool_batch_db import get_batches_by_farmer


def register_farmer(farmer):
    create_farmer(farmer.dict())
    return {"message": "Farmer registered successfully"}


def fetch_farmer_profile(farmer_id: str):
    return get_farmer(farmer_id)


def fetch_farmer_batches(farmer_id: str):
    return get_batches_by_farmer(farmer_id)

