from pydantic import BaseModel, EmailStr


class Admin(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str = "admin"