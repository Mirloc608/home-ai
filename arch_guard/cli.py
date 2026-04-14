from arch_guard.scanner import ImportScanner
from arch_guard.report import Report


def run():
    scanner = ImportScanner()
    report = Report()

    violations = scanner.scan_project(root=".")

    report.print(violations)


if __name__ == "__main__":
    run()
