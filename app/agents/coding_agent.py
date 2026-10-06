from __future__ import annotations

from app.core.agent_base import BaseAgent
from app.core.schemas import AgentResult


class CodingAgent(BaseAgent):
    name = "coding_agent"
    role = "software engineering"
    capabilities = ["debugging", "code generation", "refactoring", "testing"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = (
            "You are a senior software engineer. Provide code fixes, debugging guidance, architecture advice, "
            "and implementation steps with production-quality reasoning."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "coding"},
        )


class ResearchAgent(BaseAgent):
    name = "research_agent"
    role = "research"
    capabilities = ["research", "synthesis", "analysis", "reporting"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = (
            "You are a world-class researcher. Synthesize information and produce concise but high-quality analysis."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "research"},
        )


class GitHubAgent(BaseAgent):
    name = "github_agent"
    role = "developer operations"
    capabilities = ["issue triage", "PR review", "workflow automation", "repo analysis"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = (
            "You are a GitHub automation specialist. Provide actionable repository guidance, issue analysis, PR review comments, and release planning support."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "github"},
        )


class ChatAgent(BaseAgent):
    name = "chat_agent"
    role = "conversational assistant"
    capabilities = ["conversation", "explanation", "planning"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = "You are a highly capable general-purpose assistant with excellent reasoning and communication."
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "chat"},
        )


class FinanceAgent(BaseAgent):
    name = "finance_agent"
    role = "finance and strategy"
    capabilities = ["investment analysis", "risk assessment", "business strategy"]

    async def run(self, task: str, context=None) -> AgentResult:
        system_prompt = "You are a finance and strategy expert. Provide well-structured business and financial insight."
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "finance"},
        )
