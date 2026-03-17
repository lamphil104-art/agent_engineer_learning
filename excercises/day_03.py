import json
from pathlib import Path

from services.gemini_service import generate_insight


def save_output(data: dict, output_path: str = "outputs/result.json") -> None:
    Path("outputs").mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    user_text = input("Nhập đoạn văn bản cần phân tích:\n> ").strip()
    if not user_text:
        raise ValueError("Bạn chưa nhập văn bản.")

    result = generate_insight(user_text)
    result_dict = result.model_dump()

    print("\nKết quả JSON:")
    print(json.dumps(result_dict, ensure_ascii=False, indent=2))

    save_output(result_dict)
    print("\nĐã lưu kết quả vào outputs/result.json")


if __name__ == "__main__":
    main()