from __future__ import annotations

import asyncio
from typing import Any

from app.config import settings


class LLMService:
    def __init__(self) -> None:
        self.model = settings.DEFAULT_MODEL
        self.api_keys = {
            "openai": settings.OPENAI_API_KEY,
            "anthropic": settings.ANTHROPIC_API_KEY,
        }

    async def generate(self, prompt: str, system_prompt: str | None = None, model: str | None = None) -> str:
        model_name = model or self.model
        if settings.OPENAI_API_KEY:
            try:
                from openai import AsyncOpenAI

                client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
                completion = await client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_prompt or "You are a helpful AI assistant."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.7,
                )
                return completion.choices[0].message.content or "No response generated."
            except Exception:
                pass

        if settings.ANTHROPIC_API_KEY:
            try:
                import anthropic

                client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
                response = await asyncio.to_thread(
                    client.messages.create,
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1024,
                    messages=[{"role": "user", "content": prompt}],
                    system=system_prompt or "You are a helpful AI assistant.",
                )
                return response.content[0].text
            except Exception:
                pass

        return self._fallback_response(prompt, system_prompt)

    def _fallback_response(self, prompt: str, system_prompt: str | None = None) -> str:
        system_text = system_prompt or "You are a helpful AI assistant."
        return (
            f"LLM fallback response.\n\n"
            f"System: {system_text}\n\n"
            f"User request: {prompt}\n\n"
            "This project is configured to run without external LLM keys, but it is ready to use when keys are provided."
        )
