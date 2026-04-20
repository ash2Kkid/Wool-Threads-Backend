from app.core.firebase import db


def create_batch(batch_data: dict):
    db.collection("wool_batches").document(batch_data["id"]).set(batch_data)


def get_batch(batch_id: str):
    doc = db.collection("wool_batches").document(batch_id).get()
    return doc.to_dict() if doc.exists else None


def get_batches_by_farmer(farmer_id: str):
    docs = (
        db.collection("wool_batches")
        .where("farmer_id", "==", farmer_id)
        .stream()
    )
    return [doc.to_dict() for doc in docs]

def assign_batch(batch_id: str, manufacturer_id: str):
    db.collection("wool_batches").document(batch_id).update({
        "assigned_to": manufacturer_id,
        "status": "sent_to_manufacturer"
    })

from app.core.firebase import db

def save_batch(batch_data: dict):
    db.collection("wool_batches").document(batch_data["id"]).set(batch_data)