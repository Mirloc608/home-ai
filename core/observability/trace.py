from dataclasses import dataclass, field
from typing import Any, Optional
import time
import uuid


@dataclass
class Event:
    type: str
    timestamp: float = field(default_factory=time.time)
    data: dict = field(default_factory=dict)
    step_id: Optional[str] = None


@dataclass
class TraceContext:
    """
    Runtime-only context holder (NOT persisted, NOT stored)
    """
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    task: str = ""
