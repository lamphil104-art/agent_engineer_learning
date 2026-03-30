from utils.file_handler import load_json_file, save_json_file
from utils.vector_store import search_top_k
from services.embedding_service import embed_text
from services.rag_generation_service import generate_rag_answer
from utils.rag_eval import build_eval_report


def build_context_from_results(results: list[dict]) -> str:
    parts = []

    for idx, item in enumerate(results, start=1):
        parts.append(f"[Chunk {idx}]")
        parts.append(item["text"])
        parts.append("")

    return "\n".join(parts).strip()


def main():
    question = input("Nhập câu hỏi cho RAG:\n> ").strip()
    if not question:
        raise ValueError("Bạn chưa nhập câu hỏi.")

    print("\nĐang tạo query embedding...")
    query_embedding = embed_text(question, model="gemini-embedding-001")

    print("Đang đọc vector store...")
    vector_store = load_json_file("data/processed/vector_store.json")

    print("Đang retrieve top-k chunks...")
    top_results = search_top_k(
        query_embedding=query_embedding,
        records=vector_store,
        k=3
    )

    context = build_context_from_results(top_results)

    print("\nContext đã retrieve:")
    print(context)

    print("\nĐang gọi Gemini để sinh câu trả lời...")
    answer = generate_rag_answer(
        question=question,
        context=context,
        model="gemini-2.0-flash"
    )

    result = {
        "question": question,
        "top_k_chunks": top_results,
        "context": context,
        "answer": answer
    }

    eval_report = build_eval_report(
        question=question,
        top_k_results=top_results,
        context=context,
        answer=answer
    )

    save_json_file(result, "outputs/rag_answer.json")
    save_json_file(eval_report, "outputs/rag_eval.json")

    print("\n===== RAG ANSWER =====")
    print(answer)

    print("\n===== EVALUATION REPORT =====")
    print(eval_report)

    print("\nĐã lưu vào:")
    print("- outputs/rag_answer.json")
    print("- outputs/rag_eval.json")


if __name__ == "__main__":
    main()