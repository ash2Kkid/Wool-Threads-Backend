from pydantic import BaseModel


class Notification(BaseModel):
    id: str
    user_id: str

    title: str
    message: str

    created_at: str