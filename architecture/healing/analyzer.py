class DriftAnalyzer:

    def analyze(self, mismatches):
        insights = []

        for m in mismatches:

            if m["issue"] == "missing_runtime_instance":
                insights.append({
                    "node": m["node"],
                    "root_cause": "node_not_instantiated_in_runtime",
                    "suggestion": "add_to_bootstrap_or_loader"
                })

            if m["issue"] == "type_mismatch":
                insights.append({
                    "node": m["node"],
                    "root_cause": "implementation_drift",
                    "suggestion": "sync_type_with_spec_or_update_yaml"
                })

        return insights
