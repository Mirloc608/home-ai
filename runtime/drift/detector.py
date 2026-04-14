from runtime.drift.rules import DRIFT_RULES
from runtime.drift.reporter import report_violation


class DriftDetector:
    def process(self, signal):
        self.check_core_rules(signal)
        self.check_tool_rules(signal)
        self.check_planner_rules(signal)

    def check_core_rules(self, signal):
        for forbidden in DRIFT_RULES["core_should_not_call"]:
            if signal.source.startswith("core") and forbidden in signal.target:
                report_violation("CORE_LEAK", signal)

    def check_tool_rules(self, signal):
        for forbidden in DRIFT_RULES["tools_should_be_isolated"]:
            if signal.source.startswith("tools") and forbidden in signal.target:
                report_violation("TOOL_COUPLING", signal)

    def check_planner_rules(self, signal):
        for forbidden in DRIFT_RULES["planner_should_not_execute"]:
            if signal.source.endswith("planner") and forbidden in signal.target:
                report_violation("PLANNER_EXECUTION_LEAK", signal)
