import importlib
import pkgutil
from tools.registry import registry
from tools.contract import Tool


def load_tools(package: str = "tools"):
    """
    Auto-imports all modules under /tools
    and registers Tool subclasses automatically.
    """

    for _, module_name, _ in pkgutil.iter_modules(__path__):
        if module_name in ["base", "contract", "registry", "loader"]:
            continue

        full_module = f"{package}.{module_name}"
        module = importlib.import_module(full_module)

        register_from_module(module)


def register_from_module(module):
    """
    Find Tool subclasses and register them.
    """

    for attr_name in dir(module):
        obj = getattr(module, attr_name)

        try:
            if (
                isinstance(obj, type)
                and issubclass(obj, Tool)
                and obj is not Tool
            ):
                instance = obj()
                registry.register(instance)
        except Exception:
            continue
