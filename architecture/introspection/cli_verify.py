import sys
from architecture.introspection.verify import ArchitectureVerifier


def run(system_context):
    verifier = ArchitectureVerifier()
    result = verifier.verify(system_context)

    if result["valid"]:
        print("✅ Architecture VALID")
        sys.exit(0)

    print("🚨 ARCHITECTURE DRIFT DETECTED")

    for m in result["mismatches"]:
        print(m)

    sys.exit(1)
