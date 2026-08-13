from langchain_groq import ChatGroq
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.core.config import settings
from app.services.tool_service import fetchSimilarQueries, neo4jQuery


class LangChainService:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0
        )

        self.tools = [
            fetchSimilarQueries,
            neo4jQuery
        ]

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
You are ClinGraph, a biomedical knowledge graph assistant.

You have access to two tools:

1. fetchSimilarQueries
   Retrieves previously validated biomedical questions,
   Cypher queries, Neo4j responses, and answers.

2. neo4jQuery
   Executes Cypher queries against the Neo4j knowledge graph.

IMPORTANT:

- You decide autonomously which tools are needed.
- You may use fetchSimilarQueries.
- You may use neo4jQuery.
- You may use both.
- You may use neither when the question does not require the graph.
- Do NOT assume that fetchSimilarQueries must always be called first.
- When using the knowledge graph, rely on the actual Neo4j result.
- Do not invent node labels, relationship types, or properties.
- Use retrieved examples to understand the actual graph schema.
- Do not expose Cypher queries or internal tool calls to the user.
- Give a concise final answer.
"""
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        self.agent = create_tool_calling_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )

        self.executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            max_iterations=5,
            handle_parsing_errors=True
        )

    def generate(
        self,
        user_question: str,
        chat_history=None
    ):

        if chat_history is None:
            chat_history = []

        result = self.executor.invoke({
            "input": user_question,
            "chat_history": chat_history
        })

        return result["output"]


langchain_service = LangChainService()