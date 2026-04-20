from app.chatbot.openrouter_client import call_openrouter
from app.chatbot.prompts import SYSTEM_PROMPT

from app.database.product_db import get_all_products
from app.database.order_db import get_orders_by_customer
from app.database.tracking_db import get_tracking


# ✅ WoolThreads Identity (App Context)
APP_SUMMARY = """
WoolThreads is a wool supply chain platform that tracks wool from farm to fabric.

It helps:
- Farmers sell wool batches fairly
- Customers buy verified wool products
- Orders and shipments are traceable
- Quality and transparency improve in the wool industry
"""


# ✅ GPT Classifier (Only for random unrelated topics)
def is_allowed_topic(message: str) -> bool:

    classifier_prompt = f"""
Allowed topics:
- wool, yarn, garments, textiles
- WoolThreads app, products, orders, tracking

Question: "{message}"

Answer only YES or NO.
"""

    reply = call_openrouter(
        [{"role": "user", "content": classifier_prompt}],
        max_tokens=5
    )

    return "YES" in reply.upper()


def chatbot_response(message: str, customer_id: str = None):

    msg = message.lower().strip()

    # ✅ 0. Greetings
    if msg in ["hi", "hello", "hey"]:
        return "Hi 🧶 Ask me about wool products, tracking, or WoolThreads orders."

    # ✅ 1. WoolThreads App Info
    if "what is woolthreads" in msg or "about woolthreads" in msg:
        return APP_SUMMARY

    # ✅ 2. Wool Basic Questions Always Allowed
    if "what is wool" in msg:
        return (
            "Wool is a natural fiber from sheep (and similar animals). "
            "It is warm, breathable, and widely used in yarn, garments, and blankets."
        )

    # ✅ 3. Backend Queries First (No GPT Cost)

    # Orders
    if "my orders" in msg or "order history" in msg:
        if not customer_id:
            return "Please login first to view your orders."

        orders = get_orders_by_customer(customer_id)
        if not orders:
            return "You have not placed any orders yet."

        reply = "📦 Your recent orders:\n"
        for o in orders[:3]:
            reply += f"- {o['id']} ({o['status']})\n"
        return reply

    # Tracking
    if "track" in msg or "shipment" in msg:
        words = msg.split()
        order_id = next((w for w in words if "ord" in w.lower()), None)

        if not order_id:
            return "Please send Order ID like ORD1023."

        tracking = get_tracking(order_id.upper())

        if not tracking:
            return f"No tracking found for {order_id.upper()}."

        return (
            f"🚚 Order {order_id.upper()} is at {tracking['current_location']}.\n"
            f"Status: {tracking['status']} | ETA: {tracking['eta']}"
        )

    # Products
    if "products" in msg or "buy" in msg:
        products = get_all_products()

        if not products:
            return "No wool products available right now."

        reply = "🛍 Available products:\n"
        for p in products[:4]:
            reply += f"✅ {p['name']} — ₹{p['price']}\n"

        return reply
    
        # ✅ 3. Customer Help / Support Intents (No GPT Cost)

    # Place Order Help
    if "place order" in msg or "how to order" in msg or "buy product" in msg:
        return (
            "To place an order ✅:\n"
            "1. Open Marketplace\n"
            "2. Select a wool product\n"
            "3. Add to Cart 🛒\n"
            "4. Checkout and confirm payment\n\n"
            "Your shipment will appear in Tracking 🚚."
        )

    # Checkout / Payment Help
    if "checkout" in msg or "payment" in msg:
        return (
            "Checkout is simple ✅\n"
            "After adding items to Cart, tap Checkout.\n"
            "You’ll see delivery details + payment options."
        )

    # Delivery / ETA Help
    if "eta" in msg or "delivery time" in msg or "when will it arrive" in msg:
        return (
            "ETA means Estimated Time of Arrival 🚚\n"
            "It tells when your wool shipment is expected to reach you."
        )

    # Return / Refund Help
    if "return" in msg or "refund" in msg or "cancel order" in msg:
        return (
            "Returns depend on product type.\n"
            "Raw wool orders usually can’t be returned once shipped.\n"
            "Finished garments may support return within a limited period."
        )

    # Recommendation: Best Wool for Clothing
    if "best wool" in msg or "which wool" in msg or "recommend" in msg:
        return (
            "Here are good choices 🧶:\n"
            "✅ Merino — soft, premium, best for clothing\n"
            "✅ Alpaca — warmer and silky\n"
            "✅ Cashmere — luxury, very soft\n"
            "✅ Mohair — strong and shiny\n\n"
            "Tell me what you want to make (sweater, blanket, yarn)!"
        )

    # Contact Support
    if "support" in msg or "contact" in msg or "helpdesk" in msg:
        return (
            "For support 📞:\n"
            "You can contact WoolThreads through the app Support section.\n"
            "Soon we’ll add WhatsApp + Call support for faster help."
        )

    # ✅ 4. Classify Only Unknown Random Queries
    allowed = is_allowed_topic(message)

    if not allowed:
        return "I can only help with wool, WoolThreads products, orders, and tracking 🧶."

    # ✅ 5. GPT Response for Wool Education
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT + APP_SUMMARY},
        {"role": "user", "content": message},
    ]

    return call_openrouter(messages)