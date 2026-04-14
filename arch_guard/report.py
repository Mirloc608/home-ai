class Report:
    def print(self, violations):
        if not violations:
            print("✅ Architecture clean — no violations detected.")
            return

        print("❌ ARCHITECTURE VIOLATIONS DETECTED:\n")

        for file, module in violations:
            print(f"  - {file}")
            print(f"    → illegal import: {module}\n")
