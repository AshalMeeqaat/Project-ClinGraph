from langchain_core.tools import tool

from app.services.similar_query_service import similar_query_service
from app.database.neo4j import neo4j_connection


@tool
def fetchSimilarQueries(question: str):
    """
    Retrieve similar previously validated biomedical questions
    from the ClinGraph knowledge base.
    """

    return similar_query_service.fetch_similar_queries(
        question,
        k=3
    )


@tool
def neo4jQuery(query: str):
    """
    Execute a Cypher query against the ClinGraph Neo4j database.
    """

    return neo4j_connection.execute_query(query)