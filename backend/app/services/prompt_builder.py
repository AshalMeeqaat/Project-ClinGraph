from app.services.prompt_template import graph_prompt


def build_prompt(user_question: str, graph_context: list) -> str:

    if not graph_context:
        return user_question

    disease = graph_context[0]["disease"]

    relationship = graph_context[0]["relationship"]

    results = "\n".join(
        f"- {item}"
        for item in graph_context[0]["results"]
        if item
    )

    prompt = graph_prompt.format(
        disease=disease,
        relationship=relationship,
        results=results,
        question=user_question
    )

    print("\n========== FINAL PROMPT ==========\n")
    print(prompt)
    print("\n==================================\n")

    return prompt