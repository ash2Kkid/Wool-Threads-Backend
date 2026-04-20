from pydantic import BaseModel


class Customer(BaseModel):
    id: str
    name: str
    phone: str
    address: str

    total_orders: int = 0