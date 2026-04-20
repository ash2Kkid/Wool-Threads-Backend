from app.core.firebase import db


def create_tracking(tracking_data: dict):
    db.collection("tracking").document(tracking_data["order_id"]).set(tracking_data)


def get_tracking(order_id: str):
    doc = db.collection("tracking").document(order_id).get()
    return doc.to_dict() if doc.exists else None


def update_tracking(order_id: str, location: str, status: str):
    db.collection("tracking").document(order_id).update({
        "current_location": location,
        "status": status
    })