from core.policies.governance.decisions import DecisionType


AUTHORITY_MAP = {
    DecisionType.PLAN_CREATION: "core.cognition.planner",
    DecisionType.TOOL_SELECTION: "core.cognition.capability.planner_adapter",
    DecisionType.PLAN_REPAIR: "core.cognition.replanner",

    DecisionType.EXECUTION_ORDER: "core.execution.executor",

    DecisionType.TOOL_PERMISSION: "runtime.security.policy",

    DecisionType.STRATEGY_SCORING: "core.cognition.learning.policy",

    DecisionType.DRIFT_DETECTION: "runtime.drift.detector",
}
