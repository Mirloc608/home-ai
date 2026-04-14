from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class StepResult:
    step_id: str
    success: bool
    output: Any = None
    error: Optional[str] = None


@dataclass
class ExecutionResult:
    success: bool
    step_results: list[StepResult]
    failed_step: Optional[str] = None
