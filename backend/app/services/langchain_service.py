from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

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

    def generate(self, user_question: str):

        system_prompt = """
You are ClinGraph, a biomedical knowledge graph assistant.

Your job is to answer biomedical questions using the Neo4j knowledge graph.

You have two tools:

1. fetchSimilarQueries
   - Finds previously validated questions.
   - Returns their category, disease, intent, Cypher query,
     Neo4j response, and ideal answer.
   - Use this FIRST for graph-related questions.

2. neo4jQuery
   - Executes a Cypher query against the Neo4j database.
   - Use this AFTER examining the similar-query examples.

IMPORTANT WORKFLOW:

For a biomedical graph question:

STEP 1:
Call fetchSimilarQueries using the user's question.

STEP 2:
Examine the returned examples carefully.
Use them to determine:
- the appropriate relationship
- the correct source node label
- the correct target node label
- the correct Cypher pattern

STEP 3:
Construct a NEW Cypher query for the user's actual question.
Do NOT blindly copy the example query.

STEP 4:
Call neo4jQuery with that Cypher query.

STEP 5:
Use the actual Neo4j result to answer the user.

NEVER invent biomedical facts when Neo4j can provide the information.

If Neo4j returns no records, clearly say that the knowledge graph
does not contain matching information.

Keep the final answer concise and directly answer the user's question.

Do not expose internal tool calls, Cypher queries, embeddings,
or implementation details unless the user explicitly asks for them.
"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_question)
        ]

        # Prevent an accidental infinite tool-calling loop.
        max_iterations = 5

        for _ in range(max_iterations):

            response = self.llm_with_tools.invoke(messages)

            # No more tools needed -> final answer
            if not response.tool_calls:
                return response.content

            # Add the assistant's tool-call message
            messages.append(response)

            for tool_call in response.tool_calls:

                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                tool_id = tool_call["id"]

                if tool_name not in self.tools:
                    messages.append(
                        ToolMessage(
                            content=f"Unknown tool: {tool_name}",
                            tool_call_id=tool_id
                        )
                    )
                    continue

                try:
                    tool = self.tools[tool_name]

                    tool_result = tool.invoke(tool_args)

                    messages.append(
                        ToolMessage(
                            content=str(tool_result),
                            tool_call_id=tool_id
                        )
                    )

                except Exception as e:

                    messages.append(
                        ToolMessage(
                            content=f"Tool execution error: {str(e)}",
                            tool_call_id=tool_id
                        )
                    )

        return (
            "I was unable to complete the knowledge-graph query "
            "within the allowed tool steps."
        )


langchain_service = LangChainService()