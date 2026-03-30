import os
from dotenv import load_dotenv
from google import genai

from prompts.rag_prompt import build_rag_prompt

load_dotenv()


def get_genai_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Không tìm thấy GEMINI_API_KEY trong file .env")

    return genai.Client(api_key=api_key)


def generate_rag_answer(question: str, context: str, model: str = "gemini-2.0-flash") -> str:
    if not question.strip():
        raise ValueError("Question không được rỗng.")

    if not context.strip():
        raise ValueError("Context không được rỗng.")

    client = get_genai_client()
    prompt = build_rag_prompt(context, question)

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    if not response.text:
        raise ValueError("Model không trả về text.")

    return response.text.strip()