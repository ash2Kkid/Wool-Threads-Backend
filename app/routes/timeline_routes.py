from fastapi import APIRouter, HTTPException
from app.database.wool_batch_db import get_batch

router = APIRouter(prefix="/timeline", tags=["Timeline"])


@router.get("/{batch_id}")
def batch_timeline(batch_id: str):

    batch = get_batch(batch_id)

    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")

    return {
        "batch_id": batch_id,
        "history": batch.get("history", [])
    }