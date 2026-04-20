from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Import routers
from app.routes.auth_routes import router as auth_router
from app.routes.customer_routes import router as customer_router
from app.routes.farmer_routes import router as farmer_router
from app.routes.admin_routes import router as admin_router

from app.routes.product_routes import router as product_router
from app.routes.wool_batch_routes import router as batch_router
from app.routes.order_routes import router as order_router
from app.routes.tracking_routes import router as tracking_router

from app.routes.analytics_routes import router as analytics_router
from app.routes.chatbot_routes import router as chatbot_router
from app.routes.manufacturer_routes import router as manufacturer_router
from app.routes.revenue_routes import router as revenue_router
from app.routes.timeline_routes import router as timeline_router
from app.routes.batch_tracking_routes import router as farmer_tracking_router
from app.routes.warehouse_routes import router as warehouse_router
from app.routes.warehouse_dispatch_routes import router as warehouse_dispatch_router
from app.chatbot.chatbot_routes import router as chatbot_router
from app.routes.fabric_routes import router as fabric_router
from app.api.quality_control import router as qc_router









app = FastAPI(
    title="Wool Supply Chain Backend",
    version="1.0.0"
)

# ✅ CORS (Flutter will call this backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register all routers
app.include_router(auth_router)

app.include_router(customer_router)
app.include_router(farmer_router)
app.include_router(admin_router)

app.include_router(product_router)
app.include_router(batch_router)

app.include_router(order_router)
app.include_router(tracking_router)

app.include_router(analytics_router)
app.include_router(chatbot_router)
app.include_router(manufacturer_router)
app.include_router(revenue_router)
app.include_router(timeline_router)
app.include_router(farmer_tracking_router)
app.include_router(warehouse_router)
app.include_router(warehouse_dispatch_router)
app.include_router(fabric_router)

app.include_router(chatbot_router)
app.include_router(qc_router)

@app.get("/")
def root():
    return {
        "message": "✅ Wool Backend Running Successfully",
        "status": "ok"
    }