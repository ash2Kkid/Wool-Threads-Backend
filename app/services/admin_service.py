from app.core.firebase import db
from app.database.customer_db import get_all_customers as fetch_all_customers
from app.database.customer_db import get_customer
from app.database.farmer_db import get_all_farmers as fetch_all_farmers
from app.database.farmer_db import get_farmer


# ----------------------------
# FARMER MONITORING
# ----------------------------

def get_all_farmers():
    return fetch_all_farmers()


def get_farmer_by_id(farmer_id: str):
    return get_farmer(farmer_id)


# ----------------------------
# CUSTOMER MONITORING
# ----------------------------

def get_all_customers():
    return fetch_all_customers()


def get_customer_by_id(customer_id: str):
    return get_customer(customer_id)


# ----------------------------
# PRODUCT MONITORING
# ----------------------------

def get_all_products():
    docs = db.collection("products").stream()
    return [doc.to_dict() for doc in docs]


def search_products(keyword: str):
    docs = db.collection("products").stream()

    results = []
    keyword = keyword.lower()

    for doc in docs:
        product = doc.to_dict()
        if keyword in product["name"].lower():
            results.append(product)

    return results


# ----------------------------
# ORDER MONITORING
# ----------------------------

def get_all_orders():
    docs = db.collection("orders").stream()
    return [doc.to_dict() for doc in docs]


def get_orders_by_status(status: str):
    docs = (
        db.collection("orders")
        .where("status", "==", status)
        .stream()
    )
    return [doc.to_dict() for doc in docs]


# ----------------------------
# TRACKING MONITORING
# ----------------------------

def get_all_shipments():
    docs = db.collection("tracking").stream()
    return [doc.to_dict() for doc in docs]
