from utils.file_handler import load_json_file, save_json_file
from services.embedding_service import embed_texts


def main():
    chunks = load_json_file("data/processed/chunks.json")

    texts = [item["text"] for item in chunks]
    embeddings = embed_texts(texts, model="gemini-embedding-001")

    vector_store = []
    for item, embedding in zip(chunks, embeddings):
        vector_store.append(
            {
                "chunk_id": item["chunk_id"],
                "text": item["text"],
                "embedding": embedding,
                "source": item.get("source", "sample_doc.txt")
            }
        )

    save_json_file(vector_store, "data/processed/vector_store.json")

    print(f"Đã tạo {len(vector_store)} vector records.")
    print("Đã lưu vào data/processed/vector_store.json")

    first = vector_store[0]
    print("\nVí dụ record đầu tiên:")
    print(f"Chunk ID: {first['chunk_id']}")
    print(f"Text: {first['text']}")
    print(f"Embedding length: {len(first['embedding'])}")
    print(f"First 5 values: {first['embedding'][:5]}")


if __name__ == "__main__":
    main()