from app.core.firebase import db


def log_event(event_data: dict):
    db.collection("analytics").add(event_data)


def get_all_events():
    docs = db.collection("analytics").stream()
    return [doc.to_dict() for doc in docs]