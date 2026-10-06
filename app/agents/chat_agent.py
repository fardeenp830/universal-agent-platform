from __future__ import annotations

from app.core.agent_base import BaseAgent
from app.core.schemas import AgentResult


class GitHubAgent(BaseAgent):
    name = "github_agent"
    role = "developer operations"
    capabilities = ["PR review", "issue triage", "repo planning", "workflow automation"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = (
            "You are a GitHub operations specialist. Handle repository issues, PR feedback, and workflow strategy clearly."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "github"},
        )
