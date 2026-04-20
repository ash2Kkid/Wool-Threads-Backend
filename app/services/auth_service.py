from app.core.security import create_access_token


def login_user(user_id: str, role: str):
    """
    Generates JWT token for any user role.
    """

    token = create_access_token({
        "user_id": user_id,
        "role": role
    })

    return {"access_token": token, "token_type": "bearer"}