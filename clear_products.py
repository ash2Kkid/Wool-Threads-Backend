from app.core.firebase import db

def clear_products():
    products_ref = db.collection("products")
    docs = products_ref.stream()

    count = 0
    for doc in docs:
        products_ref.document(doc.id).delete()
        count += 1

    print(f"✅ Deleted {count} products from Firestore!")

if __name__ == "__main__":
    clear_products()