from dataclasses import dataclass
import time


@dataclass
class RuntimeSignal:
    source: str          # module emitting
    target: str          # module being called
    action: str          # function/tool call type
    timestamp: float = time.time()
