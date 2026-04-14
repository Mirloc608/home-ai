from tools.registry import registry


async def execute_tool(tool_name: str, input_data: dict):
    tool = registry.get(tool_name)

    if not tool:
        return {
            "error": f"Tool not found: {tool_name}",
            "available_tools": registry.list_tools(),
        }

    return await tool.run(input_data)
