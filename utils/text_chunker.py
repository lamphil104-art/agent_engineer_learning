from typing import List


def chunk_text_by_words(text: str, chunk_size: int = 80, overlap: int = 20) -> List[str]:
    words = text.split()

    if chunk_size <= 0:
        raise ValueError("chunk_size phải lớn hơn 0")

    if overlap < 0:
        raise ValueError("overlap không được âm")

    if overlap >= chunk_size:
        raise ValueError("overlap phải nhỏ hơn chunk_size")

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk = " ".join(chunk_words).strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks