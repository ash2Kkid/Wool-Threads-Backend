from fastapi import APIRouter
from app.services.analytics_service import get_platform_stats
from app.services.admin_service import (
    get_all_farmers,
    get_all_customers,
    get_all_products,
    get_all_orders,
    get_all_shipments,
    search_products,
    get_orders_by_status
)

router = APIRouter(prefix="/admin", tags=["Admin Monitoring"])


# ✅ DASHBOARD STATS
@router.get("/stats")
def stats():
    return get_platform_stats()


# ✅ FARMERS LIST
@router.get("/farmers")
def farmers():
    return get_all_farmers()


# ✅ CUSTOMERS LIST
@router.get("/customers")
def customers():
    return get_all_customers()


# ✅ PRODUCTS LIST
@router.get("/products")
def products():
    return get_all_products()


# ✅ SEARCH PRODUCTS
@router.get("/products/search")
def product_search(q: str):
    return search_products(q)


# ✅ ORDERS LIST
@router.get("/orders")
def orders():
    return get_all_orders()


# ✅ ORDERS FILTER BY STATUS
@router.get("/orders/status/{status}")
def orders_by_status(status: str):
    return get_orders_by_status(status)


# ✅ TRACK ALL SHIPMENTS
@router.get("/shipments")
def shipments():
    return get_all_shipments()