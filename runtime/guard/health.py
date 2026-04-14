def health_check(system_context):
    return {
        "status": "ok",
        "components": list(system_context.keys())
    }
