def build_rag_prompt(context: str, question: str) -> str:
    return f"""
You are a helpful assistant answering questions based only on the provided context.

Rules:
- Use only the information in the context
- Do not make up facts
- If the context is not enough, say: "Không có đủ thông tin trong context."
- Answer clearly and briefly

Context:
\"\"\"
{context}
\"\"\"

Question:
{question}
""".strip()