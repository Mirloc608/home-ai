from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ToolSpec:
    name: str
    description: str
    requires: List[str]   # capabilities required to use tool


TOOL_CATALOG: Dict[str, ToolSpec] = {
    "web_tool": ToolSpec(
        name="web_tool",
        description="Searches the internet",
        requires=["web_access"]
    ),

    "github_tool": ToolSpec(
        name="github_tool",
        description="Interacts with GitHub",
        requires=["github_access"]
    ),

    "llm_tool": ToolSpec(
        name="llm_tool",
        description="Calls external LLM provider",
        requires=["llm_access"]
    ),

    "shell_tool": ToolSpec(
        name="shell_tool",
        description="Executes system commands",
        requires=[]
    ),
}
