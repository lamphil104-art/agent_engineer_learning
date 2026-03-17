from services.gemini_service import generate_insight
from utils.validators import validate_user_text


def main():
    print("=== Prompt Version Test ===")

    try:
        raw_text = input("Nhập đoạn văn bản cần phân tích:\n> ")
        user_text = validate_user_text(raw_text)

        for version in ["v1", "v2"]:
            print(f"\n--- Đang chạy với prompt {version} ---")
            result = generate_insight(user_text, prompt_version=version)

            print(result.model_dump_json(indent=2))

    except Exception as e:
        print(f"\nĐã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()