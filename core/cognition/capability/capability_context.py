from dataclasses import dataclass, field
from typing import Set


@dataclass
class CapabilityContext:
    """
    What the system is allowed to use during this run.
    """

    capabilities: Set[str] = field(default_factory=set)

    def has(self, capability: str) -> bool:
        return capability in self.capabilities
