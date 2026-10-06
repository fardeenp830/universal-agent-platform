from __future__ import annotations

from typing import Dict, List

from app.agents.specialized_agents import (
    BiotechAgent,
    ChatAgent,
    CodingAgent,
    DevOpsAgent,
    FilmAgent,
    FinanceAgent,
    GitHubAgent,
    MathAgent,
    QuantumAgent,
    ResearchAgent,
    RoboticsAgent,
    ScienceAgent,
)


def get_default_agents() -> Dict[str, object]:
    return {
        "coding_agent": CodingAgent(),
        "research_agent": ResearchAgent(),
        "github_agent": GitHubAgent(),
        "chat_agent": ChatAgent(),
        "finance_agent": FinanceAgent(),
        "math_agent": MathAgent(),
        "science_agent": ScienceAgent(),
        "robotics_agent": RoboticsAgent(),
        "quantum_agent": QuantumAgent(),
        "biotech_agent": BiotechAgent(),
        "film_agent": FilmAgent(),
        "devops_agent": DevOpsAgent(),
    }


def get_agent_names() -> List[str]:
    return list(get_default_agents().keys())
