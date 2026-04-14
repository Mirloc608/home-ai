import yaml


class SpecGraph:
    """
    Converts architecture/system.yaml into a comparable graph form.
    """

    def load(self, path="architecture/system.yaml"):
        with open(path, "r") as f:
            spec = yaml.safe_load(f)["system"]

        graph = {}

        for name, node in spec.items():
            graph[name] = {
                "type": node["type"],
                "depends_on": node.get("depends_on", [])
            }

        return graph
