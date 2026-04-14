class DecisionEngine:

    def approve(self, proposal_id, inbox):
        return self._find(proposal_id, inbox), "approved"

    def reject(self, proposal_id, inbox):
        return self._find(proposal_id, inbox), "rejected"

    def _find(self, proposal_id, inbox):
        for p in inbox.queue:
            if p.id == proposal_id:
                return p
        raise Exception("Proposal not found")
