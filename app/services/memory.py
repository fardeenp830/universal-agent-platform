from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np


@dataclass
class MemoryRecord:
    id: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    embedding: Optional[np.ndarray] = field(default=None, repr=False)


class MemoryService:
    """Persistent memory service with lightweight vector-style recall.

    This implementation keeps an on-disk JSONL store and uses a deterministic
    token-hash vector to provide cosine-similarity based memory lookup without
    requiring a hosted vector database.
    """

    def __init__(self, store_path: Optional[str] = None, vector_dim: int = 256) -> None:
        self.store_path = Path(store_path or ".agent-memory.jsonl")
        self.vector_dim = vector_dim
        self._records: List[MemoryRecord] = []
        self._load()

    def _load(self) -> None:
        if not self.store_path.exists():
            return
        try:
            with self.store_path.open("r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    item = json.loads(line)
                    record = MemoryRecord(
                        id=item.get("id", str(len(self._records))),
                        content=item.get("content", ""),
                        metadata=item.get("metadata", {}),
                        embedding=np.array(item.get("embedding", [0.0] * self.vector_dim), dtype=float),
                    )
                    self._records.append(record)
        except Exception:
            self._records = []

    def _save(self) -> None:
        with self.store_path.open("w", encoding="utf-8") as fh:
            for record in self._records:
                vector_payload = record.embedding.tolist() if record.embedding is not None else [0.0] * self.vector_dim
                fh.write(
                    json.dumps(
                        {
                            "id": record.id,
                            "content": record.content,
                            "metadata": record.metadata,
                            "embedding": vector_payload,
                        }
                    )
                    + "\n"
                )

    def _normalize(self, text: str) -> List[str]:
        return re.sub(r"[^a-z0-9\s]", " ", text.lower()).split()

    def _hash_vector(self, text: str) -> np.ndarray:
        tokens = self._normalize(text)
        vector = np.zeros(self.vector_dim, dtype=float)
        if not tokens:
            return vector

        for token in tokens:
            bucket = abs(hash(token)) % self.vector_dim
            vector[bucket] += 1.0

        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        return vector

    def _cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        if a.shape != b.shape:
            return 0.0
        a_norm = np.linalg.norm(a)
        b_norm = np.linalg.norm(b)
        if a_norm == 0 or b_norm == 0:
            return 0.0
        return float(np.dot(a, b) / (a_norm * b_norm))

    def add(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> MemoryRecord:
        cleaned = content.strip()
        if not cleaned:
            raise ValueError("Memory content cannot be empty.")
        record = MemoryRecord(
            id=str(len(self._records) + 1),
            content=cleaned,
            metadata=metadata or {},
            embedding=self._hash_vector(cleaned),
        )
        self._records.append(record)
        self._save()
        return record

    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        if not self._records:
            return []

        query_vector = self._hash_vector(query)
        scored: List[tuple[float, MemoryRecord]] = []
        for record in self._records:
            if record.embedding is None:
                record.embedding = self._hash_vector(record.content)
            score = self._cosine_similarity(query_vector, record.embedding)
            if score > 0:
                scored.append((score, record))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [
            {
                "id": record.id,
                "content": record.content,
                "metadata": record.metadata,
                "score": round(score, 4),
            }
            for score, record in scored[:limit]
        ]

    def list(self) -> List[Dict[str, Any]]:
        return [{"id": record.id, "content": record.content, "metadata": record.metadata} for record in self._records]

    def clear(self) -> None:
        self._records.clear()
        self._save()


vector_memory = MemoryService()
