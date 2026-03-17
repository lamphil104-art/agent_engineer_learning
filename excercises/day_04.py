import json
from pathlib import Path

from services.gemini_service import generate_insight
from utils.validators import validate_user_text


def save_output(data: dict, output_path: str = "outputs/result.json") -> None:
    Path("outputs").mkdir(parents=True, exist_ok=True)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise RuntimeError(f"Không thể lưu file output: {e}")


def main():
    print("=== AI Insight Extractor ===")

    try:
        raw_text = input("Nhập đoạn văn bản cần phân tích:\n> ")
        user_text = validate_user_text(raw_text)

        print("Input hợp lệ. Bắt đầu xử lý...")
        result = generate_insight(user_text)
        result_dict = result.model_dump()

        print("\nKết quả JSON:")
        print(json.dumps(result_dict, ensure_ascii=False, indent=2))

        save_output(result_dict)
        print("\nĐã lưu kết quả vào outputs/result.json")

    except ValueError as e:
        print(f"\nLỗi dữ liệu đầu vào: {e}")

    except RuntimeError as e:
        print(f"\nLỗi hệ thống: {e}")

    except Exception as e:
        print(f"\nLỗi không xác định: {e}")


if __name__ == "__main__":
    main()