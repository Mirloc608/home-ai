from abc import ABC, abstractmethod
from typing import Dict, Any


class Tool(ABC):
    """
    All tools MUST inherit this.
    No exceptions.
    """

    name: str
    description: str = ""

    @abstractmethod
    async def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
