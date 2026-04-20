from app.core.firebase import db


def create_batch_tracking(data: dict):
    db.collection("batch_tracking").document(data["batch_id"]).set(data)


def get_farmer_batch_tracking(farmer_id: str):
    docs = (
        db.collection("batch_tracking")
        .where("farmer_id", "==", farmer_id)
        .stream()
    )
    return [doc.to_dict() for doc in docs]


def update_batch_tracking(batch_id: str, location: str, status: str):
    db.collection("batch_tracking").document(batch_id).update({
        "current_location": location,
        "status": status
    })