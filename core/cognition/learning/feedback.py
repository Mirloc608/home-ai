from core.cognition.learning.memory import LearningMemory
from core.cognition.learning.outcomes import ExecutionOutcome


class FeedbackProcessor:
    def __init__(self, memory: LearningMemory):
        self.memory = memory

    def ingest_execution(self, trace, plan, execution_result):
        outcome = ExecutionOutcome(
            trace_id=trace.trace_id,
            plan_id=plan.id,
            success=execution_result.success,
            failure_reason=getattr(execution_result, "error", None),
            tool_sequence=[s.tool for s in plan.steps],
            capability_context=list(getattr(trace, "capabilities", [])),
            metadata={}
        )

        self.memory.record(outcome)
