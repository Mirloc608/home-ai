import json
from core.cognition.llm import LLMClient
from core.cognition.schema import Plan
from core.cognition.prompt_builder import build_tool_aware_prompt


class Planner:
    def __init__(self):
        self.llm = LLMClient()

    async def create_plan(self, task: str, context: str = "") -> Plan:
        prompt = build_tool_aware_prompt(task, context)

        raw = await self.llm.generate(prompt)

        return self._parse(task, raw)

    def _parse(self, task: str, raw: str) -> Plan:
        try:
            data = json.loads(raw)
        except Exception:
            data = {
                "task": task,
                "intent": "parse_failure_fallback",
                "steps": [
                    {
                        "id": "step_1",
                        "type": "analyze",
                        "input": {"text": task},
                        "depends_on": []
                    }
                ],
            }

        return Plan(**data)
