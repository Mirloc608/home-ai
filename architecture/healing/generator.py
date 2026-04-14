import uuid
from datetime import datetime
from architecture.healing.proposal import RepairProposal


class ProposalGenerator:

    def generate(self, insights):

        changes = []

        for i in insights:

            if i["suggestion"] == "add_to_bootstrap_or_loader":
                changes.append({
                    "action": "ensure_instantiated",
                    "node": i["node"]
                })

            if i["suggestion"] == "sync_type_with_spec_or_update_yaml":
                changes.append({
                    "action": "sync_spec_or_runtime",
                    "node": i["node"]
                })

        return RepairProposal(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow().isoformat(),
            changes=changes,
            reason="runtime_spec_divergence",
            risk_level="medium"
        )
