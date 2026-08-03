def build_prompt(user_question: str, graph_context: list) -> str:

    if not graph_context:
        return user_question

    disease = graph_context[0]["disease"]

    drugs = "\n".join(
        f"- {drug}" for drug in graph_context[0]["drugs"]
    )

    symptoms = "\n".join(
        f"- {symptom}" for symptom in graph_context[0]["symptoms"]
    )

    prompt = f"""
You are ClinGraph, an AI medical assistant.

Your PRIMARY source of truth is the Neo4j knowledge graph below.

If the requested information exists in the graph, answer using ONLY the graph.

If the graph does not contain enough information, clearly state:
"The knowledge graph does not contain this information."

Only then may you supplement the answer with your general medical knowledge.

==============================
Knowledge Graph
==============================

Disease:
{disease}

Known Treatments:
{drugs}

Known Symptoms:
{symptoms}

==============================
User Question
==============================

{user_question}

Provide a clear and structured answer.
"""

    print(prompt)

    return prompt