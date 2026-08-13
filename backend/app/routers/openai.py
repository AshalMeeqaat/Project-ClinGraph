from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.langchain_service import langchain_service
from app.services.similar_query_service import similar_query_service


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

    # Get latest user message
    user_message = ""

    for message in reversed(request.messages):

        if message.role == "user":
            user_message = message.content
            break

    if not user_message:

        return {
            "error": "No user message provided"
        }

    # New tool-based RAG pipeline
    answer = langchain_service.generate(user_message)

    return {
        "id": "chatcmpl-clingraph",
        "object": "chat.completion",
        "created": 0,
        "model": request.model,
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


@router.get("/similar-query-test")
def similar_query_test(question: str):

    results = similar_query_service.fetch_similar_queries(
        question,
        k=3
    )

    return {
        "question": question,
        "results": results
    }


@router.get("/tool-test")
def tool_test(question: str):

    answer = langchain_service.generate(question)

    return {
        "question": question,
        "answer": answer
    }