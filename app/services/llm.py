from __future__ import annotations

from app.core.agent_base import BaseAgent
from app.core.schemas import AgentResult


class FinanceAgent(BaseAgent):
    name = "finance_agent"
    role = "finance and strategy"
    capabilities = ["market analysis", "risk assessment", "financial planning", "strategy"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = (
            "You are a finance and strategy expert. Provide risk-aware, practical financial and business analysis."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "finance"},
        )
