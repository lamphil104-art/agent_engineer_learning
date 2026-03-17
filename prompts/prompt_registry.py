from prompts.insight_prompt_v1 import build_insight_prompt_v1
from prompts.insight_prompt_v2 import build_insight_prompt_v2


PROMPT_BUILDERS = {
    "v1": build_insight_prompt_v1,
    "v2": build_insight_prompt_v2,
}


def get_prompt_builder(version: str):
    if version not in PROMPT_BUILDERS:
        raise ValueError(f"Prompt version không hợp lệ: {version}")
    return PROMPT_BUILDERS[version]