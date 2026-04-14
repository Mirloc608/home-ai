from core.cognition.capability.tool_catalog import TOOL_CATALOG
from core.cognition.capability.capability_context import CapabilityContext


class CapabilityAwarePlannerAdapter:
    """
    Filters tool availability BEFORE the LLM sees it.
    """

    def __init__(self, capability_context: CapabilityContext):
        self.context = capability_context

    def get_allowed_tools(self):
        allowed = {}

        for name, spec in TOOL_CATALOG.items():

            # tool is allowed only if ALL required caps are present
            if all(self.context.has(req) for req in spec.requires):
                allowed[name] = spec

        return allowed

    def build_tool_prompt_fragment(self):
        tools = self.get_allowed_tools()

        lines = ["AVAILABLE TOOLS (capability-filtered):"]

        for t in tools.values():
            lines.append(f"- {t.name}: {t.description}")

        return "\n".join(lines)
