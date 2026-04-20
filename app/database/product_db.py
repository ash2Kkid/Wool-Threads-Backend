from app.core.firebase import db


def add_product(product_data: dict):
    db.collection("products").document(product_data["id"]).set(product_data)


def get_all_products():
    docs = db.collection("products").stream()
    return [doc.to_dict() for doc in docs]


def get_products_by_category(category: str):
    docs = (
        db.collection("products")
        .where("category", "==", category)
        .stream()
    )
    return [doc.to_dict() for doc in docs]