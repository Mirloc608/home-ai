import os
from dotenv import load_dotenv


class SecretsManager:
    """
    Loads secrets ONLY at runtime.
    Never exposed to cognition or architecture layers.
    """

    def __init__(self, env_path=".env"):
        load_dotenv(env_path)

    def get(self, key: str, default=None):
        value = os.getenv(key, default)

        if value is None:
            raise Exception(f"Missing required secret: {key}")

        return value
