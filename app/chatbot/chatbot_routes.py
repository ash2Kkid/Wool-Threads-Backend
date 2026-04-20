from fastapi import APIRouter
from pydantic import BaseModel
from app.chatbot.chatbot_service import chatbot_response

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])


class ChatRequest(BaseModel):
    message: str
    customer_id: str | None = None


@router.post("/")
def chat(req: ChatRequest):
    reply = chatbot_response(req.message, req.customer_id)
    return {"response": reply}