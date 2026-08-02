from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ollama_service import ollama_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chat(request: ChatRequest):

    answer = ollama_service.generate(
        request.message
    )

    return {
        "answer": answer
    }