from fastapi import APIRouter
from app.models.customer_model import Customer
from app.services.customer_service import (
    register_customer,
    fetch_customer_profile,
    fetch_customer_orders
)

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/register")
def create_customer(customer: Customer):
    return register_customer(customer)


@router.get("/{customer_id}")
def get_profile(customer_id: str):
    return fetch_customer_profile(customer_id)


@router.get("/{customer_id}/orders")
def get_orders(customer_id: str):
    return fetch_customer_orders(customer_id)