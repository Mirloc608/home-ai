class DependencyResolver:
    def validate(self, spec: dict):
        defined = set(spec.keys())

        for name, node in spec.items():
            for dep in node.get("depends_on", []):
                if dep not in defined:
                    raise Exception(f"Missing dependency: {dep} for {name}")
