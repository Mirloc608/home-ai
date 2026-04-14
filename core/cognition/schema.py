from pydantic import BaseModel
from typing import List, Literal, Optional, Dict, Any


class PlanStep(BaseModel):
    id: str
    type: str  # tool name or "reason"
    input: Any
    depends_on: List[str] = []


class Plan(BaseModel):
    task: str
    intent: str
    steps: List[PlanStep]
    metadata: Optional[Dict[str, Any]] = {}
