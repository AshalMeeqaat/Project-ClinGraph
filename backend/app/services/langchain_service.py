from langchain_groq import ChatGroq

from app.core.config import settings


class LangChainService:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0
        )

    def generate(self, prompt: str):

        response = self.llm.invoke(prompt)

        return response.content


langchain_service = LangChainService()