from fastapi import APIRouter
from app.models.wool_batch_model import WoolBatch
from app.services.wool_batch_service import register_batch, send_batch_to_manufacturer

router = APIRouter(prefix="/batches", tags=["Wool Batches"])


@router.post("/")
def create_batch(batch: WoolBatch):
    return register_batch(batch)

@router.post("/{batch_id}/send/{manufacturer_id}")
def send_batch(batch_id: str, manufacturer_id: str):
    return send_batch_to_manufacturer(batch_id, manufacturer_id)