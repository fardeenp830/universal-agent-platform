from __future__ import annotations

from typing import Any, Dict, Optional

from app.core.agent_base import BaseAgent
from app.core.schemas import AgentResult


class CodingAgent(BaseAgent):
    name = "coding_agent"
    role = "software engineering"
    capabilities = ["debugging", "code generation", "refactoring", "testing"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        prompt = (
            "You are a senior software engineer. Provide a precise fix, architecture advice, and validation steps. "
            f"Task: {task}"
        )
        response = await self.llm_service.generate(prompt, system_prompt="You are a senior software engineer and technical architect.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "coding", "context": self._safe_context(context)})


class ResearchAgent(BaseAgent):
    name = "research_agent"
    role = "research and analysis"
    capabilities = ["research", "synthesis", "analysis", "reporting"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        prompt = f"Research and analyze the following: {task}"
        response = await self.llm_service.generate(prompt, system_prompt="You are a research analyst and synthesizer of complex information.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "research", "context": self._safe_context(context)})


class GitHubAgent(BaseAgent):
    name = "github_agent"
    role = "GitHub automation"
    capabilities = ["repo triage", "PR review", "issue response", "release planning"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        prompt = f"Provide GitHub-focused engineering guidance for this task: {task}"
        response = await self.llm_service.generate(prompt, system_prompt="You are a GitHub operations expert for engineering teams.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "github", "context": self._safe_context(context)})


class ChatAgent(BaseAgent):
    name = "chat_agent"
    role = "general-purpose assistant"
    capabilities = ["conversation", "question answering", "planning", "brainstorming"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        response = await self.llm_service.generate(task, system_prompt="You are a helpful, knowledgeable general assistant.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "chat", "context": self._safe_context(context)})


class FinanceAgent(BaseAgent):
    name = "finance_agent"
    role = "finance and strategy"
    capabilities = ["market analysis", "risk assessment", "financial plan", "business insight"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        prompt = f"Provide financial and strategic analysis for: {task}"
        response = await self.llm_service.generate(prompt, system_prompt="You are a finance and strategy expert.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "finance", "context": self._safe_context(context)})


class MathAgent(BaseAgent):
    name = "math_agent"
    role = "mathematics"
    capabilities = ["algebra", "calculus", "statistics", "proofs"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        response = await self.llm_service.generate(task, system_prompt="You are a mathematics expert with strong reasoning and step-by-step derivations.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "math", "context": self._safe_context(context)})


class ScienceAgent(BaseAgent):
    name = "science_agent"
    role = "science and systems"
    capabilities = ["physics", "chemistry", "biology", "astronomy"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        response = await self.llm_service.generate(task, system_prompt="You are a science educator and systems thinker with deep domain knowledge.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "science", "context": self._safe_context(context)})


class RoboticsAgent(BaseAgent):
    name = "robotics_agent"
    role = "robotics and autonomy"
    capabilities = ["control systems", "perception", "planning", "autonomy"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        response = await self.llm_service.generate(task, system_prompt="You are a robotics expert focused on control, sensing, autonomy, and safety.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "robotics", "context": self._safe_context(context)})


class QuantumAgent(BaseAgent):
    name = "quantum_agent"
    role = "quantum science"
    capabilities = ["quantum mechanics", "quantum computing", "entanglement", "algorithms"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        response = await self.llm_service.generate(task, system_prompt="You are a quantum scientist with deep knowledge of physics and computational methods.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "quantum", "context": self._safe_context(context)})


class BiotechAgent(BaseAgent):
    name = "biotech_agent"
    role = "biotechnology and life sciences"
    capabilities = ["genomics", "bioinformatics", "drug discovery", "experimental design"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        response = await self.llm_service.generate(task, system_prompt="You are a biotech and life sciences specialist with strong scientific rigor.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "biotech", "context": self._safe_context(context)})


class FilmAgent(BaseAgent):
    name = "film_agent"
    role = "filmmaking and creative storytelling"
    capabilities = ["screenwriting", "story structure", "visual direction", "editing"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        response = await self.llm_service.generate(task, system_prompt="You are a filmmaker and creative storyteller with experience in script and direction.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "film", "context": self._safe_context(context)})


class DevOpsAgent(BaseAgent):
    name = "devops_agent"
    role = "infrastructure and deployment"
    capabilities = ["deployment", "ci/cd", "cloud", "observability", "automation"]

    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> AgentResult:
        response = await self.llm_service.generate(task, system_prompt="You are a DevOps engineer focused on deployment, automation, and infrastructure health.")
        return AgentResult(agent=self.name, status="completed", result=response, metadata={"type": "devops", "context": self._safe_context(context)})
