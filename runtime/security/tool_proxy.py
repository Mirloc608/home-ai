class ToolProxy:

    def __init__(self, secrets):
        self.secrets = secrets

    def get_github_token(self):
        return self.secrets.get("GITHUB_TOKEN")
