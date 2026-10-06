from __future__ import annotations

from typing import Any, Dict, Optional

from app.core.agent_base import BaseAgent
from app.core.schemas import AgentResult


class CodingAgent(BaseAgent):
    name = "coding_agent"
    role = "software engineering"
    capabilities = ["debugging", "code generation", "refactoring", "testing"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        ctx = self._safe_context(context)
        system_prompt = (
            "You are a senior software engineer. Provide code fixes, debugging guidance, architecture advice, "
            "and implementation steps with production-quality reasoning."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "coding", "context": ctx},
        )


class ResearchAgent(BaseAgent):
    name = "research_agent"
    role = "research and analysis"
    capabilities = ["research", "synthesis", "analysis", "reporting"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        ctx = self._safe_context(context)
        system_prompt = (
            "You are a world-class researcher. Synthesize information, compare tradeoffs, and provide concise but deep analysis."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "research", "context": ctx},
        )


class GitHubAgent(BaseAgent):
    name = "github_agent"
    role = "GitHub and developer operations"
    capabilities = ["repository navigation", "PR review", "issue triage", "workflow automation"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        ctx = self._safe_context(context)
        system_prompt = (
            "You are a GitHub operations and engineering specialist. Offer PR guidance, issue triage, release planning, and code review support."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "github", "context": ctx},
        )


class ChatAgent(BaseAgent):
    name = "chat_agent"
    role = "general-purpose conversational assistant"
    capabilities = ["conversation", "explanation", "planning", "brainstorming"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        ctx = self._safe_context(context)
        system_prompt = (
            "You are a helpful, knowledgeable general assistant with strong reasoning across many domains."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "chat", "context": ctx},
        )


class FinanceAgent(BaseAgent):
    name = "finance_agent"
    role = "finance and business analysis"
    capabilities = ["market insight", "strategy", "financial modeling", "risk assessment"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        ctx = self._safe_context(context)
        system_prompt = (
            "You are a finance and strategy expert. Provide risk analysis, business insight, and practical financial guidance."
        )
        response = await self.llm_service.generate(task, system_prompt=system_prompt)
        return AgentResult(
            agent=self.name,
            status="completed",
            result=response,
            metadata={"type": "finance", "context": ctx},
        )
