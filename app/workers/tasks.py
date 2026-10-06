from __future__ import annotations

import httpx


class WebTools:
    async def fetch_text(self, url: str, timeout: float = 20.0) -> str:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.text
