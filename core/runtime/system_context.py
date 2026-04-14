class SystemContext:
    """
    Central registry of active subsystems.
    This is the ONLY wiring surface.
    """

    def __init__(self):
        self.security_policy = None
        self.planner_adapter = None
        self.learning_memory = None
        self.governance = None
        self.drift_detector = None
        self.tool_proxy = None
