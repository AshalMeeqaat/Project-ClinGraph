from app.database.neo4j import neo4j_connection
from app.services.schema_loader import schema_loader


class GraphService:

    def get_disease_context(self, disease_name: str):

        schema = schema_loader.get_schema()

        query = f"""
        MATCH (d:`{schema.LABELS["disease"]}`)
        WHERE toLower(d.name)=toLower($name)

        OPTIONAL MATCH (c)-[:{schema.RELATIONSHIPS["treats"]}]->(d)
        OPTIONAL MATCH (d)-[:{schema.RELATIONSHIPS["has_symptom"]}]->(s)

        RETURN
        d.name AS disease,
        collect(DISTINCT c.name) AS drugs,
        collect(DISTINCT s.name) AS symptoms
        """

        result = neo4j_connection.execute_query(
            query,
            {"name": disease_name}
        )

        return result


graph_service = GraphService()