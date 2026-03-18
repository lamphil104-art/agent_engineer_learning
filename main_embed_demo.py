from utils.file_handler import save_json_file
from services.embedding_service import embed_texts


def main():
    chunks = [
        "AI agents use language models, tools, and workflows.",
        "RAG retrieves external knowledge from documents before answering.",
        "Chunking splits long documents into smaller pieces.",
        "Bananas are yellow fruits."
    ]

    embeddings = embed_texts(chunks)

    vector_store = []
    for idx, (text, embedding) in enumerate(zip(chunks, embeddings), start=1):
        vector_store.append(
            {
                "chunk_id": idx,
                "text": text,
                "embedding": embedding,
                "source": "demo_doc"
            }
        )

    save_json_file(vector_store, "data/processed/vector_store.json")

    print("Đã tạo vector store:")
    for item in vector_store:
        print("\n---------------------")
        print(f"Chunk ID: {item['chunk_id']}")
        print(f"Text: {item['text']}")
        print(f"Embedding: {item['embedding']}")


if __name__ == "__main__":
    main()