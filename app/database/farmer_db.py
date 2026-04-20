from app.core.firebase import db


def create_farmer(farmer_data: dict):
    db.collection("farmers").document(farmer_data["id"]).set(farmer_data)


def get_farmer(farmer_id: str):
    doc = db.collection("farmers").document(farmer_id).get()
    return doc.to_dict() if doc.exists else None


def get_all_farmers():
    docs = db.collection("farmers").stream()
    return [doc.to_dict() for doc in docs]