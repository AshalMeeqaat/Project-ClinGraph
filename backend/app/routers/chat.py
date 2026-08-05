from fastapi import APIRouter
from pydantic import BaseModel

from app.services.langchain_service import langchain_service
from app.services.graph_service import graph_service
from app.services.prompt_builder import build_prompt

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat(request: ChatRequest):

    message = request.message

    disease = None

    if "alzheimer" in message.lower():
        disease = "Alzheimer's disease"

    if disease:

        graph_data = graph_service.get_disease_context(disease)

        prompt = build_prompt(
            user_question=message,
            graph_context=graph_data
        )

    else:

        prompt = message

    answer = langchain_service.generate(prompt)

    return {
        "answer": answer
    }