import json
from pathlib import Path


def load_json_file(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy file: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json_file(data, file_path: str) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)