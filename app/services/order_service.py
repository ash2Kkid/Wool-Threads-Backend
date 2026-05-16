from datetime import datetime
from firebase_admin import firestore
from app.core.firebase import db
from app.database.customer_db import get_customer
from app.database.product_db import get_product
from app.database.order_db import create_order
from app.database.tracking_db import create_tracking
from app.database.wool_batch_db import get_batch


def _resolve_farmer_ids(items: list[dict]) -> list[str]:
    farmer_ids: set[str] = set()

    for item in items:
        product = get_product(item["product_id"])
        if not product:
            continue

        if product.get("supplier_type") == "farmer" and product.get("supplier_id"):
            farmer_ids.add(product["supplier_id"])
            continue

        batch_id = product.get("batch_id")
        if batch_id:
            batch = get_batch(batch_id)
            if batch and batch.get("farmer_id"):
                farmer_ids.add(batch["farmer_id"])

    return sorted(farmer_ids)


def place_order(order):
    """
    Customer places order → Order saved → Tracking auto-created.
    """

    order_data = order.dict()
    order_data["farmer_ids"] = _resolve_farmer_ids(order_data["items"])

    # ✅ Save order (creates UUID inside create_order)
    saved_order = create_order(order_data)

    # ✅ Auto-create tracking linked to SAME UUID
    create_tracking({
        "order_id": saved_order["id"],   # ✅ same ID
        "status": "order_received",

        "current_location": "Processing Center",
        "eta": "3-5 days",

        # ✅ Chennai coordinates
        "lat": 13.0827,
        "lng": 80.2707,

        "updated_at": datetime.utcnow().isoformat()
    })

    customer = get_customer(saved_order["customer_id"])
    if customer:
        db.collection("customers").document(saved_order["customer_id"]).update({
            "total_orders": firestore.Increment(1)
        })

    # ✅ Return proper order object
    return saved_order
