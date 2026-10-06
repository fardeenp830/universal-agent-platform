from __future__ import annotations

from typing import Dict, List

from app.agents.registry import get_default_agents
from app.core.schemas import AgentResult, OrchestrationRequest


class AgentOrchestrator:
    def __init__(self, agents: Dict[str, object] | None = None) -> None:
        self.agents = agents or get_default_agents()

    async def route_task(self, request: OrchestrationRequest) -> List[AgentResult]:
        task_text = request.task.lower()

        if any(keyword in task_text for keyword in ["debug", "bug", "error", "exception", "traceback", "fix", "code"]):
            selected = [self.agents["coding_agent"]]
        elif any(keyword in task_text for keyword in ["research", "analyze", "study", "compare", "report", "trend"]):
            selected = [self.agents["research_agent"]]
        elif any(keyword in task_text for keyword in ["github", "pull request", "repo", "issue", "review", "commit", "merge"]):
            selected = [self.agents["github_agent"]]
        elif any(keyword in task_text for keyword in ["finance", "market", "investment", "budget", "economy"]):
            selected = [self.agents["finance_agent"]]
        else:
            selected = [self.agents["chat_agent"]]

        results: List[AgentResult] = []
        for agent in selected:
            result = await agent.run(request.task, request.context)
            results.append(result)
        return results


orchestrator = AgentOrchestrator()
