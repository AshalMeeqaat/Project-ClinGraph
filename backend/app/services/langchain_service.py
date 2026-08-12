from langchain_groq import ChatGroq

from app.core.config import settings
from app.services.tool_service import fetchSimilarQueries, neo4jQuery


class LangChainService:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0
        )

        self.tools = {
            "fetchSimilarQueries": fetchSimilarQueries,
            "neo4jQuery": neo4jQuery
        }

        self.llm_with_tools = self.llm.bind_tools(
            list(self.tools.values())
        )

    def generate(self, prompt: str):

        messages = [
            ("system", """
    You are ClinGraph, a biomedical knowledge graph assistant.

    You have two tools:

    1. fetchSimilarQueries:
    Retrieves similar previously validated biomedical questions,
    their Cypher queries, Neo4j responses, and ideal answers.

    2. neo4jQuery:
    Executes Cypher queries against the Neo4j knowledge graph.

    When answering a graph-related question:
    - First use fetchSimilarQueries to find relevant examples.
    - Use those examples to construct an appropriate Cypher query.
    - Then use neo4jQuery to retrieve the actual graph data.
    - Finally answer the user using the Neo4j result.
    """),
            ("user", prompt)
        ]

        while True:

            response = self.llm_with_tools.invoke(messages)

            if not response.tool_calls:
                return response.content

            messages.append(response)

            for tool_call in response.tool_calls:

                tool_name = tool_call["name"]
                tool_args = tool_call["args"]

                tool = self.tools[tool_name]

                tool_result = tool.invoke(tool_args)

                messages.append({
                    "role": "tool",
                    "content": str(tool_result),
                    "tool_call_id": tool_call["id"]
                })


langchain_service = LangChainService()