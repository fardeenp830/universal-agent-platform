from __future__ import annotations

from typing import Dict, List

from app.agents.coding_agent import CodingAgent
from app.agents.research_agent import ResearchAgent
from app.agents.github_agent import GitHubAgent
from app.agents.chat_agent import ChatAgent
from app.agents.finance_agent import FinanceAgent


def get_default_agents() -> Dict[str, object]:
    return {
        "coding_agent": CodingAgent(),
        "research_agent": ResearchAgent(),
        "github_agent": GitHubAgent(),
        "chat_agent": ChatAgent(),
        "finance_agent": FinanceAgent(),
    }


def get_agent_names() -> List[str]:
    return list(get_default_agents().keys())
