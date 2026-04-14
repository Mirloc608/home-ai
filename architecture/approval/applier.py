import yaml


class ProposalApplier:

    def apply(self, proposal, system_yaml_path="architecture/system.yaml"):

        if proposal.risk_level == "high":
            raise Exception("High-risk changes require manual YAML edit")

        with open(system_yaml_path, "r") as f:
            spec = yaml.safe_load(f)

        # NOTE: intentionally minimal logic
        # real implementation would map structured changes → YAML edits

        print(f"Applying approved proposal: {proposal.id}")
