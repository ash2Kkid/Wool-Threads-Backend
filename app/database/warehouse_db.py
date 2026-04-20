from app.core.firebase import db


def get_all_warehouses():
    docs = db.collection("warehouses").stream()
    return [doc.to_dict() for doc in docs]


def add_warehouse(data: dict):
    db.collection("warehouses").document(data["id"]).set(data)


def get_nearby_warehouses(city: str):
    docs = (
        db.collection("warehouses")
        .where("city", "==", city)
        .stream()
    )
    return [doc.to_dict() for doc in docs]