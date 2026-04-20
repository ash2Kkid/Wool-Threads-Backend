from app.core.firebase import db


# ----------------------------
# FARMER MONITORING
# ----------------------------

def get_all_farmers():
    docs = db.collection("farmers").stream()
    return [doc.to_dict() for doc in docs]


def get_farmer_by_id(farmer_id: str):
    doc = db.collection("farmers").document(farmer_id).get()
    return doc.to_dict() if doc.exists else None


# ----------------------------
# CUSTOMER MONITORING
# ----------------------------

def get_all_customers():
    docs = db.collection("customers").stream()
    return [doc.to_dict() for doc in docs]


def get_customer_by_id(customer_id: str):
    doc = db.collection("customers").document(customer_id).get()
    return doc.to_dict() if doc.exists else None


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