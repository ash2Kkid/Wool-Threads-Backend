from pydantic import BaseModel


class Farmer(BaseModel):
    id: str
    name: str
    email: str | None = None
    farm_name: str
    location: str

    total_batches: int = 0
    total_products: int = 0
    total_earnings: float = 0.0
