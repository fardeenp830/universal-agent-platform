from __future__ import annotations

from app.core.agent_base import BaseAgent
from app.core.schemas import AgentResult


class ResearchAgent(BaseAgent):
    name = "research_agent"
    role = "research"
    capabilities = ["research", "analysis", "synthesis", "reporting"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = (
            "You are a research analyst. Summarize facts accurately, compare options, and provide clear conclusions."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "research"},
        )
