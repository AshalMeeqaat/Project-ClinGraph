from app.services.schema_loader import schema_loader


def get_intent_mapping():

    schema = schema_loader.get_schema()

    return {

        "drugs": (
            schema.RELATIONSHIPS["treats"],
            schema.LABELS["drug"]
        ),

        "symptoms": (
            schema.RELATIONSHIPS["has_symptom"],
            schema.LABELS["symptom"]
        ),

        "genes": (
            schema.RELATIONSHIPS["associated_gene"],
            schema.LABELS["gene"]
        )

    }