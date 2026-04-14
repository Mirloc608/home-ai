import yaml
import importlib


class SystemLoader:
    def __init__(self, spec_path="architecture/system.yaml"):
        with open(spec_path, "r") as f:
            self.spec = yaml.safe_load(f)["system"]

        self.instances = {}

    def resolve_class(self, path: str):
        module_path, class_name = path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        return getattr(module, class_name)

    def build(self):
        # first pass: instantiate without dependencies
        for name, node in self.spec.items():
            cls = self.resolve_class(node["type"])
            self.instances[name] = cls()

        # second pass: inject dependencies
        for name, node in self.spec.items():
            instance = self.instances[name]

            for dep in node.get("depends_on", []):
                setattr(instance, dep, self.instances[dep])

        return self.instances
