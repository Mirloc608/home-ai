class RuntimeGraph:

    def build(self, system_context):
        graph = {}

        # ONLY explicit system registry objects
        for name, obj in system_context.items():
            graph[name] = {
                "type": f"{obj.__class__.__module__}.{obj.__class__.__name__}"
            }

        return graph
