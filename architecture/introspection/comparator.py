class GraphComparator:

    def compare(self, spec_graph, runtime_graph):
        mismatches = []

        # Check missing nodes
        for node in spec_graph:
            if node not in runtime_graph:
                mismatches.append({
                    "node": node,
                    "issue": "missing_runtime_instance"
                })

        # Check extra runtime nodes
        for node in runtime_graph:
            if node not in spec_graph:
                mismatches.append({
                    "node": node,
                    "issue": "unexpected_runtime_instance"
                })

        # Check type correctness (strict match)
        for node, spec in spec_graph.items():
            if node in runtime_graph:
                runtime_type = runtime_graph[node]["type"]

                if spec["type"] != runtime_type:
                    mismatches.append({
                        "node": node,
                        "issue": "type_mismatch",
                        "expected": spec["type"],
                        "actual": runtime_type
                    })

        return mismatches
