from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.langchain_service import langchain_service
from app.services.graph_service import graph_service
from app.services.prompt_builder import build_prompt
from app.services.entity_detector import entity_detector
from app.services.intent_detector import intent_detector
from app.services.intent_mapper import get_intent_mapping
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


    disease = entity_detector.detect(user_message)
    # Later we'll replace this with automatic detection
    intent = intent_detector.detect(user_message)

    intent_mapping = get_intent_mapping()
    
    print("\n========== ENTITY ==========")
    print(disease)

    print("\n========== INTENT ==========")
    print(intent)

    print("\n========== INTENT MAP ==========")
    print(intent_mapping)


    if disease and intent in intent_mapping:

        relationship, target_label = intent_mapping[intent]
        print("\n========== RELATIONSHIP ==========")
        print(relationship)

        print("\n========== TARGET LABEL ==========")
        print(target_label)

        graph_data = graph_service.get_relationship_context(
            disease_name=disease,
            relationship=relationship,
            target_label=target_label
        )

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
    
@router.get("/intent-test")
def intent_test(question: str):

    return {
        "question": question,
        "intent": intent_detector.detect(question)
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