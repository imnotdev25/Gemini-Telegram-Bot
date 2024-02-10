import base64
import os

from httpx import AsyncClient

from bot.config import NVIDIA_API_KEY
from bot.helpers.functions import random_string
from bot.logging import LOGGER


class Nvidia:
    def __init__(self):

        self.client = AsyncClient(headers={
            "Authorization": f"Bearer {NVIDIA_API_KEY}",
            "Accept": "application/json",
        })
        self.message = None
        self.base_url = "https://api.nvcf.nvidia.com/v2/nvcf/pexec"
        self.fetch_url_format = f"{self.base_url}/status/"
        self.payload = {
            "messages": [
                {
                    "content": f"{self.message}",
                    "role": "user"
                }
            ],
            "temperature": 0.7,
            "top_p": 1,
            "max_tokens": 1024,
            "seed": 42,
            "stream": False
        }

    def saveImg(self, bs64: str) -> str:
        try:
            with open(f"images/{random_string(7)}.jpg", "wb") as f:
                f.write(base64.b64decode(bs64))
                f.close()
            return os.path.abspath(f.name)
        except Exception as e:
            LOGGER(__name__).error(e)

    async def codeLLm(self, message: str) -> str:
        self.message = message
        invoke_url = f"{self.base_url}/functions/2ae529dc-f728-4a46-9b8d-2697213666d8"
        response = await self.client.post(invoke_url, json=self.payload)
        while response.status_code == 202:
            request_id = response.headers.get("NVCF-REQID")
            fetch_url = self.fetch_url_format + request_id
            response = await self.client.get(fetch_url)
        response.raise_for_status()
        response_body = response.json()
        return self.saveImg(response_body['choices'][0]['message']['content'])

    async def llma(self, message: str) -> str:
        self.message = message
        invoke_url = f"{self.base_url}/functions/7b3e3361-4266-41c8-b312-f5e33c81fc92"
        response = await self.client.post(invoke_url, json=self.payload)
        while response.status_code == 202:
            request_id = response.headers.get("NVCF-REQID")
            fetch_url = self.fetch_url_format + request_id
            response = await self.client.get(fetch_url)
        response.raise_for_status()
        response_body = response.json()
        return response_body['choices'][0]['message']['content']

    async def stableDiff(self, message: str) -> str:
        invoke_url = f"{self.base_url}/functions/0ba5e4c7-4540-4a02-b43a-43980067f4af"
        fetch_url_format = f"{self.base_url}/status/"

        payload = {
            "prompt": f"{message}",
            "inference_steps": 4,
            "prompt_strength": 0.9,
            "seed": 5
        }
        response = await self.client.post(invoke_url, json=payload)
        while response.status_code == 202:
            request_id = response.headers.get("NVCF-REQID")
            fetch_url = fetch_url_format + request_id
            response = await self.client.get(fetch_url)
        response.raise_for_status()
        response_body = response.json()
        return self.saveImg(bs64=response_body['b64_json'])
