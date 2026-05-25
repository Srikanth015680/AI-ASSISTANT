import os
from google import genai

API_KEY = os.getenv("LLM_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def generate_embeddings(texts):
    embeddings = []

    for text in texts:
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        embeddings.append(response.embeddings[0].values)

    return embeddings