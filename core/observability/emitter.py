from core.observability.trace import Event, TraceContext
from typing import Callable, Dict, List


class EventBus:
    """
    Pure in-memory event bus.

    NO storage. NO persistence. NO history logic.
    """

    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, handler: Callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []

        self._subscribers[event_type].append(handler)

    def emit(self, trace: TraceContext, event_type: str, data=None, step_id=None):
        event = Event(
            type=event_type,
            data=data or {},
            step_id=step_id,
        )

        handlers = self._subscribers.get(event_type, [])

        for handler in handlers:
            try:
                handler(trace, event)
            except Exception:
                # NEVER crash execution due to observability
                pass


# global singleton event bus
event_bus = EventBus()
