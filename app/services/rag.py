from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class MemoryRecord:
    id: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


class MemoryService:
    def __init__(self, store_path: Optional[str] = None) -> None:
        self.store_path = Path(store_path or ".agent-memory.jsonl")
        self._records: List[MemoryRecord] = []
        self._load()

    def _load(self) -> None:
        if not self.store_path.exists():
            return
        try:
            import json
            with self.store_path.open("r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    item = json.loads(line)
                    self._records.append(MemoryRecord(id=item.get("id", str(len(self._records))), content=item.get("content", ""), metadata=item.get("metadata", {})))
        except Exception:
            self._records = []

    def _save(self) -> None:
        import json
        with self.store_path.open("w", encoding="utf-8") as fh:
            for record in self._records:
                fh.write(json.dumps({"id": record.id, "content": record.content, "metadata": record.metadata}) + "\n")

    def add(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> MemoryRecord:
        cleaned = content.strip()
        if not cleaned:
            raise ValueError("Memory content cannot be empty.")
        record = MemoryRecord(id=str(len(self._records) + 1), content=cleaned, metadata=metadata or {})
        self._records.append(record)
        self._save()
        return record

    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        tokens = self._normalize(query)
        scored: List[tuple[float, MemoryRecord]] = []
        for record in self._records:
            score = self._score(tokens, record.content)
            if score > 0:
                scored.append((score, record))
        scored.sort(key=lambda item: item[0], reverse=True)
        return [{"id": record.id, "content": record.content, "metadata": record.metadata, "score": round(score, 4)} for score, record in scored[:limit]]

    def _normalize(self, text: str) -> List[str]:
        return re.sub(r"[^a-z0-9\s]", " ", text.lower()).split()

    def _score(self, query_tokens: List[str], content: str) -> float:
        content_tokens = self._normalize(content)
        if not query_tokens:
            return 0.0
        overlap = sum(1 for token in query_tokens if token in content_tokens)
        if overlap == 0:
            return 0.0
        return overlap / max(len(query_tokens), 1)

    def list(self) -> List[Dict[str, Any]]:
        return [{"id": record.id, "content": record.content, "metadata": record.metadata} for record in self._records]

    def clear(self) -> None:
        self._records.clear()
        self._save()
