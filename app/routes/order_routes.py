from fastapi import APIRouter
from app.models.order_model import Order
from app.services.order_service import place_order
from app.database.order_db import get_orders_by_customer
from app.database.order_db import get_orders_by_farmer




router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def new_order(order: Order):
    return place_order(order)

@router.get("/customer/{customer_id}")
def customer_orders(customer_id: str):
    return get_orders_by_customer(customer_id)

@router.get("/farmer/{farmer_id}")
def farmer_orders(farmer_id: str):
    return get_orders_by_farmer(farmer_id)