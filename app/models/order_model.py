from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    product_id: str
    name: str
    price: float
    quantity: int

class Order(BaseModel):
    id: str | None = None
    customer_id: str
    items: list[OrderItem]
    total_amount: float
    status: str = "order_received"
    created_at: str | None = None