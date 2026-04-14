from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class SecurityContext:
    """
    Defines what a tool is allowed to access during execution.
    """

    tool_name: str
    capabilities: Dict[str, Any] = field(default_factory=dict)
