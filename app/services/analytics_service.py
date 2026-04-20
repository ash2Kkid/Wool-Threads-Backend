from app.core.firebase import db


def get_platform_stats():
    customers = len(list(db.collection("customers").stream()))
    farmers = len(list(db.collection("farmers").stream()))
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