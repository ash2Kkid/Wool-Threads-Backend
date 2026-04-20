from fastapi import APIRouter
from app.models.product_model import Product
from app.services.product_service import create_product, fetch_products

router = APIRouter(prefix="/products", tags=["Products"])


# ✅ Customer Marketplace Products
@router.get("/")
def all_products():
    return fetch_products()


# ✅ Farmer/Admin Add Product
@router.post("/")
def add_product(product: Product):
    return create_product(product)