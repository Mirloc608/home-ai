class ProposalReview:

    def format(self, proposal):
        return {
            "id": proposal.id,
            "timestamp": proposal.timestamp,
            "reason": proposal.reason,
            "risk": proposal.risk_level,
            "changes": proposal.changes
        }
