def report_violation(code: str, signal):
    print("\n🚨 ARCHITECTURE DRIFT DETECTED")
    print(f"Type: {code}")
    print(f"Source: {signal.source}")
    print(f"Target: {signal.target}")
    print(f"Action: {signal.action}")
    print(f"Time: {signal.timestamp}\n")
