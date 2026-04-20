from app.core.firebase import db


def create_customer(customer_data: dict):
    db.collection("customers").document(customer_data["id"]).set(customer_data)


def get_customer(customer_id: str):
    doc = db.collection("customers").document(customer_id).get()
    return doc.to_dict() if doc.exists else None


def get_all_customers():
    docs = db.collection("customers").stream()
    return [doc.to_dict() for doc in docs]