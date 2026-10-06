from __future__ import annotations

import asyncio
from typing import Any

from celery import Celery

from app.agents.registry import get_default_agents
from app.config import settings

celery_app = Celery(
    "agent_platform",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

celery_app.conf.task_serializer = "json"
celery_app.conf.result_serializer = "json"
celery_app.conf.accept_content = ["json"]
celery_app.conf.task_routes = {"run_agent_task": {"queue": "default"}}


@celery_app.task(name="run_agent_task")
def run_agent_task(task: str, agent_name: str = "chat_agent") -> str:
    agents = get_default_agents()
    agent = agents.get(agent_name, agents["chat_agent"])

    async def _execute() -> str:
        result = await agent.run(task)
        return result.result

    return asyncio.run(_execute())


@celery_app.task(name="scheduled_agent_job")
def scheduled_agent_job(task: str, agent_name: str = "chat_agent") -> str:
    return run_agent_task(task=task, agent_name=agent_name)
