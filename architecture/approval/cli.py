from architecture.approval.inbox import ProposalInbox
from architecture.approval.review import ProposalReview
from architecture.approval.decision import DecisionEngine
from architecture.approval.audit_log import AuditLog


def run_ui():
    inbox = ProposalInbox()
    review = ProposalReview()
    decision = DecisionEngine()
    audit = AuditLog()

    print("\n🧠 Home AI Architecture Approval Interface\n")

    for p in inbox.list_pending():
        print(review.format(p))

        action = input("approve / reject / skip: ")

        if action == "approve":
            proposal, _ = decision.approve(p.id, inbox)
            audit.record(p.id, "approved")

        elif action == "reject":
            proposal, _ = decision.reject(p.id, inbox)
            audit.record(p.id, "rejected")

        else:
            continue
