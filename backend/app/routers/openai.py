from fastapi import APIRouter, HTTPException
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

    # Get the latest user message
    user_message = ""

    for message in reversed(request.messages):
        if message.role == "user":
            user_message = message.content
            break

    if not user_message:
        raise HTTPException(
            status_code=400,
            detail="No user message was provided."
        )

    print("\n========== USER QUESTION ==========")
    print(user_message)

    try:
        answer = langchain_service.generate(user_message)

    except Exception as exc:
        print("\n========== LLM ERROR ==========")
        print(exc)

        raise HTTPException(
            status_code=503,
            detail="ClinGraph is temporarily unavailable. Please try again later."
        )

    print("\n========== FINAL ANSWER ==========")
    print(answer)

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

    if not question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

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

    if not question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        answer = langchain_service.generate(question)

    except Exception as exc:
        print("\n========== TOOL ERROR ==========")
        print(exc)

        raise HTTPException(
            status_code=503,
            detail="ClinGraph is temporarily unavailable. Please try again later."
        )

    return {
        "question": question,
        "answer": answer
    }