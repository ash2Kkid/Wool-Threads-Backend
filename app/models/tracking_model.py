from pydantic import BaseModel


class Tracking(BaseModel):
    order_id: str

    current_location: str
    status: str            # In Transit / Delivered / Delayed
    eta: str               # Estimated delivery date/time