from runtime.drift.signals import RuntimeSignal
from runtime.drift.detector import DriftDetector


class RuntimeObserver:
    def __init__(self):
        self.detector = DriftDetector()

    def observe_call(self, source: str, target: str, action: str):
        signal = RuntimeSignal(
            source=source,
            target=target,
            action=action,
        )

        self.detector.process(signal)
