from app.database.customer_db import create_customer, get_customer
from app.database.order_db import get_orders_by_customer


def register_customer(customer):
    create_customer(customer.dict())
    return {"message": "Customer registered successfully"}


def fetch_customer_profile(customer_id: str):
    return get_customer(customer_id)


def fetch_customer_orders(customer_id: str):
    return get_orders_by_customer(customer_id)