import firebase_admin
from firebase_admin import credentials, firestore
from app.core.config import settings
import os
import json

# Prevent multiple initializations
if not firebase_admin._apps:
    
    if os.getenv("FIREBASE_KEY"):
        # ✅ Production (Render)
        firebase_key = json.loads(os.environ["FIREBASE_KEY"])
        cred = credentials.Certificate(firebase_key)
    else:
        # ✅ Local development
        cred = credentials.Certificate(settings.FIREBASE_KEY_PATH)

    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()