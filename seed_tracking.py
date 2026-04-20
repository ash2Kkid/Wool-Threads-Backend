from app.core.firebase import db

def seed_tracking():
    sample = {
        "order_id": "ORD1023",
        "status": "in_transit",
        "current_location": "Hyderabad Hub",
        "eta": "2 Days",

        # ✅ Add map coordinates
        "lat": 17.3850,
        "lng": 78.4867
    }

    db.collection("tracking").document("ORD1023").set(sample)

    print("✅ Tracking seeded successfully!")

if __name__ == "__main__":
    seed_tracking()