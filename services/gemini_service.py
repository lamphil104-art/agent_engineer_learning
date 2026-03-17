import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from schemas.insight_schema import InsightOutput
from prompts.prompt_registry import get_prompt_builder

load_dotenv()


def generate_insight(user_text: str, prompt_version: str = "v1") -> InsightOutput:
    print("Đang kiểm tra API key...")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Không tìm thấy GEMINI_API_KEY trong file .env")

    print("Đang khởi tạo Gemini client...")
    client = genai.Client(api_key=api_key)

    prompt_builder = get_prompt_builder(prompt_version)
    prompt = prompt_builder(user_text)

    print(f"Đang gửi request lên Gemini với prompt version: {prompt_version}...")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0,
                response_mime_type="application/json",
                response_schema=InsightOutput,
            ),
        )
    except Exception as e:
        raise RuntimeError(f"Lỗi khi gọi Gemini API: {e}")

    print("Đã nhận response từ Gemini, đang kiểm tra parsed output...")
    parsed = response.parsed

    if parsed is None:
        raise ValueError("Model không trả về parsed output đúng schema.")

    return parsed