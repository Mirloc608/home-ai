from architecture.introspection.spec_graph import SpecGraph
from architecture.introspection.runtime_graph import RuntimeGraph
from architecture.introspection.comparator import GraphComparator


class ArchitectureVerifier:
    """
    Minimal integrity check between declared and runtime architecture.
    """

    def verify(self, system_context, spec_path="architecture/system.yaml"):

        spec = SpecGraph().load(spec_path)
        runtime = RuntimeGraph().build(system_context)

        comparator = GraphComparator()
        mismatches = comparator.compare(spec, runtime)

        return {
            "valid": len(mismatches) == 0,
            "mismatches": mismatches
        }
