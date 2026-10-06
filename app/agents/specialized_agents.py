from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

from app.services.memory import MemoryService


class RAGService:
    def __init__(self, memory_service: Optional[MemoryService] = None) -> None:
        self.memory_service = memory_service or MemoryService()
        self.knowledge_base = [
            "General knowledge foundation: AI agents combine reasoning, tool use, memory, and execution loops to perform tasks reliably.",
            "Software engineering best practices include clear interfaces, tests, logging, observability, security checks, and incremental deployment.",
            "Research workflows benefit from structured questions, source evaluation, synthesis, and explicit assumptions.",
            "DevOps patterns rely on automation, infrastructure as code, environment isolation, monitoring, and rollback strategies.",
            "Finance and operations need risk analysis, scenario planning, and measurement of uncertainty before committing resources.",
            "Robotics combines sensors, controls, planning, perception, and safety constraints for reliable autonomous behavior.",
            "Quantum computing studies superposition, entanglement, interference, and noise management in complex systems.",
            "Biotechnology and life sciences depend on precise experimentation, model validation, and regulated workflows.",
        ]

    def retrieve(self, query: str, limit: int = 3) -> List[str]:
        query_tokens = self._normalize(query)
        scored: List[tuple[float, str]] = []
        for doc in self.knowledge_base:
            score = self._document_score(query_tokens, doc)
            if score > 0:
                scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in scored[:limit]]

    def add_document(self, document: str) -> None:
        if document.strip():
            self.knowledge_base.append(document.strip())

    def _normalize(self, text: str) -> List[str]:
        return re.sub(r"[^a-z0-9\s]", " ", text.lower()).split()

    def _document_score(self, query_tokens: List[str], document: str) -> float:
        doc_tokens = self._normalize(document)
        if not query_tokens:
            return 0.0
        overlap = sum(1 for token in query_tokens if token in doc_tokens)
        if overlap == 0:
            return 0.0
        return overlap / max(len(query_tokens), 1)

    def enrich_prompt(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        knowledge = self.retrieve(task, limit=3)
        memory = self.memory_service.search(task, limit=3) if self.memory_service else []
        context_parts = []
        if knowledge:
            context_parts.append("Relevant knowledge:\n" + "\n".join(f"- {item}" for item in knowledge))
        if memory:
            context_parts.append("Relevant memory:\n" + "\n".join(f"- {item['content']}" for item in memory))
        final_context = "\n\n".join(context_parts)
        return f"{task}\n\n{final_context}" if final_context else task
