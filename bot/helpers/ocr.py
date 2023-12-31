import os
import sys
import aiofiles

from httpx import AsyncClient
from aiofiles import os as aioos


async def ocrImg(path: str) -> str:
    """ OCR """
    client = AsyncClient()
    r = await client.post(url="http://localhost:3333/file", files={"file": open(path, "rb")})
    await client.aclose()
    return r.json()['result']
