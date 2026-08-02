from ollama import chat


class OllamaService:

    def generate(self, prompt: str):

        response = chat(
            model="llama3.2:latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]


ollama_service = OllamaService()