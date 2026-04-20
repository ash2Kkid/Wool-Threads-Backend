from fastapi import APIRouter
from app.services.wool_batch_service import send_batch_to_warehouse

router = APIRouter(prefix="/warehouse-dispatch", tags=["Warehouse Dispatch"])


@router.post("/{batch_id}/send/{warehouse_id}")
def dispatch_to_warehouse(batch_id: str, warehouse_id: str):
    return send_batch_to_warehouse(batch_id, warehouse_id)