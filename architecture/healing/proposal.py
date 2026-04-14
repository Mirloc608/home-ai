from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class RepairProposal:
    id: str
    timestamp: str
    changes: List[Dict[str, Any]]
    reason: str
    risk_level: str  # low | medium | high
