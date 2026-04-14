from tools.registry import registry


def get_tool_catalog():
    """
    Returns structured tool metadata for LLM consumption.
    """

    catalog = []

    for tool_name in registry.list_tools():
        tool = registry.get(tool_name)

        catalog.append({
            "name": tool.name,
            "description": getattr(tool, "description", ""),
        })

    return catalog
