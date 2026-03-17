from typing import List
from pydantic import BaseModel


class InsightOutput(BaseModel):
    topic: str
    summary: str
    key_points: List[str]
    sentiment: str
    action_items: List[str]