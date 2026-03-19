from utils.file_handler import load_json_file, save_json_file
from utils.vector_store import search_top_k
from services.embedding_service import embed_text


def main():
    query = input("Nhập câu hỏi cần truy xuất:\n> ").strip()
    if not query:
        raise ValueError("Bạn chưa nhập query.")

    print("\nĐang tạo embedding cho query...")
    query_embedding = embed_text(query, model="gemini-embedding-001")

    print("Đang đọc vector store...")
    vector_store = load_json_file("data/processed/vector_store.json")

    print(f"Đã đọc {len(vector_store)} records.")

    top_results = search_top_k(
        query_embedding=query_embedding,
        records=vector_store,
        k=3
    )

    print("\nTop-k chunks gần nhất:")
    for item in top_results:
        print("\n----------------------")
        print(f"Chunk ID: {item['chunk_id']}")
        print(f"Score: {item['score']:.6f}")
        print(f"Source: {item.get('source', 'unknown')}")
        print(f"Text: {item['text']}")

    save_json_file(top_results, "outputs/retrieval_result.json")
    print("\nĐã lưu retrieval result vào outputs/retrieval_result.json")


if __name__ == "__main__":
    main()