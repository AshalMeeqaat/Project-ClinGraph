from app.database.neo4j import neo4j_connection

from app.config.schemas import hetionet
from app.config.schemas import ctd


class SchemaLoader:

    def __init__(self):
        self.schema = None

    def load(self):

        query = """
        MATCH (d:DatasetMetadata)
        RETURN d.name AS dataset
        LIMIT 1
        """

        result = neo4j_connection.execute_query(query)

        if not result:
            raise Exception("DatasetMetadata node not found.")

        dataset = result[0]["dataset"].lower()

        if dataset == "hetionet":
            self.schema = hetionet

        elif dataset == "ctd":
            self.schema = ctd

        else:
            raise Exception(f"Unsupported dataset: {dataset}")

        print(f"\nLoaded schema: {dataset}")

        return self.schema

    def get_schema(self):

        if self.schema is None:
            raise Exception("Schema not loaded.")

        return self.schema


schema_loader = SchemaLoader()