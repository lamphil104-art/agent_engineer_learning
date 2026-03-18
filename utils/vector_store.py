from typing import List, Dict, Any
from utils.similarity import cosine_similarity


def search_top_k(
    query_embedding: List[float],
    records: List[Dict[str, Any]],
    k: int = 3
) -> List[Dict[str, Any]]:
    if k <= 0:
        raise ValueError("k phải lớn hơn 0")

    scored_records = []

    for record in records:
        embedding = record.get("embedding")
        if embedding is None:
            continue

        score = cosine_similarity(query_embedding, embedding)

        scored_record = {
            **record,
            "score": score
        }
        scored_records.append(scored_record)

    scored_records.sort(key=lambda x: x["score"], reverse=True)

    return scored_records[:k]