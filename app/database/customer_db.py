from app.core.firebase import db


def create_customer(customer_data: dict):
    db.collection("customers").document(customer_data["id"]).set(customer_data)


def get_customer_ref(customer_id: str):
    customer_ref = db.collection("customers").document(customer_id)
    if customer_ref.get().exists:
        return customer_ref

    user_ref = db.collection("users").document(customer_id)
    user_doc = user_ref.get()
    if user_doc.exists and user_doc.to_dict().get("role") == "customer":
        return user_ref

    return None


def update_customer_stats(customer_id: str, updates: dict) -> bool:
    customer_ref = get_customer_ref(customer_id)
    if customer_ref is None:
        return False

    customer_ref.update(updates)
    return True


def get_customer(customer_id: str):
    customer_doc = db.collection("customers").document(customer_id).get()
    if customer_doc.exists:
        return customer_doc.to_dict()

    user_doc = db.collection("users").document(customer_id).get()
    if not user_doc.exists:
        return None

    user_data = user_doc.to_dict()
    if user_data.get("role") != "customer":
        return None

    return {
        "id": customer_id,
        "name": user_data.get("name", "Customer"),
        "email": user_data.get("email"),
        "phone": user_data.get("phone"),
        "address": user_data.get("address")
        or f"{user_data.get('location', '')} - {user_data.get('pincode', '')}".strip(" -"),
        "location": user_data.get("location"),
        "pincode": user_data.get("pincode"),
        "total_orders": user_data.get("total_orders", 0),
    }


def get_all_customers():
    customers = {doc.id: doc.to_dict() for doc in db.collection("customers").stream()}

    user_docs = (
        db.collection("users")
        .where("role", "==", "customer")
        .stream()
    )
    for doc in user_docs:
        customers.setdefault(doc.id, get_customer(doc.id))

    return list(customers.values())
