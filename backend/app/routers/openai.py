from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.langchain_service import langchain_service
from app.services.graph_service import graph_service
from app.services.prompt_builder import build_prompt

router = APIRouter(
    prefix="/v1",
    tags=["OpenAI Compatible"]
)


class Message(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = "clingraph"
    messages: List[Message]


@router.post("/chat/completions")
def chat_completions(request: ChatCompletionRequest):

    # Get the latest user message
    user_message = ""

    for message in reversed(request.messages):
        if message.role == "user":
            user_message = message.content
            break

    disease = None

    message_lower = user_message.lower()

    # Temporary hardcoded detection
    if "alzheimer" in message_lower:
        disease = "Alzheimer's disease"

    # Later we'll replace this with automatic detection

    if disease:

        graph_data = graph_service.get_disease_context(disease)

        prompt = build_prompt(
            user_question=user_message,
            graph_context=graph_data
        )

    else:

        prompt = user_message

    print("\n========== FINAL PROMPT ==========\n")
    print(prompt)
    print("\n==================================\n")

    answer = langchain_service.generate(prompt)

    return {
        "id": "chatcmpl-clingraph",
        "object": "chat.completion",
        "created": 0,
        "model": "clingraph",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": answer
                },
                "finish_reason": "stop"
            }
        ]
    }


@router.get("/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "clingraph",
                "object": "model",
                "owned_by": "ClinGraph"
            }
        ]
    }