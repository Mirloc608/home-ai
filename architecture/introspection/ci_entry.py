from app.bootstrap import build_system
from architecture.introspection.cli_verify import run


def main():
    system_context = build_system()
    run(system_context)


if __name__ == "__main__":
    main()
