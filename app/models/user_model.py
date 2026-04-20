from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str  # customer / farmer / admin