from fastapi import APIRouter
from app.services.auth_service import login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(user_id: str, role: str):
    return login_user(user_id, role)