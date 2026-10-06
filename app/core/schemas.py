from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AgentTask(BaseModel):
    task: str
    context: Dict[str, Any] = Field(default_factory=dict)


class AgentResult(BaseModel):
    agent: str
    status: str
    result: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class OrchestrationRequest(BaseModel):
    task: str
    context: Dict[str, Any] = Field(default_factory=dict)
    user_id: Optional[str] = None


class ScheduledTask(BaseModel):
    name: str
    description: str
    schedule: str
    task_type: str
    payload: Dict[str, Any] = Field(default_factory=dict)


class TaskStatus(BaseModel):
    task_id: str
    status: str
    message: str
    result: Optional[str] = None
