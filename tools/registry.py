from typing import Dict
from tools.contract import Tool


class ToolRegistry:
    """
    Pure in-memory registry.
    No imports of tools here.
    """

    def __init__(self):
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool):
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def list_tools(self):
        return list(self._tools.keys())


registry = ToolRegistry()
