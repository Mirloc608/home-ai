# v1 Architecture Freeze Rules

FORBIDDEN_IMPORTS = {
    "core.cognition": [
        "observability.persistence",
        "observability.history",
        "memory.vector_store",
        "tools.*",
    ],

    "core.execution": [
        "observability.persistence",
        "observability.history",
    ],

    "tools": [
        "core.cognition",
        "core.execution",
        "observability.persistence",
    ],

    "memory": [
        "core.execution",
        "tools.*",
    ],
}


ALLOWED_ROOTS = [
    "core",
    "memory",
    "tools",
    "observability",
    "runtime",
    "app",
]
