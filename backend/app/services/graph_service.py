from app.database.neo4j import neo4j_connection
from app.services.schema_loader import schema_loader


class GraphService:

    def get_all_diseases(self):

        schema = schema_loader.get_schema()

        query = f"""
        MATCH (d:`{schema.LABELS["disease"]}`)
        RETURN d.name AS disease
        """

        result = neo4j_connection.execute_query(query)

        return [
            row["disease"]
            for row in result
            if row["disease"]
        ]

    def get_relationship_context(
        self,
        disease_name: str,
        relationship: str,
        target_label: str
    ):

        schema = schema_loader.get_schema()

        query = f"""
        MATCH (d:`{schema.LABELS["disease"]}`)
        WHERE toLower(d.name)=toLower($name)

        OPTIONAL MATCH (d)-[:`{relationship}`]->(t:`{target_label}`)

        RETURN
            d.name AS disease,
            collect(DISTINCT t.name) AS results
        """

        result = neo4j_connection.execute_query(
            query,
            {"name": disease_name}
        )
        print("\n========== GRAPH RESULT ==========")
        print(result)

        if result:

            result[0]["relationship"] = relationship

        return result


graph_service = GraphService()