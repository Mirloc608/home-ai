# Runtime behavior violations (NOT import-level)

DRIFT_RULES = {
    "core_should_not_call": [
        "observability.persistence",
        "observability.history",
        "memory.vector_store",
    ],

    "tools_should_be_isolated": [
        "core.cognition",
        "core.execution",
    ],

    "planner_should_not_execute": [
        "tools.*",
    ],
}
