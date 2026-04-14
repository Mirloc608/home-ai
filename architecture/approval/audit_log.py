import json
from datetime import datetime


class AuditLog:

    def record(self, proposal_id, decision):
        entry = {
            "proposal_id": proposal_id,
            "decision": decision,
            "timestamp": datetime.utcnow().isoformat()
        }

        with open("architecture/approval/audit.log", "a") as f:
            f.write(json.dumps(entry) + "\n")
