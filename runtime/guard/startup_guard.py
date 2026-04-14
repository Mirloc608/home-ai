import sys
from architecture.introspection.verify import ArchitectureVerifier
from app.bootstrap import build_system


class StartupGuard:
    """
    Hard gate before production runtime starts.
    """

    def run(self):
        system_context = build_system()

        verifier = ArchitectureVerifier()
        result = verifier.verify(system_context)

        if not result["valid"]:
            print("🚨 PRODUCTION STARTUP BLOCKED: ARCHITECTURE DRIFT DETECTED")

            for m in result["mismatches"]:
                print(m)

            sys.exit(1)

        print("✅ Startup Guard Passed — Architecture Valid")

        return system_context
