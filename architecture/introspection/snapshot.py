import json
from datetime import datetime


class SnapshotStore:

    def save(self, graph, path="architecture/snapshots"):
        timestamp = datetime.utcnow().isoformat()

        file_path = f"{path}/graph_{timestamp}.json"

        with open(file_path, "w") as f:
            json.dump(graph, f, indent=2)
