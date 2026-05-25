import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")

client = genai.Client(api_key=API_KEY)


def call_llm(system_prompt, user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{system_prompt}\n\n{user_prompt}"
    )

    return response.text, 0