import json
from tools.introspection import get_tool_catalog


def build_tool_aware_prompt(task: str, context: str) -> str:
    tools = get_tool_catalog()

    tool_block = json.dumps(tools, indent=2)

    return f"""
You are Home AI's Cognition Core.

You generate structured execution plans.

CRITICAL RULES:
- You MUST only use tools from the provided tool list
- Do NOT invent tools
- Each step must map to an existing tool or be "analyze"
- Output ONLY valid JSON
- No markdown, no commentary

AVAILABLE TOOLS:
{tool_block}

TASK:
{task}

CONTEXT:
{context}

OUTPUT FORMAT:
{{
  "task": "...",
  "intent": "...",
  "steps": [
    {{
      "id": "step_1",
      "type": "tool_name_or_analyze",
      "input": {{}},
      "depends_on": []
    }}
  ]
}}
"""
