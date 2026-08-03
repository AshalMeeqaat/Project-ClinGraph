from fastapi import APIRouter
from app.database.neo4j import neo4j_connection
from app.services.graph_service import graph_service


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

    return neo4j_connection.execute_query(query)


@router.get("/counts")
def get_counts():

    query = """
    MATCH (n)
    RETURN labels(n)[0] AS label,
           count(*) AS count
    ORDER BY count DESC
    """

    return neo4j_connection.execute_query(query)


@router.get("/nodes/{label}")
def get_nodes_by_label(label: str, limit: int = 25):

    query = f"""
    MATCH (n:`{label}`)
    RETURN
        n.id AS id,
        n.name AS name
    LIMIT $limit
    """

    return neo4j_connection.execute_query(query,{"limit": limit})


@router.get("/search/{label}")
def search_nodes(label: str, q: str, limit: int = 20):

    query = f"""
    MATCH (n:`{label}`)
    WHERE toLower(n.name) CONTAINS toLower($q)
    RETURN
        n.id AS id,
        n.name AS name
    LIMIT $limit
    """

    return neo4j_connection.execute_query(query,{"q": q,"limit": limit})

@router.get("/details/{label}/{node_id}")
def node_details(label: str, node_id: str):

    query = f"""
    MATCH (n:`{label}` {{id:$id}})
    RETURN n
    """

    result = neo4j_connection.execute_query(
        query,
        {
            "id": node_id
        }
    )

    return result

@router.get("/neighbors/{label}/{node_id}")
def neighbors(label: str, node_id: str):

    query = f"""
    MATCH (n:`{label}` {{id:$id}})-[r]-(m)

    RETURN
        type(r) AS relationship,
        labels(m)[0] AS node_type,
        m.id AS id,
        m.name AS name
    LIMIT 100
    """

    return neo4j_connection.execute_query(
        query,
        {
            "id": node_id
        }
    )
    
@router.get("/disease/{disease_id}/genes")
def disease_genes(disease_id: str):

    query = """
    MATCH (d:Disease {id:$id})-[:ASSOCIATES_GENE]->(g:Gene)

    RETURN
        g.id AS id,
        g.name AS name
    """

    return neo4j_connection.execute_query(
        query,
        {
            "id": disease_id
        }
    )
    
@router.get("/disease/{disease_id}/symptoms")
def disease_symptoms(disease_id: str):

    query = """
    MATCH (d:Disease {id:$id})-[:PRESENTS_SYMPTOM]->(s:Symptom)

    RETURN
        s.id AS id,
        s.name AS name
    """

    return neo4j_connection.execute_query(
        query,
        {
            "id": disease_id
        }
    )
    
@router.get("/disease/{disease_id}/drugs")
def disease_drugs(disease_id: str):

    query = """
    MATCH (c:Compound)-[:TREATS]->(d:Disease {id:$id})

    RETURN
        c.id AS id,
        c.name AS name
    """

    return neo4j_connection.execute_query(
        query,
        {
            "id": disease_id
        }
    )
    
@router.get("/drug/{drug_id}/diseases")
def drug_diseases(drug_id: str):

    query = """
    MATCH (c:Compound {id:$id})-[:TREATS]->(d:Disease)

    RETURN
        d.id AS id,
        d.name AS name
    """

    return neo4j_connection.execute_query(
        query,
        {
            "id": drug_id
        }
    )

@router.get("/stats")
def graph_stats():

    query = """
    MATCH (n)

    RETURN
        count(n) AS nodes
    """

    return neo4j_connection.execute_query(query)

@router.get("/context/{disease}")
def disease_context(disease: str):

    return graph_service.get_disease_context(disease)

