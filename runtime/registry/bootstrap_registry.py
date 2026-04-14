from runtime.security.secrets import SecretsManager
from runtime.security.tool_proxy import ToolProxy
from runtime.security.policy import SecurityPolicyEngine

from core.policies.governance.validator import GovernanceValidator

from core.cognition.learning.memory import LearningMemory
from core.cognition.learning.scorer import PlanScorer
from core.cognition.learning.policy import PlanningPolicy

from runtime.drift.detector import DriftDetector

from core.cognition.capability.capability_context import CapabilityContext
from core.cognition.capability.planner_adapter import CapabilityAwarePlannerAdapter


def build_runtime_graph():
    # --- internal infrastructure (NOT graph nodes) ---
    secrets = SecretsManager()
    tool_proxy = ToolProxy(secrets)

    capability_context = CapabilityContext()
    planner_adapter = CapabilityAwarePlannerAdapter(
        capability_context=capability_context
    )

    # --- declared architecture nodes ---
    security = SecurityPolicyEngine()
    governance = GovernanceValidator()

    memory = LearningMemory()
    scorer = PlanScorer(memory=memory)
    learning_policy = PlanningPolicy(scorer=scorer)

    drift_detector = DriftDetector()

    # IMPORTANT: ONLY return system.yaml declared nodes
    return {
        "security": security,
        "tool_proxy": tool_proxy,

        "governance": governance,

        "learning_memory": memory,
        "scorer": scorer,
        "learning_policy": learning_policy,

        "drift_detector": drift_detector,
        "planner_adapter": planner_adapter
    }
