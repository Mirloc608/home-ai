def summarize_trace(trace):
    return {
        "trace_id": trace.trace_id,
        "task": trace.task,
        "event_count": len(trace.events),
        "types": [e.type for e in trace.events],
    }
