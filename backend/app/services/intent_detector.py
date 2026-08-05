class IntentDetector:

    def __init__(self):

        self.intent_keywords = {

            "drugs": [
                "drug",
                "drugs",
                "medicine",
                "medication",
                "treat",
                "therapy",
                "compound"
            ],

            "symptoms": [
                "symptom",
                "symptoms",
                "sign",
                "manifestation"
            ],

            "genes": [
                "gene",
                "genes",
                "genetic",
                "protein"
            ],

            "anatomy": [
                "anatomy",
                "organ",
                "tissue",
                "body part"
            ],

            "pathways": [
                "pathway",
                "pathways"
            ],

            "side_effects": [
                "side effect",
                "adverse effect"
            ],

            "biological_process": [
                "biological process",
                "process"
            ],

            "molecular_function": [
                "molecular function",
                "function"
            ],

            "cellular_component": [
                "cellular component",
                "cell"
            ]
        }

    def detect(self, question: str):

        question = question.lower()

        for intent, keywords in self.intent_keywords.items():

            for keyword in keywords:

                if keyword in question:
                    return intent

        return "general"


intent_detector = IntentDetector()