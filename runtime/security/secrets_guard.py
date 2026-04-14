FORBIDDEN_KEYS = [
    "GITHUB_TOKEN",
    "OPENAI_API_KEY"
]


def validate_no_secret_leak(text: str):
    for key in FORBIDDEN_KEYS:
        if key in text:
            raise Exception(f"Secret leak detected: {key}")
