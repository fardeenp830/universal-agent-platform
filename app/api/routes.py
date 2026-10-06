from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, HTTPException

from app.core.orchestrator import orchestrator
from app.core.schemas import OrchestrationRequest, ScheduledTask, TaskStatus
from app.services.memory import MemoryService
from app.services.task_store import task_store
from app.workers.tasks import scheduled_agent_job

router = APIRouter(prefix="/api", tags=["agent-platform"])
memory_service = MemoryService()


@router.get("/agents")
async def list_agents() -> Dict[str, Any]:
    return {"agents": [
        "coding_agent",
        "research_agent",
        "github_agent",
        "chat_agent",
        "finance_agent",
        "math_agent",
        "science_agent",
        "robotics_agent",
        "quantum_agent",
        "biotech_agent",
        "film_agent",
        "devops_agent",
    ]}


@router.post("/orchestrate")
async def orchestrate(request: OrchestrationRequest) -> Dict[str, Any]:
    try:
        results = await orchestrator.route_task(request)
        memory_service.add(request.task, metadata={"user_id": request.user_id or "anonymous"})

        for result in results:
            task_store.add(
                task=request.task,
                agent=result.agent,
                status=result.status,
                result=result.result,
                metadata={"context": request.context, "user_id": request.user_id or "anonymous"},
            )

        return {
            "task": request.task,
            "results": [result.model_dump() for result in results],
            "status": "success",
        }
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post("/schedule")
async def schedule_task(task: ScheduledTask) -> TaskStatus:
    try:
        scheduled_agent_job.apply_async(args=[task.payload.get("task", task.description), task.task_type])
        return TaskStatus(
            task_id=f"scheduled-{task.name}",
            status="queued",
            message=f"Task '{task.name}' scheduled successfully.",
        )
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/memory")
async def list_memory() -> Dict[str, Any]:
    return {"memory": memory_service.list()}


@router.get("/memory/search")
async def search_memory(query: str) -> Dict[str, Any]:
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query is required")
    return {"results": memory_service.search(query, limit=5)}


@router.post("/memory")
async def add_memory(payload: Dict[str, str]) -> Dict[str, Any]:
    content = payload.get("content", "").strip()
    if not content:
        raise HTTPException(status_code=400, detail="Content is required")
    record = memory_service.add(content, metadata={"source": "api"})
    return {"status": "saved", "record": {"id": record.id, "content": record.content, "metadata": record.metadata}}


@router.get("/tasks")
async def list_tasks() -> Dict[str, Any]:
    return {"tasks": task_store.list()}


@router.get("/tasks/{task_id}")
async def get_task(task_id: str) -> Dict[str, Any]:
    task = task_store.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task": task}


@router.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}
