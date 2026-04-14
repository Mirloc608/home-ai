from enum import Enum


class DecisionType(str, Enum):
    # Cognitive decisions
    PLAN_CREATION = "plan_creation"
    TOOL_SELECTION = "tool_selection"
    PLAN_REPAIR = "plan_repair"

    # Execution decisions
    EXECUTION_ORDER = "execution_order"

    # Security decisions
    TOOL_PERMISSION = "tool_permission"

    # Learning decisions
    STRATEGY_SCORING = "strategy_scoring"

    # System decisions
    DRIFT_DETECTION = "drift_detection"
