from __future__ import annotations

from typing import Any, Dict, Optional

from app.agents.registry import get_default_agents
from app.core.schemas import AgentResult, OrchestrationRequest


class AgentOrchestrator:
    def __init__(self, agents: Dict[str, Any] | None = None) -> None:
        self.agents = agents or get_default_agents()

    async def route_task(self, request: OrchestrationRequest) -> list[AgentResult]:
        task_text = request.task.lower()

        if any(k in task_text for k in ["debug", "bug", "error", "exception", "traceback", "fix", "code", "python", "javascript", "java", "typescript", "go"]):
            selected = [self.agents["coding_agent"]]
        elif any(k in task_text for k in ["research", "analyze", "study", "compare", "report", "paper", "science", "math", "quantum"]):
            selected = [self.agents["research_agent"]]
        elif any(k in task_text for k in ["github", "pull request", "repo", "issue", "review", "commit", "merge", "pr"]):
            selected = [self.agents["github_agent"]]
        elif any(k in task_text for k in ["finance", "market", "investment", "budget", "economy", "stock", "crypto"]):
            selected = [self.agents["finance_agent"]]
        elif any(k in task_text for k in ["math", "algebra", "geometry", "probability", "calculus", "statistics"]):
            selected = [self.agents["math_agent"]]
        elif any(k in task_text for k in ["science", "biology", "chemistry", "physics", "astronomy", "space"]):
            selected = [self.agents["science_agent"]]
        elif any(k in task_text for k in ["robot", "robotics", "drone", "automation", "autonomy", "control"]):
            selected = [self.agents["robotics_agent"]]
        elif any(k in task_text for k in ["quantum", "qubit", "superposition", "entanglement", "schrodinger"]):
            selected = [self.agents["quantum_agent"]]
        elif any(k in task_text for k in ["biotech", "genome", "gene", "medical", "bioinformatics"]):
            selected = [self.agents["biotech_agent"]]
        elif any(k in task_text for k in ["film", "video", "cinema", "storyboard", "script", "editing", "camera"]):
            selected = [self.agents["film_agent"]]
        elif any(k in task_text for k in ["deploy", "docker", "kubernetes", "cloud", "infra", "devops", "pipeline", "ci"]):
            selected = [self.agents["devops_agent"]]
        else:
            selected = [self.agents["chat_agent"]]

        results: list[AgentResult] = []
        for agent in selected:
            result = await agent.run(request.task, request.context)
            results.append(result)
        return results


orchestrator = AgentOrchestrator()
