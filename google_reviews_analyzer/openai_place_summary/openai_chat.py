from openai import OpenAI


class OpenAIChat:
    def __init__(self, api_key: str, model: str, temperature: float, max_tokens: int):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def chat(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        return response.choices[0].message.content
