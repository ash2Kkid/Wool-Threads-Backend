from app.core.firebase import db
import uuid


import uuid
from datetime import datetime
from app.core.firebase import db


def create_order(order_data: dict):
    # ✅ Generate ID
    order_id = str(uuid.uuid4())
    order_data["id"] = order_id

    # ✅ Add created timestamp
    order_data["created_at"] = datetime.utcnow().isoformat()

    # ✅ Save to Firestore
    db.collection("orders").document(order_id).set(order_data)

    # ✅ Return saved order correctly
    return order_data


def get_order(order_id: str):
    doc = db.collection("orders").document(order_id).get()
    return doc.to_dict() if doc.exists else None


def get_orders_by_customer(customer_id: str):
    docs = (
        db.collection("orders")
        .where("customer_id", "==", customer_id)
        .stream()
    )
    return [doc.to_dict() for doc in docs]


def update_order_status(order_id: str, status: str):
    db.collection("orders").document(order_id).update({"status": status})

def get_orders_by_farmer(farmer_id: str):
    docs = (
        db.collection("orders")
        .where("farmer_id", "==", farmer_id)
        .stream()
    )
    return [doc.to_dict() for doc in docs]