from dataclasses import dataclass
from typing import Optional


@dataclass
class ToolCapabilities:
    """
    What a tool is allowed to do.
    """

    can_call_web: bool = False
    can_use_github: bool = False
    can_access_llm: bool = False

    github_token: Optional[str] = None
    llm_key: Optional[str] = None
