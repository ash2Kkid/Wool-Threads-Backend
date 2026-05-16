from pydantic import BaseModel


class Customer(BaseModel):
    id: str
    name: str
    email: str | None = None
    phone: str
    address: str

    total_orders: int = 0
