import json
import os


class ProposalStore:

    def save(self, proposal, path="architecture/healing/proposals"):
        os.makedirs(path, exist_ok=True)

        file_path = f"{path}/{proposal.id}.json"

        with open(file_path, "w") as f:
            json.dump(proposal.__dict__, f, indent=2)
