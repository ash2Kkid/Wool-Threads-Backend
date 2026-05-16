from fastapi import HTTPException
from app.database.admin_db import get_admin
from app.database.customer_db import get_customer
from app.database.farmer_db import get_farmer
from app.database.user_db import get_user
from app.core.security import create_access_token


def _resolve_user_for_role(user_id: str, role: str):
    user = get_user(user_id)
    if user:
        stored_role = user.get("role") or user.get("userType")
        if stored_role and stored_role != role:
            raise HTTPException(status_code=403, detail="Role mismatch for this user")
        return user

    if role == "customer":
        return get_customer(user_id)
    if role == "farmer":
        return get_farmer(user_id)
    if role == "admin":
        return get_admin(user_id)
    return None


def login_user(user_id: str, role: str):
    """
    Generates JWT token for any user role.
    """
    role = role.lower().strip()
    if role not in {"customer", "farmer", "admin"}:
        raise HTTPException(status_code=400, detail="Invalid role")

    user = _resolve_user_for_role(user_id, role)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    token = create_access_token({
        "user_id": user_id,
        "role": role
    })

    return {"access_token": token, "token_type": "bearer"}
