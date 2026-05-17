from app.core.firebase import db


def create_farmer(farmer_data: dict):
    db.collection("farmers").document(farmer_data["id"]).set(farmer_data)


def get_farmer(farmer_id: str):
    farmer_doc = db.collection("farmers").document(farmer_id).get()
    if farmer_doc.exists:
        return farmer_doc.to_dict()

    user_doc = db.collection("users").document(farmer_id).get()
    if not user_doc.exists:
        return None

    user_data = user_doc.to_dict()
    if user_data.get("role") != "farmer":
        return None

    return {
        "id": farmer_id,
        "name": user_data.get("name", "Farmer"),
        "email": user_data.get("email"),
        "farm_name": user_data.get("farm_name") or user_data.get("name", "Farmer"),
        "location": user_data.get("location", "Location unavailable"),
        "phone": user_data.get("phone"),
        "pincode": user_data.get("pincode"),
        "total_batches": user_data.get("total_batches", 0),
        "total_products": user_data.get("total_products", 0),
        "total_earnings": user_data.get("total_earnings", 0.0),
    }


def get_all_farmers():
    docs = db.collection("farmers").stream()
    return [doc.to_dict() for doc in docs]
