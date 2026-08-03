from fastapi import APIRouter
from app.database.neo4j import neo4j_connection

router = APIRouter(
    prefix="/database",
    tags=["Database"]
)


@router.get("/test")
def test_connection():

    query = """
    MATCH (n)
    OPTIONAL MATCH ()-[r]->()
    RETURN count(DISTINCT n) AS total_nodes,
           count(DISTINCT r) AS total_relationships
    """

    result = neo4j_connection.execute_query(query)

    return result