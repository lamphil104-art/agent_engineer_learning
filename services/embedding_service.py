from typing import List


def mock_embed_text(text: str) -> List[float]:
    text_lower = text.lower()

    score_ai = 1.0 if any(word in text_lower for word in ["ai", "agent", "model", "tool"]) else 0.1
    score_rag = 1.0 if any(word in text_lower for word in ["rag", "retrieve", "knowledge", "document", "chunk"]) else 0.1
    score_other = 1.0 if any(word in text_lower for word in ["banana", "fruit", "yellow"]) else 0.1

    return [score_ai, score_rag, score_other]


def embed_texts(texts: List[str]) -> List[List[float]]:
    return [mock_embed_text(text) for text in texts]