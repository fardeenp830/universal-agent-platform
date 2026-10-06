from __future__ import annotations

from app.core.agent_base import BaseAgent
from app.core.schemas import AgentResult


class ChatAgent(BaseAgent):
    name = "chat_agent"
    role = "conversational assistant"
    capabilities = ["conversation", "guidance", "planning", "brainstorming"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = "You are a helpful and highly capable general assistant. Provide clear, structured responses."
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "chat"},
        )
