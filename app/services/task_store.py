from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class TaskRecord:
    id: str
    task: str
    agent: str
    status: str
    result: str
    created_at: str
    metadata: Dict[str, Any] = field(default_factory=dict)


class TaskStore:
    def __init__(self, store_path: Optional[str] = None) -> None:
        self.store_path = Path(store_path or ".agent-task-history.jsonl")
        self._records: List[TaskRecord] = []
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
                    self._records.append(
                        TaskRecord(
                            id=item.get("id", str(len(self._records))),
                            task=item.get("task", ""),
                            agent=item.get("agent", "unknown_agent"),
                            status=item.get("status", "pending"),
                            result=item.get("result", ""),
                            created_at=item.get("created_at", self._now_iso()),
                            metadata=item.get("metadata", {}),
                        )
                    )
        except Exception:
            self._records = []

    def _save(self) -> None:
        with self.store_path.open("w", encoding="utf-8") as fh:
            for record in self._records:
                fh.write(
                    json.dumps(
                        {
                            "id": record.id,
                            "task": record.task,
                            "agent": record.agent,
                            "status": record.status,
                            "result": record.result,
                            "created_at": record.created_at,
                            "metadata": record.metadata,
                        }
                    )
                    + "\n"
                )

    def _now_iso(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def add(self, task: str, agent: str, status: str, result: str, metadata: Optional[Dict[str, Any]] = None) -> TaskRecord:
        record = TaskRecord(
            id=str(len(self._records) + 1),
            task=task.strip(),
            agent=agent,
            status=status,
            result=result,
            created_at=self._now_iso(),
            metadata=metadata or {},
        )
        self._records.append(record)
        self._save()
        return record

    def list(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": record.id,
                "task": record.task,
                "agent": record.agent,
                "status": record.status,
                "result": record.result,
                "created_at": record.created_at,
                "metadata": record.metadata,
            }
            for record in self._records
        ]

    def get_by_id(self, task_id: str) -> Optional[Dict[str, Any]]:
        for record in self._records:
            if record.id == task_id:
                return {
                    "id": record.id,
                    "task": record.task,
                    "agent": record.agent,
                    "status": record.status,
                    "result": record.result,
                    "created_at": record.created_at,
                    "metadata": record.metadata,
                }
        return None

    def clear(self) -> None:
        self._records.clear()
        self._save()


task_store = TaskStore()
