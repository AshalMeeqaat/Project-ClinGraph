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
   Retrieves previously validated biomedical questions, Cypher queries,
   Neo4j responses, and answers.

2. neo4jQuery
   Executes Cypher queries against the Neo4j knowledge graph.

IMPORTANT TOOL USAGE RULES:

- You decide autonomously which tools are needed.
- You may use fetchSimilarQueries.
- You may use neo4jQuery.
- You may use both.
- You may use neither when the question does not require the graph.

KNOWLEDGE GRAPH RULES:

- For any question that requires information from the knowledge graph,
  call fetchSimilarQueries BEFORE calling neo4jQuery.
- The results returned by fetchSimilarQueries are the authoritative
  reference for the graph schema.
- NEVER invent a node label.
- NEVER invent a relationship type.
- NEVER invent a property name.
- NEVER substitute a different node label or relationship type based
  on general biomedical knowledge.
- You MUST copy the node labels, relationship types, and property
  structure from the most relevant retrieved example.
- You may ONLY change the entity value needed to answer the user's
  question.
- Do NOT change the schema of the retrieved query.

For example, if the retrieved example contains:

MATCH (c:Compound)-[:TREATS]->(d:Disease)
WHERE d.name = "hypertension"
RETURN c.name
ORDER BY c.name

then use that same structure for the user's question.

Do NOT change:

Compound → Drug
Compound → Medication
Disease → Condition
TREATS → PREVENTS
or any other schema element.

Only adapt the entity value or other directly necessary value.

EXECUTION RULES:

- After retrieving a relevant validated example, adapt that query
  using the exact same schema.
- Execute the adapted query using neo4jQuery.
- Do not execute speculative queries.
- Do not try alternative schemas after a query fails.
- Do not invent a second query using different labels or relationships.
- If the adapted query returns no results, report that no matching
  information was found in the knowledge graph.
- Base graph-derived answers ONLY on the Neo4j result.
- Do not add biomedical facts from your own knowledge to a graph-derived
  answer.
- Do not expose Cypher queries or internal tool calls.
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