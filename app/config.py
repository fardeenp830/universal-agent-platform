from __future__ import annotations

import os

APP_ENV = os.getenv("APP_ENV", "development")
APP_NAME = os.getenv("APP_NAME", "Universal Agent Platform")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER", "")
GITHUB_REPO = os.getenv("GITHUB_REPO", "")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "5"))


class Settings:
    APP_NAME = APP_NAME
    APP_ENV = APP_ENV
    HOST = HOST
    PORT = PORT
    OPENAI_API_KEY = OPENAI_API_KEY
    ANTHROPIC_API_KEY = ANTHROPIC_API_KEY
    DEFAULT_MODEL = DEFAULT_MODEL
    GITHUB_TOKEN = GITHUB_TOKEN
    GITHUB_OWNER = GITHUB_OWNER
    GITHUB_REPO = GITHUB_REPO
    REDIS_URL = REDIS_URL
    SECRET_KEY = SECRET_KEY
    MAX_WORKERS = MAX_WORKERS


settings = Settings()
