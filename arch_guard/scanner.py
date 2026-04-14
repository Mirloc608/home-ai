import ast
import os
from pathlib import Path
from arch_guard.rules import FORBIDDEN_IMPORTS


class ImportScanner:
    def scan_file(self, file_path: str):
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())

        imports = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)

        return imports

    def scan_project(self, root="home-ai"):
        violations = []

        for path in Path(root).rglob("*.py"):
            imports = self.scan_file(str(path))

            for module in imports:
                for source, forbidden_list in FORBIDDEN_IMPORTS.items():
                    for forbidden in forbidden_list:
                        if forbidden.endswith("*"):
                            prefix = forbidden[:-1]
                            if module.startswith(prefix):
                                violations.append((str(path), module))
                        else:
                            if module == forbidden:
                                violations.append((str(path), module))

        return violations
