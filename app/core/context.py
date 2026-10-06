from __future__ import annotations

from typing import Any, Dict, List, Optional

from app.services.memory import MemoryService
from app.services.rag import RAGService


class AgentContext:
    def __init__(self, memory_service: Optional[MemoryService] = None, rag_service: Optional[RAGService] = None):
        self.memory_service = memory_service or MemoryService()
        self.rag_service = rag_service or RAGService(self.memory_service)

    def build_context(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        ctx = context or {}
        relevant_memories = self.memory_service.search(task, limit=5)
        rag_context = self.rag_service.retrieve(task, limit=3)
        ctx.setdefault("memory", relevant_memories)
        ctx.setdefault("knowledge", rag_context)
        return ctx
