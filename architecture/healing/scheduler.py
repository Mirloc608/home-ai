class HealingScheduler:

    def __init__(self, introspector, analyzer, generator, store):
        self.introspector = introspector
        self.analyzer = analyzer
        self.generator = generator
        self.store = store

    def run_cycle(self, system_context, spec_path):

        spec_graph, runtime_graph, mismatches = self.introspector.run(
            system_context,
            spec_path
        )

        if not mismatches:
            return "OK - no healing required"

        insights = self.analyzer.analyze(mismatches)

        proposal = self.generator.generate(insights)

        self.store.save(proposal)

        return proposal.id
