import os
import json
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
from google import genai
from google.genai import types


load_dotenv()


class SummaryOutput(BaseModel):
    topic: str
    summary: str
    key_points: List[str]


def save_output(data: dict, output_path: str = "outputs/result.json") -> None:
    Path("outputs").mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Không tìm thấy GEMINI_API_KEY trong file .env")

    client = genai.Client(api_key=api_key)

    user_text = input("Nhập đoạn văn bản cần tóm tắt:\n> ").strip()
    if not user_text:
        raise ValueError("Bạn chưa nhập văn bản.")

    prompt = f"""
You are an assistant that extracts structured summaries.

Summarize the following text and return structured JSON.

Text:
\"\"\"
{user_text}
\"\"\"
""".strip()

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0,
                response_mime_type="application/json",
                response_schema=SummaryOutput,
            ),
        )

        # Với structured output, SDK có thể parse ra object theo schema
        parsed = response.parsed

        if parsed is None:
            raise ValueError("Model không trả về parsed output đúng schema.")

        result = parsed.model_dump()

        print("\nKết quả JSON:")
        print(json.dumps(result, ensure_ascii=False, indent=2))

        save_output(result)
        print("\nĐã lưu kết quả vào outputs/result.json")

    except ValidationError as e:
        print("\nLỗi schema:")
        print(e)

    except Exception as e:
        print(f"\nĐã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()