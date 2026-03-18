from utils.vector_store import search_top_k


def main():
    vector_store = [
        {
            "chunk_id": 1,
            "text": "AI agents use language models, tools, and workflows.",
            "embedding": [0.9, 0.8, 0.1],
            "source": "sample_doc.txt"
        },
        {
            "chunk_id": 2,
            "text": "RAG retrieves external knowledge before answering.",
            "embedding": [0.8, 0.9, 0.2],
            "source": "sample_doc.txt"
        },
        {
            "chunk_id": 3,
            "text": "Chunking splits long documents into smaller pieces.",
            "embedding": [0.75, 0.85, 0.15],
            "source": "sample_doc.txt"
        },
        {
            "chunk_id": 4,
            "text": "Bananas are yellow fruits.",
            "embedding": [0.1, 0.1, 0.95],
            "source": "fruit_doc.txt"
        }
    ]

    query = {
        "text": "Why do RAG systems split documents and use external information?",
        "embedding": [0.82, 0.93, 0.12]
    }

    top_results = search_top_k(
        query_embedding=query["embedding"],
        records=vector_store,
        k=3
    )

    print("Query:")
    print(query["text"])

    print("\nTop-k results:")
    for item in top_results:
        print("\n----------------------")
        print(f"Chunk ID: {item['chunk_id']}")
        print(f"Score: {item['score']:.4f}")
        print(f"Source: {item['source']}")
        print(f"Text: {item['text']}")


if __name__ == "__main__":
    main()