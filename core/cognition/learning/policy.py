from core.cognition.learning.scorer import PlanScorer
from core.cognition.capability.tool_catalog import TOOL_CATALOG


class PlanningPolicy:
    """
    Applies learned bias to planning decisions.
    """

    def __init__(self, scorer: PlanScorer):
        self.scorer = scorer

    def rank_tools(self, tools):
        ranked = sorted(
            tools,
            key=lambda t: self.scorer.score_tool(t),
            reverse=True
        )
        return ranked

    def filter_low_confidence_tools(self, tools, threshold=0.3):
        return [
            t for t in tools
            if self.scorer.score_tool(t) >= threshold
        ]
