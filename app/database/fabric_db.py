from datetime import datetime
import uuid

def save_fabric_check(db, user_id: str, result: dict):
    doc_id = str(uuid.uuid4())

    db.collection("fabric_checks").document(doc_id).set({
        "user_id": user_id,
        "pattern": result["pattern"],
        "quality": result["quality"],
        "confidence": result["confidence"],
        "created_at": datetime.utcnow()
    })

    return doc_id