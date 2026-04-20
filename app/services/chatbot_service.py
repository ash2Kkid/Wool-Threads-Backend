from app.database.order_db import get_orders_by_customer
from app.database.tracking_db import get_tracking


def chatbot_response(customer_id: str, message: str):

    msg = message.lower()

    if "track" in msg:
        orders = get_orders_by_customer(customer_id)
        if not orders:
            return "You have no orders to track."

        latest = orders[-1]
        tracking = get_tracking(latest["id"])

        return f"Your order is currently at {tracking['current_location']} with status: {tracking['status']}."

    if "products" in msg or "new arrivals" in msg:
        return "You can browse the latest wool products in the marketplace section."

    return "I can help with tracking orders, wool info, and marketplace support."