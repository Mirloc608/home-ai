from core.observability.emitter import event_bus
from observability.persistence.sqlite_store import SQLiteTraceStore
from observability.persistence.serializer import serialize_event

store = SQLiteTraceStore()

TRACE_BUFFER = {}


def on_event(trace, event):
    trace_id = trace.trace_id

    if trace_id not in TRACE_BUFFER:
        TRACE_BUFFER[trace_id] = {
            "trace_id": trace_id,
            "task": trace.task,
            "events": []
        }

    TRACE_BUFFER[trace_id]["events"].append(serialize_event(event))

    # optional flush strategy (simple v1)
    if len(TRACE_BUFFER[trace_id]["events"]) > 20:
        store.save_trace(trace_id, TRACE_BUFFER[trace_id])
