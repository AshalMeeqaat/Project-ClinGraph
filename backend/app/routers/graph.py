from fastapi import APIRouter

from app.database.neo4j import neo4j_connection

router = APIRouter(
    prefix="/graph",
    tags=["Graph"],
)


@router.get("/labels")
def get_labels():

    query = """
    MATCH (n)
    UNWIND labels(n) AS label
    RETURN DISTINCT label
    ORDER BY label
    """

    result = neo4j_connection.execute_query(query)

    return result