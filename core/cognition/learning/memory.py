from collections import defaultdict
from core.cognition.learning.outcomes import ExecutionOutcome


class LearningMemory:
    """
    Stores structured execution outcomes for planning feedback.
    """

    def __init__(self):
        self.outcomes = []

        # aggregated stats
        self.tool_success = defaultdict(int)
        self.tool_failure = defaultdict(int)

    def record(self, outcome: ExecutionOutcome):
        self.outcomes.append(outcome)

        for tool in outcome.tool_sequence:
            if outcome.success:
                self.tool_success[tool] += 1
            else:
                self.tool_failure[tool] += 1

    def get_tool_success_rate(self, tool: str):
        total = self.tool_success[tool] + self.tool_failure[tool]
        if total == 0:
            return 0.5  # neutral prior
        return self.tool_success[tool] / total
