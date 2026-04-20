from fastapi import APIRouter
from app.services.analytics_service import get_platform_stats

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/stats")
def stats():
    return get_platform_stats()