from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

from app.database.neo4j import neo4j_connection

router = APIRouter(
    prefix="/v1/tools",
    tags=["Neo4j Tool"]
)


class Neo4jQueryRequest(BaseModel):
    query: str
    parameters: Dict[str, Any] = {}


@router.post("/neo4j-query")
def neo4j_query(request: Neo4jQueryRequest):

    results = neo4j_connection.execute_query(
        request.query,
        request.parameters
    )

    return {
        "query": request.query,
        "results": results
    }