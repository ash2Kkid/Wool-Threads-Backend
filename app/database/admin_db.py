from app.core.firebase import db


def create_admin(admin_data: dict):
    db.collection("admins").document(admin_data["id"]).set(admin_data)


def get_admin(admin_id: str):
    doc = db.collection("admins").document(admin_id).get()
    return doc.to_dict() if doc.exists else None