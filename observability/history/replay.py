"""
Replay is NOT a runtime feature anymore.

Core observability does not replay or store anything.
"""

def replay_disabled():
    raise RuntimeError(
        "Replay is handled in observability/history layer, not core."
    )
