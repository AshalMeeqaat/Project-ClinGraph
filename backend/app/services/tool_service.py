from langchain_core.tools import tool

from app.services.similar_query_service import similar_query_service
from app.database.neo4j import neo4j_connection


@tool
def fetchSimilarQueries(question: str) -> str:
    """
    Retrieve similar biomedical questions and their Cypher examples
    from the knowledge base.
    """

    results = similar_query_service.fetch_similar_queries(
        question,
        k=3
    )

    return "\n\n--- SIMILAR QUERY ---\n\n".join(results)


@tool
def neo4jQuery(query: str) -> str:
    """
    Execute a Cypher query against the Neo4j biomedical knowledge graph
    and return the graph results.
    """

    results = neo4j_connection.execute_query(query)

    return str(results)