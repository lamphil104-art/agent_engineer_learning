def build_insight_prompt_v1(user_text: str) -> str:
    return f"""
You are an assistant that extracts structured insights from text.

Your task:
- identify the main topic
- write a short summary
- extract key points
- identify the sentiment as positive, neutral, or negative
- extract concrete action items if any

Rules:
- return structured JSON only
- summary must be concise
- key_points should contain 3 to 5 items
- action_items should be specific and short
- if no action items exist, return an empty list

Text:
\"\"\"
{user_text}
\"\"\"
""".strip()