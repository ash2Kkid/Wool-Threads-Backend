from pydantic import BaseModel


class Product(BaseModel):
    id: str

    supplier_id: str            # farmer or manufacturer
    supplier_type: str          # "farmer" / "manufacturer"

    batch_id: str | None = None # Only for farmer raw products

    name: str
    category: str               # raw_material / clothing / fabric

    description: str
    price: float
    stock: int

    imageUrl: str