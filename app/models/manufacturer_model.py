from pydantic import BaseModel


class Manufacturer(BaseModel):
    name: str
    location: str
    price_per_kg: float
    rating: float