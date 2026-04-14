from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class ExecutionOutcome:
    trace_id: str
    plan_id: str
    success: bool
    failure_reason: str | None
    tool_sequence: List[str]
    capability_context: List[str]
    metadata: Dict[str, Any]
