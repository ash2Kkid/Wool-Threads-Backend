from fastapi import HTTPException
from firebase_admin import firestore
from app.core.firebase import db
from app.database.farmer_db import get_farmer, update_farmer_stats
from app.database.product_db import add_product, get_all_products
from app.database.wool_batch_db import get_batch


def _manufacturer_exists(manufacturer_id: str) -> bool:
    doc = db.collection("manufacturers").document(manufacturer_id).get()
    if doc.exists:
        return True

    docs = (
        db.collection("manufacturers")
        .where("id", "==", manufacturer_id)
        .limit(1)
        .stream()
    )
    return any(True for _ in docs)


def create_product(product):
    product_data = product.dict()

    image = product_data.get("image") or product_data.get("imageUrl")
    if not image:
        raise HTTPException(status_code=400, detail="Product image is required")

    product_data["image"] = image
    product_data.pop("imageUrl", None)

    supplier_type = product_data.get("supplier_type")
    supplier_id = product_data.get("supplier_id")
    if supplier_type:
        supplier_type = supplier_type.lower()
        product_data["supplier_type"] = supplier_type

    if supplier_type and not supplier_id:
        raise HTTPException(status_code=400, detail="supplier_id is required when supplier_type is set")

    if supplier_type == "farmer":
        if not get_farmer(supplier_id):
            raise HTTPException(status_code=404, detail="Farmer not found")
    elif supplier_type == "manufacturer":
        if not _manufacturer_exists(supplier_id):
            raise HTTPException(status_code=404, detail="Manufacturer not found")
    elif supplier_type is not None:
        raise HTTPException(status_code=400, detail="supplier_type must be either farmer or manufacturer")

    batch_id = product_data.get("batch_id")
    if batch_id and not get_batch(batch_id):
        raise HTTPException(status_code=404, detail="Batch not found")

    add_product(product_data)

    if supplier_type == "farmer":
        update_farmer_stats(supplier_id, {
            "total_products": firestore.Increment(1)
        })

    return {"message": "Product added successfully"}


def fetch_products():
    return get_all_products()
