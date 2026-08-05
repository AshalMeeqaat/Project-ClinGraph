from app.services.graph_service import graph_service


class EntityDetector:

    def detect(self, question: str):

        question = question.lower()

        diseases = graph_service.get_all_diseases()

        for disease in diseases:
            if disease.lower() in question:
                return disease

        return None


entity_detector = EntityDetector()