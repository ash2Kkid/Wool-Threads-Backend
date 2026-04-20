from fastapi import APIRouter
from app.services.chatbot_service import chatbot_response

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])


@router.post("/")
def chat(customer_id: str, message: str):
    response = chatbot_response(customer_id, message)
    return {"response": response}