from tools.contract import Tool


class EchoTool(Tool):
    name = "echo"
    description = "Returns input back unchanged"

    async def run(self, input_data: dict):
        return {
            "echo": input_data
        }
