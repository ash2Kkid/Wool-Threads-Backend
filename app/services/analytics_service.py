from app.core.firebase import db
from app.database.customer_db import get_all_customers
from app.database.farmer_db import get_all_farmers


def get_platform_stats():
    customers = len(get_all_customers())
    farmers = len(get_all_farmers())
    products = len(list(db.collection("products").stream()))
    orders = len(list(db.collection("orders").stream()))
    shipments = len(list(db.collection("tracking").stream()))

    return {
        "total_customers": customers,
        "total_farmers": farmers,
        "total_products": products,
        "total_orders": orders,
        "active_shipments": shipments
    }
