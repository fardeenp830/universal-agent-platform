from __future__ import annotations

import os
from typing import Any, Dict


class GitHubTools:
    def __init__(self, token: str | None = None, owner: str | None = None, repo: str | None = None) -> None:
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.owner = owner or os.getenv("GITHUB_OWNER")
        self.repo = repo or os.getenv("GITHUB_REPO")

    def is_configured(self) -> bool:
        return bool(self.token and self.owner and self.repo)

    def get_repo_summary(self) -> Dict[str, Any]:
        if not self.is_configured():
            return {
                "status": "not_configured",
                "message": "Set GITHUB_TOKEN, GITHUB_OWNER, and GITHUB_REPO in the environment to enable GitHub features.",
            }
        return {
            "status": "configured",
            "owner": self.owner,
            "repo": self.repo,
            "token_present": True,
        }

    def build_pr_review_comment(self, title: str, findings: str) -> str:
        return (
            f"### Review Comment\n"
            f"**Title:** {title}\n\n"
            f"**Findings:**\n{findings}\n\n"
            "Please validate this change against the latest tests and deployment requirements."
        )
