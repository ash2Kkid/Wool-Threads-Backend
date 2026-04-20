from fastapi import APIRouter
from app.models.farmer_model import Farmer
from app.services.farmer_service import (
    register_farmer,
    fetch_farmer_profile,
    fetch_farmer_batches
)

router = APIRouter(prefix="/farmers", tags=["Farmers"])


@router.post("/register")
def create_farmer(farmer: Farmer):
    return register_farmer(farmer)


@router.get("/{farmer_id}")
def get_profile(farmer_id: str):
    return fetch_farmer_profile(farmer_id)


@router.get("/{farmer_id}/batches")
def get_batches(farmer_id: str):
    return fetch_farmer_batches(farmer_id)