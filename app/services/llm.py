from __future__ import annotations

from typing import Any, Dict, Optional

from app.config import settings


class LLMService:
    def __init__(self) -> None:
        self.model = settings.DEFAULT_MODEL

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
                content = completion.choices[0].message.content
                if content:
                    return content
            except Exception:
                pass

        if settings.ANTHROPIC_API_KEY:
            try:
                import anthropic

                client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
                response = await client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1024,
                    messages=[{"role": "user", "content": prompt}],
                    system=system_prompt or "You are a helpful AI assistant.",
                )
                text_blocks = getattr(response, "content", []) or []
                if text_blocks:
                    text = "".join(getattr(block, "text", "") for block in text_blocks if getattr(block, "type", None) == "text")
                    if text:
                        return text
            except Exception:
                pass

        return self._fallback_response(prompt, system_prompt)

    def _fallback_response(self, prompt: str, system_prompt: str | None = None) -> str:
        system_text = system_prompt or "You are a helpful AI assistant."
        return (
            f"LLM fallback response.\n\n"
            f"System: {system_text}\n\n"
            f"User request: {prompt}\n\n"
            "This project is running in offline fallback mode. Add API keys in .env to enable live LLM responses."
        )
