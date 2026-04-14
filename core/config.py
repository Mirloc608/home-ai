import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Centralized configuration access point.
    No module should read os.environ directly.
    """

    # GitHub / CI
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    # LLM
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Environment
    HOME_AI_ENV = os.getenv("HOME_AI_ENV", "dev")
    HOME_AI_DEBUG = os.getenv("HOME_AI_DEBUG", "false").lower() == "true"

    # Paths
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./memory/db")
    TRACE_DB_PATH = os.getenv("TRACE_DB_PATH", "./observability.db")


settings = Settings()
