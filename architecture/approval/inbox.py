class ProposalInbox:
    """
    Stores all pending architecture changes for human review.
    """

    def __init__(self):
        self.queue = []

    def add(self, proposal):
        self.queue.append(proposal)

    def list_pending(self):
        return self.queue
