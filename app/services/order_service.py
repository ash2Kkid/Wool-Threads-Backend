from datetime import datetime
from app.database.order_db import create_order
from app.database.tracking_db import create_tracking


def place_order(order):
    """
    Customer places order → Order saved → Tracking auto-created.
    """

    # ✅ Save order (creates UUID inside create_order)
    saved_order = create_order(order.dict())

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

    # ✅ Return proper order object
    return saved_order