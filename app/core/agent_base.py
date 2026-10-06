from __future__ import annotations

from typing import Any, Dict, Optional

from app.core.schemas import AgentResult
from app.services.llm import LLMService


class BaseAgent:
    name: str = "base_agent"
    role: str = "general"
    capabilities: list[str] = []

    def __init__(self, llm_service: Optional[LLMService] = None):
        self.llm_service = llm_service or LLMService()

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        raise NotImplementedError

    def _safe_context(self, context: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        return context or {}
