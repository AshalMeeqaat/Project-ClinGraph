from fastapi import APIRouter

from app.services.langchain_service import langchain_service

router = APIRouter(
    prefix="/groq",
    tags=["Groq Test"]
)


@router.get("/test")
def test():

    answer = langchain_service.generate(
        "What is diabetes?"
    )

    return {
        "answer": answer
    }