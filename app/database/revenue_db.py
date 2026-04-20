from app.core.firebase import db


def record_farmer_payment(data: dict):
    db.collection("revenues").add(data)
    return data


def get_farmer_revenues(farmer_id: str):
    docs = (
        db.collection("revenues")
        .where("farmer_id", "==", farmer_id)
        .stream()
    )
    return [doc.to_dict() for doc in docs]