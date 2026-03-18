from utils.file_handler import save_json_file
from utils.text_chunker import chunk_text_by_words


def load_text_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    input_path = "data/raw/sample_doc.txt"
    output_path = "data/processed/chunks.json"

    text = load_text_file(input_path)

    chunks = chunk_text_by_words(
        text=text,
        chunk_size=50,
        overlap=10
    )

    chunk_records = []
    for idx, chunk in enumerate(chunks, start=1):
        chunk_records.append(
            {
                "chunk_id": idx,
                "text": chunk
            }
        )

    save_json_file(chunk_records, output_path)

    print(f"Tổng số chunk: {len(chunk_records)}")
    print(f"Đã lưu chunks vào: {output_path}")

    for item in chunk_records:
        print("\n--------------------")
        print(f"Chunk {item['chunk_id']}:")
        print(item["text"])


if __name__ == "__main__":
    main()