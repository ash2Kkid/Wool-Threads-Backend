from pydantic import BaseModel


class WoolBatch(BaseModel):
    farmer_id: str

    wool_type: str        # Merino, Alpaca, Cashmere
    quantity_kg: float
    micron: float         # quality measure

    status: str = "available"   # pending/approved/processing/shipped