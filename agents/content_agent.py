from google import genai

class ContentAgent:
    """
    Agent responsible for reviewing and summarizing content.
    """

    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def summarize(self, text: str) -> str:
        prompt = (
            "Summarize the following content in simple words:\n\n"
            f"{text}"
        )
        response = self.client.generate_text(prompt=prompt)
        return response.text
