from core.policies.governance.authority_map import AUTHORITY_MAP


class GovernanceValidator:
    def validate_decision_source(self, decision_type, caller_module):

        expected_owner = AUTHORITY_MAP.get(decision_type)

        if expected_owner is None:
            raise Exception(f"No authority defined for {decision_type}")

        if expected_owner not in caller_module:
            raise Exception(
                f"Governance violation: {caller_module} cannot decide {decision_type}. "
                f"Only {expected_owner} is authorized."
            )

        return True
