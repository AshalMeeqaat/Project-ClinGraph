from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ollama_service import ollama_service

router = APIRouter(
    prefix="/llm",
    tags=["LLM"]
)


class PromptRequest(BaseModel):
    prompt: str


@router.post("/chat")
def chat(request: PromptRequest):

    answer = ollama_service.generate(
        request.prompt
    )

    return {
        "response": answer
    }