import os

import openai


class OpenAIProcessor:
    def __init__(self):
        openai.organization = os.getenv("OPENAI_ORG")
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def test(self):
        return "This is openAI processor"

    def enter_prompt(self, prompt):
        original_prompt = f'Tell me an epic story of ${prompt} in 3 act structure. Give me Act 1'
        result = self.get_chat([
            {"role": "user", "content": original_prompt}], n=3)
        result['original_prompt'] = original_prompt
        return result

    def get_img_prompt(self, txt):
        return self.get_chat(
            [{"role": "user", "content": f'Summarize the following into one picture description: ${txt} in 70 words'}])

    def get_chat(self, messages, n=1):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, n=n)
