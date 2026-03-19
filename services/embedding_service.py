import os
from typing import List
from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_genai_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Không tìm thấy GEMINI_API_KEY trong file .env")

    return genai.Client(api_key=api_key)


def embed_text(text: str, model: str = "gemini-embedding-001") -> List[float]:
    if not text.strip():
        raise ValueError("Text để embed không được rỗng.")

    client = get_genai_client()

    response = client.models.embed_content(
        model=model,
        contents=text,
    )

    return response.embeddings[0].values


def embed_texts(texts: List[str], model: str = "gemini-embedding-001") -> List[List[float]]:
    vectors = []

    for text in texts:
        vector = embed_text(text, model=model)
        vectors.append(vector)

    return vectors