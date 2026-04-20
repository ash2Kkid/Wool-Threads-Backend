from app.core.firebase import db


def get_user(user_id: str):
    doc = db.collection("users").document(user_id).get()
    return doc.to_dict() if doc.exists else None


def create_user(user_data: dict):
    db.collection("users").document(user_data["id"]).set(user_data)


def delete_user(user_id: str):
    db.collection("users").document(user_id).delete()