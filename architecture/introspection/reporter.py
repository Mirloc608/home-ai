def report_drift(mismatches):
    if not mismatches:
        print("✅ Runtime graph matches architecture spec.")
        return

    print("\n🚨 ARCHITECTURE DRIFT DETECTED\n")

    for m in mismatches:
        print(f"- Node: {m['node']}")
        print(f"  Issue: {m['issue']}")
        if "expected" in m:
            print(f"  Expected: {m['expected']}")
            print(f"  Actual: {m['actual']}")
        print()
