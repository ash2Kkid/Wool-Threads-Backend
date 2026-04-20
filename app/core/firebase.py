import firebase_admin
from firebase_admin import credentials, firestore
from app.core.config import settings

# Prevent multiple initializations
if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_KEY_PATH)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()