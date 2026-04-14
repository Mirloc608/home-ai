from core.cognition.planner import Planner
from core.cognition.failure_context import build_failure_context


class Replanner:
    def __init__(self):
        self.planner = Planner()

    async def replan(self, task: str, plan: dict, result) -> dict:
        """
        Generate a brand new plan based on failure.
        No mutation of old plan allowed.
        """

        failure_context = build_failure_context(plan, result)

        new_plan = await self.planner.create_plan(
            task=task,
            context=failure_context
        )

        return new_plan.model_dump()
