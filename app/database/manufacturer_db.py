from app.core.firebase import db


def get_all_manufacturers():
    docs = db.collection("manufacturers").stream()
    return [doc.to_dict() for doc in docs]