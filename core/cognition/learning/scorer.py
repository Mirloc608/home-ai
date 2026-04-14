from core.cognition.learning.memory import LearningMemory


class PlanScorer:
    """
    Scores tool choices and sequences based on historical outcomes.
    """

    def __init__(self, memory: LearningMemory):
        self.memory = memory

    def score_tool(self, tool: str):
        return self.memory.get_tool_success_rate(tool)

    def score_plan(self, plan):
        score = 0.0
        count = 0

        for step in plan.steps:
            tool = step.get("tool")
            score += self.score_tool(tool)
            count += 1

        return score / max(count, 1)
