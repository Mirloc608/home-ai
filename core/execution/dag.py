from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Step:
    id: str
    type: str
    input: Any


@dataclass
class DAG:
    steps: List[Step]
