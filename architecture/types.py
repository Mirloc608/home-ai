from dataclasses import dataclass
from typing import List, Optional


@dataclass
class NodeSpec:
    type: str
    depends_on: Optional[List[str]] = None
