from utils.similarity import cosine_similarity


def main():
    chunks = [
        {
            "chunk_id": 1,
            "text": "AI agents use language models, tools, and workflows.",
            "embedding": [0.9, 0.8, 0.1]
        },
        {
            "chunk_id": 2,
            "text": "RAG retrieves external knowledge before answering.",
            "embedding": [0.8, 0.9, 0.2]
        },
        {
            "chunk_id": 3,
            "text": "Bananas are yellow fruits.",
            "embedding": [0.1, 0.1, 0.95]
        }
    ]

    query = {
        "text": "How can AI systems use outside information?",
        "embedding": [0.85, 0.95, 0.1]
    }

    scored_chunks = []

    for chunk in chunks:
        score = cosine_similarity(query["embedding"], chunk["embedding"])
        scored_chunks.append(
            {
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "score": score
            }
        )

    scored_chunks.sort(key=lambda x: x["score"], reverse=True)

    print("Query:")
    print(query["text"])

    print("\nTop chunks gần nhất:")
    for item in scored_chunks:
        print("\n------------------")
        print(f"Chunk ID: {item['chunk_id']}")
        print(f"Score: {item['score']:.4f}")
        print(f"Text: {item['text']}")


if __name__ == "__main__":
    main()