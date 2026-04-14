class Tool:
    name: str = "base"

    async def run(self, input_data: dict):
        raise NotImplementedError
