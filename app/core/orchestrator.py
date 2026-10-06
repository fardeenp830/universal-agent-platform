from __future__ import annotations

from typing import Any, Dict, List

from app.agents.registry import get_default_agents
from app.core.schemas import AgentResult, OrchestrationRequest


class AgentOrchestrator:
    def __init__(self, agents: Dict[str, object] | None = None) -> None:
        self.agents = agents or get_default_agents()

    async def route_task(self, request: OrchestrationRequest) -> List[AgentResult]:
        task_text = request.task.lower()

        if any(keyword in task_text for keyword in ["debug", "bug", "error", "exception", "traceback", "fix", "code", "python", "javascript", "java", "typescript", "golang"]):
            selected = [self.agents["coding_agent"]]
        elif any(keyword in task_text for keyword in ["research", "analyze", "study", "compare", "report", "paper", "trend", "science", "math", "quantum"]):
            selected = [self.agents["research_agent"]]
        elif any(keyword in task_text for keyword in ["github", "pull request", "repo", "issue", "review", "commit", "merge", "pr"]):
            selected = [self.agents["github_agent"]]
        elif any(keyword in task_text for keyword in ["finance", "market", "investment", "budget", "economy", "startup", "stock", "crypto"]):
            selected = [self.agents["finance_agent"]]
        elif any(keyword in task_text for keyword in ["math", "algebra", "geometry", "probability", "calculus", "statistics"]):
            selected = [self.agents["math_agent"]]
        elif any(keyword in task_text for keyword in ["science", "biology", "chemistry", "physics", "astronomy", "space"]):
            selected = [self.agents["science_agent"]]
        elif any(keyword in task_text for keyword in ["robot", "robotics", "automaton", "control", "autonomy", "drone"]):
            selected = [self.agents["robotics_agent"]]
        elif any(keyword in task_text for keyword in ["quantum", "superposition", "schrodinger", "entanglement", "qubit"]):
            selected = [self.agents["quantum_agent"]]
        elif any(keyword in task_text for keyword in ["biotech", "genome", "gene", "medical", "bioinformatics", "cell"]):
            selected = [self.agents["biotech_agent"]]
        elif any(keyword in task_text for keyword in ["film", "video", "cinema", "storyboard", "script", "editing", "camera"]):
            selected = [self.agents["film_agent"]]
        elif any(keyword in task_text for keyword in ["deploy", "docker", "kubernetes", "cloud", "ci/cd", "infra", "devops", "pipeline"]):
            selected = [self.agents["devops_agent"]]
        else:
            selected = [self.agents["chat_agent"]]

        results: List[AgentResult] = []
        for agent in selected:
            result = await agent.run(request.task, request.context)
            results.append(result)
        return results


orchestrator = AgentOrchestrator()
