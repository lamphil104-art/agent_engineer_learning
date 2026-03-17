def validate_user_text(user_text: str) -> str:
    cleaned_text = user_text.strip()

    if not cleaned_text:
        raise ValueError("Bạn chưa nhập văn bản.")

    if len(cleaned_text) < 10:
        raise ValueError("Văn bản quá ngắn. Hãy nhập ít nhất 10 ký tự.")

    if len(cleaned_text) > 5000:
        raise ValueError("Văn bản quá dài cho bài tập hôm nay. Hãy nhập dưới 5000 ký tự.")

    return cleaned_text