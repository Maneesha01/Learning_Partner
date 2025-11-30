from google import genai

class QuizAgent:
    """
    Agent responsible for generating quiz questions from study material.
    """

    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def generate_quiz(self, text: str):
        prompt = (
            "Generate 5 simple quiz questions based on the content:\n\n"
            f"{text}"
        )
        response = self.client.generate_text(prompt=prompt)
        return response.text.split("\n")
