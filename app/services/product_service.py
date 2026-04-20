from app.database.product_db import add_product, get_all_products


def create_product(product):
    add_product(product.dict())
    return {"message": "Product added successfully"}


def fetch_products():
    return get_all_products()