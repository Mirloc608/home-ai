import os
import json
import httpx


class LLMClient:
    def __init__(self):
        self.model = os.getenv("LLM_MODEL", "llama3")
        self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")

    async def generate(self, prompt: str) -> str:
        """
        Basic Ollama-compatible endpoint
        """
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=60,
            )

        data = resp.json()
        return data.get("response", "")
