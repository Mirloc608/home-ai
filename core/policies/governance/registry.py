from core.policies.governance.authority_map import AUTHORITY_MAP


class GovernanceRegistry:
    def get_owner(self, decision_type):
        return AUTHORITY_MAP.get(decision_type)

    def list_decisions(self):
        return list(AUTHORITY_MAP.keys())
