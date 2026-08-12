import pandas as pd

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


class SimilarQueryService:

    def __init__(self):
        self.excel_path = "graph_query_knowledge_base.xlsx"

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vectorstore = None

        self._load_knowledge_base()

    def _load_knowledge_base(self):

        df = pd.read_excel(self.excel_path)

        documents = []

        for _, row in df.iterrows():

            text = f"""
            User Question: {row["User Question"]}

            Category: {row["Category"]}

            Disease: {row["Disease"]}

            Intent: {row["Intent"]}

            Cypher Query: {row["Cypher Query"]}

            Neo4j Response: {row["Neo4j Response"]}

            Ideal LLM Answer: {row["Ideal LLM Answer"]}
            """

            documents.append(text)

        self.vectorstore = FAISS.from_texts(
            documents,
            self.embeddings
        )

    def fetch_similar_queries(self, question: str, k: int = 3):

        results = self.vectorstore.similarity_search(
            question,
            k=k
        )

        return [
            result.page_content
            for result in results
        ]


similar_query_service = SimilarQueryService()