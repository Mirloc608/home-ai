from runtime.guard.startup_guard import StartupGuard


def main():
    guard = StartupGuard()

    system_context = guard.run()

    # ONLY reach here if architecture is valid
    print("🚀 Home AI Runtime Starting Safely")

    # handoff to scheduler / gateway / runtime loop
    from runtime.scheduler import start_scheduler
    start_scheduler(system_context)


if __name__ == "__main__":
    main()
