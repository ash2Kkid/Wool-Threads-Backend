from app.core.firebase import db


def create_farmer(farmer_data: dict):
    db.collection("farmers").document(farmer_data["id"]).set(farmer_data)


def get_farmer_ref(farmer_id: str):
    farmer_ref = db.collection("farmers").document(farmer_id)
    if farmer_ref.get().exists:
        return farmer_ref

    user_ref = db.collection("users").document(farmer_id)
    user_doc = user_ref.get()
    if user_doc.exists and user_doc.to_dict().get("role") == "farmer":
        return user_ref

    return None


def update_farmer_stats(farmer_id: str, updates: dict) -> bool:
    farmer_ref = get_farmer_ref(farmer_id)
    if farmer_ref is None:
        return False

    farmer_ref.update(updates)
    return True


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
    farmers = {doc.id: doc.to_dict() for doc in db.collection("farmers").stream()}

    user_docs = (
        db.collection("users")
        .where("role", "==", "farmer")
        .stream()
    )
    for doc in user_docs:
        farmers.setdefault(doc.id, get_farmer(doc.id))

    return list(farmers.values())
