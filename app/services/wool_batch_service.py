import uuid
from app.core.firebase import db
from fastapi import HTTPException
from app.database.wool_batch_db import create_batch
from app.database.wool_batch_db import assign_batch, get_batch
from app.database.manufacturer_db import get_all_manufacturers
from app.database.revenue_db import record_farmer_payment
from datetime import datetime

from app.database.batch_tracking_db import create_batch_tracking
from app.database.warehouse_db import get_all_warehouses
from app.models.wool_batch_model import WoolBatch



def send_batch_to_manufacturer(batch_id: str, manufacturer_id: str):

    batch = get_batch(batch_id)

    # ✅ Prevent crash
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")

    qty = batch["quantity_kg"]

    # ✅ Find Manufacturer
    manufacturers = get_all_manufacturers()
    manu = next((m for m in manufacturers if m["id"] == manufacturer_id), None)

    if not manu:
        raise HTTPException(status_code=404, detail="Manufacturer not found")

    price = manu["price_per_kg"]

    # ✅ Timeline Update
    history = batch.get("history", [])

    # Add first step if empty
    if len(history) == 0:
        history.append({
            "status": "available",
            "time": datetime.utcnow().isoformat()
        })

    # Add sent step
    history.append({
        "status": "sent_to_manufacturer",
        "time": datetime.utcnow().isoformat(),
        "manufacturer_id": manufacturer_id,
        "manufacturer_name": manu["name"]
    })

    # ✅ Assign batch (status update)
    assign_batch(batch_id, manufacturer_id)

    # ✅ Save status + timeline in Firestore
    db.collection("wool_batches").document(batch_id).update({
        "status": "sent_to_manufacturer",
        "assigned_to": manufacturer_id,
        "history": history
    })

    # ✅ Revenue record
    record_farmer_payment({
        "farmer_id": batch["farmer_id"],
        "batch_id": batch_id,
        "manufacturer_id": manufacturer_id,
        "amount": qty * price,
        "status": "pending",

        # ✅ Date (optional future analytics)
        "created_at": datetime.utcnow().isoformat(),

        # ✅ Market benchmark placeholder
        "expected_market_price": qty * 400
    })

    create_batch_tracking({
    "batch_id": batch_id,
    "farmer_id": batch["farmer_id"],
    "current_location": "Farmer Collection Center",
    "status": "Dispatched to Buyer",
    "eta": "3-5 days"
})

    return {
        "message": "✅ Batch sent successfully",
        "batch_id": batch_id,
        "manufacturer": manu["name"],
        "timeline_updated": True
    }


def send_batch_to_warehouse(batch_id: str, warehouse_id: str):

    batch = get_batch(batch_id)

    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")

    # ✅ Find warehouse
    warehouses = get_all_warehouses()
    wh = next((w for w in warehouses if w["id"] == warehouse_id), None)

    if not wh:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    # ✅ Timeline history update
    history = batch.get("history", [])

    history.append({
        "status": "sent_to_warehouse",
        "time": datetime.utcnow().isoformat(),
        "warehouse_id": warehouse_id,
        "warehouse_name": wh["name"]
    })

    # ✅ Update batch document
    db.collection("wool_batches").document(batch_id).update({
        "status": "sent_to_warehouse",
        "warehouse_id": warehouse_id,
        "history": history
    })

    # ✅ Tracking entry starts here
    create_batch_tracking({
        "batch_id": batch_id,
        "farmer_id": batch["farmer_id"],
        "current_location": wh["name"],
        "status": "Arriving at Warehouse",
        "eta": "1-2 days"
    })

    return {
        "message": "✅ Batch sent to Warehouse successfully",
        "warehouse": wh["name"]
    }




def register_batch(batch: WoolBatch):
    batch_data = batch.dict()

    # ✅ Auto ID
    batch_data["id"] = "BATCH-" + uuid.uuid4().hex[:5].upper()

    create_batch(batch_data)

    return {"message": "Batch created", "batch": batch_data}

from app.database.wool_batch_db import get_batches_by_farmer

def fetch_farmer_batches(farmer_id: str):
    return get_batches_by_farmer(farmer_id)