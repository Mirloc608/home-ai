from tools.registry import registry


def validate_step(step: dict) -> bool:
    """
    Ensures tool exists OR is allowed system primitive.
    """

    allowed_primitives = {"analyze"}

    if step["type"] in allowed_primitives:
        return True

    return registry.get(step["type"]) is not None
