from core.cognition.capability.tool_catalog import TOOL_CATALOG
from core.cognition.capability.capability_context import CapabilityContext


class PlanValidator:
    """
    Ensures no invalid tool usage reaches execution.
    """

    def validate(self, plan, capability_context: CapabilityContext):

        for step in plan.steps:
            tool_name = step.get("tool")

            if tool_name not in TOOL_CATALOG:
                raise Exception(f"Unknown tool: {tool_name}")

            spec = TOOL_CATALOG[tool_name]

            for req in spec.requires:
                if not capability_context.has(req):
                    raise Exception(
                        f"Capability violation: {tool_name} requires {req}"
                    )

        return True
